# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['isortd']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-cors>=0.7.0,<0.8.0',
 'aiohttp>=3.7.0,<4.0.0',
 'aiohttp_cors>=0.7.0,<0.8.0',
 'click>=7.1.2,<8.0.0',
 'isort>=5,<6']

setup_kwargs = {
    'name': 'isortd',
    'version': '0.1.5',
    'description': 'isort daemon. Http api to isort',
    'long_description': "# isortd\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/urm8/isortd/build?style=for-the-badge)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/isortd?style=for-the-badge)\n![PyPI](https://img.shields.io/pypi/v/isortd?style=for-the-badge)\n![Docker Image Version (latest by date)](https://img.shields.io/docker/v/urm8/isortd?style=for-the-badge)\n\nSimple http handler for [isort](https://github.com/PyCQA/isort) util. I liked the idea of putting \n[black[d]](https://black.readthedocs.io/en/stable/blackd.html) into my docker compose file and using\n[BlackConnect](https://plugins.jetbrains.com/plugin/14321-blackconnect) plugin for auto sort without setting up\nmy dev env every time, but I was still missing sort formatting tool, that would work the same way. So its here...\nMb I'll release [IsortConnect](https://github.com/urm8/IsortConnect) and it will be more usable.\n## install\n```\n$ pip install isortd\n$ python -m isortd\n``` \n\n## todo\n    - socket support\n    - pypi ci",
    'author': 'mm',
    'author_email': 'megafukz@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/urm8/isortd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
