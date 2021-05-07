#!/usr/local/bin python3
# -*- coding: utf-8 -*-

"""
    created by iprobeyang@gmail.com 2021/5/7
"""
from fast_tracker.utils import functions

filename = 'a'
line = 20
lineno = functions
name='d'
trace = "filename:{fn}, line:{ln}, lineno:{lo}, func_name:{fu}".format(
            fn=filename, ln=line, lo=lineno, fu=name
        )
print(trace)