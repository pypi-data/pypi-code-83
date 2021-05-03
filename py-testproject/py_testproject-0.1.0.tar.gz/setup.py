# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['py_testproject']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'desert>=2020.11.18,<2021.0.0',
 'marshmallow>=3.11.1,<4.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['py-testproject = py_testproject.console:main']}

setup_kwargs = {
    'name': 'py-testproject',
    'version': '0.1.0',
    'description': 'Hypermodern Python testing',
    'long_description': '[![Tests](https://github.com/twarnock/py_testproject/workflows/Tests/badge.svg)](https://github.com/twarnock/py_testproject/actions?workflow=Tests)\n\n[![Codecov](https://codecov.io/gh/twarnock/py_testproject/branch/master/graph/badge.svg)](https://codecov.io/gh/twarnock/py_testproject)\n\n[![PyPI](https://img.shields.io/pypi/v/py_testproject.svg)](https://pypi.org/project/py_testproject)\n\n# Python Test Project\n\nBased on Hypermodern Python\n',
    'author': 'Tom Warnock',
    'author_email': 'thomas.warnock@cloudreach.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/twarnock/py_testproject',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
