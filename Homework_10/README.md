# Homework 10 - Tensorflow

The deadline of this homework is on **Friday, 1st of July, 23:59:00 UTC+2**.

This week's homework is about tensorflow.
Be sure to install pandas in your environment.

    conda install tensorflow

or

    pip install tensorflow

No additional libraries are allowed for this homework. All the necessary imports are already there. As always, you can run `pytest` files locally before pushing to see if you have passed the task and homework.

The tasks of this week are:

- Load Data: `cifar_classifier.py`
- Create Model: `cifar_classifier.py`
- (optional) Play Around: Its best if you use a Jupyter notebook, so that you do not loose a trained model.


## 1. Load Data

In the file `cifar_classifier.py` you can find a function called `load_cifar10()` which is supposed to load the Cifar10 dataset as training and test data.

- Load the cifar10 dataset from the tensorflow library
- The images are represented as three dimensional pixels with RGB-values. Normalize these values, so that they are in the interval [0, 1]. When training a neural network it is almost always a good idea to do that.
- The labels are integers from zero to nine, that represent the 10 classes of images. They should be one-hot encoded, meaning that they are translated into a vector (1D array) with the length of the number of classes. The value of that vector, whose index is the value from the original encoding is supposed to be one, all others are supposed to be zero.
**Example:**

0 will become [1 0 0 0 0 0 0 0 0 0]

4 will become [0 0 0 0 1 0 0 0 0 0]

**Hint:** There is a tensorflow function for doing exactly that.

## 2. Create Model

Your task is to implement the architecture that is described below with tensorflow's functional API.

- The input layer has to be able to take the cifar10 images as input. Initialize it with the required shape. Remember, that each pixel consists of three values
- The first hidden layer is supposed to be a convolutional layer with 32 filters, a 3 x 3 kernel, relu as activation function and a stride of 1 on each axis.
- The second hidden layer is supposed to have exactly the same attributes as the first one. Simply making a model deeper often increases the performance.
- The third hidden layer is supposed to flatten its input over all dimensions. The result will be a one dimensional tensor (i.e. vector).
- The output layer is supposed to be a Dense layer. Dense layers require one dimensional input, therefore we have flattened before. Make sure that the output size matches the number of image categories. Each output value will represent the certainty of the model, that the presented image belonged to the respective category. Use softmax as activation function. Softmax will (among other things) make sure, that the certainty values sum up to one and thereby resemble a probability distribution.
- Before returning the model you have to compile it. Use categorical cross-entropy as loss function (it is just perfect for comparing probability distributions). Use Adam as optimizer and the accuracy as single metric.

**Hint:** Trying to train a model can help a lot in debugging it. If you have some wrong output shapes in your model, you will get helpful error messages. For training you can use the provided code (maybe when it comes to testing, train for a single epoch, only).

## 3. (optional) Play Around
**Important:** Before you try out different architectures, make sure that you pushed a version that satisfies the pytest to your GitHub repo!


If you reached this point, you have created a simple but effective neural network architecture for cifar10. But training the model is, were the interesting part begins. We will not require you to do any training (this would kill the autocorrection bot and also it can take a while of waiting), but we want to motivate you to play around with your model. For training it you can use the provided code. 

In the python script you can also find a function for plotting the training and validation accuracies and losses. If the curves for the training and the validation data are really far apart in the end, this indicates an overfit and you have probably trained for too many epochs. The model started to simply memorize the examples and will perform terribly in a real world task.

You can try and change things about your model and see, how this impacts the performance and training. Here are some ideas. Note, that the explanations are oversimplifications of the underlying processes and there can always be different results then described:
- **recommended:** use a global average pooling layer instead of the flattening layer. This will increase the number of epochs that is required for getting good results, but you will also note a drastical difference in the plotted training history.
- Make the model deeper: adding further layers to a model almost always improves the accuracy (up to a certain point). This is often considered "throwing computational power at a problem": the training process requires more operations with increasing size of trainable parameters. Also, with heavy overparameterization and no information bottleneck, an overfit can become more likely.
- Change the layers: Having more filters is similar to adding more layers. Increasing the kernel size and strides can reduce runtime and help in generalizing (preventing overfit), but might impacts performance (accuracy). Different activation functions have individual properties.
- Change the optimizing process: You can for instance try and find a sweetspot for the learning rate. This however highly depends on training noise (a learning rate that is good in one training run can randomly be not so good in the next one) and impacts the training progress per epoch. You can also try out an optimizer different than Adam. Adam is usually the best "first guess" for the choice of an optimizer for just any ANN training.
- And so on, try out whatever comes to your mind.

**Note:** Since we did not talk about serializing models, a trained model will be lost after the python script is finished. Therefore you should maybe use jupyter lab for testing model training.

**And another Note:** Neural networks are still pretty much blackboxes for us. The process of creating architectures and devising training procedures is therefore often considered "more art than science". One way or another: playing around with neural networks definitely helps in giving you at least intuitions about how to improve models. Experience is an extremely important thing for neural network engineers.


**Happy programming!**
