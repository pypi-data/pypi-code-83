import importlib_resources as _resources

try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser


# Version of easydubins package
__version__ = "1.2.0"

# Read config file
_cfg = _ConfigParser()
with _resources.path("easydubins", "config.cfg") as _path:
    _cfg.read(str(_path))
DECIMAL_ROUND = int(_cfg.get("fixed", "decimal_round"))
