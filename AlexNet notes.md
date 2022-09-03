# AlexNet paper

Until recently, datasets of labelled images were relatively small. But, objects in realistic setting exhibit connsiderable variability, so we need a huge training data set to teach.
For eg, ImageNet, which consists of over 15 million labeled high res images in over 22,000 categories.

We also need a model with large learning capacity. There is a lot of data we dont have and to compensate for that we need to have a lot of prior knowledge. CNN constitute one such class of models. CNN models have much fewer connections and parameters and are thus, easier to train.

## AlexNet
 
 1. One of the largest neural networks on the subsets of ImageNet
 2. 5 convolutional layers and 3 fully connected layers
 3. Uses ReLU non-linearity because it does not saturate which makes sure the gradient descent doesn't slow down.
 4. Trained on 2 GTX 580, 3GB.
 5. The parallelization scheme puts half the kernels on each GPU. ALso the GPUs communicate only in some layers.
 6. ReLU dont need Normalization to prevent saturating but local normalization scheme aids generalization. Uses Local Response Normalization.
 7. Pooling is generally done without overlapping where stride = filter size, but here overlapping pooling was used and it was found that top1 and top5 error rates reduced by 0.4% and 0.3% respectively.
 8. Output is given by a 1000 way Softmax layer.
 9. The kernels of the second, fourth, and fifth convolutional layers are connected only to those kernel maps in the previous layer which reside on the same GPU.
 10. Overfitting prevention measures:
     
     a. Data Augmentation: From each 256x256 image, 5 224x224 patches were taken(4 corners and 1 center) and they were also flipped horizontally. Also, PCA was performed on the set of RGB pixel values.
     
     b. Dropout: For each training epoch, nodes were randomly dopped. This technique reduces complex co-adaptations of neurons, since a neuron cannot rely on the presence of particular other neurons. Used only in first 2 fully connected layers here.
 11. Stochastic gradient descent was used with a batch size of 128, momentum of 0.9.