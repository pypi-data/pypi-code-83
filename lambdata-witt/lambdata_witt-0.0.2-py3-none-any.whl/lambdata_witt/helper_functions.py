import pandas as pd
import numpy as np
import random

test_list = [1,2,3,4,float('NAN')]
data = {'col1':['a','b','c','d','e','f',float('nan')], 'col2':['Bird','Cow',float('nan'),'Platypus','Giraffe','Zebra','Monkey'],'col3':[1,2,3,4,5,6,7]}
test_df = pd.DataFrame(data=data)


# def null_count(df):
#     count = pd.isna(df).sum().sum()
#     return count
#     #Was this meant to be two for loops?

class NullCount:
    def __init__(self):
        #import pandas as pd
        return

    def NullCounter(df):
        count = pd.isna(df).sum().sum()
        return count


class TrainTest:
    def __init__(self):
        return

    def TrainTestSplit(df, frac):
        a = df
        b = float(frac)
        print(b)
        train = a.sample(frac=b)
        test = df.drop(train.index[0:])

        return [print(train), print(test)]
        
