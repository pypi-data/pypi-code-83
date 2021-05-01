# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commanderbot_ext',
 'commanderbot_ext.ext',
 'commanderbot_ext.ext.faq',
 'commanderbot_ext.ext.help_chat',
 'commanderbot_ext.ext.help_chat.sql_store',
 'commanderbot_ext.ext.invite',
 'commanderbot_ext.ext.jira',
 'commanderbot_ext.ext.pack',
 'commanderbot_ext.ext.ping',
 'commanderbot_ext.ext.poster_board',
 'commanderbot_ext.ext.quote',
 'commanderbot_ext.ext.roles',
 'commanderbot_ext.ext.status',
 'commanderbot_ext.ext.vote',
 'commanderbot_ext.lib']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.9,<2.0.0',
 'aiosqlite>=0.17.0,<0.18.0',
 'beet>=0.17.2,<0.18.0',
 'commanderbot>=0.7.0,<0.8.0',
 'discord.py>=1.7.1,<2.0.0',
 'lectern>=0.9.1,<0.10.0']

setup_kwargs = {
    'name': 'commanderbot-ext',
    'version': '0.7.0',
    'description': 'A collection of cogs and extensions for discord.py bots.',
    'long_description': '# CommanderBot Ext\n\nA collection of cogs and extensions for discord.py bots.\n\n[![package-badge]](https://pypi.python.org/pypi/commanderbot-ext/)\n[![version-badge]](https://pypi.python.org/pypi/commanderbot-ext/)\n\n[package-badge]: https://img.shields.io/pypi/v/commanderbot-ext.svg\n[version-badge]: https://img.shields.io/pypi/pyversions/commanderbot-ext.svg\n',
    'author': 'Arcensoth',
    'author_email': 'arcensoth@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/CommanderBot-Dev/commanderbot-ext',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
