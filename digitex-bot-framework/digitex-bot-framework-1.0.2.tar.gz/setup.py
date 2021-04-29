# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digitex_bot_framework']

package_data = \
{'': ['*']}

install_requires = \
['digitex-engine-client']

setup_kwargs = {
    'name': 'digitex-bot-framework',
    'version': '1.0.2',
    'description': 'Digitex Bot Framework',
    'long_description': None,
    'author': 'Sergey Bugaev',
    'author_email': 'bugaevc@smartdec.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://digitex.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
