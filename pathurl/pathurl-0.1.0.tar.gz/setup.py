# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pathurl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pathurl',
    'version': '0.1.0',
    'description': 'OO url manipulation',
    'long_description': '<p align="center">\n<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n',
    'author': 'Stephanos Kuma',
    'author_email': 'stephanos@kuma.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spapanik/pathurl',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
