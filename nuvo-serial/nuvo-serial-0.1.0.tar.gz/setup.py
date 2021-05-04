# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nuvo_serial']

package_data = \
{'': ['*']}

install_requires = \
['icontract>=2.4', 'pyserial-asyncio>=0.5', 'pyserial>=3.5', 'typeguard>=2.10']

setup_kwargs = {
    'name': 'nuvo-serial',
    'version': '0.1.0',
    'description': 'Python API implementing the Nuvo Grand Concerto/Essentia G multi-zone audio amplifier serial control protocol',
    'long_description': None,
    'author': 'sprocket-9',
    'author_email': 'sprocketnumber9@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
