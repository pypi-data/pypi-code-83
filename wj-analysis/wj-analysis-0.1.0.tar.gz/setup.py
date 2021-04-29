# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wj_analysis',
 'wj_analysis.common',
 'wj_analysis.digital_med',
 'wj_analysis.facebook',
 'wj_analysis.facebook_insig',
 'wj_analysis.instagram',
 'wj_analysis.twitter']

package_data = \
{'': ['*']}

install_requires = \
['pandas==1.0.3', 'spacy==2.1.8', 'torch==1.5.0', 'transformers==2.8.0']

setup_kwargs = {
    'name': 'wj-analysis',
    'version': '0.1.0',
    'description': 'Whale&Jaguar Libary - Analysis',
    'long_description': None,
    'author': 'Sebastian Franco',
    'author_email': 'jsfranco@whaleandjaguar.co',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.6.1,<4.0',
}


setup(**setup_kwargs)
