# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['feature_grouper']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.0,<2.0.0', 'scikit-learn>=0.24.0,<0.25.0', 'scipy>=1.6.0,<2.0.0']

setup_kwargs = {
    'name': 'feature-grouper',
    'version': '0.1.2',
    'description': 'Simple dimensionality reduction through hierarchical clustering of correlated features.',
    'long_description': None,
    'author': 'Alex Kyllo',
    'author_email': 'alex.kyllo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://feature-grouper.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
