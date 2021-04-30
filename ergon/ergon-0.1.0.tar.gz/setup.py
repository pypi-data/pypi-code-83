# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ergon']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.63.0,<0.64.0']

setup_kwargs = {
    'name': 'ergon',
    'version': '0.1.0',
    'description': 'Fullstack python framework faster release product.',
    'long_description': None,
    'author': 'Quan Vu',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
