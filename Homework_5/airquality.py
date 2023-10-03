import matplotlib.pyplot as plt
import numpy as np


def main():
    df = np.load('data/airdata.npy', allow_pickle=True)
    plot_airquality(df)
    plt.tight_layout()
    plt.show()


def plot_airquality(data): # data.shape = (2,31)
    '''Returns the figure object and two axes'''

    days = np.arange(1,len(data[0])+1)

    # create 2 subplots 
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)
    ax1.plot(data)
    ax2.plot(data)
    plt.show()


if __name__ == "__main__":
    main()
