import numpy as np
def degree_doubling(a):
    '''
    Given coefficients of a Chebyshev series, yields the coefficients
    used for the degree doubling method.


    Parameters
    ----------
    a : array_like
        Coefficients of a Chebyshev series.

    Returns
    -------
    b : array
        Coefficients of the polynomial obtained by degree doubling.

    '''
    n = len(a)-1
    b = np.zeros(2*n+1)
    b[:n+1] += np.flip(a)
    b[n:] += a
    return b
