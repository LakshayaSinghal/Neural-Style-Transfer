# Generative Adversial Network (GAN)

GANs are deep neural networks net architectures comprised of two neural networks competing aginst one another.
It is used to generate data that mimics a given distribution.

Two classes of models in machine learning:
1. **Discriminative** : It is used to discriminate between two different classes of data.
2. **Generative** : A generatuve model G to be trained on training data X sampled from same true distribution D is the one which, given same standard random distribution Z produces a distribution D' which is close to D according to some closeness metric. Mathematically, Z~Z maps to a sample G(Z)~D'.

![GANs Structure](/GANs/Notes/assets/GANs%20structure.png)


The discriminator produces an output of 0 if the image is fake and 1 if the image is real. Our goal is to train the genrative model such that it fool sthe discriminator and gives an output of 0.5.

## Loss function

We use the binary cross entropy function for both the true data set and the generated data set.

![Loss function](/GANs/Notes/assets/loss%20function%20for%20GAns.png)

The labels for the true data set is 1, This is y so putting this in the binary cross entropy function, we get:

![Loss function for true data set](/GANs/Notes/assets/loss%20function%20for%20true%20data%20set.png)


Similarly, the labels for the data coming from generative network is 0, putting this in the loss function:

![Loss function for geenrated data set](/GANs/Notes/assets/loss%20function%20for%20generated%20data%20set.png)

The final loss function is the addition of the above 2 loss functions.

Objective of the discriminator is to correctly classify fake vs the real data set, for this the above oss functions should be maximized.

The task of the generator on the other hand, is to minimize the loss function.

### Choose the best discriminator:

 ![Best discriminator](/GANs/Notes/assets/best%20discriminatorr.png)

 For proof, refer to the following video:

 [Proof for best discriminator](https://www.youtube.com/watch?v=pPlnx9D8WZQ&list=PLdxQ7SoCLQAMGgQAIAcyRevM8VvygTpCu&index=3)

 The optimal value of D is not practically calculable becuase pdata(X) is not known in priori.

 The role of generator is reverse of that of D i.e. min so the optimaql G that minimizes the loss function occurs when D = D*g. So we get optimal G* as:

 ![Optimal G*](/GANs/Notes/assets/optimal%20G*.png)