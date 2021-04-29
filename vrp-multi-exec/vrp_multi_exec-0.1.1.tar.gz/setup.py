# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vrp_multi_exec',
 'vrp_multi_exec.entry_points',
 'vrp_multi_exec.lib',
 'vrp_multi_exec.lib.handlers',
 'vrp_multi_exec.lib.logging',
 'vrp_multi_exec.lib.parsers']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'click>=7.1.2,<8.0.0',
 'gevent>=21.1.2,<22.0.0',
 'loguru>=0.5.3,<0.6.0',
 'paramiko>=2.7.2,<3.0.0']

entry_points = \
{'console_scripts': ['multi_exec = vrp_multi_exec.entry_points.multi_exec:cli']}

setup_kwargs = {
    'name': 'vrp-multi-exec',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Maged Motawea',
    'author_email': 'magedmotawea@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
