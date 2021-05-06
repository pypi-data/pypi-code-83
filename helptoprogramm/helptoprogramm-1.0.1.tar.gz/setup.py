# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['helptoprogramm']
setup_kwargs = {
    'name': 'helptoprogramm',
    'version': '1.0.1',
    'description': '',
    'long_description': None,
    'author': 'tikotstudio',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
