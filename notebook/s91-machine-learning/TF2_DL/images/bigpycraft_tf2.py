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


MAIN    = "images/tf2_main.png"
IMG_01  = "images/tf2up_ml.png"
IMG_02  = "images/tf2_ecosystem.png"
 

LOGO_TF_01   = "images/bg_logo_tensorflow_no_shadow_1.png"
ML01_IMG_01  = "images/lab01_Data_Flow_Graph.png"
ML01_IMG_02  = "images/lab01_install_TF_jupyter.png"
ML01_IMG_03  = "images/lab01_install_TF_pycharm.png"
ML01_IMG_04  = "images/lab01_TF_Mechanics1.png"
ML01_IMG_05  = "images/lab01_TF_Mechanics2.png"
ML01_IMG_06  = "images/lab01_Tensor_Ranks1.png"
ML01_IMG_07  = "images/lab01_Tensor_Ranks2.png"
ML01_IMG_10  = "images/lab01_tboard_10.png"
ML01_IMG_11  = "images/lab01_tboard_11.png"
ML01_IMG_12  = "images/lab01_tboard_12.png"
ML01_IMG_21  = "images/lab01_tboard_21.png"
ML01_IMG_22  = "images/lab01_tboard_22.png"

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

ML11_IMG_41  = "images/lab11_colormaps.png"
ML11_IMG_42  = "images/lab11_simple_cnn.png"
ML11_IMG_43  = "images/lab11-5_cnn_tf_layers.png"
ML11_IMG_44  = "images/lab11-5_cnn_ensemble_layers.png"
ML11_IMG_45  = "images/lab11-5_cnn_ensemble_prediction.png"
ML11_IMG_46  = "images/lab11-6_cnn_ensemble_exercise.png"
