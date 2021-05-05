# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_plan']

package_data = \
{'': ['*']}

install_requires = \
['cleo>=0.8.1,<0.9.0']

entry_points = \
{'console_scripts': ['fastapi-template = fastapi_template:start']}

setup_kwargs = {
    'name': 'fastapi-plan',
    'version': '0.1.0',
    'description': 'Dead simple template manager for FastAPI applications',
    'long_description': '# fastapi-template\nDead simple template manager for FastAPI applications\n',
    'author': 'rafsaf',
    'author_email': 'rafal.safin12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafsaf/fastapi-template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
