#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:27:32 2020

@author: lgalarra
"""
import numpy as np
import pandas as pd

from hipar.utils import project_on_numerical_attributes, numerical_attributes, project_on_attributes
from mdlp.discretization import MDLP


class HiPaRDiscretizer :
    """
    Class used to discretize the numerical variables of a data frame. The discretization
    is based on the MDLP algorithm. MDLP uses an external categorical binary variable 'y' as reference to guarantee
    that the resulting intervals have low entropy w.r.t. 'y'. Since we work on regression analysis
      Parameters
        ----------
        force_discretization : bool, default=False
            If true, it forces the object to discretize a numerical variable even if it is suboptimal
            from an entropy point of view.
        percentile_cut : int, default=50
            MDLP discretizes the numerical variables of a dataset based on the magnitude of an external numerical
            variable provided in the fit method. This variable is binarized using the percentile cut to create two
            classes that guide the discretization.
        min_support : int, default=10
            Support threshold for discretizations. If one of the intervals obtained by discretiziting an attribute
            has less than min_support points, the attribute is discarded for discretization


    """
    def __init__(self, force_discretization=False, percentile_cut=50, min_support=10) :
        self.force_discretization = force_discretization
        self.percentile_cut = percentile_cut
        if self.force_discretization :
            self._mdlp = MDLP(min_depth=1)
        else :
            self._mdlp = MDLP()
        self.min_support = min_support

    def _binarize_target(self, y) :
        cut_value = np.percentile(y, self.percentile_cut)
        return np.array([0 if v <= cut_value else 1 for v in y])

        
    def fit(self, X, y, excluded_attributes_in_conditions=set()) :
        numerical_attrs = [x for x in numerical_attributes(X) if x not in excluded_attributes_in_conditions]
        if len(numerical_attrs) > 0 :
            self._mdlp.fit(np.array(project_on_attributes(X, numerical_attrs)), self._binarize_target(y))
        return self

    def _interval_to_str(self, attribute, interval):
        '''
        Small function to represent an interval as a string (latter usable to construct a pandas query)

        Keyword arguments:
        attribute -- the attribute name concerned by the interval
        interval -- a tuple representing the interval
        minv -- the maximum value possible for this attribute
        maxv -- the minimum value possible for this attribute
        '''
        if (interval[0] == -np.inf) and (interval[1] == np.inf):
            s = None
        elif interval[0] == -np.inf:
            s = attribute + '<' + str(interval[1])
        elif interval[1] == np.inf:
            s = attribute + '>=' + str(interval[0])
        else:
            s = attribute + '>=' + str(interval[0]) + ' and ' + attribute + '<' + str(interval[1])

        return s

    def transform(self, X, excluded_attributes_in_conditions=set()) :
        X_transformed = X.copy()
        numerical_attrs = [x for x in numerical_attributes(X) if x not in excluded_attributes_in_conditions]
        if len(numerical_attrs) == 0 :
            return X_transformed

        X_num = project_on_attributes(X, numerical_attrs)
        conv_X = self._mdlp.transform(X_num)

        for i in range(conv_X.shape[1]):
            a = numerical_attrs[i]
            intervals = self._mdlp.cat2intervals(conv_X, i)
            tmp_cols = {}
            for j, v in enumerate(intervals):
                vs = self._interval_to_str(a, v)
                if vs is not None:
                    if vs not in tmp_cols :
                        tmp_cols[vs] = pd.Series(data=[False for v in intervals],
                                                 index=X_transformed.index)

                    tmp_cols[vs].iat[j] = True

            add_attribute = True
            for vs, values in tmp_cols.items() :
                histogram = values.value_counts()
                if not histogram[histogram > self.min_support].all() :
                    add_attribute = False
                    break

            if add_attribute :
                X_transformed = pd.concat([X_transformed, pd.DataFrame(tmp_cols)], axis=1)

        return X_transformed
    
    def fit_transform(self, X, y, excluded_attributes_in_conditions=set()) :
        self.fit(X, y, excluded_attributes_in_conditions=excluded_attributes_in_conditions)
        return self.transform(X, excluded_attributes_in_conditions=excluded_attributes_in_conditions)
      

HIPARDiscretizer = HiPaRDiscretizer