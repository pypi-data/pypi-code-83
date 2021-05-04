import time
import matplotlib.pyplot as plt
import numpy as np

#from numba import cuda

#import funcDictionary as dic
#import funcDictionaryLevenshtein as dicLeven
#import plotData
#import textdistance as td

#from scipy import sparse
import pandas as pd
import math

#from numbapro import vectorize

def specificity():
    """
    info: 
    input: 
    output: 
    """

    df = pd.read_excel('specific.xlsx')
    specs_raw = list(df['BetaConfi'])
    CDR3s_raw = list(df['CDR3beta'])
    print("\n len(specs_raw): ", len(specs_raw), "; len(CDR3s_raw): ", len(specs_raw))
    specs = list()
    CDR3s = list()
    for i in range(len(specs_raw)):
        if math.isnan(specs_raw[i]) == False and math.isnan(specs_raw[i]) == False:
            specs.append(float(specs_raw[i]))
            CDR3s.append(CDR3s_raw[i])
        #data = pd.read_csv('virus_databank.csv', low_memory=False)

    idx_max = len(CDR3s)

    return CDR3s, idx_max, specs

