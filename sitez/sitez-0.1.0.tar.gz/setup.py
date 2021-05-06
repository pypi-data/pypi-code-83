# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sitez']

package_data = \
{'': ['*']}

install_requires = \
['html-dsl>=0.4.0,<0.5.0',
 'pydantic>=1.8.1,<2.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['sitez = sitez.__main__:run']}

setup_kwargs = {
    'name': 'sitez',
    'version': '0.1.0',
    'description': 'another site generator',
    'long_description': None,
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
