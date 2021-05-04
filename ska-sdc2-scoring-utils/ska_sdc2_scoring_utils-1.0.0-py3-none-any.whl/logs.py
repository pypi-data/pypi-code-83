# coding: utf-8
"""Logging functions."""
import sys
import logging

LOGFORMAT_VERBOSE = "%(levelname)-7.7s| %(message)-150s [%(filename)s L%(lineno)d]"
LOGFORMAT = "%(message)-80s"


def init_logger(level=logging.DEBUG, verbose=False, use_root_logger=False):
    """Initialise the logger."""
    handler = logging.StreamHandler(sys.stdout)
    if use_root_logger:
        logger = logging.getLogger("")
    else:
        logger = logging.getLogger("ska.sdc")
    if verbose:
        formatter = logging.Formatter(LOGFORMAT_VERBOSE)
    else:
        formatter = logging.Formatter(LOGFORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
