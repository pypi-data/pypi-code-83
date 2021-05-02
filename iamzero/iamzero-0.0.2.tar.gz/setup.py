# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iamzero', 'iamzero.instrumentation']

package_data = \
{'': ['*']}

install_requires = \
['bump2version>=1.0.1,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'statsd>=3.3.0,<4.0.0',
 'wrapt>=1.12.1,<2.0.0']

setup_kwargs = {
    'name': 'iamzero',
    'version': '0.0.2',
    'description': 'iam-zero least-privilege instrumentation client for Python',
    'long_description': None,
    'author': 'Chris Norman',
    'author_email': 'chris@exponentlabs.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
