# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyglslify']
setup_kwargs = {
    'name': 'pyglslify',
    'version': '0.1.0',
    'description': 'Thin wrapper for the glslify nodejs tool, use stack.gl shader modules in Python.',
    'long_description': None,
    'author': 'Anentropic',
    'author_email': 'ego@anentropic.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
