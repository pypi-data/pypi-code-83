#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 01:22:23 2021

@author: danish
"""
import pandas as pd
import numpy as np


def reversal_cal(x):
    temp = x[:3]
    curr = x[3]
    if (temp == 1).all() and curr == -1:
        return -1
    elif (temp == -1).all() and curr == 1:
        return 1
    else:
        return 0


def reversal(close_price, open_price):
    c_o_signal = np.where(close_price - open_price > 0, 1, -1)
    reversal_signal = c_o_signal.rolling(4).apply(reversal_cal,)
    return reversal_signal
