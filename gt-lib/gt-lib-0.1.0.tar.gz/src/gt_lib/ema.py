#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:02:24 2021

@author: danish
"""
import pandas as pd
import numpy as np


# ema calculator
def ema(close_price, n=12):
    if n >= 1:
        if not isinstance(n, int):
            print('n is not an int value')
        return close_price.ewm(span=n, min_periods=n).mean().to_numpy()
    else:
        return np.nan
