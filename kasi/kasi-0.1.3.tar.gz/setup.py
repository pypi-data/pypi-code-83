# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kasi']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.4,<2.0.0']

entry_points = \
{'console_scripts': ['kasi = kasi.cli:main']}

setup_kwargs = {
    'name': 'kasi',
    'version': '0.1.3',
    'description': 'KASI (Korea Astronomy and Space Science Institute) Open API Python Wrapper',
    'long_description': '====\nKASI\n====\n\n.. container::\n\n    .. image:: https://img.shields.io/pypi/v/kasi.svg\n            :target: https://pypi.python.org/pypi/kasi\n            :alt: PyPI Version\n\n    .. image:: https://img.shields.io/pypi/pyversions/kasi.svg\n            :target: https://pypi.python.org/pypi/kasi/\n            :alt: PyPI Python Versions\n\n    .. image:: https://img.shields.io/pypi/status/kasi.svg\n            :target: https://pypi.python.org/pypi/kasi/\n            :alt: PyPI Status\n\n    .. badges from below are commendted out\n\n    .. .. image:: https://img.shields.io/pypi/dm/kasi.svg\n            :target: https://pypi.python.org/pypi/kasi/\n            :alt: PyPI Monthly Donwloads\n\n.. container::\n\n    .. image:: https://img.shields.io/github/workflow/status/elbakramer/kasi/CI/master\n            :target: https://github.com/elbakramer/kasi/actions/workflows/ci.yml\n            :alt: CI Build Status\n    .. .. image:: https://github.com/elbakramer/kasi/actions/workflows/ci.yml/badge.svg?branch=master\n\n    .. image:: https://img.shields.io/github/workflow/status/elbakramer/kasi/Documentation/master?label=docs\n            :target: https://elbakramer.github.io/kasi/\n            :alt: Documentation Build Status\n    .. .. image:: https://github.com/elbakramer/kasi/actions/workflows/documentation.yml/badge.svg?branch=master\n\n    .. image:: https://img.shields.io/codecov/c/github/elbakramer/kasi.svg\n            :target: https://codecov.io/gh/elbakramer/kasi\n            :alt: Codecov Coverage\n    .. .. image:: https://codecov.io/gh/elbakramer/kasi/branch/master/graph/badge.svg\n\n    .. image:: https://img.shields.io/requires/github/elbakramer/kasi/master.svg\n            :target: https://requires.io/github/elbakramer/kasi/requirements/?branch=master\n            :alt: Requires.io Requirements Status\n    .. .. image:: https://requires.io/github/elbakramer/kasi/requirements.svg?branch=master\n\n    .. badges from below are commendted out\n\n    .. .. image:: https://img.shields.io/travis/elbakramer/kasi.svg\n            :target: https://travis-ci.com/elbakramer/kasi\n            :alt: Travis CI Build Status\n    .. .. image:: https://travis-ci.com/elbakramer/kasi.svg?branch=master\n\n    .. .. image:: https://img.shields.io/readthedocs/kasi/latest.svg\n            :target: https://kasi.readthedocs.io/en/latest/?badge=latest\n            :alt: ReadTheDocs Documentation Build Status\n    .. .. image:: https://readthedocs.org/projects/kasi/badge/?version=latest\n\n    .. .. image:: https://pyup.io/repos/github/elbakramer/kasi/shield.svg\n            :target: https://pyup.io/repos/github/elbakramer/kasi/\n            :alt: PyUp Updates\n\n.. container::\n\n    .. image:: https://img.shields.io/pypi/l/kasi.svg\n            :target: https://github.com/elbakramer/kasi/blob/master/LICENSE\n            :alt: PyPI License\n\n    .. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2Felbakramer%2Fkasi.svg?type=shield\n            :target: https://app.fossa.com/projects/git%2Bgithub.com%2Felbakramer%2Fkasi?ref=badge_shield\n            :alt: FOSSA Status\n\n.. container::\n\n    .. image:: https://badges.gitter.im/elbakramer/kasi.svg\n            :target: https://gitter.im/kasi/community\n            :alt: Gitter Chat\n    .. .. image:: https://img.shields.io/gitter/room/elbakramer/kasi.svg\n\n    .. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n            :target: https://github.com/psf/black\n            :alt: Code Style: Black\n\nKASI (Korea Astronomy and Space Science Institute) Open API Python Wrapper\n\n* Free software: `MIT License`_\n* Documentation: https://kasi.readthedocs.io.\n\n.. _`MIT License`: https://github.com/elbakramer/kasi/blob/master/LICENSE\n\nFeatures\n--------\n\n* Provides simple python wrappers for KASI_ OpenAPIs described in `this page`_.\n\n.. _KASI: https://kasi.re.kr/kor/index\n.. _`this page`: https://astro.kasi.re.kr/information/pageView/31\n\nUsage\n-----\n\nCheck `this notebook`_ for example usage.\n\n.. _`this notebook`: https://github.com/elbakramer/kasi/blob/master/notebooks/usage.ipynb\n\nInstall\n-------\n\nUse ``pip`` for install:\n\n.. code-block:: console\n\n    $ pip install kasi\n\nIf you want to setup a development environment, use ``poetry`` instead:\n\n.. code-block:: console\n\n    # Install poetry using pipx\n    $ python -m pip install pipx\n    $ python -m pipx ensurepath\n    $ pipx install poetry\n\n    # Clone repository\n    $ git clone https://github.com/elbakramer/kasi.git\n    $ cd kasi/\n\n    # Install dependencies and hooks\n    $ poetry install\n    $ poetry run pre-commit install\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `elbakramer/cookiecutter-poetry`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`elbakramer/cookiecutter-poetry`: https://github.com/elbakramer/cookiecutter-poetry\n',
    'author': 'Yunseong Hwang',
    'author_email': 'kika1492@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elbakramer/kasi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
