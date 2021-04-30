# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cimsparql']

package_data = \
{'': ['*']}

install_requires = \
['SPARQLWrapper', 'networkx', 'numpy', 'pandas', 'requests', 'tables']

extras_require = \
{'parse_xml': ['pendulum', 'lxml']}

setup_kwargs = {
    'name': 'cimsparql',
    'version': '1.7.0',
    'description': 'CIM query utilities',
    'long_description': None,
    'author': 'Statnett Datascience',
    'author_email': 'Datascience.Drift@Statnett.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/statnett/cimsparql.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
