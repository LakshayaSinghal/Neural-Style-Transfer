# VGG paper

Many attempts have been made to improve on ALexNEt. The best perfomring submissions used smaller window size and smaller stride of the first convolutional layer. Another line of improvements dealt with training
and testing the networks densely over the whole image and over multiple scales. Another important parameter of VGG is its depth. Different models with different number of layers were created.

## VGG

 1. INput size is 224x224 RGB image. The preprocessing done is that the mean RGB value is subtracted, computed on the training set on each pixel.
 2. Passed through multiple filters, all being 3x3. In one configuration 1x1 was also used.
 3. Convolutuion stride is fixed at 1.
 4. Padding is such that the size of the image doesn't change or 'same' type of padding.
 5. Spatial pooling follow some of the conv. layers. MAx pooling is performed over 2x2 window with a stride of 2
 6. 3 fully connected layers follow - 4096,4096, 1000.
 7. Dropout with a probability of 0.5 is used after the first 2 FC layers.
 8. The final layer is the softmax layer.
 9. All hidden layers use ReLU activation.
 10. Only one of the networks use local response normalization and th eparameters are samea s ALexNet.
 11. The training was regularised by weight decay (the L2 penalty multiplier set to 5 · 10 −4 )
 12. The initialisation of the network weights is important, since bad initialisation can stall learning due to the instability of gradient in deep nets. To circumvent this problem, we began with training the configuration A (Table 1), shallow enough to be trained with random initialisation. Then, when training deeper architectures, we initialised the first four convolutional layers and the last three fully- connected layers with the layers of net A (the intermediate layers were initialised randomly). We did not decrease the learning rate for the pre-initialised layers, allowing them to change during learning.

 ![VGG networks](/VGG/assets/Screenshot%20from%202022-09-14%2023-49-24.png)
