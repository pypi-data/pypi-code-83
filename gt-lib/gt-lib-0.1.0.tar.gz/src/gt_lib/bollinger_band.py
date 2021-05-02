#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:02:38 2021

@author: danish
"""
import pandas as pd
import numpy as np
from gt_lib.sma import sma
from gt_lib.ema import ema
from gt_lib.volatility import volatility


# n period bolliger band
def bollinger_band(price_data, period=20, n=2, ma='sma'):
    n = abs(n)
    if ma == 'sma':
        mean_line = sma(price_data, period)
    elif ma == 'ema':
        mean_line = ema(price_data, period)

    upper_line = mean_line + n * volatility(price_data, period)
    lower_line = mean_line - n * volatility(price_data, period)
    return upper_line, mean_line, lower_line
