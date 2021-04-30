# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marleu_emr']

package_data = \
{'': ['*']}

install_requires = \
['credstash>=1.17.1,<2.0.0',
 'cryptography==3.3.2',
 'paramiko>=2.7.2,<3.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['marleu-ec2 = marleu_emr.emr:main']}

setup_kwargs = {
    'name': 'marleu-emr',
    'version': '0.1.1',
    'description': 'Deployment tool for EMR',
    'long_description': None,
    'author': 'Martin Leuthold',
    'author_email': None,
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
