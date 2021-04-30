# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'inp',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'aahnik',
    'author_email': 'daw@aahnik.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
