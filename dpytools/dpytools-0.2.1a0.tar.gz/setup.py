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
    'version': '0.2.1a0',
    'description': 'Simple tools to build discord bots using discord.py',
    'long_description': '\n[![PyPI status](https://img.shields.io/pypi/status/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI version fury.io](https://badge.fury.io/py/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI downloads](https://img.shields.io/pypi/dm/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n[![PyPI license](https://img.shields.io/pypi/l/dpytools.svg)](https://pypi.python.org/pypi/dpytools/)\n\n\n# dpytools\nToolset to speed up developing discord bots using discord.py\n\n# Features\n- Easy to read typehinted code\n- Active development\n\n## Main components\n- checks \n- commands\n- menus\n- parsers\n\n# Instalation\nInstall the latest version of the library with pip.\n```\npip install -U dpytools\n```\n\n# Project Home\nhttps://github.com/chrisdewa/dpytools\n\n# Changelog\nhttps://github.com/chrisdewa/dpytools/blob/master/CHANGELOG.md\n\n# F. A. Q.\nhttps://github.com/chrisdewa/dpytools/blob/master/FAQ.md\n\n# Status of the project\nEarly development. \nOnly se in production after extensive testing.\nExpect breaking changes in future updates\n\n# Contributing\nFeel free to make a pull request. Or rise any issues.',
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
