"""A collection of Data Science helper functions"""

import pandas as pd
import numpy as np

animals = ['zebra', 'monkey', 'giraffe', 'dog']

def nullsum(df):
    # TODO implement the function

    return df.isnull().sum().sum()

print("This is executed when importing lambdata")
