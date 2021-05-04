# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_dragonpay_py3',
 'django_dragonpay_py3.api',
 'django_dragonpay_py3.migrations']

package_data = \
{'': ['*'], 'django_dragonpay_py3': ['templates/dragonpay_soapxml/*']}

setup_kwargs = {
    'name': 'django-dragonpay-py3',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Cymmer John Maranga',
    'author_email': 'cymmer4@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
