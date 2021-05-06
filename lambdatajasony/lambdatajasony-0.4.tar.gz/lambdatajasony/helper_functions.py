import pandas
import numpy

"Three new classes for my helper functions"

class NullCount:

    def nulls(self, df):
      
      return df.isnull().sum().sum()


class RandomizedDataFrame:
  
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

"One old function"

def train_test_split(df, frac = 0.2):
    train = df.sample(frac = frac, replace = False, random_state = 60)
    test = df.drop(train.index)
    
    return train, test



