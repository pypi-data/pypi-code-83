# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dropbox_api_team_6']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'dropbox>=11.7.0,<12.0.0',
 'pytest-mock>=3.6.0,<4.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['simple_requests = '
                     'dropbox_api_team_6.simple_requests:main']}

setup_kwargs = {
    'name': 'dropbox-api-team-6',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'sergey_shorin',
    'author_email': 'Sergio.shorin@mail.ru',
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
