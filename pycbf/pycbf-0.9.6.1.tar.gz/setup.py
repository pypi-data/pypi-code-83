# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycbf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycbf',
    'version': '0.9.6.1',
    'description': 'An API for CBF/imgCIF Crystallographic Binary Files',
    'long_description': '# `pycbf` - CBFlib for python\n\nThis repository builds the `pycbf` portion of [CBFlib] only, as a\nbinary wheel installable through `pip install pycbf`.\n\nIn order to do this, it has some limitations compared to the full build of CBFlib:\n\n- No HDF5 bindings\n- No (custom) libTiff bindings\n- No CBF regex capabilities\n\n[cbflib]: https://github.com/yayahjb/cbflib\n',
    'author': 'Herbert J. Bernstein',
    'author_email': 'yaya@bernstein-plus-sons.com',
    'maintainer': 'Nicholas Devenish',
    'maintainer_email': 'ndevenish@gmail.com',
    'url': 'http://www.bernstein-plus-sons.com/software/CBF/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
