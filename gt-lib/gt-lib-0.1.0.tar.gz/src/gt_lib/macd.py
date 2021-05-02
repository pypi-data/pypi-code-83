#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:06:52 2021

@author: danish
"""

import pandas as pd
import numpy as np
from gt_lib.ema import ema


# n period MACD
def macd(price_data, short_window=12, long_window=26, signal_window=9):
    short_ma = ema(price_data, short_window)
    long_ma = ema(price_data, long_window)
    macd_line = short_ma - long_ma
    signal_line = ema(pd.Series(macd_line), signal_window)
    return macd_line, signal_line, (macd_line - signal_line)
