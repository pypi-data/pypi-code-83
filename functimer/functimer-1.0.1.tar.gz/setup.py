# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['functimer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'functimer',
    'version': '1.0.1',
    'description': 'A function decorator/wrapper package to time a given function.',
    'long_description': '# functimer\n\nA function decorator/wrapper package to time a given function.\n\n### Installation\nPYPI:\n\n    pip install functimer\n\nManual:\n\n    poetry build\n    pip install dist/*.whl\n\nHow to install [Poetry](https://python-poetry.org/docs/#installation).\n\n### Quick Example\nComprehensive Examples in `examples`\n```py\n@timed(unit=Unit.second, number=1)\ndef timed_sleep(seconds):\n    sleep(seconds)\n\nruntime = timed_sleep(0.3)\n```\n\n### Tests\nRun `pytest` in the root directory of the repo.\n\n### License\nMIT\n',
    'author': 'Edward Emmett',
    'author_email': 'edemms12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/EJEmmett/functimer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
