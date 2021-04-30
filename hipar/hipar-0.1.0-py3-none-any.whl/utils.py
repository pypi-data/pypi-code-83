#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:38:41 2020

@author: lgalarra
"""
import pandas as pd
import numpy as np
from hipar.types import DataSeries

def project_on_attributes(df : pd.DataFrame, attrs : list) :
    result = []
    if isinstance(df, pd.DataFrame) :
        return df[attrs]
    elif isinstance(df, pd.Series) or isinstance(df, dict) :
        for a in attrs :
            result.append((a, df[a]))

    return pd.Series([x[1] for x in result], index=[x[0] for x in result])

def project_on_numerical_attributes(df : DataSeries) :
    result = {}
    if isinstance(df, pd.DataFrame) :
        return df[numerical_attributes(df)]
    elif isinstance(df, pd.Series) or isinstance(df, dict) :
        for k in df.keys() :
            if type(df[k]) in [int, float, np.int64, np.float64] :
                result[k] = df[k]
    return pd.Series(result)

def numerical_attributes(df: pd.DataFrame) :
    return list(df.select_dtypes(include=np.number))

def project_on_categorical_attributes(df: pd.DataFrame) :
    result = {}
    if isinstance(df, pd.DataFrame) :
        return df[categorical_attributes(df)]
    elif isinstance(df, pd.Series) or isinstance(df, dict) :
        for k in df.keys() :
            if type(df[k]) not in [int, float, np.int64, np.float64] :
                result[k] = df[k]
    return pd.Series(result)

def categorical_attributes(df: pd.DataFrame) :
    return list(df.select_dtypes(exclude=['int64', 'float64']))
