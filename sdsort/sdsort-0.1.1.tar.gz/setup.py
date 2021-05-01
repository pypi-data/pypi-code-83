# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdsort']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['sdsort = sdsort:main']}

setup_kwargs = {
    'name': 'sdsort',
    'version': '0.1.1',
    'description': 'Sorts class methods according to the step-down rule',
    'long_description': "# sdsort\nSorts methods within python classes according to the step-down rule, as described in [Robert C. Martin's](https://en.wikipedia.org/wiki/Robert_C._Martin) [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/).\nMore concretely, methods are ordered in a depth-first-traversal order of the dependency tree.\n\n## Installation\n`pip install sdsort`\n\n## Usage\nTo target individual files, run the `sdsort` command, followed by the paths to the files that should be sorted:\n```\nsdsort <file_1> <file_2>\n```\n\nTo sort all `*.py` files in a directory, and all of its subdirectories, run the `sdsort` command followed by the directory path:\n```\nsdsort <directory_path>\n```\n\n## Maturity\nIt's early days. Consider this an alpha for now.\n",
    'author': 'Eiríkur Fannar Torfason',
    'author_email': 'eirikur.torfason@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eirikurt/sdsort',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
