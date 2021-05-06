# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hiyori', 'hiyori.resolvers']

package_data = \
{'': ['*']}

install_requires = \
['magicdict>=1.0.6,<2.0.0', 'magichttp>=1.1.1,<2.0.0']

extras_require = \
{':python_version <= "3.7"': ['importlib-metadata>=4.0.1,<5.0.0'],
 'aiodns': ['aiodns>=2.0.0,<3.0.0']}

setup_kwargs = {
    'name': 'hiyori',
    'version': '0.2.1',
    'description': 'Hiyori is an http client for asyncio.',
    'long_description': 'hiyori\n======\n.. image:: https://github.com/futursolo/hiyori/actions/workflows/everything.yml/badge.svg\n   :target: https://github.com/futursolo/hiyori/actions/workflows/everything.yml\n\n.. image:: https://coveralls.io/repos/github/futursolo/hiyori/badge.svg?branch=master\n   :target: https://coveralls.io/github/futursolo/hiyori?branch=master\n\n.. image:: https://img.shields.io/pypi/v/hiyori.svg\n   :target: https://pypi.org/project/hiyori/\n\nHiyori is an http client for asyncio.\n\nInstall\n-------\n.. code-block:: shell\n\n    $ pip install -U hiyori\n\nSource Code\n-----------\n:code:`hiyori` is open sourced under Apache License 2.0 and its source code is hosted on `GitHub <https://github.com/futursolo/hiyori/>`_.\n\nLicense\n-------\nCopyright 2021 Kaede Hoshikawa\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n',
    'author': 'Kaede Hoshikawa',
    'author_email': 'futursolo@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/futursolo/hiyori',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
