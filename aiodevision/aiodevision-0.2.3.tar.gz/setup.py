# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiodevision']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'aiodevision',
    'version': '0.2.3',
    'description': 'A simple asynchronous wrapper for the Idevision API.',
    'long_description': '# aiodevision\nA simple async wrapper for the idevision api.\n\nNote: this may be unstable. This is an experimental wrapper, and is undocumented (for now).\n\nIf you would like to contribute/add anything, feel free to make a PR.\n\n# Installation\nFor installing the stable version, do\n```py\npip install aiodevision\n```\n\nIf you wanna install the dev version, do\n```py\npip install git+\n\ntodo:\n- Add Better Exception Haandling\n- Handle Ratelimits \n\n\n\n',
    'author': 'MrKomodoDragon',
    'author_email': 'svrchn921@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MrKomodoDragon/aiodevision',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
