# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipicn']

package_data = \
{'': ['*']}

install_requires = \
['geoip2>=4.1.0,<5.0.0', 'ipaddress>=1.0.23,<2.0.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'ipicn',
    'version': '2021.5.5',
    'description': 'A tool to help determine whether ip is in China',
    'long_description': None,
    'author': 'ehco1996',
    'author_email': 'zh19960202@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
