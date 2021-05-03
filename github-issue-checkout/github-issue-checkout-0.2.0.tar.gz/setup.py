# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['github_issue_checkout']
install_requires = \
['inquirer>=2.7.0,<3.0.0', 'setuptools>=56.0.0,<57.0.0']

entry_points = \
{'console_scripts': ['github-issue-checkout = github_issue_checkout:main']}

setup_kwargs = {
    'name': 'github-issue-checkout',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'Karim Stekelenburg',
    'author_email': 'karim@animo.id',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
