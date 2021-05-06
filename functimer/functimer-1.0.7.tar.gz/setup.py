# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['examples', 'functimer', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functimer',
    'version': '1.0.7',
    'description': 'A decorator/wrapper package to time a given function.',
    'long_description': '# functimer\n\nA decorator/wrapper package to time a given function.\n\n[![PyPI version](https://badge.fury.io/py/functimer.svg)](https://badge.fury.io/py/functimer)\n\n---\n### Installation\nPYPI:\n\n    pip install functimer\n\nManual:\n\n    poetry build\n    pip install dist/*.whl\n\nHow to install [Poetry](https://python-poetry.org/docs/#installation).\n\n### Quick Example\nComprehensive Examples in `examples`\n```py\n@timed(unit=Unit.second, number=1)\ndef timed_sleep(seconds):\n    sleep(seconds)\n\nruntime = timed_sleep(1)\n"1.00 s"\n```\n\n### Tests\nRun `pytest` in the root directory of the repo.\n\n### License\nMIT\n',
    'author': 'Edward Emmett',
    'author_email': 'edemms12@gmail.com',
    'maintainer': 'Edward Emmett',
    'maintainer_email': 'edemms12@gmail.com',
    'url': 'https://github.com/EJEmmett/functimer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
