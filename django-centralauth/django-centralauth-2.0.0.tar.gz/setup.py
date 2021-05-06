# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['centralauth',
 'centralauth.client',
 'centralauth.client.management',
 'centralauth.client.management.commands',
 'centralauth.provider',
 'centralauth.provider.migrations']

package_data = \
{'': ['*'],
 'centralauth.client': ['locale/de/LC_MESSAGES/*',
                        'templates/centralauth/client/*'],
 'centralauth.provider': ['locale/de/LC_MESSAGES/*']}

install_requires = \
['Django>=2.2',
 'django-oauth-toolkit>=1.5',
 'requests-oauthlib>=1.3',
 'requests>=2.25']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'], 'docs': ['Sphinx>=3.5']}

setup_kwargs = {
    'name': 'django-centralauth',
    'version': '2.0.0',
    'description': 'App for managing user access and permissions from multiple projects.',
    'long_description': "django-centralauth\n==================\n\n.. image:: https://img.shields.io/pypi/v/django-centralauth.svg\n   :target: https://pypi.org/project/django-centralauth/\n   :alt: Latest Version\n\n.. image:: https://github.com/lenarother/django-centralauth/workflows/Test/badge.svg?branch=master\n   :target: https://github.com/lenarother/django-centralauth/actions?workflow=Test\n   :alt: CI Status\n\n.. image:: https://codecov.io/gh/lenarother/django-centralauth/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/lenarother/django-centralauth\n   :alt: Coverage Status\n\n.. image:: https://readthedocs.org/projects/django-centralauth/badge/?version=latest\n   :target: https://django-centralauth.readthedocs.io/en/stable/?badge=latest\n   :alt: Documentation Status\n\n\ndjango-centralauth solves the problem of managing user access and permissions\nfrom multiple projects in one central place.\n\n\nFeatures\n--------\n\n* based on OAuth2 standard.\n* provider app to set up your own user-management application.\n* client app for delegating authentication and permissions management to provider.\n\n\nRequirements\n------------\n\ndjango-centralauth supports Python 3 only and requires at least Django 2. and django-oauth-toolkit.\n\n\nPrepare for development\n-----------------------\n\n.. code-block:: shell\n\n    $ poetry install\n\n\nNow you're ready to run the tests:\n\n.. code-block:: shell\n\n    $ poetry run py.test\n\n\nResources\n---------\n\n* `Documentation <https://django-centralauth.readthedocs.io>`_\n* `Bug Tracker <https://github.com/moccu/django-centralauth/issues>`_\n* `Code <https://github.com/moccu/django-centralauth/>`_\n",
    'author': 'Magdalena Rother',
    'author_email': 'rother.magdalena@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lenarother/django-centralauth',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4',
}


setup(**setup_kwargs)
