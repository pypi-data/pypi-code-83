# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepgrp', 'deepgrp._scripts']

package_data = \
{'': ['*'],
 'deepgrp': ['_mss/mss.c',
             '_mss/mss.c',
             '_mss/mss.c',
             '_mss/mss.h',
             '_mss/mss.h',
             '_mss/mss.h',
             '_mss/pymss.pyx',
             '_mss/pymss.pyx',
             '_mss/pymss.pyx']}

install_requires = \
['Cython>=0.29.15,<0.30.0',
 'hyperopt>=0.2.3,<0.3.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'tensorflow==2.1.0',
 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['deepgrp = deepgrp.__main__:main',
                     'parse_rm = deepgrp._scripts.parse_rm:main',
                     'preprocess_sequence = '
                     'deepgrp._scripts.preprocess_sequence:main']}

setup_kwargs = {
    'name': 'deepgrp',
    'version': '0.2.0',
    'description': 'DNA repeat annotations',
    'long_description': None,
    'author': 'Fabian Hausmann',
    'author_email': 'fabian.hausmann@zmnh.uni-hamburg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
