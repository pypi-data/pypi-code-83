# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['marleu_emr']

package_data = \
{'': ['*']}

install_requires = \
['credstash>=1.17,<2.0',
 'cryptography==3.3.2',
 'paramiko>=2.7,<3.0',
 'requests>=2.25,<3.0']

entry_points = \
{'console_scripts': ['marleu-emr = marleu_emr.emr:main']}

setup_kwargs = {
    'name': 'marleu-emr',
    'version': '0.1.3',
    'description': 'Deployment tool for EMR',
    'long_description': '# marleu-emr\n\nThis is a tool to interacti with EMR clusters.',
    'author': 'Martin Leuthold',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mleuthold/python-tooling',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
