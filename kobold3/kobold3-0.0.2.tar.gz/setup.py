# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kobold3']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'rich>=10.1.0,<11.0.0']

entry_points = \
{'console_scripts': ['kb = kobold.core:main', 'kobold = kobold.core:main']}

setup_kwargs = {
    'name': 'kobold3',
    'version': '0.0.2',
    'description': 'a bold key-value store for knowledge and config management',
    'long_description': None,
    'author': 'rcox771',
    'author_email': 'russ771@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
