# Neural-Style-Transfer

![Neural Style Transfer Result](/assets/nst%20result.gif)


# About The Project

## Aim

The aim of this project is to use transfer learning and use a trained neural networks to apply style of an input style image to an input content image. 

## Description

Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image. This requires an already trained Neural Network (VGG-19 in this case) and while the output is being generated, the parameters of the Neural Network stays the same but the pixels in the ouput image are changed every iteration.
[Image Style Transfer Using Convolutional Neural Networks](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf)

## Tech Stack
This section contains the technologies we used for this project.
* [Keras](https://keras.io/)
* [TensorFlow](https://www.tensorflow.org/)
* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)
* [Numpy](https://numpy.org/doc/#)  
* [Google Colab](https://colab.research.google.com/)


# Getting Started

## Prerequisites

- Linux 18.04 or above
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) installed on system

## Installation

1. Navigate to a directory of your choice and download 'environment.yml' and 'script.sh'. enter following commands in terminal:
    > wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/environment.yml

    > wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/script.sh
2. Run the following commands in order. They create a new conda environment, download the necessary dependencies and the source files in new folder 'nst'.<br> 
**Say yes to any installation asked**. the commands might take a while to complete.

    create environment : 
    >conda env create -f environment.yml

    activate environment : 
    >conda activate nst
    
    change script permission :
    >chmod +x script.sh

    run script :
    >source script.sh

3. You're all set! <br> To perform Neural Style Transfer on your own images **you can put the content and style image in the nst folder** and run the following command
    > python3 main.py

    it'll ask you to specify the name of content and style images (**including extensions** like .png, .jpg, etc) and then run the style transfer.
    The **results will be saved in 'res' directory**.
    
    if you run into any error regarding some **DNN library or shared library not found**, run the following command before running main.py
    > export LD\_LIBRARY_PATH=LD_LIBRARY_PATH:$CONDA_PREFIX/lib/


---


As a bonus point you can also **run Style Transfer with hyperparameters of your choice**.

To do that run :

    python3 main.py -h
![](https://i.imgur.com/KUGRB1S.png)

    
for example :
- choose number of iterations : 
    > python3 main.py -n 2000            
    
    runs style style transfer for 2000 iterations.
    default no. of iterations = 5000.

-  choose alpha : 
    > python3 main.py --alpha 1e5

    runs style transfer with alpha = 1e5.
    default alpha = 1e4.
- choose beta value : 
    > python3 main.py --beta 1e-1           

    runs style transfer with beta = 1e-1.
    default beta = 1.

- choose learning rate :     
    > python3 main.py -l 20         
      
    runs style transfer with learning rate = 20.
    default learning rate = 5.


# Theory and Approach

Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.

The principle of neural style transfer is to define two distance functions, one that describes how different the content of two images are, Lcontent, and one that describes the difference between the two images in terms of their style, Lstyle. Then, given three images, a desired style image, a desired content image, and the input image (initialized with the content image), we try to transform the input image to minimize the content distance with the content image and its style distance with the style image.

![NST flowchart 1](/assets/NST.png)

In summary, we’ll take the base input image, a content image that we want to match, and the style image that we want to match. We’ll transform the base input image by minimizing the content and style distances (losses) with backpropagation, creating an image that matches the content of the content image and the style of the style image.

![NST flowchart 2](/assets/Flowchart2.png)




# Results

![NST result](/assets/nst%20result.gif)
***

# Future Works

We enjoyed working on GANs during our project and plan to continue exploring the field for further applications and make new projects. Some of the points that We think this project can grow or be a base for are listed below.

 1. Trying different databases to get an idea of preprocessing different types of images and building models specific to those input image types.
 2. This is a project applied on individual Image to Image translation. Further the model can be used to process black and white sketch video frames to generate colored videos.


# Contributors
* [Labeeb Asari](https://github.com/labeeb-7z)
* [Lakshaya Singhal](https://github.com/Greyless)

# Acknowledgements and Resources
* [SRA VJTI](https://www.sravjti.in/) Eklavya 2021  
* Referred [this](https://www.tensorflow.org/) for understanding the use of tensorflow
* Completed [these](https://www.coursera.org/specializations/deep-learning) 3 courses for understanding Deep Learning concepts like Convulational Neural networks and learnt to make a DL model
* Referred [this](https://www.tensorflow.org/tutorials/generative/pix2pix) for understanding code statements
* Special Thanks to our awesome mentors [Neel Shah](https://github.com/Neel-Shah-29) and [Pratham Shah](https://github.com/shahpratham) who always helped us during our project journey

# License
The [License](LICENSE) used in this project.