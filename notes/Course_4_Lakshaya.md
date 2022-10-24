# Convolutional Neural Networks

## Convolution over RGB images (3d)

![3d convolution](/Deep%20Learning/assets/3d%20convolution.png)

![multiple filters](/Deep%20Learning/assets/Multipple%20filters.png)

## Building a CNN

![A single layer](/Deep%20Learning/assets/a%20single%20layer%20of%20cnn.png)

CNNs are less prone to over fitting

![Notations](/Deep%20Learning/assets/Notations.png)

![Example of CNN](/Deep%20Learning/assets/example%20of%20cnn.png)


Types of layer in CNN:

 1. Convolution
 2. Pooling
 3. Fully connected


## Pooling

### Max pooling

![Max pooling](/Deep%20Learning/assets/max%20pooling.png)

It takes a certain area and only keeps the highest value in the area.

It helps make the image smaller and keep only important features and discards less imp features.

For multiple channels, max pooling is done individually on each channel.

### Average pooling

Not used often, just finds average of a certain area.


![CNN example](/Deep%20Learning/assets/CNN%20example.png)


## Why convolutions?

Convolutions help us make the image smaller so we are not passing huge amounts of data to our neural network.
It also decreases the amount of parameters.

![Why covolutions](/Deep%20Learning/assets/Why%20convolutions%3F.png)


## LeNet-5

![LeNet-5](/Deep%20Learning/assets/lenet5.png)


## AlexNet

![AlexNet](/Deep%20Learning/assets/AlexNet.png)

Local response normalization takes all the channels for a particular height and width and normalizes them. It doesn't have a huge impact so its not in use as much.

## VGG-16

A very simplified network.

![VGG16](/Deep%20Learning/assets/VGG16.png)

## ResNet

ResNet uses a shortcut.

The activats of laye a[l] are added to z[l+2] and then tis sum is passed through the activation function to get a[l+2].

![ResNet](/Deep%20Learning/assets/ResNet.png)

![ResNet2](/Deep%20Learning/assets/resnet2.png)

We see that making your networks deeper could hurt the accuracy.

## 1x1 Convolutions

![1x1 convolution](/Deep%20Learning/assets/1x1%20convolutions.png)

It allows us to chnage the number of channels. It also helps us add non-linearity.

## Inception network

The idea is that instead of using one filter or pooling, you can use all of them and concatenate all the outputs.

![Inception Network](/Deep%20Learning/assets/Inception%20network.png)

![Inception problem](/Deep%20Learning/assets/inception%20problem.png)

There is a problem of omputational cost since for eg in this case we end up having to do 120million multiplications.

To solve this, we will use 1x1 convolution to decrease the number of channels.

![Inception 1x1](/Deep%20Learning/assets/inception%201x1.png)

Inception Network is just the inception module repeated many times.

## MobileNet

Low compute enviroments

To decrease the number of mltiplications we use **Depthwise Seperable Convolution**

First we convolve layer by layer for each filter.

![Dephtwise convolution](/Deep%20Learning/assets/depthwise%20comvolutiom.png)

Then we do pointwise convolution to finally get a single channel output that we gety from a 3d convoltion.

![Pointwise Convolution](/Deep%20Learning/assets/POintwise%20convolution.png)

## MobileNetV2

It allows for a richer set of computations, while also keeping the memory small.

![MobileNetV2](/Deep%20Learning/assets/MobileNetv2.png)


## EfficientNet

Helps us scale up or down depending upon the resources of device being used.
We can change the resolution, change the depth or change the width of the neural network(size of the kernels and filters).


# Object Detection

## Object Localization

![Object Localization vs Detection](/Deep%20Learning/assets/Object%20localization%20vs%20detection.png)

Lets say we need to localize an object. For that we are gonna need 4 more outputs from our neural network namely bx, by, bh and bw. bx and by gives us the center of the box need to be drawn and bh and bw give us the width and the height of the box.

We will also need another output to detect if there are objects. Lets call it Pc. So, the output the following:

![Objecgt Localization](/Deep%20Learning/assets/Object%20localization.png)

The loss function used here was square loss for simplicity, we can use different loss functions for different outputs like log loss for c1 c2 and c3, square loss for bx by bh bw and logistic regression loss for Pc.

Also notice how for Pc = 0, we dont care about the other outputs so they are not included in the loss function.


## Landmark detection

We might need to detect points in the imag say for example the corner of the eye, lips, shoulder, elbows.

Detecting the position of such festures is the basis of AR technology, ood detection, position detection,etc.

We need to add outputs for lx and ly which the position of the desired location. we will need a labelled set with the location already labelled to train the network.

![Landmark detection](/Deep%20Learning/assets/Landmark%20Detection.png)

## Object Detection

### Sliding Windows
  
 In this, we essentially pass a small window over the image to get sections of the image which we pass through the CNN individually.
 
 Not very efficient but can be made more efficient by using convolution, we will get a grid whose each pixel will correspond to a square box on the image. The activation will determine the location of the box on the original image.

### Bounding Box prediction YOLO algorithm

 ![YOLO](/Deep%20Learning/assets/YOLO.png)


## Intersection Over Union

It gives us a measure of how accurate our bounding box is. 

