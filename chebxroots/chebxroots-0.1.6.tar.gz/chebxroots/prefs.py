class Prefs:
    '''
    Sets values for some parameters of chebxroots.

    Parameters
    ----------
    fixeddegree : int
        Fix the degree of the Chebyshev expansion. If left empty, an optimal
        degree is determined.
        The default is None.
    maxdeg : int
        Maximal degree determined with stopping criterion sum_{j=[2/3 N]}^N |a_j| < eps
        from [1] where the a_j are Chebychev coefficients.  The default is 500.
    eps : float
        Epsilon for stopping criterion from [1]. The default is 1e-11.
    maxsplit : int
        Maximal number of subintervals. The default is 160.
    rounderr : float
        Rounding error used in degdubroots to restrict to roots on unit disk. The default is 0.000001.
    splitting : bool
        If True, it is allowed to split the considered interval in subintervals.
        The default is True.
    memoization : bool
        If true, memoization is used for the evaluation of the function in chebsroots.
    stepsize : int
        Stepsize for finding the optimal degree. The default is 1.

    References
    ----------
    ..  [1] John P. Boyd "Computing zeros on a real interval through Chebyshev
        expansion and polynomial rootfinding", SIAM Journal on
        Numerical Analysis, vol. 40, no. 5, pp. 1666-1682, 2002
    '''

    def __init__(self, fixeddegree = None, maxdeg = 500, eps = 1e-3, maxsplit = 160, rounderr=0.000001, splitting = True, memoization = False, stepsize = 1):
        self.fixeddegree = fixeddegree
        self.maxdeg = maxdeg
        self.maxsplit = maxsplit
        self.rounderr = rounderr
        self.eps = eps
        self.splitting = splitting
        self.memoization = memoization
        self.stepsize = 1
