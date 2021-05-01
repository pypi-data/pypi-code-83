# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdsort']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['sdsort = sdsort:main']}

setup_kwargs = {
    'name': 'sdsort',
    'version': '0.1.0',
    'description': 'Sorts functions and methods according to the step-down rule',
    'long_description': None,
    'author': 'Eiríkur Fannar Torfason',
    'author_email': 'eirikur.torfason@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
