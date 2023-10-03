import numpy as np

import matplotlib

try:

    import cifar_classifier as testfile

except ModuleNotFoundError:

    assert False, "The name of your file is supposed to be 'cifar_classifier.py'!"


def test_load_data(filename="cifar_classifier", allowed_imports={"numpy", "matplotlib.pyplot", "helpers"}):
    """ Checks whether plots returned by plot_airquality have the correct attributes. """
    X_train, y_train, X_test, y_test = testfile.load_cifar10()
    
    assert np.all(X_train <= 1) and np.all(X_train >= 0), "The training data is not normalized"    
    assert np.all(X_test <= 1) and np.all(X_test >= 0), "The testing data is not normalized"
    
    assert np.all([sum(label) == 1 for label in y_train]), "The training labels are not one-hot encoded"    
    assert np.all([sum(label) == 1 for label in y_train]), "The testing labels are not one-hot encoded"
    