import pandas
import numpy

def null_count(df):
    return df.isnull().sum().sum()

def train_test_split(df, frac = 0.2):
    train = df.sample(frac = frac, replace = False, random_state = 60)
    test = df.drop(train.index)
    
    return train, test

def randomize(df, seed = 50):
    return df.sample(frac = 1, replace = False, random_seed = seed)

def list_2_series(listtoseries, df):
    df['list'] = pd.Series(listtoseries)
    return df



