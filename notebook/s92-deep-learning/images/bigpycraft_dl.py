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


LOGO_TF_01   = "images/bg_logo_tensorflow_no_shadow_1.png"

DL01_IMG_01  = "images/dl_101_01_activity_recognition.png"
DL01_IMG_02  = "images/dl_101_02_ml_diagram1.png"
DL01_IMG_03  = "images/dl_101_03_ml_diagram2.png"
DL01_IMG_04  = "images/dl_101_04_ml_diagram3.png"
DL01_IMG_05  = "images/dl_101_05_ml_scinario.png"

DL02_IMG_01  = "images/dl_102_01_dl_popularity.png"
DL02_IMG_02  = "images/dl_102_02_tf2_concept_diagram.png"
DL02_IMG_03  = "images/dl_102_03_tf1_vs_tf2.png"
DL02_IMG_04  = "images/dl_102_04_tf1_vs_tf2.png"
DL02_IMG_05  = "images/dl_102_05_tf1_vs_tf2.png"
DL02_IMG_06  = "images/dl_102_06_sequential_api.png"
DL02_IMG_07  = "images/dl_102_07_functional_api.png"
DL02_IMG_90  = "images/"



