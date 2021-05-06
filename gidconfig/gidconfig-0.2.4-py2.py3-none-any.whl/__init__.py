"""
Configuration provider package, that exposes the section as attribute and also automatically keeps the config file and object in sync.
Through the Factory/Strategy the config objects are singletons as long as they point to the same file.
"""

__version__ = '0.2.4'

from .standard import *
from .data import *
import logging
import gidlogger as glog

log = glog.library_base_logger(__name__)
