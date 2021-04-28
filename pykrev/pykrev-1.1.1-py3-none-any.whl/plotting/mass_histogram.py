from ..formula import calculate_mass
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import math

def mass_histogram(formula_list,
                   mz_list = [],
                   me_list = [],
                   method = 'monoisotopic',
                   bin_width = [],
                   summary_statistics = False,
                   density = False,
                   hist = True,
                   kde = False,
                   kde_color = 'red',
                   **kwargs):
    """ 
	Docstring for function PyKrev.mass_histogram
	====================
	This function takes a list of molecular formula strings and plots a histogram of the atomic masses or mass errors calculated using    method.  
    
	Use
	----
	mass_histogram(Y)
    
    	Returns the fig and ax handles and a tuple containing the mean, median and standard deviation 
    
	Parameters
	----------
	Y: A list of molecular formula strings.
	method: the method used to calculate formula mass. See pk.calculate_mass for more information. 
            one of
            'monoisotopic'
            'average'
            'nominal'
            'mz'- plot a list of mz values provided explicitly by the user
            'me'- plot a list of mass error values provided explicitly by the user
    bin_width: an integer or float specifying the size of each histogram bin
    mz_list: a list or numpy array of mz values, must be provided to use method 'mz'. 
    summary_statistics: boolean, if true print the mean, median and standard deviation on the chart
    density: boolean, report normalised freq on y axis (as opposed to counts)
    hist: boolean, plot histogram bars.
    kde: boolean, plot a kernel density estimate line using scipy.gaussian_kde (forces density to be TRUE)
    kde_color = color of the kde line 
    **kwargs: key word arguments to plt.hist
    
    """
    assert method in ['monoisotopic','average','nominal','mz','me'], 'Provide a valid method. See docstring for info.'
    if method == 'mz':
        assert len(mz_list) > 1, 'provide a list of mz values'
        mass = mz_list
    elif method == 'me':
        assert len(me_list) > 1, 'provide a list of mass error values'
        mass = me_list
    else: 
        mass = calculate_mass(formula_list, method = method)
    
    if kde == True:
        #use scipy gaussian_kde to compute the kde on the mass list 
        from scipy import stats
        kde = stats.gaussian_kde(mass)
        xx = np.linspace(min(mass), max(mass), 1000)
        #plot the kde
        plt.plot(xx,kde(xx),color = kde_color)
        #density must be true if kde is true
        density = True
    #calculate summary statistics
    mass_mean = np.mean(mass)
    mass_median = np.median(mass)
    mass_std = np.std(mass)
    # plot the histogram
    if hist == True: 
        if bin_width:
            assert type(bin_width) == int or type(bin_width) == float, 'Provide a scalar value for bin width'
            n = math.ceil((mass.max() - mass.min())/bin_width)
            plt.hist(x=mass, bins = n, density = density, **kwargs)
        else:
            plt.hist(x=mass, density = density, **kwargs)
    plt.grid(axis='y', alpha=0.75)
    if method == 'mz':
        plt.xlabel('m/z')
    elif method == 'me':
        plt.xlabel('Mass error (ppm)')
    else:
        plt.xlabel(f"{method[0].upper()}{method[1::]} atomic mass")
    if density == True:
        plt.ylabel("Frequency")
    else:
        plt.ylabel("Counts")
    if summary_statistics:
    ## add to the upper right of the plot
        plt.annotate(f"$\mu={np.round(mass_mean,2)}$\nm = {np.round(mass_median,2)}\n$\sigma={np.round(mass_std,2)}$", xy=(0.75, 0.75), xycoords='axes fraction')
    fig = plt.gcf()
    ax = plt.gca()
    return fig, ax , (mass_mean, mass_median, mass_std)