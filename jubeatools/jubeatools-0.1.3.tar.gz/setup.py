# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jubeatools',
 'jubeatools.formats',
 'jubeatools.formats.eve',
 'jubeatools.formats.jubeat_analyser',
 'jubeatools.formats.jubeat_analyser.memo',
 'jubeatools.formats.jubeat_analyser.memo1',
 'jubeatools.formats.jubeat_analyser.memo2',
 'jubeatools.formats.jubeat_analyser.mono_column',
 'jubeatools.formats.jubeat_analyser.tests',
 'jubeatools.formats.jubeat_analyser.tests.data',
 'jubeatools.formats.jubeat_analyser.tests.memo',
 'jubeatools.formats.memon',
 'jubeatools.testutils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'marshmallow>=3.6.0,<4.0.0',
 'more-itertools>=8.4.0,<9.0.0',
 'multidict>=5.1.0,<6.0.0',
 'parsimonious>=0.8.1,<0.9.0',
 'path>=15.1.2,<16.0.0',
 'python-constraint>=1.4.0,<2.0.0',
 'simplejson>=3.17.0,<4.0.0',
 'sortedcontainers>=2.3.0,<3.0.0']

entry_points = \
{'console_scripts': ['jubeatools = jubeatools.cli:convert']}

setup_kwargs = {
    'name': 'jubeatools',
    'version': '0.1.3',
    'description': 'A toolbox for jubeat file formats',
    'long_description': '# Jubeatools\nA toolbox to convert between jubeat file formats\n\n## How to install\n```sh\npip install jubeatools\n```\n\nYou need Python 3.8 or greater\n\n## How to use\n```sh\njubeatools ${source} ${destination} -f ${output format} (... format specific options)\n```\n\n## Which formats are supported\n### Memon\n|        | input | output |\n|--------|:-----:|:------:|\n| v0.2.0 | ✔️     | ✔️      |\n| v0.1.0 | ✔️     | ✔️      |\n| legacy | ✔️     | ✔️      |\n\n### Jubeat Analyser\n|                      | input | output |\n|----------------------|:-----:|:------:|\n| #memo2               | ✔️     | ✔️      |\n| #memo1               | ✔️     | ✔️      |\n| #memo                | ✔️     | ✔️      |\n| mono-column (1列形式) | ✔️     | ✔️      |',
    'author': 'Stepland',
    'author_email': '16676308+Stepland@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Stepland/jubeatools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
