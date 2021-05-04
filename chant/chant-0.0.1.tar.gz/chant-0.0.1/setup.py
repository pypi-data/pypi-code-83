# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['chant']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'chant',
    'version': '0.0.1',
    'description': '',
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
