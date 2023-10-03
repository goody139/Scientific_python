from tensorflow.keras.activations import relu, softmax
import numpy as np

import matplotlib

try:

    import cifar_classifier as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'cifar_classifier.py'!"


def test_load_data(filename="cifar_classifier", allowed_imports={"numpy", "matplotlib.pyplot", "helpers"}):
    """ Checks whether the model returned by create model has the correct attributes. """
    
    model = testfile.create_model()
    
    # this can fail with awkwardly built tensorflow
    # assert "functional" in model.name, "Please use the functional API for creating the model"
    assert np.all(np.array([32, 32, 3]) == model.layers[0].output.shape[1:]), "Wrong input shape, remember that each pixel consists of three values"
    assert "Conv2D" in str(type(model.layers[1])), "The first hidden layer is suppose to be a convolutional layer"
    assert "Conv2D" in str(type(model.layers[2])), "The second hidden layer is suppose to be a convolutional layer"
    assert np.all(np.array([30, 30]) == model.layers[1].output.shape[1:-1]), "The first convolutional layer has a wrong output shape. It should have the correct one by default"
    assert np.all(np.array([28, 28]) == model.layers[2].output.shape[1:-1]), "The second convolutional layer has a wrong output shape. It should have the correct one by default"
    assert model.layers[1].output.shape[-1] == 32, "The first convolutional layer has the wrong number of filters"
    assert model.layers[2].output.shape[-1] == 32, "The second convolutional layer has the wrong number of filters"
    assert model.layers[1].activation == relu and model.layers[2].activation == relu, "Use relu as ativation function"
    assert model.layers[1].kernel_size == (3,3) and model.layers[2].kernel_size == (3,3), "The Kernel sizes are meant to represent a 3 x 3 moving window"
    assert model.layers[1].strides == (1, 1) and model.layers[2].strides == (1, 1), "The 'sliding window' is supposed to move one pixel per step"
    assert "Flatten" in str(type(model.layers[3])), "The third hidden layer is supposed to flatten its input tensor"
    assert "Dense" in str(type(model.layers[4])), "The otput layer is supposed to be a dense layer"
    assert model.layers[4].output.shape[1] == int("101",3), "The otput dimensionality of the network has to be the same as that of the labels"
    assert model.layers[4].activation == softmax, "Use softmax as the activation function for the output layer"
    
