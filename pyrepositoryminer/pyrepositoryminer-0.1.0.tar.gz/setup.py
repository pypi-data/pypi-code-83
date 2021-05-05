# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyrepositoryminer']

package_data = \
{'': ['*']}

install_requires = \
['pygit2>=1.5.0,<2.0.0', 'radon>=4.5.0,<5.0.0', 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['pyrepositoryminer = pyrepositoryminer.main:app']}

setup_kwargs = {
    'name': 'pyrepositoryminer',
    'version': '0.1.0',
    'description': 'Efficient Repository Mining in Python',
    'long_description': '# pyrepositoryminer\n\n[![CI workflow](https://github.com/fabianhe/pyrepositoryminer/actions/workflows/test.yaml/badge.svg)](https://github.com/fabianhe/pyrepositoryminer/actions/workflows/test.yaml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nEfficient Repository Mining in Python\n\n## Development Setup\n\n1. Install [poetry](https://github.com/python-poetry/poetry)\n   ```bash\n   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -\n   ```\n2. Install the dependencies\n   ```bash\n   poetry install\n   ```\n3. Install the [pre-commit](https://github.com/pre-commit/pre-commit) hooks\n   ```bash\n   pre-commit install\n   ```\n',
    'author': 'Fabian Heseding',
    'author_email': '39628987+fabianhe@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fabianhe/pyrepositoryminer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
