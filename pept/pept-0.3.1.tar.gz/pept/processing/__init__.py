#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# File   : __init__.py
# License: GNU v3.0
# Author : Andrei Leonard Nicusan <a.l.nicusan@bham.ac.uk>
# Date   : 22.06.2020


'''The PEPT-oriented post-processing suite, including occupancy grid,
vector velocity fields, etc.

Summary
-------
This module contains fast, robust functions that operate on PEPT-like data
and integrate with the `pept` library's base classes.

Modules Provided
----------------

::

    pept.processing
    │
    Functions imported into the subpackage root:
    ├── circles2d :             Pixellise circles onto occupancy grid.
    ├── occupancy2d :           Pixellise trajectories onto occupancy grid.
    ├── circles2d_ext :         Circle pixellisation low-level Cython routine.
    └── occupancy2d_ext :       Trajectory pixellisation low-level C routine.

'''


from    .occupancy      import  circles2d
from    .occupancy      import  occupancy2d

from    .circles_ext    import  circles2d_ext
from    .occupancy_ext  import  occupancy2d_ext



__all__ = [
    "circles2d",
    "occupancy2d",
    "circles2d_ext",
    "occupancy2d_ext",
]


__license__ = "GNU v3.0"
__maintainer__ = "Andrei Leonard Nicusan"
__email__ = "a.l.nicusan@bham.ac.uk"
__status__ = "Beta"
