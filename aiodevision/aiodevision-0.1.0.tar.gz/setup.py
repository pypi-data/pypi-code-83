# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiodevision']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'aiodevision',
    'version': '0.1.0',
    'description': 'A simple asynchronous wrapper for the Idevision API.',
    'long_description': None,
    'author': 'MrKomodoDragon',
    'author_email': 'svrchn921@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
