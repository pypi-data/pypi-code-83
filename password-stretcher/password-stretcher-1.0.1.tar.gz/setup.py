# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['password_stretcher', 'password_stretcher.lib', 'password_stretcher.lib.stat']

package_data = \
{'': ['*'],
 'password_stretcher': ['lists/*'],
 'password_stretcher.lib.stat': ['assets/*']}

install_requires = \
['requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['password-stretcher = password_stretcher.stretcher:main']}

setup_kwargs = {
    'name': 'password-stretcher',
    'version': '1.0.1',
    'description': 'A deadly password mangler',
    'long_description': None,
    'author': 'TheTechromancer',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
