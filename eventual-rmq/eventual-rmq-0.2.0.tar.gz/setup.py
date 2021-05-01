# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eventual_rmq']

package_data = \
{'': ['*']}

install_requires = \
['eventual>=0,<1']

setup_kwargs = {
    'name': 'eventual-rmq',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Ivan Dmitriesvkii',
    'author_email': 'ivan.dmitrievsky@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
