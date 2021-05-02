
from __future__ import absolute_import

from __future__ import print_function

from __future__ import division

from io import open

# -----------------------------------------------------------------------------

from wsurf.geolab.geometry.bsplinesurface import BsplineSurface


def open_obj_file(file_name):
    file_name = str(file_name)
    obj_file = open(file_name, encoding='utf-8')
    for l in obj_file:
        splited_line = l.split(' ')
        # bspline surface
        if splited_line[0] == 'surf':
           return BsplineSurface(file_name)
    return None