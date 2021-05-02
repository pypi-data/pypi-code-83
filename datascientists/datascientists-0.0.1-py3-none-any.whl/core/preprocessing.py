# Hide all other packages
__all__ = ['preprocessing']

import numpy as np
import pandas as pd
from IPython.display import display, Latex

class preprocessing:
    def __init__(self, df):
        """
        Accept a Pandas DataFrame object.

        df: DataFrame object
        """

        self.df = df

    # Define function standardize returning standardized units
    def standardize(self, formula=False):
        """
        Return a DataFrame with standardized units.

        formula: boolean
            Return formula.
        """

        # Display formula
        if formula is True:
            display(Latex(r"$z = \frac{X - \mu}{\sigma}$"))

        # Convert any array of numbers to standardized units
        return (self.df - np.mean(self.df)) / np.std(self.df)

    def normalize(self, formula=False):
        pass