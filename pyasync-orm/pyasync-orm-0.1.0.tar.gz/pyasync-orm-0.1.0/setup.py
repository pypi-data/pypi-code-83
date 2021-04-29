# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyasync_orm']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyasync-orm',
    'version': '0.1.0',
    'description': 'An async ORM.',
    'long_description': None,
    'author': 'Ron Williams',
    'author_email': 'rnwprogramming@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
