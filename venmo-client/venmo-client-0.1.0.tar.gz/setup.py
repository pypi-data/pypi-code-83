# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['venmo_client', 'venmo_client.model']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'rich>=10.1.0,<11.0.0']

setup_kwargs = {
    'name': 'venmo-client',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Sharad Vikram',
    'author_email': 'sharad.vikram@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
