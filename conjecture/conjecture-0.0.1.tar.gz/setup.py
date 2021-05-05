# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['conjecture']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'conjecture',
    'version': '0.0.1',
    'description': 'A pythonic assertion library',
    'long_description': None,
    'author': 'Daniel Knell',
    'author_email': 'contact@danielknell.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
