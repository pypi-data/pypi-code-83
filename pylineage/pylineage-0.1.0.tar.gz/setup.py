# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylineage']

package_data = \
{'': ['*'], 'pylineage': ['templates/*']}

install_requires = \
['graphviz>=0.16,<0.17',
 'networkx>=2.5.1,<3.0.0',
 'pydot>=1.4.2,<2.0.0',
 'regex>=2021.4.4,<2022.0.0']

setup_kwargs = {
    'name': 'pylineage',
    'version': '0.1.0',
    'description': 'Data Lineage for Python',
    'long_description': '# pylineage\nData Lineage for Python\n',
    'author': 'jasperpaalman',
    'author_email': 'jasper_paalman@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jasperpaalman/pylineage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
