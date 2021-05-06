# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tutompy']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'desert>=2020.11.18,<2021.0.0',
 'marshmallow>=3.11.1,<4.0.0',
 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['tutompy = tutompy.console:main']}

setup_kwargs = {
    'name': 'tutompy',
    'version': '0.1.0',
    'description': 'The hypermodern Python project',
    'long_description': '# tutompy\n[![Tests](https://github.com/pamlinux/tutompy/workflows/Tests/badge.svg)](https://github.com/pamlinux/tutompy/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/pamlinux/tutompy/branch/master/graph/badge.svg)](https://codecov.io/gh/pamlinux/tutompy)\nMy repository for hypermodern-python tutorial by Claudio Jolowicz\n',
    'author': 'Pierre-Alain Moret',
    'author_email': 'moret.pierre.alain@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pamlinux/tutompy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
