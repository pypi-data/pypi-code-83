"""
@author: Walter Verwer
@git: https://github.com/walterverwer

"""

# Let users know if they're missing any of our hard dependencies
hard_dependencies = ('rpy2')
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f'{dependency}: {e}')

if missing_dependencies:
    raise ImportError(
        'Unable to import required dependencies:\n' + '\n'.join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

# Functions in walpy
from .r_importer import r_importer
from .suppress import suppress
from .write_run import write_run