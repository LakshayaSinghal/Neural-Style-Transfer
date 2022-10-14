import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
#%matplotlib inline
from tensorflow.keras.preprocessing import image
from tensorflow.keras import models 
from tensorflow.keras import losses
from tensorflow.keras import layers
from tensorflow.keras import backend as K
import time
import functools
import sys
import getopt

#print(tf.test.is_gpu_available())


#define layers from which we're extracting features
content_layers = ['block5_conv2'] 

style_layers = ['block1_conv1',
                'block2_conv1',
                'block3_conv1', 
                'block4_conv1', 
                'block5_conv1'
               ]

layer_names = content_layers+style_layers
num_content_layers = len(content_layers)
num_style_layers = len(style_layers)
