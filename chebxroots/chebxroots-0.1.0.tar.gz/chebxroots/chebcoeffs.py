import numpy as np
import functools


def chebcoeffs(f , a = -1, b = 1  , deg = 17):
    '''
    Computes the coefficients for the Chebyshev expansion of
    a fucntion in a given interval.

    Parameters
    ----------
    func : callable, f(x, *args)
    	A function that takes a float as argument and returns a float.
    a : float, optional
    	Lower boundary of the considered interval. The default is -1.
    b : float, optional
    	Lower boundary of the considered interval. The default is 1.
    deg : int, optional
    	Degree of the Chebyshev expansion. The default is 17.
        
    Returns
    -------
    coeffs : array
    	An array of the coefficients of the Chebyshev expansion.

    '''
    N = deg

    # create chebyshev points
    xk = (b - a) / 2 * chebpts(N+1) + (b + a) / 2

    #compute interpolation matrix
    p = np.ones(N+1)
    p[0] = 2
    p[N] = 2
    p = p[np.newaxis]
    J = 2 / (p.T @ p * N)

    i = np.arange(N+1)[np.newaxis]
    I = np.cos(np.pi * (i.T @ i) / N)

    I = I * J

    #compute the values of f at the Chebyshev points. vectoriz f just to be safe
    fvec = np.vectorize(f)
    fvals = fvec(xk)

    #compute the weights

    coeffs = I.dot(fvals)
    return coeffs

@functools.lru_cache(maxsize=200)
def chebpts(n):
    '''
    Yields Chebyshev points of the second kind.

    Parameters
    ----------
    n : int
        The amount of Chebyshev points of the second kind.

    Returns
    -------
    x : array
        An array containing the Chebyshev points of the second kind.

    '''

    # Special case (no points)
    if n == 0:
        x = []
    # Special case (single point)
    elif n == 1:
        x = 0

    else:
        # Chebyshev points:
        m = n - 1

        #x = np.sin(np.pi*(np.r_[-m:m+1:2]/(2*m))) use for chebfun
        x = np.cos(np.pi*(np.r_[0:m+1]/m))


    return x
