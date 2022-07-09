# package/mvr_step1_crawler.py
from bs4 import BeautifulSoup 
from urllib.request import urlopen
from tqdm.notebook import tqdm

import pandas as pd
import re


def crawl_movie_list_top10(url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'):
    
    Ranking   = []
    Title     = []
    Link      = []
    Range_ac  = []

    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")

    table_tag = soup.find('table', 'list_ranking')
    tbody_tag = table_tag.find('tbody')
    tr_tags = tbody_tag.find_all('tr')

    for tr_tag in tr_tags[1:11]:
        
        td_tags = tr_tag.find_all('td')

        # 순위
        ranking = td_tags[0].find('img')
        ranking = ranking['alt']   
        ranking = int(ranking)

        # 영화명
        movie = td_tags[1].find('a')
        title = movie.get_text().strip()

        # link
        root_url = 'https://movie.naver.com' if movie['href'].startswith('/') else ''
        link = root_url + movie['href']
        link = link.strip()
        
        # range_ac
        range_sign = td_tags[2].find('img')
        range_sign = range_sign['alt']
        range_sign = '-' if range_sign=='down' else ''
        range_num = td_tags[3].get_text()
        range_num = range_num.strip()
        range_ac = range_sign + range_num
    
        Ranking.append(ranking)
        Title.append(title)
        Link.append(link)
        Range_ac.append(range_ac)

    data   = {'순위':Ranking, '영화명':Title, '변동폭':Range_ac, '링크':Link }
    top10_df = pd.DataFrame(data)
    top10_df.set_index('순위', inplace=True)
    
    return top10_df   


if __name__ == "__main__":
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    top10_df = crawl_movie_list_top10(url)
    
    file_name_step1 = 'data/movie_top10.csv'
    top10_df.to_csv(file_name_step1, encoding='UTF-8')

    top10_df
    
