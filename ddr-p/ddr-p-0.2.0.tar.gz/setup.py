# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ddrp']

package_data = \
{'': ['*']}

install_requires = \
['Pint>=0.17,<0.18',
 'cookiecutter>=1.7.2,<2.0.0',
 'numpy>=1.20.1,<2.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'seaborn>=0.11.1,<0.12.0',
 'srsly>=2.4.0,<3.0.0']

setup_kwargs = {
    'name': 'ddr-p',
    'version': '0.2.0',
    'description': 'data-driven research papers, making use of Python and LaTeX for automation and reproducibility.',
    'long_description': None,
    'author': 'Thurston Sexton',
    'author_email': 'thurston.sexton@nist.gov',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
