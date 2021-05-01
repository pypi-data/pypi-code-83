import time
import os
import re
from pythonapm import constants
from pythonapm.constants import skip_urls

try:
    from collections.abc import Callable  # noqa
except ImportError:
    from collections import Callable  # noqa

def current_milli_time():
    return int(round(time.time() * 1000))


def is_non_empty_string(string):
    if not isinstance(string, str):
        return False
    elif string == '':
        return False

    return True

def is_empty_string(string):
    if isinstance(string, str):
        if string == '':
            return True
    
    return False

def is_digit(char):
    if isinstance(char,str):
        return char.isdigit()  
    elif isinstance(char,int):
        if char >= 0 and char <= 9:
            return True  
    return False

def is_callable(fn):
    return isinstance(fn, Callable)


def is_allowed_url(url):
    if not is_non_empty_string(url):
        return False
    
    if url.endswith(skip_urls):
        return False

    return True

def get_normalized_url(url):
    if is_non_empty_string(url):
        return re.sub(r"/\d+/","/*/", url)

    return url



