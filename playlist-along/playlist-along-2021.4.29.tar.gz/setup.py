# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['playlist_along']

package_data = \
{'': ['*']}

install_requires = \
['charset-normalizer>=1.3.6,<2.0.0',
 'click>=7.0,<8.0',
 'single-source>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['playlist-along = playlist_along.__main__:main']}

setup_kwargs = {
    'name': 'playlist-along',
    'version': '2021.4.29',
    'description': 'Playlist Along',
    'long_description': "Playlist Along\n==============\n\n|Status| |PyPI| |Python Version| |License|\n\n|Read the Docs| |Tests| |Codecov|\n\n|Black|\n\n.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d\n   :target: https://badgen.net/badge/status/alpha/d8624d\n   :alt: Project Status\n.. |PyPI| image:: https://img.shields.io/pypi/v/playlist-along.svg\n   :target: https://pypi.org/project/playlist-along/\n   :alt: PyPI\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/playlist-along\n   :target: https://pypi.org/project/playlist-along\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/playlist-along.svg\n   :target: https://opensource.org/licenses/MIT\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/playlist-along/latest.svg?label=Read%20the%20Docs\n   :target: https://playlist-along.readthedocs.io/\n   :alt: Read the documentation at https://playlist-along.readthedocs.io/\n.. |Tests| image:: https://github.com/hotenov/playlist-along/workflows/Tests/badge.svg\n   :target: https://github.com/hotenov/playlist-along/actions?workflow=Tests\n   :alt: Tests\n.. |Codecov| image:: https://codecov.io/gh/hotenov/playlist-along/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/hotenov/playlist-along\n   :alt: Codecov\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n\n\nFeatures\n--------\n\n* Different CLI utils for m3u playlists\n* TBD\n\n\nRequirements\n------------\n\n* TODO\n\n\nInstallation\n------------\n\nYou can install *Playlist Along* via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install playlist-along\n\n\nUsage\n-----\n\nPlease see the `Command-line Reference <Usage_>`_ for details.\n\n\nContributing\n------------\n\nContributions are very welcome.\nTo learn more, see the `Contributor Guide`_.\n\n\nLicense\n-------\n\nDistributed under the terms of the `MIT license`_,\n*Playlist Along* is free and open source software.\n\n\nIssues\n------\n\nIf you encounter any problems,\nplease `file an issue`_ along with a detailed description.\n\n\nCredits\n-------\n\nThis project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.\n\n.. _@cjolowicz: https://github.com/cjolowicz\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _MIT license: https://opensource.org/licenses/MIT\n.. _PyPI: https://pypi.org/\n.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _file an issue: https://github.com/hotenov/playlist-along/issues\n.. _pip: https://pip.pypa.io/\n.. github-only\n.. _Contributor Guide: CONTRIBUTING.rst\n.. _Usage: https://playlist-along.readthedocs.io/en/latest/usage.html\n",
    'author': 'Artem Hotenov',
    'author_email': 'qa@hotenov.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hotenov/playlist-along',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
