#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:22:33 2021

@author: danish
"""
import pandas as pd
import numpy as np


def bearish_fractal(x):
    if (x[2] >= x).all():
        return -1
    return 0


def bullish_fractal(x):
    if (x[2] <= x).all():
        return 1
    return 0


def fractal(high_price, low_price):
    bearish_sig = high_price.rolling(5).apply(bearish_fractal, raw=False).to_numpy()
    bullish_sig = low_price.rolling(5).apply(bullish_fractal, raw=False).to_numpy()
    return bearish_sig, bullish_sig
