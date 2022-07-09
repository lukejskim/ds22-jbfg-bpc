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



Reference = lambda file, w=None, h=None : \
    Image(filename=file, width=w, height=h) 


# images
Figure4_1 ='images/Figure4-1.png'   # NumPy 배열에서 요소 색인하기
Figure4_2 ='images/Figure4-2.png'   # 2차원 배열 슬라이싱

Table4_3  = "images/Table4-3.png"   # 단항 유니버설 함수
Table4_4  = "images/Table4-4.png"   # 이항 유니버설 함수
Table4_5  = "images/Table4-5.png"   # 기본 배열 통계 메소드
Table4_6  = "images/Table4-6.png"   # 배열 집합연산
Table4_7  = "images/Table4-7.png"   # 자주 사용하는 numpy.linalg 함수
Table4_8  = "images/Table4-8.png"   # 일부 numpy.random 함수

Table5_1  = "images/Table5-1.png"   # DataFrame 생성자에서 사용 가능한 입력 데이터
Table5_2  = "images/Table5-2.png"   # pandas의 주요 Index 객체
Table5_3  = "images/Table5-3.png"   # Index 메소드와 속성
Table5_4  = "images/Table5-4.png"   # reindex 메소드(보간) 옵션
Table5_5  = "images/Table5-5.png"   # 재색인 함수 인자
Table5_6  = "images/Table5-6.png"   # DataFrame의 값 선택하기
Table5_7  = "images/Table5-7.png"   # 산술연산 메소드
Table5_8  = "images/Table5-8.png"   # 순위의 동률을 처리하는 메소드
Table5_9  = "images/Table5-9.png"   # 축소 메소드 옵션
Table5_10 = "images/Table5-10.png"  # 기술통계와 요약통계
Table5_11 = "images/Table5-11.png"  # 유일값, 값세기, 버리기 메소드
Table5_12 = "images/Table5-12.png"  # NA 처리 메소드
Table5_13 = "images/Table5-13.png"  # fillna 함수 인자

UTC_TimeZone = "images/UTC_Timezone.png"  # UTC 타임존




# 웹크롤링
BDA_WC_10  = "images/Img_BestSandwitch_P1-1.png"
BDA_WC_11  = "images/Img_BestSandwitch_P1-2.png"
BDA_WC_12  = "images/Img_BestSandwitch_P2-1.png"
BDA_WC_20  = "images/img_mcdonalds.png"


main1    = "images/Img_BestSandwitch_P1-1.png"
main2    = "images/Img_BestSandwitch_P1-2.png"
subpage1 = "images/Img_BestSandwitch_P2-1.png"


LOGO_TF_01   = "images/bg_logo_tensorflow_no_shadow_1.png"
ML01_IMG_01  = "images/lab01_Data_Flow_Graph.png"
ML01_IMG_02  = "images/lab01_install_TF_jupyter.png"
ML01_IMG_03  = "images/lab01_install_TF_pycharm.png"
ML01_IMG_04  = "images/lab01_TF_Mechanics1.png"
ML01_IMG_05  = "images/lab01_TF_Mechanics2.png"
ML01_IMG_06  = "images/lab01_Tensor_Ranks1.png"
ML01_IMG_07  = "images/lab01_Tensor_Ranks2.png"

ML02_IMG_01  = "images/lab02_TF_Mechanics1.png"
ML02_IMG_02  = "images/lab02_TF_Mechanics2.png"

ML03_IMG_01  = "images/lab03_tb_graph3_1.png"
ML03_IMG_02  = "images/lab03_tb_graph3_2.png"
ML03_IMG_03  = "images/lab03_tb_graph3_3.png"
ML03_IMG_04  = "images/lab03_tb_graph3_4.png"
ML03_IMG_05  = "images/lab03_tb_graph3_5.png"

ML04_IMG_01  = "images/lab04_1_regression_using_3input.png"
ML04_IMG_02  = "images/lab04_2_hypothesis_using_matrix.png"


