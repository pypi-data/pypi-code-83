#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 4 17:54:00 2021

@author: lgalarra
"""
import numpy as np

from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score

smaller_the_better = lambda x, y : x < y
larger_the_better = lambda x, y : x > y

metric_comparators_dict = {mean_squared_error : smaller_the_better,
                           median_absolute_error : smaller_the_better,
                           r2_score : larger_the_better}

def better_performance(metric, v1, v2):
    return metric_comparators_dict[metric](v1, v2)


def interclass_variance(tids, y, y_mean=None) :
    full_index = set(y.index)
    global_mean = np.mean(y) if y_mean is None else y_mean
    tids_c = list(full_index.difference(set(tids)))
    pattern_mean = np.mean(y.loc[tids])
    pattern_complement_mean = np.mean(y.loc[tids_c])
    return len(tids) * pow(pattern_mean - global_mean, 2)  + len(tids_c) * pow(pattern_complement_mean - global_mean, 2)