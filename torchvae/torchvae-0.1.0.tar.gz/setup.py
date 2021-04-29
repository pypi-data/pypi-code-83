# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchvae']

package_data = \
{'': ['*']}

install_requires = \
['pytorch-lightning>=1.2.10,<2.0.0', 'torch>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'torchvae',
    'version': '0.1.0',
    'description': 'A simple implementation of a variational autoencoder for PyTorch',
    'long_description': None,
    'author': 'Santiago SILVA',
    'author_email': '16252054+sssilvar@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
