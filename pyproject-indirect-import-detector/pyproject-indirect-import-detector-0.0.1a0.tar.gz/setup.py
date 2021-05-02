# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyproject_indirect_import_detector']

package_data = \
{'': ['*']}

install_requires = \
['result>=0.6.0,<0.7.0',
 'setuptools>=56.0.0,<57.0.0',
 'stdlib-list>=0.8.0,<0.9.0',
 'termcolor>=1.1.0,<2.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['pyproject-indirect-import-detector = '
                     'pyproject_indirect_import_detector.main:_main']}

setup_kwargs = {
    'name': 'pyproject-indirect-import-detector',
    'version': '0.0.1a0',
    'description': '',
    'long_description': None,
    'author': 'keno',
    'author_email': 'keno.ss57@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
