# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['summarize_dataframe']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'summarize-dataframe',
    'version': '0.1.0',
    'description': 'A package to provide summary data about pandas DataFrame',
    'long_description': '# Summarize dataframe\n',
    'author': 'fbraza',
    'author_email': 'fbraza@tutanota.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fbraza/summarize_dataframe',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
