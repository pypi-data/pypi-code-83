# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cclm', 'cclm.augmentation', 'cclm.pretrainers']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=1.1.3,<2.0.0',
 'mlflow>=1.16.0,<2.0.0',
 'tensorflow>=2.0.0,<3.0.0',
 'tokenizers>=0.10.0,<0.11.0',
 'tqdm>=4.0.0,<5.0.0']

setup_kwargs = {
    'name': 'cclm',
    'version': '0.1.0',
    'description': 'NLP framework for composing together models modularly',
    'long_description': None,
    'author': 'jamesmf',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
