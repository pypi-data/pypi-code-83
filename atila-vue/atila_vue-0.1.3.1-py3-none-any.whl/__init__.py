__version__ = "0.1.3.1"

import os
import sys
import skitai
from . import services

BASE_DIR = os.path.dirname (__file__)
sys.path.insert (0, os.path.join (os.path.dirname (__file__), 'entities', 'models'))

def __config__ (pref):
    skitai.mount ("/", os.path.join (BASE_DIR, 'entities/wsgi:application'), pref, name = 'entities')

def __setup__ (app, mntopt):
    app.mount ("/", services)
