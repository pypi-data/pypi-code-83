from chebxroots import chebxroots, chebcoeffs, clenshaw
import numpy as np
import matplotlib.pyplot as plt

def plotxroots(f,  x1=-1,x2=1, method = 'degdub',prefs = None, width=15, height=6):
    """
    Returns the plot of the chebyshev approximation of the function f. In addition, if splitting is chosen to be TRUE, the function will eventually (if
    calculated degree is too high) be split into subintervals and then evaluated on each subinterval. The calculated roots are also plotted as well as the
    subinterval borders.

    Parameters
    ----------
    f : callable
        a real valued function to be approximated and to find the roots of.
    x1 : float, optional
        lower boundary of the considered interval. The default is 1.
    x2 : float,optional
        upper boundary of the considered interval. The default is 1.
    method :  {'convtopow', 'degdub'}, optional
        The method for conversion to ordinary series of power form. Either
        'convtopow'("convert to power") or 'degdub' ("degree doubling") can be
        chosen. The default is 'convtopow'.
    prefs : class, optional
        Sets values for some parameters of chebxroots. See also ../../chebxroots/prefs. The default is None.
    width: float, optional
        width of plot
    height: float, optioanol
        height of plot

    Returns
    -------
    ax : Axes Instance of matplotlib.pyplot containing axis, Tick, Lin2D etc.

    Examples
    --------
    Plot approximated graph and roots of :math:'\sin(x)'
    >>> f = lambda x: numpy.´sin(x)
    >>> ax= plotxroots(f,x1=0,x2=100)

    """
    #create plot
    fig,ax=plt.subplots()
    fig.set_figwidth(width)
    fig.set_figheight(height)
    #calculate roots, subinterval borders, and coefficients (for each subinterval)
    roots_f,borders_f,coefs_f=chebxroots(f, x1, x2, method=method, prefs =prefs, enhancedoutput=True)
    yvals=[]
    xvals=[]
    #evaluate function through clenshaw algorithm in every subinterval
    for j in range(len(coefs_f)):
        #subinterval borders
        b1=borders_f[j]
        b2=borders_f[j+1]
        x=np.linspace(b1,b2,round((b2-b1)*100))
        #chebyshev coefficients for the subinterval
        c=chebcoeffs(f,a=b1,b=b2,deg=len(coefs_f[j]))
        #evaluate function on subinterval
        y=clenshaw((2*x-(b1+b2))/(b2-b1),c)
        yvals.append(y)
        xvals.append(x)
        #draw a vertical line to visualize borders of subintervals
        ax.axvline(b2, color='r', linestyle='--')
        roots_interval=roots_f[roots_f<=b2]
        roots_interval=roots_interval[roots_interval>=b1]
        #scatter plot of calculated roots
        ax.scatter(roots_interval,np.zeros(len(roots_interval)), label= 'roots found in interval {}'.format(j))

    xvals=np.concatenate(xvals).ravel()
    yvals=np.concatenate(yvals).ravel()
    ax.plot(xvals,yvals)
    ax.grid(True, which='both', linestyle= '--')
    plt.legend(loc='upper left')
    plt.xticks(borders_f)
    plt.title('Chebyshev approximation of the function f, approximated on {} intervals'.format(len(coefs_f)))
    plt.legend(loc='upper left')
    return ax
