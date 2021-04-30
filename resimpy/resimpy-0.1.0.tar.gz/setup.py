# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resimpy']

package_data = \
{'': ['*']}

install_requires = \
['Shapely>=1.7.1,<2.0.0',
 'matplotlib>=3.4.1,<4.0.0',
 'numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'pyvista>=0.29.1,<0.30.0',
 'scipy==1.6.1',
 'seaborn>=0.11.1,<0.12.0']

setup_kwargs = {
    'name': 'resimpy',
    'version': '0.1.0',
    'description': 'Oil&Gas Reservoir Simulation tools',
    'long_description': None,
    'author': 'scuervo',
    'author_email': 'scuervo91@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
