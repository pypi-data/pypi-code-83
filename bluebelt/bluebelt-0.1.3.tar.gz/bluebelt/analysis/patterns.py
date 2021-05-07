import pandas as pd
import numpy as np
import numpy.polynomial.polynomial as poly
import scipy.stats as stats

import warnings

import matplotlib.pyplot as plt
#from matplotlib.ticker import FormatStrFormatter
import bluebelt.helpers.mpl_format as mpl_format

import bluebelt.styles.paper as paper

class Polynomial():
    
    """
    Find the polynomial of a series and project a bandwidth
    series: pandas.Series
    shape: int or tuple
        when an int is provided the polynomial is provided as n-th degree polynomial
        when a tuple is provided the function will find an optimised polynomial between first and second value of the tuple
        default value: (0, 6)
    validation: string
        validation type for shape tuple
        p_val: test for normal distribution of the residuals
        rsq: check for improvement of the rsq value
        default value: p_val
    threshold: float
        the threshold for normal distribution test or rsq improvement
        default value: 0.05
    confidence: float
        the bandwidth confidence
        default value: 0.8
    outlier_sigma: float
        outliers are datapoints outside the outlier_sigma fraction
        default value: 2
    adjust: boolean
        adjust polynomial for outliers
        default value: True
    """

    def __init__(self, series, shape=(0, 6), validation='p_val', threshold=0.05, confidence=0.8, outlier_sigma=2, adjust=True, **kwargs):
        
        self.series = series
        self.shape = shape
        self.validation = validation
        self.threshold = threshold
        self.confidence = confidence
        self.outlier_sigma = outlier_sigma
        self.adjust = adjust

        self.calculate()

    def calculate(self):
        
        self.sigma_level = stats.norm.ppf(1-(1-self.confidence)/2)

        # set pattern and residuals
        self.pattern, self.residuals, self.p_val, self.rsq = _poly_hand_granade(series=self.series, shape=self.shape, validation=self.validation, threshold=self.threshold)

        # set outliers
        self.outliers = pd.Series(data=np.where(self.residuals.abs() > self.residuals.std() * self.outlier_sigma, self.series, None), index=self.series.index)
        self.outliers_count = np.count_nonzero(self.outliers)

        self.adjusted = self.series.loc[~self.outliers.notnull()]
        
        # replace pattern and residuals if adjust=True
        if self.adjust:
            # replace outliers with None values
            values = pd.Series(data=np.where(self.outliers.notnull(), None, self.series).astype(np.float), index=self.series.index)
            self.pattern, self.residuals, self.p_val, self.rsq = _poly_hand_granade(series=values, shape=self.shape, validation=self.validation, threshold=self.threshold)
        
        # set bounds
        self.upper = self.pattern + self.residuals.std() * self.sigma_level
        self.lower = self.pattern - self.residuals.std() * self.sigma_level

    def plot(self, **kwargs):
        
        style = kwargs.get('style', paper)
        kwargs.pop('style', None)

        path = kwargs.pop('path', None)        
        
        # prepare figure
        fig = plt.figure(constrained_layout=False, **kwargs)
        gridspec = fig.add_gridspec(nrows=2, ncols=1, height_ratios=[5,3], wspace=0, hspace=0)
        ax1 = fig.add_subplot(gridspec[0, 0], zorder=50)
        ax2 = fig.add_subplot(gridspec[1, 0], zorder=40)
        
        # observations
        ax1.plot(self.series, **style.patterns.observations)

        # pattern
        ax1.plot(self.pattern, **style.patterns.pattern)
        
        # outliers
        ax1.plot(self.outliers, **style.patterns.outlier_background)
        ax1.plot(self.outliers, **style.patterns.outlier)

        # bandwidth
        ax1.fill_between(self.series.index, self.lower, self.upper, **style.patterns.bandwidth_fill_between)
        ax1.plot(self.lower, **style.patterns.lower)
        ax1.plot(self.upper, **style.patterns.upper)
        
        # labels
        ax1.set_title(f'{self.pattern.name} probability chart of {self.series.name}', **style.patterns.title)
        ax1.set_ylabel('value')

        #ax1.text(0.02, 0.9, r'$R^2$'+f': {self.rsq}', transform=ax1.transAxes, va='center', ha='left')
        

        # set x axis locator
        mpl_format.axisformat(ax1, self.series)


        # histogram
        ax2.hist(self.residuals, **style.patterns.histogram)
        ax2.set_yticks([])

        # get current limits
        xlims = ax2.get_xlim()
        ylims = ax2.get_ylim()
        
        # fit a normal distribution to the data
        norm_mu, norm_std = stats.norm.fit(self.residuals.dropna())
        pdf_x = np.linspace(xlims[0], xlims[1], 100)
        ax2.plot(pdf_x, stats.norm.pdf(pdf_x, norm_mu, norm_std), **style.patterns.normal_plot)

        # histogram x label
        ax2.set_xlabel('residuals distribution')
 
                
        ax2.set_ylim(ylims[0], ylims[1]*1.5)
        ax2.spines['left'].set_visible(False)
        ax2.spines['right'].set_visible(False)

        #ax2.text(0.02, 0.7, "residuals distribution", transform=ax2.transAxes, va='center', ha='left')
        #ax2.text(0.02, 0.7, f'p: {self.p_val:1.2f}', transform=ax2.transAxes, va='center', ha='left')

        plt.gcf().subplots_adjust(right=0.8)

        if path:
            plt.savefig(path)
            plt.close()
        else:
            plt.close()
            return fig

