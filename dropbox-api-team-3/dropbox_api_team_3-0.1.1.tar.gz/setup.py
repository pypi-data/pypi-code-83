# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dropbox_api_team_3']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'dropbox>=11.7.0,<12.0.0',
 'pytest-mock>=3.6.0,<4.0.0',
 'python-dotenv>=0.17.1,<0.18.0']

entry_points = \
{'console_scripts': ['dropbox_api_team_3 = dropbox_api_team_3.main:main']}

setup_kwargs = {
    'name': 'dropbox-api-team-3',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
