# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['muscad', 'muscad.utils', 'muscad.vitamins']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'muscad',
    'version': '0.5.0',
    'description': '',
    'long_description': None,
    'author': 'Guillaume Pujol',
    'author_email': 'guillp.linux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
