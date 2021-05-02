#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:41:16 2021

@author: danish
"""
import pandas as pd
import numpy as np
from gt_lib.ema import ema


def double_ema(price_data, n):
    ma = ema(price_data, n)
    return (2 * ma - ema(pd.Series(ma))).to_numpy()
