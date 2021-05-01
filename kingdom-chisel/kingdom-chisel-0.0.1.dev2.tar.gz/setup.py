# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['chisel']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'kingdom-chisel',
    'version': '0.0.1.dev2',
    'description': 'Common toolkit for python web backends',
    'long_description': '# chisel\n⛏ Common sharpening utilities to our python backends. \n\n## Usage\n\n```shell\npip install kingdom-chisel\n```\n\n```python\nfrom chisel import core\n```\n',
    'author': 'Rui Conti',
    'author_email': 'rui@t10.digital',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/t10d/chisel',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
