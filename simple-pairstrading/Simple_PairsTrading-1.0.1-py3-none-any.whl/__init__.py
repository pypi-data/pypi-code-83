#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from Simple_PairsTrading import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import norm
import pmdarima as pm
from datetime import date
from dateutil.relativedelta import relativedelta
import yfinance as yf
import statsmodels.tsa.stattools as ts
import datetime
import itertools
from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn
from scipy.signal import find_peaks
from scipy.signal import savgol_filter
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint
import sys


