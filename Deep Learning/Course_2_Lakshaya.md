

## Bias and Variance

![Bias and variance](/Deep%20Learning/assets/Bias%20And%20variance.png)

![High Bias and High Variance](/Deep%20Learning/assets/high%20bias%20and%20variance.png)


### How to fix Bias and Variance?

![Steps to Fix](/Deep%20Learning/assets/steps%20to%20fix.png)


## Regularization

![Regularization](/Deep%20Learning/assets/Regulariztion.png)

![Regularization 2](/Deep%20Learning/assets/regularization%202.png)


## Dropout

![Dropout](/Deep%20Learning/assets/Dropout.png)


## Normalization

![Normalization](/Deep%20Learning/assets/NOrmalization.png)

If we use unnormalized x, we get a cost function that is more like a swuished out bar. The gradient descent oscillates back and forth a lot so the learning rate has to be very low.

## Vanishing or exploding gradients

When we have a very deep neiral networks with alinear activationg function for each layer, if the weigts of each layer was a little larger than the identity matrix, each subsequent layer would increase the value for Z, this leads to an exponential increase in the value of y^. This is called **Exploding Gradient**.

Similarly, if the weights were a littel smaller than identity matrix, the value for y^ will decrease exponentially. This is called **Variation Gradient**.

This leads to an increase or decrease exponentially for the gradients sent back. this makes training difficult.

### Solution:
 #### Weight initialzation
 In this method we set the initial values of weights close to 1, so the porblem of exploding or vanishing decreses.
 
 ![Weight initialization](/Deep%20Learning/assets/Weight%20initialization.png)


## Gradient checking

This allows to get an idea for how accurate our logic involving forward propagation adn backpropagation is. If the th evalues of approx d(theta) and actual d(theta) dont match, we can assume that we have a bug somewhere.

![Gradient Checking](/Deep%20Learning/assets/Gradient%20checking.png)


## Mini-Batch Gradient descent

Batch gradient referes to when we use the entire batch at the same time to train the network.

Mini-batch graddient descent refers to when we divide the batch into multiple mini-batches (call them X{t} where t refers to the batch number).

This is much faster than batch gradient descent.

![Graph mini batch](/Deep%20Learning/assets/Mini%20batch%20gradient%20descent%20graph.png)

Batch size:

![Mini batch size](/Deep%20Learning/assets/mini%20batch%20size.png)

## Exponentially weighted average

![Exponentially weighted average](/Deep%20Learning/assets/Exponentially%20weighted%20average.png)

When we actually implement moving average and B is 0.98, the curve startes lower than expected. see the green curve (expected) and the purple curve (actual).

![bias correctiom](/Deep%20Learning/assets/bias%20correction.png)

Lets see how to fix it.

![Bias correction](/Deep%20Learning/assets/bias%20correction%202.png)

## Gradient Descent with Momentum

We want oscillations to be faster in the direction towards the minima adn we want the oscillations to be slower in the direction perpendicular to the minima.

![gradient descent with momentum](/Deep%20Learning/assets/gradient%20descent%20with%20momentum.png)


## RMSprop

It can also speed up gradient descent.

![RMSprop](/Deep%20Learning/assets/RMSprop.png)

To ensure the denominators are not zero, we sometimes add a very small value (epsilon).

## Adam Optimization Algorithm

It combines momentum and RMSprop.

ADAM stands for Adaptive moment estimation.

![Adam Optimization](/Deep%20Learning/assets/Adam%20Optimization.png)

## Learning rate decay

![Learning Rate Decay](/Deep%20Learning/assets/Learning%20rate%20decay.png)

![Learning rate decay other methods](/Deep%20Learning/assets/Learning%20rat%20edecay%20other%20methods.png)

## Problems with Local Optima

The optima are not concave points strictly, they can also be saddle points (shaped like a saddle).

Also plateaus can exist which a huge region where slope stays close to zero for large space.
They can make learning slow.


## Usin Appropriate Scale to pick hyperparameters

![logarithmic](/Deep%20Learning/assets/hyperparameter%20selection%20random%2C%20logarithmic.png)

![Hyperparameters for exponentially weighted averages](/Deep%20Learning/assets/Hyperparameters%20for%20exponentially%20weighted%20averages.png)

When Beta is close to 1, small changes can have large effects. SO the sampling process is made more dense when Beta is close to 1.

## Implementing Batch Norm

![Implementing Batch Norm](/Deep%20Learning/assets/Implementing%20Batch%20Norm.png)

![Batch norm to a network](/Deep%20Learning/assets/Batch%20Norm%20to%20a%20netwrok.png)

![Batch Norm for Mini batches](/Deep%20Learning/assets/BAtch%20norm%20for%20mini%20batches.png)

We can ignore db here beacuse due to batch norm beta is added which takes care of db.

![Batch Norm Gradient Descent](/Deep%20Learning/assets/batch%20norm%20gradient%20descent.png)

Batch Norm works because it makes weights in the later layers more robust to chnages than the layers in earlier layers.

Batch Norm also has a small regularization effect.

(Little doubts, go through once again)

## Softmax

![Softmax](/Deep%20Learning/assets/Softmax.png)

![Loss function](/Deep%20Learning/assets/Loss%20function%20for%20softmax.png)

![Gradient descent](/Deep%20Learning/assets/Gradient%20descent%20for%20softmax.png)

While using frameworks, we dont need to worry about back prop, it is taken care of by the framework.
