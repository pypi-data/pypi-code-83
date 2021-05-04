# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['actymath', 'actymath.columns']

package_data = \
{'': ['*'], 'actymath': ['table_data/*']}

install_requires = \
['pandas>=1.1.5,<2.0.0', 'parse>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'actymath',
    'version': '0.1.0',
    'description': 'Actuarial Math and commutation functions for life insurance product - with a Pandas backend',
    'long_description': None,
    'author': 'Matt Gosden',
    'author_email': 'mdgosden@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ttamg/actymath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
