# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['til']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['til = til.main:til_command']}

setup_kwargs = {
    'name': 'til-cli',
    'version': '0.1.0',
    'description': 'Keep track of things you learn each day',
    'long_description': None,
    'author': 'Kamyar Ghasemlou',
    'author_email': 'github@kamy.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
