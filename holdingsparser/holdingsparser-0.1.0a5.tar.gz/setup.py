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
    'version': '0.1.0a5',
    'description': 'A program that parses 13F reports filed with the SEC.',
    'long_description': 'holdingsparser\n--------------\n\n.. image:: https://img.shields.io/pypi/v/holdingsparser.svg\n    :target: https://pypi.org/project/holdingsparser\n    :alt: PyPI badge\n\n.. image:: https://img.shields.io/pypi/pyversions/holdingsparser.svg\n    :target: https://pypi.org/project/holdingsparser\n    :alt: PyPI versions badge\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n    :alt: Black formatter badge\n\n.. image:: https://img.shields.io/pypi/l/transmission-clutch.svg\n    :target: https://en.wikipedia.org/wiki/MIT_License\n    :alt: License badge\n\n.. image:: https://img.shields.io/pypi/dm/holdingsparser.svg\n    :target: https://pypistats.org/packages/holdingsparser\n    :alt: PyPI downloads badge\n\nBackground\n==========\nFrom `investor.gov`_ (educational website from the SEC):\n\n    An institutional investment manager that uses the U.S. mail (or other means or instrumentality of interstate commerce) in the course of its business, and exercises investment discretion over $100 million or more in Section 13(f) securities (explained below) must report its holdings quarterly on Form 13F with the Securities and Exchange Commission (SEC).\n\n`holdingsparser` fetches 13-F filings from `EDGAR`_ and outputs the holding entries in a TSV file.\n\nQuick start\n===========\n\nInstall the package:\n\n.. code-block:: console\n\n    pip install --user holdingsparser\n\nUpgrade the package:\n\n.. code-block:: console\n\n    pip install --user --pre -U holdingsparser\n\nSearch for a filing with the CIK:\n\n.. code-block:: console\n\n    holdingsparser 0001166559\n\nAlternatively:\n\n.. code-block:: console\n\n    python -m holdingsparser 0001166559\n\n.. _investor.gov: https://www.investor.gov/introduction-investing/investing-basics/glossary/form-13f-reports-filed-institutional-investment\n.. _EDGAR: https://www.sec.gov/edgar/searchedgar/companysearch.html\n',
    'author': 'mhadam',
    'author_email': 'michael@hadam.us',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mhadam/holdingsparser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
