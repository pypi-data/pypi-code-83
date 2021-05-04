"""
datascientists._config is considered explicitly upstream of everything else in pandas,
should have no intra-pandas dependencies.

importing `dates` and `display` ensures that keys needed by _libs
are initialized.
"""

from datascientists._config.pandas_config import *
from datascientists._config.plotly_config import *