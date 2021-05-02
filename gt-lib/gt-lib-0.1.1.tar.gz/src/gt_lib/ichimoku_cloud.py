#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:32:29 2021

@author: danish
"""
import pandas as pd
import numpy as np


def ichimoku_cloud(high_price, low_price, close_price):
    conversion_line = (high_price.rolling(9).max() + low_price.rolling(9).min()) / 2
    base_line = (high_price.rolling(26).max() + low_price.rolling(26).min()) / 2
    leading_span_a = (conversion_line + base_line) / 2
    leading_span_b = (high_price.rolling(52).max() + low_price.rolling(52).min()) / 2
