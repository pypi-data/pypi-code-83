# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awyes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'awyes',
    'version': '0.1.0',
    'description': 'Simplify your aws deployment',
    'long_description': None,
    'author': 'trumanpurnell',
    'author_email': 'truman.purnell@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '==3.7.10',
}


setup(**setup_kwargs)
