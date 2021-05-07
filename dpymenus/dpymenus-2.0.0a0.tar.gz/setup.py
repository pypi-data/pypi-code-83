# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dpymenus',
 'dpymenus.constants',
 'dpymenus.sessions',
 'dpymenus.settings',
 'dpymenus.types']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.7,<2.0', 'emoji>=1.2,<2.0', 'toml>=0.10,<0.11']

entry_points = \
{'console_scripts': ['examples = runner:__poetry_run', 'fmt = scripts:fmt']}

setup_kwargs = {
    'name': 'dpymenus',
    'version': '2.0.0a0',
    'description': 'Simplified menus for discord.py developers.',
    'long_description': '<h1 align="center">Discord Menus</h1>\n\n<div align="center">\n  <strong><i>Simplified menus for discord.py developers.</i></strong>\n  <br>\n  <br>\n\n  <a href="https://pypi.org/project/dpymenus/">\n    <img src="https://img.shields.io/pypi/v/dpymenus?color=0073B7&label=Latest&style=for-the-badge" alt="Version" />\n  </a>\n\n  <a href="https://dpymenus.readthedocs.io/en/latest/">\n    <img src="https://img.shields.io/readthedocs/dpymenus/latest?style=for-the-badge" alt="Docs" />\n  </a>\n\n  <a href="https://python.org">\n    <img src="https://img.shields.io/pypi/pyversions/dpymenus?color=0073B7&style=for-the-badge" alt="Python Version" />\n  </a>\n</div>\n\n<br>\n\n---\n\n<img align="right" src="assets/demo.gif" alt="user creates an embed, reaction buttons are added, and user navigates the\nmenu by clicking the buttons">\n\n### Table of Contents\n\n**[The Book](https://dpymenus.com)** <br>\n**[API Docs](https://dpymenus.readthedocs.io/en/latest/?badge=latest)** <br>\n**[Examples](https://github.com/robertwayne/dpymenus/tree/master/examples)**\n\n- [Features](#features)\n- [Quick Start](#quick-start)\n- [Example](#examples)\n- [Support](#support)\n- [Contributing](#contributing)\n\n<br>\n<br>\n<br>\n\n---\n\n<div align="center">\n  <h1>\n    You are viewing the active dev branch.\n    There are no stability or documentation guarantees on this branch.\n  </h1>\n</div>\n\n## Features\n\n`dpymenus` is an unofficial add-on for the `discord.py` library that lets you quickly compose various styles of menus\nwhich react to user input.\n\n- Handles text & button input, normalization, and validation\n- Easy-to-build menus with paginated data, multiple choices, and polls\n- Template system for quickly defining a cohesive style for your menus\n- User-defined callbacks & event hooks for complex use-cases\n- Awesome examples and documentation to get rolling quickly\n\n## Quick Start\n\nRead **["Installation"](https://dpymenus.com/installation.html)** from **[The Book](https://dpymenus.com)**.\n\n## Examples\n\n```python\nfrom discord.ext import commands\nfrom dpymenus import Page, PaginatedMenu\n\n\nclass Demo(commands.Cog):\n    def __init__(self, client):\n        self.client = client\n\n    @commands.command()\n    async def demo(self, ctx: commands.Context):\n        page1 = Page(title=\'Page 1\', description=\'First page test!\')\n        page1.add_field(name=\'Example A\', value=\'Example B\')\n\n        page2 = Page(title=\'Page 2\', description=\'Second page test!\')\n        page2.add_field(name=\'Example C\', value=\'Example D\')\n\n        page3 = Page(title=\'Page 3\', description=\'Third page test!\')\n        page3.add_field(name=\'Example E\', value=\'Example F\')\n\n        menu = PaginatedMenu(ctx)\n        menu.add_pages([page1, page2, page3])\n        await menu.open()\n\n\ndef setup(client):\n    client.add_cog(Demo(client))\n```\n\nThe **[examples directory](https://github.com/robertwayne/dpymenus/tree/master/examples)** contains working examples for\nalmost every feature of the library.\n\nIn addition, the chapter on **["Examples"](https://dpymenus.com/installation.html)**\nwalks you through setting up the built-in example runner.\n\n## Support\n\nIf you are looking for support on how to use particular library functions, please ask in the\n**[discussions](https://github.com/robertwayne/dpymenus/discussions)** tab.\n\nIf you\'ve encountered a bug,\n**[submit an issue](https://github.com/robertwayne/dpymenus/issues/new)**.\n\nIn addition, feel free to add me on Discord @ `Rob (롭)#0013` -- I am open to discuss the library and assist when I am\nfree, but I prefer you use the GitHub options as it may help other people as well.\n\n## Contributing\n\n`dpymenus` is open-source for a reason -- I welcome all additions, bug fixes, and changes if they fit within the scope\nof the library. Please see the chapter on **["Contributing"](https://dpymenus.com/contributing.html)**\nin the book for detailed information. Don\'t be shy!\n\n---\n\nHave you found this library useful? Please leave a ⭐ on the project -- it means a lot to me!\n\nCheck out my other discord.py utility: **[cogwatch](https://github.com/robertwayne/cogwatch)** -- Automatic\nhot-reloading for your discord.py command files.\n',
    'author': 'Rob Wagner',
    'author_email': 'rob@robwagner.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/robertwayne/dpymenus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
