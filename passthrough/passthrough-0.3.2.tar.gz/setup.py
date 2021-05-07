# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['passthrough',
 'passthrough.extensions',
 'passthrough.extensions.exm',
 'passthrough.extensions.file',
 'passthrough.extensions.pt']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.5.0,<5.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=3.7.3,<4.0.0'],
 'pds4_tools': ['pds4_tools>=1.2,<2.0']}

entry_points = \
{'passthrough.extensions': ['exm = passthrough.extensions.exm',
                            'file = passthrough.extensions.file',
                            'pt = passthrough.extensions.pt']}

setup_kwargs = {
    'name': 'passthrough',
    'version': '0.3.2',
    'description': 'Passthrough - Template-Driven PDS4 Data Product Generation',
    'long_description': None,
    'author': 'Ariel Ladegaard',
    'author_email': 'arl13@aber.ac.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ExoMars-PanCam/passthrough',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
