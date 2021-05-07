# -*- coding: utf-8 -*-

"""
Some useful utilities for Python's ``threading`` module.
"""

from typing import Final, List

from simplethread.decorators import synchronized
from simplethread.decorators import threaded

__all__: Final[List[str]] = ["synchronized", "threaded"]
