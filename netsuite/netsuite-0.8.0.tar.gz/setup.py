# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netsuite', 'netsuite.cli', 'netsuite.soap_api']

package_data = \
{'': ['*']}

install_requires = \
['authlib>=0.15.3,<0.16.0',
 'httpx>=0.18,<0.19',
 'oauthlib>=3.1.0,<4.0.0',
 'pydantic>=1.8,<2.0']

extras_require = \
{'all': ['orjson>=3,<4', 'ipython>=7,<8', 'zeep[async]>=4.0.0,<5.0.0'],
 'cli': ['ipython>=7,<8'],
 'orjson': ['orjson>=3,<4'],
 'soap_api': ['zeep[async]>=4.0.0,<5.0.0']}

entry_points = \
{'console_scripts': ['netsuite = netsuite.cli:main']}

setup_kwargs = {
    'name': 'netsuite',
    'version': '0.8.0',
    'description': 'Make async requests to NetSuite SuiteTalk SOAP/REST Web Services and Restlets',
    'long_description': "# netsuite\n\n[![Continuous Integration Status](https://github.com/jmagnusson/netsuite/actions/workflows/ci.yml/badge.svg)](https://github.com/jmagnusson/netsuite/actions/workflows/ci.yml)\n[![Continuous Delivery Status](https://github.com/jmagnusson/netsuite/actions/workflows/cd.yml/badge.svg)](https://github.com/jmagnusson/netsuite/actions/workflows/cd.yml)\n[![Code Coverage](https://img.shields.io/codecov/c/github/jmagnusson/netsuite?color=%2334D058)](https://codecov.io/gh/jmagnusson/netsuite)\n[![PyPI version](https://img.shields.io/pypi/v/netsuite.svg)](https://pypi.python.org/pypi/netsuite/)\n[![License](https://img.shields.io/pypi/l/netsuite.svg)](https://pypi.python.org/pypi/netsuite/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/netsuite.svg)](https://pypi.org/project/netsuite/)\n[![PyPI status (alpha/beta/stable)](https://img.shields.io/pypi/status/netsuite.svg)](https://pypi.python.org/pypi/netsuite/)\n\nMake async requests to NetSuite SuiteTalk SOAP/REST Web Services and Restlets\n\n## Beta quality disclaimer\n\nThe project's API is still very much in fluctuation. Please consider pinning your dependency to this package to a minor version (e.g. `poetry add netsuite~0.7` or `pipenv install netsuite~=0.7.0`), which is guaranteed to have no breaking changes. From 1.0 and forward we will keep a stable API.\n\n## Installation\n\nWith default features (REST API + Restlet support):\n\n    pip install netsuite\n\nWith Web Services SOAP API support:\n\n    pip install netsuite[soap_api]\n\nWith CLI support:\n\n    pip install netsuite[cli]\n\nWith `orjson` package (faster JSON handling):\n\n    pip install netsuite[orjson]\n\nWith all features:\n\n    pip install netsuite[all]\n\n## Documentation\n\nIs found here: https://jmagnusson.github.io/netsuite/\n",
    'author': 'Jacob Magnusson',
    'author_email': 'm@jacobian.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jmagnusson.github.io/netsuite/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
