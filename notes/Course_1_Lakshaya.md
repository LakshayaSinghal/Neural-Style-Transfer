# Neural Networks

[Andrew NG course 1](https://youtube.com/playlist?list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0 "Andrew NG course 1")

Neural Networks use supervised learning where the ntwork needs to be trained using predefined, labeled data so the netwrok is tuned to make predictions. The performance of the network depends upon the complexity and scale of network and also the amount of data used to train it.

![Performance vs Data](/Deep%20Learning/assets/Data%20vs%20Performance.png "Performance vs Data")

We have also seen algorthmic innovations in recent years that make the neural networks faster and better.

For Neural netowrks, we use binary classification, where 1 means true and 0 means false.

For eg, if a cat image was to be identified, a 1 would mean it is a cat image and a 0 would mean it is not a cat image.

For training, lets say our data set includes m cases and each case has nx data, then our input is a matrix of dimensions (nx, m) where every case is its own column. A matix of dimension (m, nx) can also be used but the former is easier to implement
 
![Input matrix](/Deep%20Learning/assets/input%20matrix.png "Input matrix")

For output, we need a single output for each case {0,1} hence our output set will be a matrix of dimension (1,m).
 
![Ouput Matrix](/Deep%20Learning/assets/output%20matrix.png)

## Logistic Regression

The output tells us the probability of a certain case. Therefore, the out y^ lies between 0 and 1.

We can use logistic regression only but that doesn't necessarily give us values between 0 and 1. Hence, we also make use of the sigmoid function. It takes input of any real number and maps it between 0 and 1.

![Sigmoid Function](/Deep%20Learning/assets/Sigmoid%20function.png)

The function used for this is as follows

![y^ Function](/Deep%20Learning/assets/function%20used.png)

## Loss Function

We need to define a loss function that gives a measure of how good our network is. Its parameters are the output expected and the output recieved.    L(y^,y).

We can use the squared difference but for easier optimization, we use the following loss function

**L(y^,y) = -[ylog(y^)+(1-y)log(1-y^)]**

The loss function is defined for one trainig example but we need a measure of how well the netwrok performs for all the training examples. Hence, we define a **Cost Function**.

![Cost function](/Deep%20Learning/assets/cost%20function.png "Cost function")

We want to fine the w,b for which the cost function is minimum.

## Gradient Descent

Our cost function using log has made the function a convex function. On graphing, we get a single bowl. We get a single minima instead of multiple local minima.

![Cost function graph](/Deep%20Learning/assets/cost%20function%20graph.png "COst function Graph")

The way gradient descent works is that we take a random value of w and b and then we step down in the steepest downhil direction. After multiple iterations we reach the global optimum or atleast close to it.

![Gradient Descent](/Deep%20Learning/assets/Gradient%20descent.png "Gradient Descent")


**Recap:**

![Recap](/Deep%20Learning/assets/Logistic%20regression%20formulae.png)

We know that to the network, a weighted sum of the previous data is taken, which is then passed to a sigmoid function, using which we get a Loss function for back propagation.

Now to tune the network, we can change the weights. To minimize the loss function, we need to know how the loss function changes by changing each of the weights. Hence, we find the derivative of the Loss function wrt to each weights. The derivation is given below for one training example.

![Logistic Regression Derivatives](/Deep%20Learning/assets/Logistic%20Regression%20Derivatives.png)

For m examples we take an average as mentioned above (Cost function).

![cost function 2](/Deep%20Learning/assets/cost%20function%202.png)

Similarly, for backpropagation, the derivative of the cost function wrt to each weight is found and then an average of all the derivatives is taken.

![Derivative for m example](/Deep%20Learning/assets/m%20example%20derivative.png)

Algorithm:

![Algorithm step 1](/Deep%20Learning/assets/algorithm%20for%20derivative.png)

![Algorithm step 2](/Deep%20Learning/assets/algorithm%20for%20derivative%20step%202.png)

One iteration of the above steps gives us a single step of gradient descent. All the steps need to be repeated all over again and again for each step of the gradient descent to get us closer and closer to the optima.

The problem with the above method is that it uses 2 for loops for one iteration, one to loop through all the data and second to loop through all the weights. Explicit for loops make the algorithm extremely inefficient and make the program run slower, especially for larger and larger data sets.

There is a set of techniques call **Vectorization** that allow us to get rid of explciit for loops.


# Vectorization

We know that we need to find the weighted sum for a list of data. If we do it in normal way, we will need a for loop to loop through all the weights and the values and then we need to multiply and add them.

![Non vectorized](/Deep%20Learning/assets/Non%20vectorized.png)

But, if we vectorize our data (matrices), we can do the multiplication much faster in python (numpy).

![Vectorized](/Deep%20Learning/assets/Vectorized.png)

We can understand that the weigth matrix needs to be transposed for multiplication.

For vectorized multiplication, the numpy method is as follows

![Vectorized numpy](/Deep%20Learning/assets/vectorized%20numpy.png)

The difference in time taken by both methods can be of factor 500, which gives huge savings in time.

Numpy method:

![Numpy Method](/Deep%20Learning/assets/Implement%20logistic%20regression%20using%202%20lines%20of%20codes.png)


Gradient Descent:

![gradient Descent](/Deep%20Learning/assets/gradient%20descent.png)


# Neural Networks

![Neural Network](/Deep%20Learning/assets/Neural%20Netwrok.png)

Input layer is numebred layer 0. Its not counted when counting number of layers.

Each node has different weights associated with it, so instead of a 1d matrix as seen in Logistic Regression, we have a 2d matrix where each row in the transpose corresponds to the weights for a different node.

![Weights matix](/Deep%20Learning/assets/Weights%20matrix.png)

The matrices for Z and A will also be 2d. Each column in the matrix will correspond to different training example and each row will correspond to the nodes for the same example.

![Z and A 2d matrix](/Deep%20Learning/assets/Z%20and%20A%20matrices.png)

## Activation Function

We have been using sigmoid but other have applications too.

There is also **tanh** function which naps from m-1 to 1. It is just a sigmoid function but shifted.
Tanh is almost always superior, one exception is the output layer where we want data to be mapped between 0 to 1.
Also, the mean of tanh is closer to 0 which is helpful.

One problem with both these functions is that as the input value reached very high negative or positive values, the slope tends to zero so the gradient descent decreases.

Another popular function is ReLU.

![ReLU](/Deep%20Learning/assets/ReLU.png)

The derivative of this function is 1 when value is greater than 0 and the derivative is 0 when the value is smaller than 0.

As a rule of thumb, when we want binary classification (output layer), we use Signmoid or else ReLU is an increasingly popular choice for an activation function.

![Activation Functions](/Deep%20Learning/assets/Activation%20functions.png)


**Why do we need activation functions?**

If we elminate activation functions, we will just have linear functions no matter how large our model is. FOr eg, in a 2 layer model, if our hidden layer is linear and our output layer uses sigmoid function, it is no different than Logistic Regression. The hidden layer is useless since the composition of 2 or more linear fundtions is a linear function.

Linear activation functions could be usefull when we are doing regression, eg to predict pricing of house which takes values other than 0 to 1.

Sigmoid derivative:

![SIgmoid Derivative](/Deep%20Learning/assets/Sigmoid%20Derivative.png)

Tanh derivative:

![Tanh Derivative](/Deep%20Learning/assets/tanh%20derivative.png)

ReLU derivative:

![ReLU derivative](/Deep%20Learning/assets/ReLU%20derivative.png)


The formulas remain the same except the dimension of w,b,A,Z,dw,db, etc changes to accomodate all the nodes.

# Random Initialization

For logistic Regression, initializing all the weights to 0 worked but it wont work for a neural network.

This is because when all weights are 0, activation for 2 different nodes become 0 and subsequently so do the dw1 and dw2. This leads to the new weights being equal. This means no matter how much we optimize, these nodes will compute exactly the same.

The solution is to initialize the parameters randomly.

We usually take a random value and multiply it by 0.01 since we usually want a small starting value as we know larger values on the sigmoid or tanh functions lead to smaller and smaller derivatives.


# Deep L-Layer Neural Network

A netwrok with multiple layers is **deep** while a networ with less layers is called **shallow**

Notations : 

![Notation](/Deep%20Learning/assets/notation.png)

## Forward Propagation

![Forward Propagation](/Deep%20Learning/assets/forward%20propagation.png)

When dealing with such large , matrices, get your dimensions right.

[Get your dimensions right](https://www.youtube.com/watch?v=yslMo3hSbqE&list=PLkDaE6sCZn6Ec-XTbcX1uRg2_u4xOEky0&index=38)

![Forward Propagation for l layer](/Deep%20Learning/assets/Forward%20Propagation%20for%20l%20layer.png)

## Intuition about Deep Layer Learning

![Intuition](/Deep%20Learning/assets/Intuition.png)

The early layers detect more basic features and the later layers pick up more complex features.

## Backward Propagation

![Backward Propagation](/Deep%20Learning/assets/Backward%20Propagation.png)


