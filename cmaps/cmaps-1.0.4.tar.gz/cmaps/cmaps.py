#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from glob import glob

import matplotlib.cm
import numpy as np

from ._version import __version__
from .colormap import Colormap

CMAPSFILE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'colormaps')
USER_CMAPFILE_DIR = os.environ.get('CMAP_DIR')

class Cmaps(object):
    """colormaps"""

    def __init__(self, ):
        self._parse_cmaps()
        self.__version__ = __version__

    def _coltbl(self, cmap_file):
        pattern = re.compile(r'(\d\.?\d*)\s+(\d\.?\d*)\s+(\d\.?\d*).*')
        with open(cmap_file) as cmap:
            cmap_buff = cmap.read()
        cmap_buff = re.compile('ncolors.*\n').sub('', cmap_buff)
        if re.search(r'\s*\d\.\d*', cmap_buff):
            return np.asarray(pattern.findall(cmap_buff), 'f4')
        else:
            return np.asarray(pattern.findall(cmap_buff), 'u1') / 255.


    def _parse_cmaps(self):
        if USER_CMAPFILE_DIR is not None:
            cmapsflist = sorted(glob(os.path.join(USER_CMAPFILE_DIR, '*.rgb')))
            for cmap_file in cmapsflist:
                cname = os.path.basename(cmap_file).split('.rgb')[0]
                # start with the number will result illegal attribute
                if cname[0].isdigit() or cname.startswith('_'):
                    cname = 'C' + cname
                if '-' in cname:
                    cname = cname.replace('-', '_')
                if '+' in cname:
                    cname = cname.replace('+', '_')

                cmap = Colormap(self._coltbl(cmap_file), name=cname)
                matplotlib.cm.register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)

                cname = cname + '_r'
                cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
                matplotlib.cm.register_cmap(name=cname, cmap=cmap)
                setattr(self, cname, cmap)
    @property
    def N3gauss(self):
        cname = "N3gauss"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "3gauss.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def N3gauss_r(self):
        cname = "N3gauss_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "3gauss.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def N3saw(self):
        cname = "N3saw"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "3saw.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def N3saw_r(self):
        cname = "N3saw_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "3saw.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BkBlAqGrYeOrReViWh200(self):
        cname = "BkBlAqGrYeOrReViWh200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BkBlAqGrYeOrReViWh200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BkBlAqGrYeOrReViWh200_r(self):
        cname = "BkBlAqGrYeOrReViWh200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BkBlAqGrYeOrReViWh200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrWh2YeOrReVi22(self):
        cname = "BlAqGrWh2YeOrReVi22"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrWh2YeOrReVi22.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrWh2YeOrReVi22_r(self):
        cname = "BlAqGrWh2YeOrReVi22_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrWh2YeOrReVi22.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrRe(self):
        cname = "BlAqGrYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrRe_r(self):
        cname = "BlAqGrYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrReVi200(self):
        cname = "BlAqGrYeOrReVi200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlAqGrYeOrReVi200_r(self):
        cname = "BlAqGrYeOrReVi200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlAqGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlGrYeOrReVi200(self):
        cname = "BlGrYeOrReVi200"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlGrYeOrReVi200_r(self):
        cname = "BlGrYeOrReVi200_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlGrYeOrReVi200.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlRe(self):
        cname = "BlRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlRe_r(self):
        cname = "BlRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlWhRe(self):
        cname = "BlWhRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlWhRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlWhRe_r(self):
        cname = "BlWhRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlWhRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkOrange18(self):
        cname = "BlueDarkOrange18"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkOrange18.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkOrange18_r(self):
        cname = "BlueDarkOrange18_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkOrange18.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkRed18(self):
        cname = "BlueDarkRed18"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkRed18.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueDarkRed18_r(self):
        cname = "BlueDarkRed18_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueDarkRed18.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueGreen14(self):
        cname = "BlueGreen14"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueGreen14.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueGreen14_r(self):
        cname = "BlueGreen14_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueGreen14.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRed(self):
        cname = "BlueRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRed_r(self):
        cname = "BlueRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRedGray(self):
        cname = "BlueRedGray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRedGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueRedGray_r(self):
        cname = "BlueRedGray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueRedGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueWhiteOrangeRed(self):
        cname = "BlueWhiteOrangeRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueWhiteOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueWhiteOrangeRed_r(self):
        cname = "BlueWhiteOrangeRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueWhiteOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueYellowRed(self):
        cname = "BlueYellowRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BlueYellowRed_r(self):
        cname = "BlueYellowRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BlueYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BrownBlue12(self):
        cname = "BrownBlue12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BrownBlue12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def BrownBlue12_r(self):
        cname = "BrownBlue12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "BrownBlue12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_coldhot(self):
        cname = "CBR_coldhot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_coldhot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_coldhot_r(self):
        cname = "CBR_coldhot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_coldhot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_drywet(self):
        cname = "CBR_drywet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_drywet_r(self):
        cname = "CBR_drywet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_set3(self):
        cname = "CBR_set3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_set3_r(self):
        cname = "CBR_set3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_wet(self):
        cname = "CBR_wet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_wet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def CBR_wet_r(self):
        cname = "CBR_wet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "CBR_wet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Cat12(self):
        cname = "Cat12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "Cat12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Cat12_r(self):
        cname = "Cat12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "Cat12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GHRSST_anomaly(self):
        cname = "GHRSST_anomaly"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GHRSST_anomaly.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GHRSST_anomaly_r(self):
        cname = "GHRSST_anomaly_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GHRSST_anomaly.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_cool(self):
        cname = "GMT_cool"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_cool_r(self):
        cname = "GMT_cool_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_copper(self):
        cname = "GMT_copper"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_copper_r(self):
        cname = "GMT_copper_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_drywet(self):
        cname = "GMT_drywet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_drywet_r(self):
        cname = "GMT_drywet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_drywet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gebco(self):
        cname = "GMT_gebco"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gebco_r(self):
        cname = "GMT_gebco_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_globe(self):
        cname = "GMT_globe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_globe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_globe_r(self):
        cname = "GMT_globe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_globe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gray(self):
        cname = "GMT_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_gray_r(self):
        cname = "GMT_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_haxby(self):
        cname = "GMT_haxby"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_haxby_r(self):
        cname = "GMT_haxby_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_hot(self):
        cname = "GMT_hot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_hot_r(self):
        cname = "GMT_hot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_jet(self):
        cname = "GMT_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_jet_r(self):
        cname = "GMT_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_nighttime(self):
        cname = "GMT_nighttime"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_nighttime.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_nighttime_r(self):
        cname = "GMT_nighttime_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_nighttime.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_no_green(self):
        cname = "GMT_no_green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_no_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_no_green_r(self):
        cname = "GMT_no_green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_no_green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_ocean(self):
        cname = "GMT_ocean"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_ocean_r(self):
        cname = "GMT_ocean_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_paired(self):
        cname = "GMT_paired"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_paired_r(self):
        cname = "GMT_paired_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_panoply(self):
        cname = "GMT_panoply"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_panoply.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_panoply_r(self):
        cname = "GMT_panoply_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_panoply.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_polar(self):
        cname = "GMT_polar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_polar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_polar_r(self):
        cname = "GMT_polar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_polar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_red2green(self):
        cname = "GMT_red2green"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_red2green.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_red2green_r(self):
        cname = "GMT_red2green_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_red2green.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief(self):
        cname = "GMT_relief"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_r(self):
        cname = "GMT_relief_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_oceanonly(self):
        cname = "GMT_relief_oceanonly"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief_oceanonly.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_relief_oceanonly_r(self):
        cname = "GMT_relief_oceanonly_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_relief_oceanonly.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_seis(self):
        cname = "GMT_seis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_seis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_seis_r(self):
        cname = "GMT_seis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_seis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_split(self):
        cname = "GMT_split"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_split.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_split_r(self):
        cname = "GMT_split_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_split.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_topo(self):
        cname = "GMT_topo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_topo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_topo_r(self):
        cname = "GMT_topo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_topo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwyg(self):
        cname = "GMT_wysiwyg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwyg_r(self):
        cname = "GMT_wysiwyg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwyg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwygcont(self):
        cname = "GMT_wysiwygcont"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwygcont.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GMT_wysiwygcont_r(self):
        cname = "GMT_wysiwygcont_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GMT_wysiwygcont.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GSFC_landsat_udf_density(self):
        cname = "GSFC_landsat_udf_density"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GSFC_landsat_udf_density.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GSFC_landsat_udf_density_r(self):
        cname = "GSFC_landsat_udf_density_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GSFC_landsat_udf_density.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GrayWhiteGray(self):
        cname = "GrayWhiteGray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GrayWhiteGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GrayWhiteGray_r(self):
        cname = "GrayWhiteGray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GrayWhiteGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenMagenta16(self):
        cname = "GreenMagenta16"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenMagenta16.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenMagenta16_r(self):
        cname = "GreenMagenta16_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenMagenta16.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenYellow(self):
        cname = "GreenYellow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenYellow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def GreenYellow_r(self):
        cname = "GreenYellow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "GreenYellow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Accent(self):
        cname = "MPL_Accent"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Accent.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Accent_r(self):
        cname = "MPL_Accent_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Accent.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Blues(self):
        cname = "MPL_Blues"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Blues.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Blues_r(self):
        cname = "MPL_Blues_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Blues.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BrBG(self):
        cname = "MPL_BrBG"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BrBG.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BrBG_r(self):
        cname = "MPL_BrBG_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BrBG.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BuGn(self):
        cname = "MPL_BuGn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BuGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BuGn_r(self):
        cname = "MPL_BuGn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BuGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BuPu(self):
        cname = "MPL_BuPu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BuPu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_BuPu_r(self):
        cname = "MPL_BuPu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_BuPu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Dark2(self):
        cname = "MPL_Dark2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Dark2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Dark2_r(self):
        cname = "MPL_Dark2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Dark2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_GnBu(self):
        cname = "MPL_GnBu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_GnBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_GnBu_r(self):
        cname = "MPL_GnBu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_GnBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Greens(self):
        cname = "MPL_Greens"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Greens.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Greens_r(self):
        cname = "MPL_Greens_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Greens.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Greys(self):
        cname = "MPL_Greys"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Greys.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Greys_r(self):
        cname = "MPL_Greys_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Greys.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_OrRd(self):
        cname = "MPL_OrRd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_OrRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_OrRd_r(self):
        cname = "MPL_OrRd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_OrRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Oranges(self):
        cname = "MPL_Oranges"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Oranges.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Oranges_r(self):
        cname = "MPL_Oranges_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Oranges.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PRGn(self):
        cname = "MPL_PRGn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PRGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PRGn_r(self):
        cname = "MPL_PRGn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PRGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Paired(self):
        cname = "MPL_Paired"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Paired_r(self):
        cname = "MPL_Paired_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Paired.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Pastel1(self):
        cname = "MPL_Pastel1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Pastel1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Pastel1_r(self):
        cname = "MPL_Pastel1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Pastel1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Pastel2(self):
        cname = "MPL_Pastel2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Pastel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Pastel2_r(self):
        cname = "MPL_Pastel2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Pastel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PiYG(self):
        cname = "MPL_PiYG"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PiYG.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PiYG_r(self):
        cname = "MPL_PiYG_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PiYG.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuBu(self):
        cname = "MPL_PuBu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuBu_r(self):
        cname = "MPL_PuBu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuBuGn(self):
        cname = "MPL_PuBuGn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuBuGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuBuGn_r(self):
        cname = "MPL_PuBuGn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuBuGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuOr(self):
        cname = "MPL_PuOr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuOr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuOr_r(self):
        cname = "MPL_PuOr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuOr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuRd(self):
        cname = "MPL_PuRd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_PuRd_r(self):
        cname = "MPL_PuRd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_PuRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Purples(self):
        cname = "MPL_Purples"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Purples.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Purples_r(self):
        cname = "MPL_Purples_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Purples.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdBu(self):
        cname = "MPL_RdBu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdBu_r(self):
        cname = "MPL_RdBu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdGy(self):
        cname = "MPL_RdGy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdGy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdGy_r(self):
        cname = "MPL_RdGy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdGy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdPu(self):
        cname = "MPL_RdPu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdPu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdPu_r(self):
        cname = "MPL_RdPu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdPu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdYlBu(self):
        cname = "MPL_RdYlBu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdYlBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdYlBu_r(self):
        cname = "MPL_RdYlBu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdYlBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdYlGn(self):
        cname = "MPL_RdYlGn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdYlGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_RdYlGn_r(self):
        cname = "MPL_RdYlGn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_RdYlGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Reds(self):
        cname = "MPL_Reds"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Reds.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Reds_r(self):
        cname = "MPL_Reds_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Reds.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set1(self):
        cname = "MPL_Set1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set1_r(self):
        cname = "MPL_Set1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set2(self):
        cname = "MPL_Set2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set2_r(self):
        cname = "MPL_Set2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set3(self):
        cname = "MPL_Set3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Set3_r(self):
        cname = "MPL_Set3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Set3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Spectral(self):
        cname = "MPL_Spectral"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Spectral.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_Spectral_r(self):
        cname = "MPL_Spectral_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_Spectral.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_StepSeq(self):
        cname = "MPL_StepSeq"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_StepSeq.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_StepSeq_r(self):
        cname = "MPL_StepSeq_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_StepSeq.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlGn(self):
        cname = "MPL_YlGn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlGn_r(self):
        cname = "MPL_YlGn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlGn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlGnBu(self):
        cname = "MPL_YlGnBu"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlGnBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlGnBu_r(self):
        cname = "MPL_YlGnBu_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlGnBu.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlOrBr(self):
        cname = "MPL_YlOrBr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlOrBr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlOrBr_r(self):
        cname = "MPL_YlOrBr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlOrBr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlOrRd(self):
        cname = "MPL_YlOrRd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlOrRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_YlOrRd_r(self):
        cname = "MPL_YlOrRd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_YlOrRd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_afmhot(self):
        cname = "MPL_afmhot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_afmhot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_afmhot_r(self):
        cname = "MPL_afmhot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_afmhot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_autumn(self):
        cname = "MPL_autumn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_autumn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_autumn_r(self):
        cname = "MPL_autumn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_autumn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_bone(self):
        cname = "MPL_bone"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_bone.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_bone_r(self):
        cname = "MPL_bone_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_bone.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_brg(self):
        cname = "MPL_brg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_brg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_brg_r(self):
        cname = "MPL_brg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_brg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_bwr(self):
        cname = "MPL_bwr"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_bwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_bwr_r(self):
        cname = "MPL_bwr_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_bwr.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_cool(self):
        cname = "MPL_cool"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_cool_r(self):
        cname = "MPL_cool_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_cool.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_coolwarm(self):
        cname = "MPL_coolwarm"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_coolwarm.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_coolwarm_r(self):
        cname = "MPL_coolwarm_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_coolwarm.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_copper(self):
        cname = "MPL_copper"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_copper_r(self):
        cname = "MPL_copper_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_copper.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_cubehelix(self):
        cname = "MPL_cubehelix"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_cubehelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_cubehelix_r(self):
        cname = "MPL_cubehelix_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_cubehelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_flag(self):
        cname = "MPL_flag"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_flag.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_flag_r(self):
        cname = "MPL_flag_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_flag.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_earth(self):
        cname = "MPL_gist_earth"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_earth.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_earth_r(self):
        cname = "MPL_gist_earth_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_earth.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_gray(self):
        cname = "MPL_gist_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_gray_r(self):
        cname = "MPL_gist_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_heat(self):
        cname = "MPL_gist_heat"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_heat.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_heat_r(self):
        cname = "MPL_gist_heat_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_heat.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_ncar(self):
        cname = "MPL_gist_ncar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_ncar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_ncar_r(self):
        cname = "MPL_gist_ncar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_ncar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_rainbow(self):
        cname = "MPL_gist_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_rainbow_r(self):
        cname = "MPL_gist_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_stern(self):
        cname = "MPL_gist_stern"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_stern.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_stern_r(self):
        cname = "MPL_gist_stern_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_stern.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_yarg(self):
        cname = "MPL_gist_yarg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_yarg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gist_yarg_r(self):
        cname = "MPL_gist_yarg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gist_yarg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gnuplot(self):
        cname = "MPL_gnuplot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gnuplot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gnuplot_r(self):
        cname = "MPL_gnuplot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gnuplot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gnuplot2(self):
        cname = "MPL_gnuplot2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gnuplot2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_gnuplot2_r(self):
        cname = "MPL_gnuplot2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_gnuplot2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_hot(self):
        cname = "MPL_hot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_hot_r(self):
        cname = "MPL_hot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_hsv(self):
        cname = "MPL_hsv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_hsv_r(self):
        cname = "MPL_hsv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_jet(self):
        cname = "MPL_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_jet_r(self):
        cname = "MPL_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_ocean(self):
        cname = "MPL_ocean"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_ocean_r(self):
        cname = "MPL_ocean_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_ocean.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_pink(self):
        cname = "MPL_pink"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_pink.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_pink_r(self):
        cname = "MPL_pink_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_pink.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_prism(self):
        cname = "MPL_prism"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_prism.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_prism_r(self):
        cname = "MPL_prism_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_prism.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_rainbow(self):
        cname = "MPL_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_rainbow_r(self):
        cname = "MPL_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_s3pcpn(self):
        cname = "MPL_s3pcpn"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_s3pcpn.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_s3pcpn_r(self):
        cname = "MPL_s3pcpn_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_s3pcpn.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_s3pcpn_l(self):
        cname = "MPL_s3pcpn_l"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_s3pcpn_l.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_s3pcpn_l_r(self):
        cname = "MPL_s3pcpn_l_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_s3pcpn_l.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_seismic(self):
        cname = "MPL_seismic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_seismic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_seismic_r(self):
        cname = "MPL_seismic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_seismic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_spring(self):
        cname = "MPL_spring"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_spring.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_spring_r(self):
        cname = "MPL_spring_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_spring.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_sstanom(self):
        cname = "MPL_sstanom"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_sstanom.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_sstanom_r(self):
        cname = "MPL_sstanom_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_sstanom.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_summer(self):
        cname = "MPL_summer"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_summer.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_summer_r(self):
        cname = "MPL_summer_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_summer.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_terrain(self):
        cname = "MPL_terrain"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_terrain.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_terrain_r(self):
        cname = "MPL_terrain_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_terrain.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_viridis(self):
        cname = "MPL_viridis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_viridis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_viridis_r(self):
        cname = "MPL_viridis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_viridis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_winter(self):
        cname = "MPL_winter"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_winter.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def MPL_winter_r(self):
        cname = "MPL_winter_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "MPL_winter.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_banded(self):
        cname = "NCV_banded"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_banded.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_banded_r(self):
        cname = "NCV_banded_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_banded.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blu_red(self):
        cname = "NCV_blu_red"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blu_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blu_red_r(self):
        cname = "NCV_blu_red_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blu_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blue_red(self):
        cname = "NCV_blue_red"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blue_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_blue_red_r(self):
        cname = "NCV_blue_red_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_blue_red.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_bright(self):
        cname = "NCV_bright"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_bright.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_bright_r(self):
        cname = "NCV_bright_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_bright.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_gebco(self):
        cname = "NCV_gebco"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_gebco_r(self):
        cname = "NCV_gebco_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_gebco.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jaisnd(self):
        cname = "NCV_jaisnd"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jaisnd.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jaisnd_r(self):
        cname = "NCV_jaisnd_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jaisnd.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jet(self):
        cname = "NCV_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_jet_r(self):
        cname = "NCV_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_manga(self):
        cname = "NCV_manga"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_manga.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_manga_r(self):
        cname = "NCV_manga_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_manga.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_rainbow2(self):
        cname = "NCV_rainbow2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_rainbow2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_rainbow2_r(self):
        cname = "NCV_rainbow2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_rainbow2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_roullet(self):
        cname = "NCV_roullet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_roullet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NCV_roullet_r(self):
        cname = "NCV_roullet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NCV_roullet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_a(self):
        cname = "NEO_div_vegetation_a"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_a.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_a_r(self):
        cname = "NEO_div_vegetation_a_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_a.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_b(self):
        cname = "NEO_div_vegetation_b"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_b.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_b_r(self):
        cname = "NEO_div_vegetation_b_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_b.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_c(self):
        cname = "NEO_div_vegetation_c"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_c.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_div_vegetation_c_r(self):
        cname = "NEO_div_vegetation_c_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_div_vegetation_c.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_modis_ndvi(self):
        cname = "NEO_modis_ndvi"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_modis_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NEO_modis_ndvi_r(self):
        cname = "NEO_modis_ndvi_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NEO_modis_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef(self):
        cname = "NMCRef"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef_r(self):
        cname = "NMCRef_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel(self):
        cname = "NMCVel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel_r(self):
        cname = "NMCVel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NMCVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NOC_ndvi(self):
        cname = "NOC_ndvi"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NOC_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NOC_ndvi_r(self):
        cname = "NOC_ndvi_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "NOC_ndvi.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def OceanLakeLandSnow(self):
        cname = "OceanLakeLandSnow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "OceanLakeLandSnow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def OceanLakeLandSnow_r(self):
        cname = "OceanLakeLandSnow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "OceanLakeLandSnow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Gallet13(self):
        cname = "SVG_Gallet13"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Gallet13.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Gallet13_r(self):
        cname = "SVG_Gallet13_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Gallet13.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa06(self):
        cname = "SVG_Lindaa06"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa06.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa06_r(self):
        cname = "SVG_Lindaa06_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa06.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa07(self):
        cname = "SVG_Lindaa07"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa07.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_Lindaa07_r(self):
        cname = "SVG_Lindaa07_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_Lindaa07.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_bhw3_22(self):
        cname = "SVG_bhw3_22"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_bhw3_22.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_bhw3_22_r(self):
        cname = "SVG_bhw3_22_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_bhw3_22.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_es_landscape_79(self):
        cname = "SVG_es_landscape_79"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_es_landscape_79.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_es_landscape_79_r(self):
        cname = "SVG_es_landscape_79_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_es_landscape_79.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_feb_sunrise(self):
        cname = "SVG_feb_sunrise"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_feb_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_feb_sunrise_r(self):
        cname = "SVG_feb_sunrise_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_feb_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_foggy_sunrise(self):
        cname = "SVG_foggy_sunrise"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_foggy_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_foggy_sunrise_r(self):
        cname = "SVG_foggy_sunrise_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_foggy_sunrise.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_fs2006(self):
        cname = "SVG_fs2006"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_fs2006.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def SVG_fs2006_r(self):
        cname = "SVG_fs2006_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "SVG_fs2006.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def StepSeq25(self):
        cname = "StepSeq25"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "StepSeq25.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def StepSeq25_r(self):
        cname = "StepSeq25_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "StepSeq25.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def UKM_hadcrut(self):
        cname = "UKM_hadcrut"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "UKM_hadcrut.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def UKM_hadcrut_r(self):
        cname = "UKM_hadcrut_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "UKM_hadcrut.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ViBlGrWhYeOrRe(self):
        cname = "ViBlGrWhYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ViBlGrWhYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ViBlGrWhYeOrRe_r(self):
        cname = "ViBlGrWhYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ViBlGrWhYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlGrYeRe(self):
        cname = "WhBlGrYeRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlGrYeRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlGrYeRe_r(self):
        cname = "WhBlGrYeRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlGrYeRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlReWh(self):
        cname = "WhBlReWh"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhBlReWh_r(self):
        cname = "WhBlReWh_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhBlReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrRe(self):
        cname = "WhViBlGrYeOrRe"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrRe_r(self):
        cname = "WhViBlGrYeOrRe_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrRe.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrReWh(self):
        cname = "WhViBlGrYeOrReWh"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhViBlGrYeOrReWh_r(self):
        cname = "WhViBlGrYeOrReWh_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhViBlGrYeOrReWh.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlue(self):
        cname = "WhiteBlue"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlue.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlue_r(self):
        cname = "WhiteBlue_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlue.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlueGreenYellowRed(self):
        cname = "WhiteBlueGreenYellowRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlueGreenYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteBlueGreenYellowRed_r(self):
        cname = "WhiteBlueGreenYellowRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteBlueGreenYellowRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteGreen(self):
        cname = "WhiteGreen"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteGreen.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteGreen_r(self):
        cname = "WhiteGreen_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteGreen.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteYellowOrangeRed(self):
        cname = "WhiteYellowOrangeRed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteYellowOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def WhiteYellowOrangeRed_r(self):
        cname = "WhiteYellowOrangeRed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "WhiteYellowOrangeRed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg(self):
        cname = "amwg"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_r(self):
        cname = "amwg_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg256(self):
        cname = "amwg256"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg256.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg256_r(self):
        cname = "amwg256_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg256.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_blueyellowred(self):
        cname = "amwg_blueyellowred"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg_blueyellowred.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def amwg_blueyellowred_r(self):
        cname = "amwg_blueyellowred_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "amwg_blueyellowred.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_9step(self):
        cname = "cb_9step"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_9step.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_9step_r(self):
        cname = "cb_9step_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_9step.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow(self):
        cname = "cb_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_r(self):
        cname = "cb_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_inv(self):
        cname = "cb_rainbow_inv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow_inv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cb_rainbow_inv_r(self):
        cname = "cb_rainbow_inv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cb_rainbow_inv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_0(self):
        cname = "circular_0"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_0.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_0_r(self):
        cname = "circular_0_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_0.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_1(self):
        cname = "circular_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_1_r(self):
        cname = "circular_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_2(self):
        cname = "circular_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def circular_2_r(self):
        cname = "circular_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "circular_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cividis(self):
        cname = "cividis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cividis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cividis_r(self):
        cname = "cividis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cividis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_algae(self):
        cname = "cmocean_algae"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_algae.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_algae_r(self):
        cname = "cmocean_algae_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_algae.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_amp(self):
        cname = "cmocean_amp"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_amp.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_amp_r(self):
        cname = "cmocean_amp_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_amp.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_balance(self):
        cname = "cmocean_balance"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_balance.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_balance_r(self):
        cname = "cmocean_balance_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_balance.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_curl(self):
        cname = "cmocean_curl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_curl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_curl_r(self):
        cname = "cmocean_curl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_curl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_deep(self):
        cname = "cmocean_deep"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_deep.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_deep_r(self):
        cname = "cmocean_deep_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_deep.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_delta(self):
        cname = "cmocean_delta"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_delta.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_delta_r(self):
        cname = "cmocean_delta_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_delta.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_dense(self):
        cname = "cmocean_dense"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_dense.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_dense_r(self):
        cname = "cmocean_dense_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_dense.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_gray(self):
        cname = "cmocean_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_gray_r(self):
        cname = "cmocean_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_haline(self):
        cname = "cmocean_haline"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_haline.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_haline_r(self):
        cname = "cmocean_haline_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_haline.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_ice(self):
        cname = "cmocean_ice"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_ice.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_ice_r(self):
        cname = "cmocean_ice_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_ice.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_matter(self):
        cname = "cmocean_matter"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_matter.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_matter_r(self):
        cname = "cmocean_matter_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_matter.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_oxy(self):
        cname = "cmocean_oxy"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_oxy.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_oxy_r(self):
        cname = "cmocean_oxy_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_oxy.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_phase(self):
        cname = "cmocean_phase"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_phase.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_phase_r(self):
        cname = "cmocean_phase_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_phase.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_solar(self):
        cname = "cmocean_solar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_solar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_solar_r(self):
        cname = "cmocean_solar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_solar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_speed(self):
        cname = "cmocean_speed"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_speed.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_speed_r(self):
        cname = "cmocean_speed_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_speed.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_tempo(self):
        cname = "cmocean_tempo"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_tempo.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_tempo_r(self):
        cname = "cmocean_tempo_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_tempo.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_thermal(self):
        cname = "cmocean_thermal"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_thermal.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_thermal_r(self):
        cname = "cmocean_thermal_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_thermal.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_turbid(self):
        cname = "cmocean_turbid"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_turbid.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmocean_turbid_r(self):
        cname = "cmocean_turbid_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmocean_turbid.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_b2r(self):
        cname = "cmp_b2r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_b2r.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_b2r_r(self):
        cname = "cmp_b2r_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_b2r.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_flux(self):
        cname = "cmp_flux"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_flux.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_flux_r(self):
        cname = "cmp_flux_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_flux.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_haxby(self):
        cname = "cmp_haxby"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cmp_haxby_r(self):
        cname = "cmp_haxby_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cmp_haxby.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam(self):
        cname = "cosam"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam_r(self):
        cname = "cosam_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam12(self):
        cname = "cosam12"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam12.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cosam12_r(self):
        cname = "cosam12_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cosam12.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cyclic(self):
        cname = "cyclic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def cyclic_r(self):
        cname = "cyclic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "cyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def default(self):
        cname = "default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def default_r(self):
        cname = "default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def detail(self):
        cname = "detail"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "detail.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def detail_r(self):
        cname = "detail_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "detail.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def drought_severity(self):
        cname = "drought_severity"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "drought_severity.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def drought_severity_r(self):
        cname = "drought_severity_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "drought_severity.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def example(self):
        cname = "example"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "example.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def example_r(self):
        cname = "example_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "example.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def extrema(self):
        cname = "extrema"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "extrema.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def extrema_r(self):
        cname = "extrema_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "extrema.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_default(self):
        cname = "grads_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_default_r(self):
        cname = "grads_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_rainbow(self):
        cname = "grads_rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def grads_rainbow_r(self):
        cname = "grads_rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "grads_rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gscyclic(self):
        cname = "gscyclic"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gscyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gscyclic_r(self):
        cname = "gscyclic_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gscyclic.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsdtol(self):
        cname = "gsdtol"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsdtol.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsdtol_r(self):
        cname = "gsdtol_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsdtol.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsltod(self):
        cname = "gsltod"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsltod.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gsltod_r(self):
        cname = "gsltod_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gsltod.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gui_default(self):
        cname = "gui_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gui_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def gui_default_r(self):
        cname = "gui_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "gui_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix(self):
        cname = "helix"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix_r(self):
        cname = "helix_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix1(self):
        cname = "helix1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def helix1_r(self):
        cname = "helix1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "helix1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hlu_default(self):
        cname = "hlu_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hlu_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hlu_default_r(self):
        cname = "hlu_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hlu_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcold_18lev(self):
        cname = "hotcold_18lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcold_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcold_18lev_r(self):
        cname = "hotcold_18lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcold_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcolr_19lev(self):
        cname = "hotcolr_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcolr_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotcolr_19lev_r(self):
        cname = "hotcolr_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotcolr_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotres(self):
        cname = "hotres"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotres.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def hotres_r(self):
        cname = "hotres_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "hotres.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lithology(self):
        cname = "lithology"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "lithology.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def lithology_r(self):
        cname = "lithology_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "lithology.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hot(self):
        cname = "matlab_hot"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hot_r(self):
        cname = "matlab_hot_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hot.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hsv(self):
        cname = "matlab_hsv"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_hsv_r(self):
        cname = "matlab_hsv_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_hsv.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_jet(self):
        cname = "matlab_jet"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_jet_r(self):
        cname = "matlab_jet_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_jet.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_lines(self):
        cname = "matlab_lines"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_lines.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def matlab_lines_r(self):
        cname = "matlab_lines_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "matlab_lines.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mch_default(self):
        cname = "mch_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "mch_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mch_default_r(self):
        cname = "mch_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "mch_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncl_default(self):
        cname = "ncl_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncl_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncl_default_r(self):
        cname = "ncl_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncl_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncview_default(self):
        cname = "ncview_default"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncview_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def ncview_default_r(self):
        cname = "ncview_default_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "ncview_default.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nice_gfdl(self):
        cname = "nice_gfdl"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nice_gfdl.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nice_gfdl_r(self):
        cname = "nice_gfdl_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nice_gfdl.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes(self):
        cname = "nrl_sirkes"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_r(self):
        cname = "nrl_sirkes_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_nowhite(self):
        cname = "nrl_sirkes_nowhite"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes_nowhite.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def nrl_sirkes_nowhite_r(self):
        cname = "nrl_sirkes_nowhite_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "nrl_sirkes_nowhite.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perc2_9lev(self):
        cname = "perc2_9lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "perc2_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def perc2_9lev_r(self):
        cname = "perc2_9lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "perc2_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def percent_11lev(self):
        cname = "percent_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "percent_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def percent_11lev_r(self):
        cname = "percent_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "percent_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_1(self):
        cname = "posneg_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_1_r(self):
        cname = "posneg_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_2(self):
        cname = "posneg_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def posneg_2_r(self):
        cname = "posneg_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "posneg_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_1(self):
        cname = "prcp_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_1_r(self):
        cname = "prcp_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_2(self):
        cname = "prcp_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_2_r(self):
        cname = "prcp_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_3(self):
        cname = "prcp_3"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def prcp_3_r(self):
        cname = "prcp_3_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "prcp_3.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_15lev(self):
        cname = "precip2_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_15lev_r(self):
        cname = "precip2_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_17lev(self):
        cname = "precip2_17lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip2_17lev_r(self):
        cname = "precip2_17lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip2_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip3_16lev(self):
        cname = "precip3_16lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip3_16lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip3_16lev_r(self):
        cname = "precip3_16lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip3_16lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_11lev(self):
        cname = "precip4_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_11lev_r(self):
        cname = "precip4_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_diff_19lev(self):
        cname = "precip4_diff_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_diff_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip4_diff_19lev_r(self):
        cname = "precip4_diff_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip4_diff_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_11lev(self):
        cname = "precip_11lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_11lev_r(self):
        cname = "precip_11lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_11lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_12lev(self):
        cname = "precip_diff_12lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_12lev_r(self):
        cname = "precip_diff_12lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_1lev(self):
        cname = "precip_diff_1lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def precip_diff_1lev_r(self):
        cname = "precip_diff_1lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "precip_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def psgcap(self):
        cname = "psgcap"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "psgcap.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def psgcap_r(self):
        cname = "psgcap_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "psgcap.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar(self):
        cname = "radar"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_r(self):
        cname = "radar_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_1(self):
        cname = "radar_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def radar_1_r(self):
        cname = "radar_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "radar_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_gray(self):
        cname = "rainbow_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_gray_r(self):
        cname = "rainbow_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_gray(self):
        cname = "rainbow_white_gray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+white+gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_gray_r(self):
        cname = "rainbow_white_gray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+white+gray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white(self):
        cname = "rainbow_white"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+white.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_white_r(self):
        cname = "rainbow_white_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow+white.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow(self):
        cname = "rainbow"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rainbow_r(self):
        cname = "rainbow_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rainbow.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rh_19lev(self):
        cname = "rh_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rh_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def rh_19lev_r(self):
        cname = "rh_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "rh_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_1(self):
        cname = "seaice_1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_1_r(self):
        cname = "seaice_1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_2(self):
        cname = "seaice_2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def seaice_2_r(self):
        cname = "seaice_2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "seaice_2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_21(self):
        cname = "so4_21"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_21.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_21_r(self):
        cname = "so4_21_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_21.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_23(self):
        cname = "so4_23"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_23.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def so4_23_r(self):
        cname = "so4_23_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "so4_23.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spread_15lev(self):
        cname = "spread_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "spread_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def spread_15lev_r(self):
        cname = "spread_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "spread_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def srip_reanalysis(self):
        cname = "srip_reanalysis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "srip_reanalysis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def srip_reanalysis_r(self):
        cname = "srip_reanalysis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "srip_reanalysis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_9lev(self):
        cname = "sunshine_9lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_9lev_r(self):
        cname = "sunshine_9lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_9lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_diff_12lev(self):
        cname = "sunshine_diff_12lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def sunshine_diff_12lev_r(self):
        cname = "sunshine_diff_12lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "sunshine_diff_12lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def t2m_29lev(self):
        cname = "t2m_29lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "t2m_29lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def t2m_29lev_r(self):
        cname = "t2m_29lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "t2m_29lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrAvg1(self):
        cname = "tbrAvg1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrAvg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrAvg1_r(self):
        cname = "tbrAvg1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrAvg1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrStd1(self):
        cname = "tbrStd1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrStd1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrStd1_r(self):
        cname = "tbrStd1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrStd1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrVar1(self):
        cname = "tbrVar1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrVar1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbrVar1_r(self):
        cname = "tbrVar1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbrVar1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_240_300(self):
        cname = "tbr_240_300"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_240-300.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_240_300_r(self):
        cname = "tbr_240_300_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_240-300.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_stdev_0_30(self):
        cname = "tbr_stdev_0_30"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_stdev_0-30.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_stdev_0_30_r(self):
        cname = "tbr_stdev_0_30_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_stdev_0-30.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_var_0_500(self):
        cname = "tbr_var_0_500"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_var_0-500.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def tbr_var_0_500_r(self):
        cname = "tbr_var_0_500_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "tbr_var_0-500.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp1(self):
        cname = "temp1"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp1_r(self):
        cname = "temp1_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp1.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_19lev(self):
        cname = "temp_19lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_19lev_r(self):
        cname = "temp_19lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_19lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_18lev(self):
        cname = "temp_diff_18lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_18lev_r(self):
        cname = "temp_diff_18lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_18lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_1lev(self):
        cname = "temp_diff_1lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def temp_diff_1lev_r(self):
        cname = "temp_diff_1lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "temp_diff_1lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def testcmap(self):
        cname = "testcmap"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "testcmap.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def testcmap_r(self):
        cname = "testcmap_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "testcmap.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thelix(self):
        cname = "thelix"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "thelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def thelix_r(self):
        cname = "thelix_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "thelix.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def topo_15lev(self):
        cname = "topo_15lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "topo_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def topo_15lev_r(self):
        cname = "topo_15lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "topo_15lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def uniform(self):
        cname = "uniform"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "uniform.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def uniform_r(self):
        cname = "uniform_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "uniform.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_ClarkU(self):
        cname = "vegetation_ClarkU"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_ClarkU.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_ClarkU_r(self):
        cname = "vegetation_ClarkU_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_ClarkU.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_modis(self):
        cname = "vegetation_modis"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_modis.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def vegetation_modis_r(self):
        cname = "vegetation_modis_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "vegetation_modis.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wgne15(self):
        cname = "wgne15"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wgne15.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wgne15_r(self):
        cname = "wgne15_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wgne15.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wh_bl_gr_ye_re(self):
        cname = "wh_bl_gr_ye_re"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wh-bl-gr-ye-re.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wh_bl_gr_ye_re_r(self):
        cname = "wh_bl_gr_ye_re_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wh-bl-gr-ye-re.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wind_17lev(self):
        cname = "wind_17lev"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wind_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wind_17lev_r(self):
        cname = "wind_17lev_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wind_17lev.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wxpEnIR(self):
        cname = "wxpEnIR"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wxpEnIR.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def wxpEnIR_r(self):
        cname = "wxpEnIR_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "ncar_ncl",  "wxpEnIR.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Carbone42(self):
        cname = "Carbone42"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "Carbone42.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def Carbone42_r(self):
        cname = "Carbone42_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "Carbone42.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef(self):
        cname = "NMCRef"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCRef_r(self):
        cname = "NMCRef_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NMCRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel2(self):
        cname = "NMCVel2"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NMCVel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NMCVel2_r(self):
        cname = "NMCVel2_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NMCVel2.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSRef(self):
        cname = "NWSRef"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSRef_r(self):
        cname = "NWSRef_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSRef.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSSPW(self):
        cname = "NWSSPW"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSSPW.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSSPW_r(self):
        cname = "NWSSPW_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSSPW.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSVel(self):
        cname = "NWSVel"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def NWSVel_r(self):
        cname = "NWSVel_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "NWSVel.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def TopoGray(self):
        cname = "TopoGray"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "TopoGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def TopoGray_r(self):
        cname = "TopoGray_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "TopoGray.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def TwoClass(self):
        cname = "TwoClass"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "TwoClass.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def TwoClass_r(self):
        cname = "TwoClass_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "TwoClass.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mask(self):
        cname = "mask"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "mask.rgb")
        cmap = Colormap(self._coltbl(cmap_file), name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

    @property
    def mask_r(self):
        cname = "mask_r"
        if cname in matplotlib.cm._cmap_registry:
            return matplotlib.cm.get_cmap(cname)
        cmap_file = os.path.join(CMAPSFILE_DIR, "self_defined",  "mask.rgb")
        cmap = Colormap(self._coltbl(cmap_file)[::-1], name=cname)
        matplotlib.cm.register_cmap(name=cname, cmap=cmap)
        return cmap

