# Import NumPy here
import numpy as np


def expomultiadditive_division(a, b, c):
    """ returns the result of expomultiadditive division """
    return (np.exp(a*(b+c))) / (np.power(a,2)- np.power(b,2) + np.power(c,2))


def strange_pattern(shape):
    """ takes a shape tuple (n, m) as input and generates a boolean 2D NumPy array with this pattern """
    
    # first of all initialize 2D numpy array with only zeros
    array = np.zeros(shape, dtype=bool)

    # counter is a variable to realize the shift of the pattern 
    counter = 0
    for i in array: 
        if counter == 3: 
            counter = 0

        # every third place should equal to one 
        i[counter::3] = 1
        counter +=1  

    return array 

def dimension_reduction(array):
    """ Reduces the dimension of the given array
    
    Args: 
        array (int) : the array to be reduced 
    Returns: 
        s_d (float) : standard deviation of the entire array 
    
    """

    # first dimension gets reduced to its sum 
    array = np.sum(array, axis=0)

    # last dimension gets reduced to its median 
    array = np.median(array, axis=array.ndim-1)
    
    return np.std(array)


def interpolate(numbers, n_steps):
    """
    list of n floating point numbers 
    takes numbers as an input and returns a NumPy array of size n_steps * (n - 1) + 1, 
    where the first and every n_steps-th entry afterwards are the original numbers.
    The other values should be linearly interpolated between those original numbers

    """
    
    # array size should be : n_steps *(len(numbers)-1)+1
    b = np.array([], dtype='float64')
    for i in range(len(numbers)-1):
        a = np.linspace(numbers[i], numbers[i+1], n_steps +1)
        b = np.hstack((b[:-1], a))

    array_size = n_steps *(len(numbers)-1)+1
    assert b.size == array_size
    
    return b

if __name__ == "__main__":
    # use this for your own testing!
    pass
