# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['viadot',
 'viadot.examples',
 'viadot.flows',
 'viadot.sources',
 'viadot.tasks',
 'viadot.tasks.open_apis']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.9,<2.0.0',
 'azure-storage-blob>=12.8.0,<13.0.0',
 'black>=20.8b1,<21.0',
 'install>=1.3.4,<2.0.0',
 'mkdocs-material>=7.1.3,<8.0.0',
 'mkdocs>=1.1.2,<2.0.0',
 'mkdocstrings>=0.15.0,<0.16.0',
 'pandas>=1.2.4,<2.0.0',
 'prefect>=0.14.16,<0.15.0',
 'pyarrow>=3.0.0,<4.0.0',
 'pyodbc>=4.0.30,<5.0.0',
 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'viadot',
    'version': '0.1.6',
    'description': '',
    'long_description': None,
    'author': 'Alessio Civitillo',
    'author_email': 'acivitillo@dyvenia.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
