# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iregex', 'iregex.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'iregex',
    'version': '0.1.3',
    'description': 'An idiomatic regex generator using OOP principals instead of long unreadable strings.',
    'long_description': None,
    'author': 'Ryan',
    'author_email': 'ryanpeach@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
