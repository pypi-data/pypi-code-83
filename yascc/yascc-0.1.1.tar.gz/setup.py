# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yascc']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'yascc',
    'version': '0.1.1',
    'description': 'swap cases',
    'long_description': None,
    'author': 'urm8',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
