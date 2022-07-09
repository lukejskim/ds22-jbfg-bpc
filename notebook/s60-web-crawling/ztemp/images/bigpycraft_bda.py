from IPython.display import Image

import time
import os

def chk_processting_time(start_time, end_time):
    process_time = end_time - start_time
    p_time = int(process_time)
    p_min = p_time // 60
    p_sec = p_time %  60
    print('처리시간 : {p_min}분 {p_sec}초 경과되었습니다.'.format(
            p_min = p_min,
            p_sec = p_sec
        ))
    return process_time

Figure = lambda file, w=None, h=None : \
    Image(filename=file, width=w, height=h)


# 데이터분석 실습
BDA_PD_331_1 = "./images/seoul_population_2018_3Q.png"


# 웹크롤링
BDA_PE_411_1 = "./images/Img_BestSandwitch_P1-1.png"
BDA_PE_411_2 = "./images/Img_BestSandwitch_P1-2.png"
BDA_PE_412_1 = "./images/Img_BestSandwitch_P2-1.png"
BDA_PE_413_1 = "./images/rank_music_top100.png"
BDA_PE_413_2 = "./images/rank_movie_top10.png"
BDA_PE_413_3 = "./images/rank_movie_top10_1.png"
BDA_PE_413_4 = "./images/rank_movie_top10_2.png"
BDA_PE_413_4 = "./images/rank_movie_top10_2.png"
BDA_PE_420_1 = "./images/mcdonalds_seoul.png"
