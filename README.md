# Neural-Style-Transfer

![Neural Style Transfer Input](/assets/ryuk%20starry%20night%20input.png)

![Neural Style Transfer output](/assets/starry-night%20result.png)

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


# Theory and Approach

Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but “painted” in the style of the style reference image.

The principle of neural style transfer is to define two distance functions, one that describes how different the content of two images are, Lcontent, and one that describes the difference between the two images in terms of their style, Lstyle. Then, given three images, a desired style image, a desired content image, and the input image (initialized with the content image), we try to transform the input image to minimize the content distance with the content image and its style distance with the style image.

In summary, we’ll take the base input image, a content image that we want to match, and the style image that we want to match. We’ll transform the base input image by minimizing the content and style distances (losses) with backpropagation, creating an image that matches the content of the content image and the style of the style image.

# Results

![example1in](/assets/cat%20abstract%20input.png)
![example1out](/assets/cat%20abstract%20result.png)
***
![example2in](/assets/green%20input.png)
![example2out](/assets/green%20result.png)
***
![example3in](/assets/ryuk%20abstract%20inout.png)
![example3out](/assets/ryuk%20abstract%20output.png)
***
![example4in](/assets/sketch%20flower%20input.png)
![example4out](/assets/sketch%20flower%20output.png)
***
![example5in](/assets/ryuk%20starry%20night%20input.png)
![example4out](/assets/starry-night%20result.png)
***

# Future Works

We enjoyed working with Neural Networks during our project and plan to continue exploring to make new projects. We are particularly interested in exploring GANs to achieve Neural Style Transfer and to make new projects using GANs.

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