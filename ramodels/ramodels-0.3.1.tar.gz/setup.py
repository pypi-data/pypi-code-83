# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ramodels', 'ramodels.lora', 'ramodels.mo']

package_data = \
{'': ['*']}

install_requires = \
['pydantic==1.8.1']

setup_kwargs = {
    'name': 'ramodels',
    'version': '0.3.1',
    'description': 'Pydantic data models for OS2mo',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2021 Magenta ApS <https://magenta.dk>\nSPDX-License-Identifier: MPL-2.0\n-->\n\n\n# MoLoRa Data Models\n\nMoLoRa data validation models powered by [pydantic](https://github.com/samuelcolvin/pydantic/#pydantic).\n\n## Versioning\nThis project uses [Semantic Versioning](https://semver.org/) with the following strategy:\n- MAJOR: Incompatible changes to existing data models\n- MINOR: Backwards compatible updates to existing data models OR new models added\n- PATCH: Backwards compatible bug fixes\n\n<!--\n## Getting Started\n\nTODO: README section missing!\n\n### Prerequisites\n\n\nTODO: README section missing!\n\n### Installing\n\nTODO: README section missing!\n\n## Running the tests\n\nTODO: README section missing!\n\n## Deployment\n\nTODO: README section missing!\n\n## Built With\n\nTODO: README section missing!\n\n## Authors\n\nMagenta ApS <https://magenta.dk>\n\nTODO: README section missing!\n-->\n## License\n- This project: [MPL-2.0](MPL-2.0.txt)\n- Dependencies:\n  - pydantic: [MIT](MIT.txt)\n\nThis project uses [REUSE](https://reuse.software) for licensing. All licenses can be found in the [LICENSES folder](LICENSES/) of the project.\n\n',
    'author': 'Magenta',
    'author_email': 'info@magenta.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://magenta.dk/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
