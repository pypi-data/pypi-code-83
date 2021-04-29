import numpy as np
from math import ceil
from chebxroots import convert_to_powers, degree_doubling, chebcoeffs, prefs
#from degree_doubling import degree_doubling
#from chebcoeffs import chebcoeffs
#from prefs import Prefs
import functools


def chebxroots(func, a = -1, b = 1, method = 'degdub', enhancedoutput = False, prefs = None):
    '''
    Computes the roots of the Chebyshev expansion of a real-valued function
    in a given real interval.

    The function 'func' is approximated by (potentially) piecewise Chebyshev expansions
    .. math::
    	c_{0} + c_{1}  T_{1} (x) + c_{2} T_{2} (x) + ... + c_{N} T_{N} (x)

    These polynomials are then rewritten into  an ordinary series of power form.
    Afterwards a polynomial rootfinder is applied to obtain the roots in the
    interval ('a', 'b').



    Parameters
    ----------
    func : callable
        A real valued function to find the roots of.
    a : float, optional
        Lower boundary of the considered interval. The default is -1.
    b : float, optional
        Lower boundary of the considered interval. The default is 1.
    method : {'convtopow', 'degdub'}, optional
        The method for conversion to ordinary series of power form. Either
        'convtopow'("convert to power") or 'degdub' ("degree doubling") can be
        chosen. The default is 'degdub'.
    enhancedoutput : bool, optional
        If True, borders and coeffs are additionally returned.
        The default is False.

    Returns
    -------
    roots : array_like
        An array containing the roots of the Chebyshev expansion.
    borders : array_like
        An array containing the borders of the subintervals.
    coeffs : list
        A list of the coefficients of the Chebyshev series for each subinterval

    Notes
    -----
    In the case of "degree doubling" one considers a polynomial of degree
    2 * N. Having the coefficients for the Chebychev series :math:'c_j',
    the considered polynomial is
        .. math:: 2 c_0 x^N + \sum_j= 1 c_j (x^{N-j} + x^{N+j})
    The real part of the roots on the unit disk are the roots of the original
    Chebyshev series in ('a', 'b').

    The function is assumed to be analytic, convergence might be slower for a
    non-analytic function.

    The algorithm is taken from [1]_*.

    For the polynomial rootfinding numpy.roots is used.

    References
    ----------
    ..  [1] John P. Boyd "Computing zeros on a real interval through Chebyshev
        expansion and polynomial rootfinding", SIAM Journal on
        Numerical Analysis, vol. 40, no. 5, pp. 1666-1682, 2002

    Examples
    --------
    Compute the root of :math:'\exp(x)-1'
    >>> f = lambda x: numpy.exp(x)-1
    >>> print(chebxroots(f))
    [9.02056208e-16]
    '''
    if prefs == None:
        prefs = Prefs()

    if prefs.memoization == True:
        @functools.lru_cache(maxsize=None)
        def g(x):
            return func(x)
    else:
        def g(x):
            return func(x)

    #set up the maximal degree for splitting
    if method == 'convtopow':
        Nmax = 18
    elif method == 'degdub':
        Nmax = 40
    else:
        print('Please use either convtopow or degdub as method.')
        return


    if prefs.fixeddegree != None:
        N = prefs.fixeddegree
        if isinstance(N, int) == False:
            print('<maxdeg> needs to be either an integer or left empty.')
            return
        if N >= prefs.maxdeg:
            print('Maximal degree is reached, please try a smaller fixed degree or change maxdeg in your Prefs.')
            return
        chebco = chebcoeffs(g,a,b,N)


    #look for an optimal N
    else:
        sz = prefs.stepsize
        for N in range(1,prefs.maxdeg,sz):
            chebco = chebcoeffs(g, a, b, N)
            t = np.sum(np.abs(chebco[ round(2 / 3 * N) : ]))
            if t < prefs.eps:
                break
        #check if N is equal to or larger than maxdeg
        if N == prefs.maxdeg:
            print('Maximal degree is reached, please try a smaller interval.')
            return


    #check if degree is smaller than Nmax a
    if (N <= Nmax) or (prefs.splitting == False) or (prefs.fixeddegree != None):
        if method == 'convtopow':
            roots = convtopowroots(chebco, a, b)
            borders = np.array([a])
            coeffs = [chebco]

        elif method == 'degdub':
            roots = degdubroots(chebco, a, b, prefs)
            borders = np.array([a])
            coeffs = [chebco]


    #else split into equdistant subintervals
    else:
        numintvls = ceil(N / Nmax)

        #check if numintvls is smaller than maxsplit
        if numintvls >= prefs.maxsplit:
            print('Maximal number of subintervals is reached, please try a smaller interval.')

        else:

            subborders = np.linspace(a, b, numintvls+1)

            roots = np.array([])
            coeffs = []
            borders = np.array([])


            for k in range(numintvls):
                intvroots, intvborders, intvcoeffs = chebxroots(g, subborders[k], subborders[k+1], enhancedoutput = True, prefs = prefs)

                roots = np.concatenate((roots, intvroots))
                coeffs += intvcoeffs
                borders = np.concatenate((borders, intvborders))


    #add b to borders
    borders = np.concatenate((borders, np.array([b])))
    #order and remove duplicates
    roots = ordernremove(roots)
    borders = ordernremove(borders)

    if enhancedoutput == True:
        return roots, borders, coeffs
    else:
        return roots


def ordernremove(x):
    """
    Sorts an array and removes duplicates.

    Parameters
    ----------
    x : array_like
        Array to be sorted.

    Returns
    -------
    nodupl : array_like
        The array sorted and without duplicates.

    """
    nodupl = np.unique(x)
    sorted = np.sort(nodupl)
    return sorted

def convtopowroots(chebco, a, b):
    """
    Computes the roots of a Chebyshev polynomial
    with the convert to powers method.

    Parameters
    ----------
    chebco : array_like
        Coefficients of a Chebyshev polynomial
    a : float
        Lower interval boundary.
    b : float
        Upper interval boundary.

    Returns
    -------
    roots : array_like
        Roots of the Chebyshev polynomial.

    """
    polyco = convert_to_powers(chebco)
    roots = np.roots(polyco[::-1])

    #restrict to roots in [a,b]
    roots = roots[np.isreal(roots)]
    roots = (b - a) / 2 * roots + (b + a) / 2

    roots = roots[roots <= b]
    roots = roots[roots >= a]
    roots = np.real(roots)
    return roots

def degdubroots(chebco, a, b, prefs):
    """
    Computes the roots of a Chebyshev polynomial
    with degree doubling.


    Parameters
    ----------
    chebco : array_like
        Coefficients of a Chebyshev polynomial
    a : float
        Lower interval boundary.
    b : float
        Upper interval boundary.
    prefs : TYPE
        DESCRIPTION.

    Returns
    -------
    roots : array_like
        Roots of the Chebyshev polynomial.

    """
    polyco = degree_doubling(chebco)
    roots = np.roots(polyco)

    #restrict to roots on the unit disk, margin to accommodate small errors
    roots = roots[np.absolute(roots) <= 1 + prefs.rounderr]
    roots = roots[np.absolute(roots) >= 1 - prefs.rounderr]
    roots = np.real(roots)
    roots = (b - a) / 2 * roots + (b + a) / 2
    return roots
