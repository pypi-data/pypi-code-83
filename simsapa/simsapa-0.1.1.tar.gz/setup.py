# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simsapa', 'simsapa.app', 'simsapa.layouts']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3.4,<4.0.0',
 'PyMuPDF>=1.18.12,<2.0.0',
 'PyQt5>=5.15.4,<6.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'SQLAlchemy>=1.4.6,<2.0.0']

setup_kwargs = {
    'name': 'simsapa',
    'version': '0.1.1',
    'description': 'Simsapa Dhamma Reader',
    'long_description': None,
    'author': 'Gambhiro',
    'author_email': 'gambhiro.bhikkhu.85@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
