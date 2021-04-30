# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sslcompare']

package_data = \
{'': ['*'],
 'sslcompare': ['testssl.sh/*', 'testssl.sh/bin/*', 'testssl.sh/etc/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['sslcompare = sslcompare.sslcompare:main']}

setup_kwargs = {
    'name': 'sslcompare',
    'version': '1.2.2',
    'description': "Compares a server's cipher suites with a provided baseline",
    'long_description': None,
    'author': 'Arthur Le Corguille',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
