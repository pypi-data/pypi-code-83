# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("pandas", "numpy", "plotly", "scipy")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

# datascientists version
from datascientists._version import __version__

# Hypothesis Testing
from datascientists.core.hypothesisTesting import *

# Preprocessing
from datascientists.core.preprocessing import *

# Regression
from datascientists.core.regression import *

# Simulation
from datascientists.core.simulation import *

# Statistical Test
from datascientists.core.statisticalTest import *

# module level doc-string
__doc__ = f"""
NAME
    datascientists - https://pypi.org/project/datascientists/

AUTHOR
    Zacks Shen

DESCRIPTION
    Quick Data Science tools, providing data processing and visualization in Hypotheses Testing, Regression, and etc.

README
    https://pypi.org/project/datascientists/

DEPENDICES
    numpy
    pandas
    scipy
    plotly
    kaleido
    jupyter
    jupyterlab
    ipywidgets
"""