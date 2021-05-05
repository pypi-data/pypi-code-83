# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nanook', 'nanook.midi', 'nanook.scripts']

package_data = \
{'': ['*']}

install_requires = \
['aioconsole>=0.3.1,<0.4.0',
 'click>=7.1.2,<8.0.0',
 'mido>=1.2.9,<2.0.0',
 'python-rtmidi>=1.4.9,<2.0.0',
 'uvloop>=0.15.2,<0.16.0']

entry_points = \
{'console_scripts': ['nanook = nanook.scripts.cli:main']}

setup_kwargs = {
    'name': 'nanook',
    'version': '0.1.0',
    'description': 'Command line tool for managing scenes on the KORG nanoKONTROL Studio MIDI controller.',
    'long_description': None,
    'author': 'Miklos Aubert',
    'author_email': 'miklos.aubert@gmail.com',
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
