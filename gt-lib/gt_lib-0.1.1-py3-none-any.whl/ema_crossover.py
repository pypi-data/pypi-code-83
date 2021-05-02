#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:13:29 2021

@author: danish
"""
import pandas as pd
import numpy as np
from gt_lib.ema import ema


# n periods ems crossover
def ema_crossover(price_data, fast_period, slow_period):
    fast_line = ema(price_data, fast_period)
    slow_line = ema(price_data, slow_period)
    signal = pd.Series(np.where(pd.Series(fast_line) > pd.Series(slow_line), 1, -1))
    graph_signal = ((signal - signal.shift(1))/2).fillna(0).astype(int)
    return graph_signal.to_numpy()
