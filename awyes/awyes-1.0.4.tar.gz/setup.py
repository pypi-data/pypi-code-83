# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awyes']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.62,<2.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'awyes',
    'version': '1.0.4',
    'description': 'Simplify aws deployment',
    'long_description': None,
    'author': 'trumanpurnell',
    'author_email': 'truman.purnell@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
