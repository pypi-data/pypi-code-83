import numpy as np

#Convert to powers

def convert_to_powers(a):
    '''
    Converts the coefficients of a polynomial written as a Chebyshev series
    into the coefficients in ordinary series of power form.

    Parameters
    ----------
    a : array
        Rank-1 array of coefficients of a Chebyshev series.

    Returns
    -------
    b : array
        An array of the coefficients of the polynomial in ordinary
        series of power form.

    '''
    a_even = a[::2]
    a_odd = a[1::2]


    Q_even = np.identity(len(a_even))
    vector = np.arange(1,len(a_even))

    Q_even_sub = np.diag(2**(2*(vector+1)-3))

    Q_even[1:1+Q_even_sub.shape[0], 1:1+Q_even_sub.shape[1]] = Q_even_sub

    for i in range(len(a_even)):
        for k in range(i):
            Q_even[i-k-1,i] = round(-(2*(i+1)-2*(k+1))*(2*(i+1)-2*(k+1)-1)/(2*(k+1)*(4*(i+1)-2*(k+1)-4))*Q_even[i-k,i],0)

    Q_odd = np.zeros((len(a_odd),(len(a_odd))))

    for i in range(len(a_odd)):
        Q_odd[i,i] = 2**(2*(i+1)-2)
        for k in range(i):
            Q_odd[i-k-1,i] = -((2*(i+1)-2*(k+1)+1)*((i+1)-(k+1)))/((k+1)*(4*(i+1)-2*(k+1)-2))*Q_odd[i-k,i]
    
    b_even = np.dot(Q_even, a_even)
    b_odd = np.dot(Q_odd, a_odd)

    b=np.zeros(len(a))

    b[::2]=b_even
    b[1::2]=b_odd

    return b
