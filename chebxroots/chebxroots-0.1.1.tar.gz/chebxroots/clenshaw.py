import numpy as np

def clenshaw(x,c):
	'''

	Clenshaw scheme for scalar-valued functions



	Parameters
	----------
	x : float
		point at which to evaluate.
	c : array
		weights of the Chebyshev series for a (specific) function.

	Returns
	-------
	y : float
		function value evaluated at x.


    	Notes
    	-----
	C is a column vector, Y = CLENSHAW(X, C) evaluates the Chebyshev
     	expansion
     	Y = P_N(X) = C(1)*T_0(X) + ... + C(N)*T_{N-1}(X) + C(N+1)*T_N(X)
   	using Clenshaw's algorithm.
	 '''
	bk1=0*x
	bk2=0*x
	x=2*x
	n=range(c.size)
	for k in n[c.size:1:-2]:
		bk2=c[k] +x*bk1-bk2
		bk1=c[k-1]+x*bk2-bk1
	if np.mod(c.size-1,2)==1:
		tmp=bk1
		bk1=c[1]+x*bk1-bk2
		bk2=tmp
	y=c[0]+ 0.5*x*bk1-bk2
	return y
