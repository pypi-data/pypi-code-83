#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

import numpy as np

# -----------------------------------------------------------------------------

'''_'''

__author__ = 'Davide Pellis'


def sum_repeated(array, field):
    field = field[:]
    imap = np.zeros(np.amax(field)+1, dtype=np.int)
    index = np.arange(array.shape[0])
    k, j = np.unique(field, True)
    imap[k] = np.arange(k.shape[0])
    result = array[j]
    field = np.delete(field,j)
    index = np.delete(index,j)
    while field.shape[0] > 0:
        _, j = np.unique(field, True)
        result[imap[field[j]]] += array[index[j]]
        field = np.delete(field,j)
        index = np.delete(index,j)
    return result


def repeated_range(array, offset=0):
    if array.shape[0] == 0:
        return np.array([])
    k = np.unique(array)
    imap = np.zeros(np.amax(k) + 1, dtype=np.int)
    imap[k] = np.arange(offset, offset + k.shape[0])
    rrange = imap[array]
    return rrange


def orthogonal_vectors(array):
    array = format_array(array)
    if len(array.shape) == 1:
        return orthogonal_vector(array)
    O = np.zeros(array.shape)
    O[:,0] = - array[:,1]
    O[:,1] = array[:,0]
    O[np.where((O[:,0] == 0) & (O[:,1] == 0))[0],1] = 1
    O = O / np.linalg.norm(O, axis=1, keepdims=True)
    return O


def orthogonal_vector(array):
    if array[0] == 0 and array[1] == 0:
            if array[2] == 0:
                raise ValueError('zero vector')
            return np.array([1,0,0])
    O = np.array([-array[1],array[0],0])
    return O / np.linalg.norm(O)


def normalize(array, axis=1):
    array = format_array(array)
    eps = 1e-10
    array = array / (np.linalg.norm(array, axis=axis, keepdims=True) + eps)
    return array


def remap(source, target_range=(0,1)):
    t_int = target_range[1] - target_range[0]
    s_min = np.min(source)
    s_max = np.max(source)
    s_int = s_max - s_min
    s = t_int/s_int
    remapped = (source - s_min) * s + target_range[0]
    return remapped


def format_array(array, shape=None):
    if array is None:
        return None
    if type(shape) is int:
        shape = (shape,)
    if type(array) == float or type(array) == int:
        array = np.array(array)
    elif type(array) == tuple:
        array = list(array)
    if type(array) == list:
        array = np.array(array)
    if shape is None or array.shape == shape:
        return array
    else:
        array_shape = list(array.shape)
        for i in range(len(shape)-len(array.shape)):
            array_shape = [1] + array_shape
        shape = np.array(shape)
        array_shape = np.array(array_shape)
        shape[shape == None] = array_shape[shape == None]
        repeats = shape - array_shape + 1
        array = np.tile(array, repeats)
        cmd = 'array['
        for n in shape:
            cmd += ':{},'.format(n)
        cmd += ']'
        array = eval(cmd)
    return array

            
def bounding_shape(arrays):
    shape = []
    for array in arrays:
        if type(array) != np.ndarray:
            array = np.array(array)
        for i in range(len(array.shape) - len(shape)):
            shape = [1] + shape
        for i in range(len(shape)):
            if array.shape[i] > shape[i]:
                shape[i] = array.shape[i]
    return shape

    
    
    
    
    
    
    
    
    
    
    
    
    
    