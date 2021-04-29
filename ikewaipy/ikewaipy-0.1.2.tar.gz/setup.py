# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ikewaipy']

package_data = \
{'': ['*']}

install_requires = \
['python_dateutil>=2.5.3,<3.0.0',
 'requests',
 'setuptools>=21.0.0,<22.0.0',
 'urllib3>=1.15.1,<2.0.0']

setup_kwargs = {
    'name': 'ikewaipy',
    'version': '0.1.2',
    'description': '',
    'long_description': '# ikewaipy\n\nPython library for accessing Ike Wai (ikewai.org) data and metadata.\n\n\n## Development:\nThe poetry library is used for managing this library\n\nTesting - use:\n```\npoetry run pytest\n```\nTo execute library tests\n\nBuilding/Publishing - use:\n```\npoetry build  \n```\nTo publish after build use:\n```\npoetry publish\n```\nThis will push to PyPI (if you have permission)\n',
    'author': 'Sean Cleveland',
    'author_email': 'sean.b.cleveland@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
