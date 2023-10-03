import os
import numpy as np
from matplotlib import pyplot as plt
from scipy import fft, ndimage, stats


def passfilter(arr, cutoff, kind='lowpass', srate=256):
    '''Returns a complex array with a filtered version of the input signal'''
    fourier = fft.fft(arr)
    freqs = fft.fftfreq(arr.size, d=1/srate)
    freqs = np.abs(freqs)
    
    if kind == 'lowpass':
        fourier[freqs > cutoff] = 0 
    if kind == 'highpass':
        fourier[freqs < cutoff] = 0 
        
    filtered = np.fft.ifft(fourier)
    return filtered    

def equal_var(sample1, sample2, p_threshold=0.05):
    '''Returns True if it is likely that sample1 and sample2 have equal variance, False otherwise'''
    res = stats.levene(sample1,sample2)
    return(0 if res[1]<p_threshold else 1)


def equal_mean(sample1, sample2, p_threshold=0.05):
    '''Returns True if it is likely that sample1 and sample2 have equal mean, False otherwise'''
    res = stats.ttest_ind(sample1,sample2)
    return(False if res[1]<p_threshold else True)


def bloom(img, strength=5, blur=10):
    '''Returns a copy of img with an added bloom effect'''
    # YOUR CODE HERE


if __name__ == '__main__':
    # task 1
    xs = np.linspace(0, 10, 1000)
    arr = np.sin(xs) + 0.5 * np.sin(xs * 30) + 0.3 * np.sin(xs * 50)

    plt.plot(arr, label='original')
    plt.plot(passfilter(arr, 5, kind='lowpass').real, label='lowpass')
    plt.plot(passfilter(arr, 5, kind='highpass').real, label='highpass')
    plt.legend()
    plt.show()

    # task 2
    sample1 = np.random.normal(loc=0.3, scale=0.2, size=400)
    sample2 = np.random.normal(loc=0.5, scale=0.8, size=900)
    print('Sample 1:', stats.describe(sample1))
    print('Sample 2:', stats.describe(sample2))
    print('Equal mean?', equal_mean(sample1, sample2))
    print('Equal variance?', equal_var(sample1, sample2))

