#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:16:31 2021

@author: danish
"""
import pandas as pd
import numpy as np


# n period volatility calculator
def volatility(price_data, n=0):
    if n == 0:
        n = len(price_data)
    if n >= 1 and isinstance(n, int):
        return price_data.rolling(n).std().to_numpy()
    else:
        return np.nan
