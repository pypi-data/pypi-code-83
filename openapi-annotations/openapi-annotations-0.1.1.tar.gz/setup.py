# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['openapi_annotations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'openapi-annotations',
    'version': '0.1.1',
    'description': 'Generate OpenApi with code-first annotations. Use type-hint info and docstrings to document your API. This is an experimental library!',
    'long_description': None,
    'author': 'Mathias Colpaert',
    'author_email': 'mathias.colpaert@trensition.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mathi123/openapi-annotation',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
