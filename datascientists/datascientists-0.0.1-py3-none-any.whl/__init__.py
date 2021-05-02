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

# Preprocessing
from datascientists.core.preprocessing import *

# Regression
from datascientists.core.regression import *

# Hypothesis Testing
from datascientists.core.hypothesisTesting import *

# module level doc-string
__doc__ = f"""
NAME
    datascientists - https://zacks.one

AUTHOR
    Zacks Shen

DESCRIPTION
    Quick Data Science tools.

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