import os
import numpy as np
from matplotlib import pyplot as plt

import maths


def test_passfilter():
    assert hasattr(maths, 'passfilter'), 'maths.py does not contain a "passfilter" function'
    xs = np.linspace(-10, 10, 1000)
    arr = np.sin(xs * 2) + np.sin(xs * 15) + np.sin(xs * 100 + 3)

    res = maths.passfilter(arr, 10)
    assert res.dtype == np.complex, 'Result is not complex'
    assert res.shape == arr.shape, f'Shape of the result {res.shape} does not match the input shape {arr.shape}'

    f1 = maths.passfilter(arr, 5)
    assert np.allclose(f1.real, np.load(os.path.join(os.path.dirname(__file__), 'data/r1.npy')))
    assert np.allclose(f1.imag, np.load(os.path.join(os.path.dirname(__file__), 'data/i1.npy')))
    f2 = maths.passfilter(arr, 15, srate=512)
    assert np.allclose(f2.real, np.load(os.path.join(os.path.dirname(__file__), 'data/r2.npy')))
    assert np.allclose(f2.imag, np.load(os.path.join(os.path.dirname(__file__), 'data/i2.npy')))
    f3 = maths.passfilter(arr, 10, kind='highpass')
    assert np.allclose(f3.real, np.load(os.path.join(os.path.dirname(__file__), 'data/r3.npy')))
    assert np.allclose(f3.imag, np.load(os.path.join(os.path.dirname(__file__), 'data/i3.npy')))

    xs = np.linspace(0, 10, 500)
    arr = np.sin(xs * 0.5) + np.sin(xs * 20) + np.sin(xs * 50 - 1)
    f4 = maths.passfilter(arr, 15, kind='highpass')
    assert np.allclose(f4.real, np.load(os.path.join(os.path.dirname(__file__), 'data/r4.npy')))
    assert np.allclose(f4.imag, np.load(os.path.join(os.path.dirname(__file__), 'data/i4.npy')))


def random_sample(mean, var):
    return np.random.normal(loc=mean, scale=var, size=np.random.randint(1000, 5000))


def test_equal_var():
    assert hasattr(maths, 'equal_var'), 'maths.py does not contain a "equal_var" function'
    variances = [0.1, 1, 2, 4, 7]
    p_threshold = 0.05
    correct = []
    for _ in range(100):
        var1, var2 = np.random.choice(variances, 2)
        sample1 = random_sample(np.random.uniform(-10, 10), var1)
        sample2 = random_sample(np.random.uniform(-10, 10), var2)
        correct.append(maths.equal_var(sample1, sample2, p_threshold) == (var1 == var2))
    assert np.mean(correct) >= 1 - p_threshold, 'Random tests for equal variance failed'


def test_equal_mean():
    assert hasattr(maths, 'equal_mean'), 'maths.py does not contain a "equal_mean" function'
    variances = [0.1, 1, 2, 4, 7]
    means = [-5, -2, 0.3, 10, 25]
    p_threshold = 0.05
    correct = []
    for _ in range(100):
        var1, var2 = np.random.choice(variances, 2)
        mean1, mean2 = np.random.choice(means, 2)
        sample1 = random_sample(mean1, var1)
        sample2 = random_sample(mean2, var2)
        correct.append(maths.equal_mean(sample1, sample2, p_threshold) == (mean1 == mean2))
    assert np.mean(correct) >= 1 - p_threshold, 'Random tests for equal mean failed'

