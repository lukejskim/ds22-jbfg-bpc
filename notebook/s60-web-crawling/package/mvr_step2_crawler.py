# package/mvr_step2_crawler.py
from bs4 import BeautifulSoup 
from urllib.request import urlopen
from tqdm.notebook import tqdm

import pandas as pd
import re

# star_scores = mv_info_area.find_all('div', 'star_score')
def get_scores(star_scores):
    '''
    관람객, 평론가, 네티즌의 평점을 리턴
    Return : str()
    '''
    arr_score = list()
    for star_score in star_scores:
        each_score = star_score.get_text()
        re_score = re.search('\d{1,2}\.\d{1,2}', each_score)

        if re_score is not None:
            score = re_score.group()
            arr_score.append(score)
            # print('[{}]'.format(score))
        else :
            pass

    if len(arr_score) > 2:
        score1 = arr_score[0]
        score2 = arr_score[1]
        score3 = arr_score[2]
    else:
        score1 = '0.00'
        score2 = '0.00'
        score3 = '0.00'

    scores = "관람객:{} / 평론가:{} / 네티즌:{}".format(score1, score2, score3)
    return scores




# info_spec = mv_info_area.find('dl', 'info_spec')
def get_movie_info(info_spec):
    '''
    영화정보(장르, 감독, 출연, 등급, 관객수)를 리턴
    Return : dict()
    '''
    arr_dt = info_spec.find_all('dt')
    arr_dd = info_spec.find_all('dd')

    dt_step = [ 'step1', 'step2', 'step3', 'step4', 'step9' ]
    mv_dict = {
        'genre'     : None,
        'director'  : None,
        'casting'   : None,
        'rating'    : None,
        'ticketing' : None,
    }

    for idx in range(len(arr_dt)):
        dt_class = arr_dt[idx]['class'][0]
        dd_value = arr_dd[idx]
        # print('{} : {} -> {}'.format(idx, dt_class, type(dd_value)))

        mv_dict = collect_mv_dict(mv_dict, dt_class, dd_value)
        
    return mv_dict
    

def collect_mv_dict(mv_dict, dt_class, dd_value):
    if dt_class=='step1':
        genreTag =  dd_value
        genre = genreTag
        genre = genreTag.find('span').get_text()
        genre = genre.replace('\n', '')
        genre = genre.replace('\r', '')
        genre = genre.replace('\t', '')
        genre = genre.strip()
        mv_dict['genre'] = genre        
        
    elif dt_class=='step2':
        directorTag =  dd_value
        director = directorTag
        director = directorTag.get_text()
        director = director.strip()
        mv_dict['director'] = director        
        
    elif dt_class=='step3':
        castingTag =  dd_value
        casting = castingTag
        casting = castingTag.get_text()
        casting = casting.replace('더보기', '')
        casting = casting.strip()
        mv_dict['casting'] = casting

    elif dt_class=='step4':
        ratingTag =  dd_value
        rating = ratingTag
        rating = ratingTag.get_text()
        rating = rating.replace('\n', '')
        rating = rating.replace('\r', '')
        rating = rating.replace('\t', '')
        rating = rating.strip()
        mv_dict['rating'] = rating

    elif dt_class=='step9':
        ticketingTag =  dd_value
        ticketing = ticketingTag
        ticketing = ticketingTag.find('p').get_text()
        ticketing = ticketing.strip()
        mv_dict['ticketing'] = ticketing

    return mv_dict


def crawl_movie_detail_page(df) :
    '''
    영화상세페이지를 크롤링 한후, DataFrame에 컬럼정보를 추가한다.
    Return : DataFrame
    '''

    Score     = []
    Genre     = []
    Director  = []
    Casting   = []
    Rating    = []
    Ticketing = []

    for url_page in tqdm(df['링크']):

        html = urlopen(url_page)
        soup = BeautifulSoup(html, "lxml")

        mv_info_area = soup.find('div', 'mv_info_area')

        # 스코어
        star_scores = mv_info_area.find_all('div', 'star_score')
        scores = get_scores(star_scores)

        # 영화정보
        info_spec = mv_info_area.find('dl', 'info_spec')
        mv_dict = get_movie_info(info_spec)

        # 리스트에 담기
        Score.append(scores)
        Genre.append(mv_dict['genre'])
        Director.append(mv_dict['director'])
        Casting.append(mv_dict['casting'])
        Rating.append(mv_dict['rating'])
        Ticketing.append(mv_dict['ticketing'])

    # DataFrame에 추가
    df['평점'] = Score
    df['장르'] = Genre
    df['감독'] = Director
    df['출연'] = Casting
    df['등급'] = Rating
    df['흥행'] = Ticketing

    # print('Crawling is Finished !!!')
    
    columns = list(df.columns)
    columns.append(columns.pop(2))
    
    final_df = df.loc[:, columns]
        
    return final_df



if __name__ == "__main__":
    # df = pd.read_csv(file_name_step1, encoding='UTF-8')
    df = pd.read_csv(file_name_step1, encoding='UTF-8', index_col='순위')

    final_df = crawl_movie_detail_page(df)
    
    file_name_step2 = 'data/movie_top10_final.csv'
    final_df.to_csv(file_name_step1, encoding='UTF-8')

    final_df
    
