# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['typecho']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'typecho',
    'version': '0.1.0',
    'description': 'A simple and powerful asgi web framework.',
    'long_description': None,
    'author': 'zzp198',
    'author_email': 'zzp198@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
