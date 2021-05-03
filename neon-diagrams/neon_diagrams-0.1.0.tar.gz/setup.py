# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neon_diagrams']

package_data = \
{'': ['*']}

install_requires = \
['black>=21.4b2,<22.0', 'diagrams>=0.19.1,<0.20.0']

setup_kwargs = {
    'name': 'neon-diagrams',
    'version': '0.1.0',
    'description': 'Diagrams for Neon Law',
    'long_description': None,
    'author': 'neon law',
    'author_email': 'support@neonlaw.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
