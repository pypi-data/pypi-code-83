# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpytools']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.7.1,<2.0.0']

setup_kwargs = {
    'name': 'dpytools',
    'version': '0.1.0a0',
    'description': 'Simple tools to build discord bots using discord.py',
    'long_description': "\n[![PyPI status](https://img.shields.io/pypi/status/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI version fury.io](https://badge.fury.io/py/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI downloads](https://img.shields.io/pypi/dm/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI license](https://img.shields.io/pypi/l/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n\n\n# dpytools\nToolset to speed up developing discord bots using discord.py\n\n<hr>\n\n## Status of the project\n\nEarly development. As such it's expected to be unstable and unsuited for production.\n\nAll the presented tools have stringdocs.\n<hr>\n\n# Instalation\nInstall the latest version of the library with pip.\n```\npip install -U dpytools\n```\n\n# Contributing\nFeel free to make a pull request.",
    'author': 'chrisdewa',
    'author_email': 'alexdewa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chrisdewa/dpytools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
