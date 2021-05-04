# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dropbox_api_team_5']
setup_kwargs = {
    'name': 'dropbox-api-team-5',
    'version': '0.1.0',
    'description': 'DropBox skripts',
    'long_description': None,
    'author': 'AlexandrVolkov',
    'author_email': 'hramyh.w@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
