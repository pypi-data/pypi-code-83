# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dropbox_api_team_4', 'dropbox_api_team_4.func']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'dropbox>=11.7.0,<12.0.0',
 'python-dotenv>=0.17.1,<0.18.0']

entry_points = \
{'console_scripts': ['fucking-dropbox = dropbox_api_team_4.dropbox_logic:main']}

setup_kwargs = {
    'name': 'dropbox-api-team-4',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Ilnar Gomelyanov',
    'author_email': 'hibushland@gmail.com',
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
