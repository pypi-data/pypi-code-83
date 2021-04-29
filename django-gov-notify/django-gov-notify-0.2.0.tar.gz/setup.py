# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_gov_notify']

package_data = \
{'': ['*']}

install_requires = \
['django>=2.2.12,<4.0', 'notifications-python-client==5.4.1']

setup_kwargs = {
    'name': 'django-gov-notify',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Nick Smith',
    'author_email': 'nick.smith@torchbox.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<3.9',
}


setup(**setup_kwargs)
