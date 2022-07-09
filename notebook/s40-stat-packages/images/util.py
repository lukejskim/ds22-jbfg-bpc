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


# Figure = lambda file, w=None, h=None : \
#     Image(filename=file, width=w, height=h) 
    
def Figure(img_name, w=None, h=None):
    
    file = img_path(img_name)
    
    load_image = Image(filename=file, width=w, height=h) 
    return load_image
    
    
def img_path(img_key):
    load_img = dict()

    load_img["NumPy"] = "images/numpy_logo.png"
    
    load_img["피보나치"  ] = "images/A202_fibonacci.png"
    load_img["fibonachi" ] = "images/A202_fibonacci.png"
    load_img["스택" ] = "images/A202_stack.png"
    load_img["stack"] = "images/A202_stack.png"
    load_img["큐" ]   = "images/A202_queue.png"
    load_img["queue"] = "images/A202_queue.png"

    load_img["iterators"] = "images/A306_iterators.png"
    load_img["이터레이터"] = "images/A306_iterators.png"
    load_img["generator"] = "images/A307_generator_iterator_diagram.png"
    load_img["제너레이터"] = "images/A307_generator_iterator_diagram.png"
    
    return load_img[img_key]
    