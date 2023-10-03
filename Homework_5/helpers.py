import numpy as np
import types


def mandelbrot(x, y, dx, dy, dims=(300, 400), threshold=25, iterations=200):
    """ Returns a boolean matrix indicateing for each position whether it is inside the Mandelbrot Set or not. """

    xs, ys = np.meshgrid(np.linspace(x, x + dx, dims[1]), np.linspace(y, y + dy, dims[0]))
    c = xs + ys * 1j

    zs = np.zeros(dims, dtype=np.complex128)

    for i in range(iterations):

        abs_zs = np.abs(zs)
        zs[abs_zs < threshold] = zs[abs_zs < threshold] ** 2 + c[abs_zs < threshold]

    return np.abs(zs) < threshold


def imports_of_your_file(filename, testfile):
    """ Yields all imports in the tested file. """

    for name, val in vars(testfile).items():
        if isinstance(val, types.ModuleType):
            # get direct imports
            yield val.__name__

        else:
            # get from x import y imports
            imprt = getattr(testfile, name)

            if hasattr(imprt, "__module__") and not str(imprt.__module__).startswith("_") and not str(imprt.__module__) == filename:
                yield imprt.__module__

