#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:07:08 2021

@author: danish
"""
import pandas as pd
import numpy as np


# sma calculator
def sma(close_price, n=12):
    if n >= 1 and isinstance(n, int):
        return close_price.rolling(n).mean().to_numpy()
    else:
        return np.nan
