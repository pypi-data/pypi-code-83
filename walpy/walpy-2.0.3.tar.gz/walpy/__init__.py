"""
@author: Walter Verwer
@git: https://github.com/walterverwer

"""
hard_dependecies = ['rpy2']
# Let users know if they're missing any of our hard dependencies
try:
    import rpy2
except ImportError as e:
    print('You are missing one of the following packages:', hard_dependecies,
          '\n If after installing all packages you still have some problems, ',
          'make sure that especially rpy2 is correctly installed!')

# Functions in walpy
from .r_importer import r_importer
from .suppress import suppress
from .write_run import write_run