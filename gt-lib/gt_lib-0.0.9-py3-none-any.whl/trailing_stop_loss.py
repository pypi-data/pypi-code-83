#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 02:37:42 2021

@author: danish
"""
import pandas as pd
import numpy as np


def t_stop_loss(price_data, limit=-0.002):
    pct_cha = price_data.pct_change().to_numpy()
    return np.where(pct_cha < limit, -1, 0)
