import tensorflow as tf

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

import os
os.environ['TF_GPU_ALLOCATOR']='cuda_malloc_async'

model = VGG16()


def getprediction(imagepath) :
    image = load_img(imagepath,target_size = (224,224))
    image = img_to_array(image)
    image = image.reshape(1,image.shape[0],image.shape[1], image.shape[2])
    image = preprocess_input(image)
    prediciton = model.predict(image)
    label = decode_predictions(prediciton)
    print(label)
    # label = label[0][0]
    return label