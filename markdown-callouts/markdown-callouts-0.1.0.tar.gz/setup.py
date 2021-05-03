# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['markdown_callouts']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.3,<4.0']

entry_points = \
{'markdown.extensions': ['callouts = markdown_callouts:CalloutsExtension']}

setup_kwargs = {
    'name': 'markdown-callouts',
    'version': '0.1.0',
    'description': 'Markdown extension: a classier alternative to admonitions',
    'long_description': None,
    'author': 'Oleh Prypin',
    'author_email': 'oleh@pryp.in',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/oprypin/markdown-callouts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
