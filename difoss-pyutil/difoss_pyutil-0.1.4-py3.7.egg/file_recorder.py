#!python3
# -*- coding:utf-8 -*-
# author: difosschan
#
__all__ = (
    'update',
    'pick',
    'store',
)

from typing import *
from . import P
import functools
import inspect
import os
import json


def pick(filename: str):
    o = {}
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            o.update(json.load(f))
    return o

def store(filename: str, o: Any):
    dir_name = os.path.dirname(filename)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(filename, 'w') as f:
        json.dump(o, f, indent=2)


def update(join_filename_by_kwargs: Callable[[dict,], str]):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            args_dict = dict(zip(inspect.getfullargspec(func).args, args))
            args_dict.update(kwargs)
            filename = join_filename_by_kwargs(**args_dict)
            # P('update()', filename=filename, _must=True)
            o = dict(
                project_name=args_dict.get('project_name', ''),
                base_path=args_dict.get('base_path', ''),
            )
            o.update(pick(filename))
            kwargs.update({'_o': o})

            d = func(*args, **kwargs)
            if d:
                store(filename, d)

            return d

        return inner
    return wrapper
