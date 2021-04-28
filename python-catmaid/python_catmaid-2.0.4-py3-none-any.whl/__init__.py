__version__ = "2.0.4"
__version_vector__ = (2, 0, 4)

from . import config

logger = config.logger

# Flatten namespace by importing contents of all modules of pymaid
from .fetch import *
from .client import *
from .upload import *
from .cluster import *
from .user_stats import *
from .core import *
from .utils import *
from .morpho import *
from .connectivity import *

"""
try:
    from .snapshot import *
except Exception as error:
    logger.warning(str(error))
    logger.warning('Error importing pymaid.snapshot:\n' + str(error))
"""
