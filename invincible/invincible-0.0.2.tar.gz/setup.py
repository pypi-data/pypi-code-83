# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['invincible']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0']

entry_points = \
{'console_scripts': ['invincible = invincible:main']}

setup_kwargs = {
    'name': 'invincible',
    'version': '0.0.2',
    'description': 'Keep restarting process for ever',
    'long_description': '',
    'author': 'Hernan Ezequiel Di Giorgi',
    'author_email': 'hernan.digiorgi@gmail.com',
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
