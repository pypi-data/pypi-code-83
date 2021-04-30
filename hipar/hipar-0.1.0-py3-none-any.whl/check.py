#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:30:05 2020

@author: lgalarra
"""

def _check_min_support(min_support) :
    if isinstance(min_support, int):
        if min_support < 1:
            raise ValueError("Minimum support must be strictly positive")
    elif isinstance(min_support, float):
        if min_support < 0 or min_support > 1:
            raise ValueError("Minimum support must be between 0 and 1 (inclusive)")
    else:
        raise TypeError("Mimimum support must be of type int or float")
    return min_support

def _check_overlap_bias(overlap_bias) :
    if isinstance(overlap_bias, int) or isinstance(overlap_bias, float) :
        if overlap_bias < 0 :
            raise ValueError("Overlap bias must be non-negative")
    else :
        raise TypeError("Overlap bias must be of type int or float")
        
    return overlap_bias

def _check_support_bias(support_bias) :
    if isinstance(support_bias, int) or isinstance(support_bias, float) :
        if support_bias < 0 :
            raise ValueError("Support bias must be non-negative")
    else :
        raise TypeError("Support bias must be of type int or float")
        
    return support_bias


def _check_min_k(k):
    if isinstance(k, int) :
        if k < 1:
            raise ValueError("You must select at least 1 rule")
    else:
        raise TypeError("Number of rules 'min_k' must be of type int")

    return k

def _check_iv_percentile(percentile) :
    if isinstance(percentile, int) or (isinstance(percentile, float)
                                       and percentile.is_integer()) :
        if percentile < 0 or percentile > 100 :
            raise TypeError("Interclass variance percentile must be between 0 and 100 (inclusive)")
            
    else :
        raise TypeError("Interclass variance must be an integer")

    return percentile

def _check_cross_validation_rounds(k) :
    if isinstance(k, int) :
        if k < 2 :
            raise ValueError("The number of cross-validation rounds must be of at least 2")
    else :
        raise TypeError("Number of cross-validation rounds must be of type int")

    return k