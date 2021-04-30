"""
# package wizzi utils:
## Installation:
```bash
pip install wizzi_utils
```
## Usage
```bash
import wizzi_utils as wu # improts all that is available
```
* The above will give you access to all functions and tests that the dependencies modules in them is installed in your
python environment.<br />
* Everything in misc_tools and misc_tools_test must work because when you 'pip install wizzi_utils', setup.py makes sure
to install the requirements to misc_tools module.  <br />
* Everything else, e.g. torch_tools, will work only if you have all the modules needed for torch_tools installed.
  * In torch_tools example, to know what is needed go to:
    wizzi_utils.torch.\_\_init__.py # for the tools
    wizzi_utils.torch.test.\_\_init__.py # for the tests and examples

## Examples:
```bash
import wizzi_utils as wu

# direct access to the misc_tools module - must work
print(wu.misc_tools.to_str(var=1, title='my_int'))

# access to a function in the main module misc_tools via name space 'wu' - must work
print(wu.to_str(var=2, title='my_int'))  # notice only wu namespace

# access to a function in the torch module - will work if you have torch and the rest of the modules needed
print(wu.tt.to_str(var=3, title='my_int')) # notice wu and tt namespaces. tt for torch tools

# access to a function in the matplotlib module - same rules as torch example above
print(wu.pyplt.get_RGB_color(color_str='r'))

# access to a module test
wu.algs.test.test_all()  # all tests
wu.algs.test.find_centers_test() # specific test
wu.test.to_str_test()  # access mist tools tests
```
"""

__version__ = '6.0.4'
# __all__ = ['misc_tools']  # TODO future

# default package - available without extra namespace
from wizzi_utils.misc import *

# extra packages - available with extra namespace - requires extra modules
from wizzi_utils import algorithms as algs
from wizzi_utils import coreset as cot
from wizzi_utils import json as jt
from wizzi_utils import open_cv as cvt
from wizzi_utils import pyplot as pyplt
from wizzi_utils import socket as st
from wizzi_utils import torch as tt


def test_all_modules():
    # misc package
    test.test_all()

    try:
        # algorithms package
        algs.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # coreset package
        cot.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # json package
        jt.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # open_cv package
        cvt.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # pyplot package
        pyplt.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # socket package
        st.test.test_all()
    except AttributeError as err:
        exception_error(err)

    try:
        # torch package
        tt.test.test_all()
    except AttributeError as e:
        exception_error(e)
    return