![INtersection over union](/Deep%20Learning/assets/INtersection%20over%20union.png)

We can take ratio = 0.5 for benchmark of accuracy or for more strict enviroments, we can take a higher ratio.

## Non-Max supression

Sometimes, the algorithm may detect the same object multiple times leading to different boxes overlapping over the same object.

Each box has a prpobability of being current so for Non-max suppression we keep the box with the highest probability and supress the nearby boxes with low probability.

![Non-Max supression Algorithm](/Deep%20Learning/assets/non-max%20supression%20algorithm.png)

## Anchor Boxes

This helps us when the midpoints of 2 objects coincide. So for training, we need to add another set of outputs where each set corresponds to an anchor box of different shape.

![Anchor box algorithm](/Deep%20Learning/assets/Anchor%20boxes.png)

![Anchor box example](/Deep%20Learning/assets/Anchor%20boxes%20example.png)

There are a few cases this doesnt handle well, example if there are 3 overlapping objects instead of 2 or the shape of the 2 anchor boxes is the same.

## YOLO algorithm

![YOLO with anchor boxes](/Deep%20Learning/assets/YOLO%20with%20anchor%20boxes.png)

![YOLO non max supressed](/Deep%20Learning/assets/YOLO%20non%20max%20supressed.png)


## Semantic Segmentation with U-Net

This is for making a pixel by pixel detection of an object.
We take every single pixel and label is applied corresponding to the class it belongs to.

## Transpose Convolution

It gives us an output that is bigger than the input, for eg, a 2x2 image convolved with a filter of size 3x3 gives an output of 4x4.

Here, instead of putting the filter on the input, we put the filter on the output.

![Transpose convolution](/Deep%20Learning/assets/Transpose%20convoltuoin.png)

The kernel is multiplied by each pixel and the multiplied kernel is placed on the output.
Here, the stride taken is 2 to be able to completely fill the output.
For places wehre the output overlaps, the outputs are added.

## U-Net Architecture

![U-Net Architecture](/Deep%20Learning/assets/U_Net%20Architecture.png)


# Face Recognition

For face recognition, we genrally have only one face for each person to compare to and we dont have a large database for each person, therefor we need a fucntion **d** that gives us the degree of difference between the data image and the input image. For this, we use Siamese NEtwork

## Siamese Network

We will use a ConvNet and obtain a vector in the end that is not passed through softmax since we are no classifying.

This vector will be compared when we want to conmpare 2 images. The function d is given as follows:

![Siamese Network](/Deep%20Learning/assets/siamese%20network.png)

We will use backprop to obtain parameters that satisy the goven conditions.

![Learning Objectives](/Deep%20Learning/assets/LEarning%20Objectives%20face%20recog.png)

We want the d(A,P) to be smaller than d(A,N). To further intensifying the divide, we add alpha to d(A,N) which ensures that the difference is atleast equal to alpha.

Triple function is defines using 3 images - anchor, positive example and negatove example.

![Loss Function](/Deep%20Learning/assets/Loss%20function%20face%20recog.png)

We can have multiple sets for the same person while training.
To train we need to choose triplets that are "hard" to train on. If chosen randomly, d(A,P) will almost always be smaller than d(A,N).

Another way to train the neural network is as follows:

Take 2 identical neural netoworks and pass the images to be compared to each of them individually. Take the 128 lnong vectors from both neural networks and use this 256 long vector to apply sigmoid to it. The sigmoid will be closer to 1 if the faces match and closer to 0 if they dont.

The activationn applied is as follows:

![Binary Classification](/Deep%20Learning/assets/Binary%20classification%20face%20recog.png)


# Neural Style Transfer

We know that earlier stages of a CNN pick up more basic features like lines and the later layers of the CNN pick up more complex features like tires, eyes, legs, etc.

Neural style transfer requires a style image and a content image.

## Cost Function

![NST cost function](/Deep%20Learning/assets/NST%20cost%20function.png)

We start with a completely random image and slowly, using gradient descent, take the image closer and closer to both the content image and the style image while reduing the loss.

![NST process](/Deep%20Learning/assets/NST%20process.png)

The features for both style and content are picked up from different layers becaue different layers detect different levels of complexity.

If the features of content were detected from say layer 'l', the cost function wrt to the generated image will be calculate using layer 'l' of both the content image and the generated image.

![Content Cost funcition](/Deep%20Learning/assets/NST%20content%20cost%20function.png)

When we consider style, a style usually is defined by the relation of one feature of the style to the other.

To capture this, we need to consider 2 channels in a layer of CNN. Each channel detects different features and if for the features of these 2 channels, if they occur together, they are correlated. So, we need to find what features are correlated and which ones aren't.

To compare the Generated image and the Style image, we need to compare the same 2 channels in both images to see if the correlation between the 2 channels is the same.

![NST style matrix](/Deep%20Learning/assets/NST%20style%20matrix.png)

Fr cost function, the authors used a Normalization constant.

![Style cost function](/Deep%20Learning/assets/style%20cost%20function.png)

We get more pleasing results if we use different layers, so the cost function becomes:

![style cost using multiple layers](/Deep%20Learning/assets/Style%20cost%20function%20using%20multiple%20layers.png)
