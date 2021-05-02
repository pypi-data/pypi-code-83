#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:34:38 2021

@author: danish
"""
import pandas as pd
import numpy as np


def wma_apply(x):
    count = 1
    wma = 0
    for i in x:
        wma += (i*count)
        count += 1
    return wma/((len(x) * (len(x) + 1))/2)


def wma(price_data, n):
    return price_data.rolling(n).apply(wma_apply, raw=True).to_numpy()

