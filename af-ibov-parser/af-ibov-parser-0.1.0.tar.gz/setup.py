# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['af_ibov_parser']

package_data = \
{'': ['*']}

install_requires = \
['canonicaljson>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['af-ibov-parser = af_ibov_parser.cli:main']}

setup_kwargs = {
    'name': 'af-ibov-parser',
    'version': '0.1.0',
    'description': 'fillme',
    'long_description': '# Aerofin Ibov Parser\n\nA CLI that parses archives from the ibovespa website into json records.\n\nA directory will be created for each archive file (yearly) and a json file\nwill be created per archive record.\n\n## Requirements\n\n* python >= 3.6\n* asyncio\n* typing (type hints)\n\n## Installation\n\nIntalling from gitlab:\n\n```bash\npip install -u git+https://gitlab.com/aerofin/tooling/af-ibov-parser.git@master\n```\n\nInstalling from pypi:\n\n```bash\npip install -u af-ibov-parser\n```\n\n## Usage\n\nOnce installed, the CLi will be available as `af-ibov-parser`.\n\nRun `af-ibov-parser --help` for commands or check the [docs website](https://af-ibov-parser.readthedocs.org).\n\n## Development\n\nA `Makefile` is provided for common tasks, such as running tests.\n\nThe project uses poetry as "project tooling".\n\nA `setup.py` file is generated using `dephell`.\n\nTests are based on `pytest` but they can be used by running `make test`.\n\nThe project also depends on `mypy` in strict mode which is used before running the actual tests.\n\n## License\n\nMIT\n',
    'author': 'Leonardo Rossetti',
    'author_email': 'me@lrossetti.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
