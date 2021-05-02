#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:31:36 2021

@author: danish
"""
import pandas as pd
import numpy as np
from math import sqrt
from gt_lib.weighted_moving_average import wma

def hull_moving_avg(price_data, n):
    print(n/2)
    n_wma = wma(price_data, n)
    half_n_wma = (2 * wma(price_data, n/2))
    return wma((half_n_wma - n_wma), sqrt(n))
