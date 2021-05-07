import pandas as pd
import matplotlib.pyplot as plt
import numpy

""" 

Classes and methods that I will find helpful when exploring and analysing data
    
"""

class NullCount(pd.DataFrame):
    """
    
    A subclass of Pandas DataFrames with a new method attached that returns
    the sum of all nulls
    
    """
    def nulls(self, df):
      
      return df.isnull().sum().sum()


class RandomizedDataFrame(pd.DataFrame):
  """
  
  Another subclass with an extra method to quickly shuffle its contents. It occurs
  to me that I should include the nulls method in this one, but that's for the
  weekend
  
  """
  def __init__(self, df, seed = 50):
    self.df = df
    self.randomseed = seed

  def shuffle(self):
    return self.df.sample(frac = 1, replace = False)


class HungryDataFrame:
    
    def __init__(self, listy, df):
        self.listy = listy
        self.df = df

  
    def mutate(self):
        self.df['list'] = pd.Series(self.listy)

        return self.df

class FriendlyError(Exception):
    
    """ A friendlier error message"""
    
    pass

def train_test_split(df, frac = 0.2):
    """
    A simple function that splits a DataFrame into a train and test set
    

    Parameters
    ----------
    df : a Pandas DataFrame
        
    frac : the fraction of the DataFrame that goes into the test set. the 
           default is 0.2

    Returns
    -------
    train : A Pandas DataFrame with 1-frac of the data
    
    test : A Pandas DataFrame with frac of the data

    """
    if isinstance(df, pd.DataFrame):
        
        train = df.sample(frac = 1 - frac, replace = False, random_state = 60)
        test = df.drop(train.index)
        
        return train, test
    
    else:
        
        raise FriendlyError("Sorry. It is my fault, not yours")