def _poly_hand_granade(series, shape=(0, 6), validation='p_val', threshold=0.05, **kwargs):

    """
    Find the polynomial of a series.
    series = the pandas Series
    shape: int or tuple
        when an int is provided the polynomial is provided as n-th degree polynomial
        when a tuple is provided the function will find an optimised polynomial between first and second value of the tuple
    validation: only for tuple shape
        p_val: test for normal distribution of the residuals
        rsq: check for improvement of the rsq value
    threshold: the threshold for normal distribution test or rsq improvement
    """

    # get the index
    index = series.index.astype(int)-series.index.astype(int).min()
    index = index / np.gcd.reduce(index)

    # drop nan values
    _index = series.dropna().index.astype(int)-series.index.astype(int).min()
    _index = _index / np.gcd.reduce(_index)

    # get the values
    values = series.dropna().values

    # set first rsq
    _rsq = 0


    if isinstance(shape, int):
        pattern = pd.Series(index=series.index, data=np.polynomial.polynomial.polyval(index, np.polynomial.polynomial.polyfit(_index, values, shape)), name=f'{get_nice_polynomial_name(shape)}')
        residuals = pd.Series(index=series.index, data=[a - b for a, b in zip(series.values, pattern)])
        
        p_val = stats.mstats.normaltest(residuals.dropna().values)[1]
        rsq = np.corrcoef(series.values, pattern.values)[1,0]**2


    elif isinstance(shape, tuple):

        with warnings.catch_warnings():
            warnings.filterwarnings('error')
            for shape in range(shape[0], shape[1]+1):
                try:
                    pattern = pd.Series(index=series.index, data=np.polynomial.polynomial.polyval(index, np.polynomial.polynomial.polyfit(_index, values, shape)), name=f'{get_nice_polynomial_name(shape)}')
                    residuals = pd.Series(index=series.index, data=[a - b for a, b in zip(series.values, pattern)])
                    
                    np_err = np.seterr(divide='ignore', invalid='ignore') # ignore possible divide by zero
                    rsq = np.corrcoef(series.values, pattern.values)[1,0]**2
                    np.seterr(**np_err) # go back to previous settings
                    
                    p_val = stats.mstats.normaltest(residuals.dropna().values)[1]

                    if validation=='p_val' and p_val >= threshold:
                        break
                    elif validation=='rsq' and (rsq - _rsq) / rsq < threshold:
                        pattern = pd.Series(index=series.index, data=poly.polyval(index, poly.polyfit(_index, values, shape-1)), name=f'{get_nice_polynomial_name(shape-1)}')    
                        residuals = pd.Series(index=series.index, data=[a - b for a, b in zip(series.values, pattern)])
                        
                        # reset rsq
                        rsq = _rsq
                        break
                    
                    # set previous rsq to current rsq
                    _rsq = rsq

                except poly.pu.RankWarning:
                    print(f'RankWarning at {get_nice_polynomial_name(shape)}')
                    break
    else:
        pattern = None
        residuals = None

    return pattern, residuals, p_val, rsq

def periodical(series, period='1W', how=None, **kwargs):

    if how=='min':
        result = series.resample(rule=period, label='left').min().reindex_like(series, method='ffill')
    elif how=='max':
        result = series.resample(rule=period, label='left').max().reindex_like(series, method='ffill')
    elif how=='std':
        result = series.resample(rule=period, label='left').std().reindex_like(series, method='ffill')
    else:
        result = series.resample(rule=period, label='left').mean().reindex_like(series, method='ffill')

    if kwargs.get('step'):
        result = result.divide(kwargs.get('step')).round(0).multiply(kwargs.get('step'))
    
    return result

def anomalies(df=None, values=None, pattern=None, sigma=2):
    """
    pass a DataFrame and two strings with the column names or
    two series for values or pattern
    """

    # dataframe or series
    if df is not None:
        values = df[values]
        pattern = df[pattern]

    residuals = pd.Series(index=values.index, data=[a - b for a, b in zip(values, pattern)])

    return pd.Series(index=values.index, data=(residuals.abs() > (residuals.std() * sigma)))


# get things nicer
def get_nice_polynomial_name(shape):
    if shape==0:
        return 'linear'
    if shape==1:
        return str(shape)+'st degree polynomial'
    elif shape==2:
        return str(shape)+'nd degree polynomial'
    elif shape==3:
        return str(shape)+'rd degree polynomial'
    else:
        return str(shape)+'th degree polynomial'