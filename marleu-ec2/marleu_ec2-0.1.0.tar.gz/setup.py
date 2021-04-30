# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marleu_ec2']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.17.60,<2.0.0']

entry_points = \
{'console_scripts': ['marleu-ec2 = marleu_ec2.ec2:main']}

setup_kwargs = {
    'name': 'marleu-ec2',
    'version': '0.1.0',
    'description': 'Deployment tools for EC2',
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
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
