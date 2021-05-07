# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pettifogger',
 'pettifogger.checks',
 'pettifogger.utils',
 'pettifogger.workflow',
 'pettifogger.workflow.structure',
 'pettifogger.workflow.structure.jobs']

package_data = \
{'': ['*'],
 'pettifogger': ['testdata/.github/workflows/*'],
 'pettifogger.checks': ['testdata/jobs/*', 'testdata/schema/*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'jsonschema>=3.2.0,<4.0.0',
 'networkx>=2.5.1,<3.0.0',
 'ruamel.yaml>=0.17.4,<0.18.0',
 'watchdog>=2.1.0,<3.0.0']

entry_points = \
{'console_scripts': ['pettifogger = pettifogger.main:main']}

setup_kwargs = {
    'name': 'pettifogger',
    'version': '0.2.7',
    'description': 'Github actions workflow validator',
    'long_description': None,
    'author': 'Aki Mäkinen',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/blissfulreboot/python/pettifogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
