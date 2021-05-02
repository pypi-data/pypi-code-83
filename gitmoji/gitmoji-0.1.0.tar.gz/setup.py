# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitmoji']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gitmoji',
    'version': '0.1.0',
    'description': 'Helper package that reflects gitmoji philosofy! :tada:',
    'long_description': '<h1 align="center">\n    <strong>gitmoji</strong>\n</h1>\n<p align="center">\n    <a href="https://github.com/Kludex/gitmoji" target="_blank">\n        <img src="https://img.shields.io/github/last-commit/Kludex/gitmoji" alt="Latest Commit">\n    </a>\n        <img src="https://img.shields.io/github/workflow/status/Kludex/gitmoji/Test">\n        <img src="https://img.shields.io/codecov/c/github/Kludex/gitmoji">\n    <br />\n    <a href="https://pypi.org/project/gitmoji" target="_blank">\n        <img src="https://img.shields.io/pypi/v/gitmoji" alt="Package version">\n    </a>\n    <img src="https://img.shields.io/pypi/pyversions/gitmoji">\n    <img src="https://img.shields.io/github/license/Kludex/gitmoji">\n</p>\n\n\n## Installation\n\n``` bash\npip install gitmoji\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Marcelo Trylesinski',
    'author_email': 'marcelotryle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Kludex/gitmoji',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
