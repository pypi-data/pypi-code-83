# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['holdingsparser']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0',
 'lxml>=4.6.3,<5.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['holdingsparser = holdingsparser.__main__:main']}

setup_kwargs = {
    'name': 'holdingsparser',
    'version': '0.1.0a2',
    'description': 'A program that parses 13F reports filed with the SEC.',
    'long_description': 'holdingsparser\n--------------\n\n.. image:: https://img.shields.io/pypi/v/holdingsparser.svg\n    :target: https://pypi.org/project/holdingsparser\n    :alt: PyPI badge\n\n.. image:: https://img.shields.io/pypi/pyversions/holdingsparser.svg\n    :target: https://pypi.org/project/holdingsparser\n    :alt: PyPI versions badge\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n    :alt: Black formatter badge\n\n.. image:: https://img.shields.io/pypi/l/transmission-clutch.svg\n    :target: https://en.wikipedia.org/wiki/MIT_License\n    :alt: License badge\n\n.. image:: https://img.shields.io/pypi/dm/holdingsparser.svg\n    :target: https://pypistats.org/packages/holdingsparser\n    :alt: PyPI downloads badge\n\nQuick start\n===========\n\nInstall the package:\n\n.. code-block:: console\n\n    pip install --user holdingsparser\n\nMake a client:\n\n.. code-block:: console\n\n    holdingsparser 0001166559\n',
    'author': 'mhadam',
    'author_email': 'michael@hadam.us',
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
