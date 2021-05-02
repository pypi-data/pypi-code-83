# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eventual_rmq']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=6.8.0,<7.0.0', 'eventual>=0,<1', 'orjson>=3.5.2,<4.0.0']

setup_kwargs = {
    'name': 'eventual-rmq',
    'version': '0.2.1',
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
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
