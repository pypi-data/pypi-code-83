

# region [Imports]


import asyncio
import gc
import os
import re
import sys
import json
import lzma
import time
import queue
import platform
import subprocess
from enum import Enum, Flag, auto
from time import sleep, time
from pprint import pprint, pformat
from typing import Union
from datetime import tzinfo, datetime, timezone, timedelta
from functools import wraps, lru_cache, singledispatch, total_ordering, partial
from contextlib import contextmanager
from collections import Counter, ChainMap, deque, namedtuple, defaultdict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from inspect import isfunction, ismethod, isroutine, isclass


import gidlogger as glog


# endregion[Imports]

# region [TODO]


# endregion [TODO]

# region [AppUserData]


# endregion [AppUserData]

# region [Logging]

log = glog.aux_library_logger(__name__)

# endregion[Logging]

# region [Constants]


# endregion[Constants]


def debug_timing_print(func):
    @wraps(func)
    def _function_print_time(*args, **kwargs):
        start_time = time()
        _out = func(*args, **kwargs)
        if hasattr(args[0], func.__name__):
            report = f"'{func.__name__}' of the '{args[0].__class__.__name__}' class took {str(round(time()-start_time, ndigits=4))} seconds"
        else:
            report = f"'{func.__name__}' took {str(round(time()-start_time, ndigits=4))} seconds"

        print(report)
        return _out
    if os.getenv('IS_DEV') == 'true':
        return _function_print_time
    else:
        return func


def debug_timing_log(logger):
    def _decorator(func):
        @wraps(func)
        def _function_print_time(*args, **kwargs):
            start_time = time()
            _out = func(*args, **kwargs)
            if hasattr(args[0], func.__name__):
                report = f"'{func.__name__}' of '{str(args[0])}' took {str(round(time()-start_time, ndigits=4))} seconds"
            else:
                report = f"'{func.__name__}' took {str(round(time()-start_time, ndigits=4))} seconds"

            logger.debug(report, extra={'func_name_override': func.__name__})
            return _out
        if os.getenv('IS_DEV') == 'true':
            return _function_print_time
        else:
            return func

    return _decorator


# region[Main_Exec]


if __name__ == '__main__':
    pass

# endregion[Main_Exec]
