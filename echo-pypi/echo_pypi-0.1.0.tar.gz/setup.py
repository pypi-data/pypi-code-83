# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['echo_pypi']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

setup_kwargs = {
    'name': 'echo-pypi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
