# Hide all other packages
__all__ = ["hypothesisTesting"]

import numpy as np
from scipy import stats
from IPython.display import display, Latex
from datascientists.core.preprocessing import *
from datascientists._config import *

class hypothesisTesting:
    def __init__(self, df, labels=[], CI=95):
        """
        Accept a Pandas DataFrame object with one label.

        df: DataFrame object
            df is the sample or population dataset.
        label: str
            A column name of df
        type: str
            Default: None
            One of "mean", "median", or None. If none, the program will return a pure histogram.
        CI: float
            Default: 95
            Confidence Interval: between 0 to 100.
        repetition: int
            Default: 10000
            The times of the experiment repetition.

        >>> import pandas as pd
        >>> import datascientists as ds
        >>> df = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')

        >>> df_hypo = ds.simulation(df, 'sepal_length', type='mean', CI=99, repetition=5000)
        """

        self.df = df
        self.labels = labels
        self.type = type
        self.CI = CI

    def chisquare(self, observed, expected):
        # Calculate test statistic and p-value
        result = stats.chisquare(self.df[observed], self.df[expected])
        testStatistic, pvalue = result[0], result[1]

        a = (100 - self.CI) / 100
        print(f'Confidence Interval: {self.CI}%')
        print(f'a: {a}')
        print(f'p-value: {pvalue}')

        if pvalue < a:
            print(f'Reject H0 since p-value < a')
        else:
            print(f'Accept H0 since p-value > a')
        
        # Generate df with residual and chi-square
        df = self.df.copy()
        df['Residual']  = df[observed] - df[expected]
        df['Chi-Square'] = df['Residual']**2 / df[expected]
        df.loc['Total'] = [
            np.sum(df[observed]),
            np.sum(df[expected]),
            np.sum(df['Residual']),
            np.sum(df['Chi-Square'])
        ]
        return df

    # Update in next version
    def chi2_contingency(self):
        testStatistic, pvalue, dof, expected = stats.chi2_contingency(self.df)
        return testStatistic, pvalue, dof, expected
