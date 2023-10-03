from helpers import imports_of_your_file

import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

warnings.filterwarnings('ignore')

try:
    import density as testfile

except ModuleNotFoundError:

    assert False, 'The name of your file is supposed to be "density.py"!'


def test_density(filename='density', allowed_imports={"numpy", "pandas", "matplotlib.pyplot"}):
    """ Checks whether plots returned by make_densityplot have the correct attributes. """

    iris = pd.read_csv('data/iris.csv', index_col=0)

    np.random.seed(0)
    fig = testfile.make_densityplot(iris)

    try:
        ax_joint, ax_marg_x, ax_marg_y = fig.ax_joint, fig.ax_marg_x, fig.ax_marg_y
    except ValueError:
        assert False, 'Your figure should have a joint and two marginal axes'

    # test ax_marg_x
    # check for shaded=True
    assert not ax_marg_x.lines, 'It seems like your marginal densities for the xaxis are not shaded'
    # get ref data
    npz = np.load('ref_data/ax_marg_x.npz')
    for i, file in enumerate(npz.files):
        result = ax_marg_x.collections[i].get_paths()[0].vertices
        assert np.allclose(npz[file], result), 'There seems to be a mistake in the data of your marginal x plot'


    # test ax_marg_y
    # check for shaded=True
    assert not ax_marg_y.lines, 'It seems like your marginal densities for the yaxis are not shaded'

    npz = np.load('ref_data/ax_marg_y.npz')
    for i, file in enumerate(npz.files):
        result = ax_marg_y.collections[i].get_paths()[0].vertices
        assert np.allclose(npz[file], result), 'There seems to be a mistake in the data of your marginal y plot'


if __name__ == "__main__":
    test_density()
    print('pass')