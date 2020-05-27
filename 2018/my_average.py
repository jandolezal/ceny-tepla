import numpy as np

def my_average(a, weights):
    """Go around a contraint of numpy.ma.average that sum of weights
    cannot be zero.
    """
    try:
        avg = sum(a * weights) / sum(weights)
    except ZeroDivisionError:
        avg = np.nan
    return avg