ML05_IMG_01  = "images/lab05_Pass_or_Fail.png"
ML05_IMG_02  = "images/lab05_Linear-svm-scatterplot_svg.png"
ML05_IMG_03  = "images/lab05_Logistic-equation.png"
ML05_IMG_04  = "images/lab05_Logistic-curve_svg.png"
ML05_IMG_05  = "images/lab05_Logistic-cost_function.png"
ML05_IMG_06  = "images/lab05_Diabetes_data.png"

ML06_IMG_01  = "images/lab06_Multinomial_classification_for_grade.png"
ML06_IMG_02  = "images/lab06_zoo_animal_type.png"
ML06_IMG_03  = "images/lab06_zoo_data.png"

ML07_IMG_01  = "images/lab07_training_test_data.png"
ML07_IMG_02  = "images/lab07_traing_test_sets.png"
ML07_IMG_03  = "images/lab07_large_learning_rate_overshooting.png"
ML07_IMG_04  = "images/lab07_small_learning_rate.png"
ML07_IMG_05  = "images/lab07_Non-normalized_inputs.png"
ML07_IMG_06  = "images/lab07_Normalized_data.png"
ML07_IMG_07  = "images/lab07_Overfitting.png"
ML07_IMG_08  = "images/lab07_Regularization.png"
ML07_IMG_09  = "images/lab07_mnist_dataset.png"
ML07_IMG_10  = "images/lab07_mnist_traindata.png"


ML09_IMG_01  = "images/lab09_biological_neuron_1.jpg"
ML09_IMG_02  = "images/lab09_biological_neuron_2.jpg"
ML09_IMG_03  = "images/lab09_biological_neuron_3.jpg"
ML09_IMG_04  = "images/lab09_biological_neuron_4.jpg"
ML09_IMG_05  = "images/lab09_biological_neuron_5.jpg"
ML09_IMG_06  = "images/lab09_activation_functions.png"

ML09_IMG_11  = "images/lab09_xor_problem-linearly_separable.png"
ML09_IMG_12  = "images/lab09_neural_net2.jpeg"
ML09_IMG_13  = "images/lab09_cnn.jpeg"
ML09_IMG_14  = "images/lab09_tensorboard.png"
ML09_IMG_15  = "images/lab09_backpropagation.png"

ML09_IMG_20  = "images/lab09_tensorboard_step.png"
ML09_IMG_21  = "images/lab09_tensorboard_01.png"
ML09_IMG_22  = "images/lab09_tensorboard_02.png"
ML09_IMG_23  = "images/lab09_tensorboard_03.png"
ML09_IMG_24  = "images/lab09_tensorboard_04.png"

ML10_IMG_01  = "images/lab10-1_ReLU_01.png"
ML10_IMG_02  = "images/lab10-1_ReLU_02_tensorboard.png"
ML10_IMG_03  = "images/lab10-1_ReLU_03_backpropagation.png"
ML10_IMG_04  = "images/lab10-1_ReLU_04_vanishing_gradient.png"
ML10_IMG_05  = "images/lab10-1_ReLU_05_geoffrey_hinton_summary.png"
ML10_IMG_06  = "images/lab10-1_ReLU_06_sigmoid.png"
ML10_IMG_07  = "images/lab10-1_ReLU_07_Rectified_Linear_Unit.png"
ML10_IMG_08  = "images/lab10-1_ReLU_08_Sigmoid_and_Rectified_Linear_Unit.png"
ML10_IMG_09  = "images/lab10-1_ReLU_09_activation_functions_on_IFAR-10.png"

ML10_IMG_21  = "images/lab10-2_W-init_01_cost_function.png"
ML10_IMG_22  = "images/lab10-2_W-init_02_use_RBM.png"
ML10_IMG_23  = "images/lab10-2_W-init_03_activation_functions_on_IFAR-10.png"

ML10_IMG_31  = "images/lab10-3_dropout_01_overfitting.png"
ML10_IMG_32  = "images/lab10-3_dropout_02_overfitting.png"
ML10_IMG_33  = "images/lab10-3_dropout_03_dropout.png"
ML10_IMG_34  = "images/lab10-3_dropout_04_dropout.png"
ML10_IMG_35  = "images/lab10-3_dropout_05_ensemble.png"


