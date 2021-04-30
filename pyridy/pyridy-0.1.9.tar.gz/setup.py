# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyridy', 'pyridy.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pytest>=6.2.3,<7.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'pyridy',
    'version': '0.1.9',
    'description': 'Support library for measurements made with the Ridy Android App',
    'long_description': '# Ridy-Support-Library\n\nPython Support Library to import and process Ridy files',
    'author': 'Philipp Simon Leibner',
    'author_email': 'philip.leibner@ifs.rwth-aachen.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
