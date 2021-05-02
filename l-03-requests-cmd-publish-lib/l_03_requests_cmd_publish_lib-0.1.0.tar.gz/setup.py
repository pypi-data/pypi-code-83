# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['l_03_requests_cmd_publish_lib']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'pytest-mock>=3.6.0,<4.0.0', 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['simple_requests = '
                     'l_03_requests_cmd_publish_lib.simple_requests:main']}

setup_kwargs = {
    'name': 'l-03-requests-cmd-publish-lib',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Rustem Saitgareev',
    'author_email': 'rus.saitgareev@gmail.com',
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
