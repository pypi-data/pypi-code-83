# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['discordapi']
setup_kwargs = {
    'name': 'discordapi',
    'version': '0.1',
    'description': 'The DiscordAPI (v9) libary. Read the documentation: http://documentations.7m.pl/python/discordapi/v9/latest_version/Doc.html',
    'long_description': None,
    'author': 'Nekit',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
