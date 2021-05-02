# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nyt_recipe']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.3,<5.0.0', 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['nyt_recipe = nyt_recipe.main:main']}

setup_kwargs = {
    'name': 'nyt-recipe',
    'version': '1.0.0',
    'description': 'Downloads recipes from the NYT Cooking website and converts them into an Apple Notes-compatible format',
    'long_description': '![PyPi](https://img.shields.io/pypi/v/nyt_recipe) ![License](https://img.shields.io/pypi/l/MI)\n\n`nyt_recipe` is a Python 3 script that is used to download recipes from\n[NYT Cooking](https://cooking.nytimes.com/) and save them to a file in a format\nthat can easily be imported by Apple Notes.\n\n## Installation\n\n`nyt_recipe` should be installed using `pip`:\n\n```bash\n$ python3 -m pip install nyt-recipe\n```\n\n## Usage\n\nProvide a URL or list of URLs to the script. The script will place the output\nfiles in the `recipes` directory inside the current user\'s home directory.\n\n```bash\n$ nyt_recipe https://cooking.nytimes.com/recipes/1020044-vegetable-paella-with-chorizo\nSaved recipe "Vegetable Paella With Chorizo" to /Users/ianbrault/recipes/vegetable_paella_with_chorizo.html\n```\n',
    'author': 'Ian Brault',
    'author_email': 'ian@brault.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ianbrault/nyt_recipe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
