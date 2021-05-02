#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:29:08 2021

@author: danish
"""
import pandas as pd
import numpy as np
from gt_lib.rsi import rsi


def stochastic_rsi(price_data):
    rsi_data = rsi(price_data)
    period_max_rsi = rsi_data.rolling(14).max()
    period_min_rsi = rsi_data.rolling(14).min()
    return (rsi - period_min_rsi) / (period_max_rsi - period_min_rsi)
