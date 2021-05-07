# Hide all other packages
__all__ = ['preprocessing']

import numpy as np
import pandas as pd
from IPython.display import display, Latex

class preprocessing:
    def __init__(self, df, columns=[]):
        """
        Accept a Pandas DataFrame object.

        df: DataFrame object
        columns: A list of column names of df. Other columns will not be processed.
        """

        self.df = df
        self.columns = columns

    # Define function standardize returning standardized units
    def standardize(self, formula=False):
        """
        Return a DataFrame with standardized units.

        formula: boolean
            Return formula.

        >>> import pandas as pd
        >>> import datascientists as ds
        >>> df = pd.read_csv('https://github.com/mwaskom/seaborn-data/raw/master/iris.csv')

        >>> df_preprocessing = ds.preprocessing(df)
        >>> df_preprocessing.standardize(formula=True).head()

        >>> df_preprocessing = ds.preprocessing(df, columns=['petal_length', 'petal_width', 'sepal_length', 'sepal_width'])
        >>> df_preprocessing.standardize(formula=False).head()
        """

        # Display formula
        if formula is True:
            display(Latex(r"$z = \frac{X - \mu}{\sigma}$"))

        # Standardize all data
        if self.columns == []:
            df = (self.df - np.mean(self.df)) / np.std(self.df)
        # Standardize specificed data based on self.columns
        else:
            #Extrat self.columns from self.df as df
            df = self.df[self.columns]
            # Standardization
            df = (df - np.mean(df)) / np.std(df)
            # Add the unstandardized columns from self.df to df
            for col in self.df.columns:
                if col not in df.columns:
                    df[col] = self.df[col]
            # Recovery the df columns order to the original sequence
            df = df[self.df.columns]

        return df

    def normalize(self, formula=False):
        pass