# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['actymath', 'actymath.columns']

package_data = \
{'': ['*'], 'actymath': ['table_data/*']}

install_requires = \
['pandas>=1.1.5,<2.0.0', 'parse>=1.19.0,<2.0.0']

setup_kwargs = {
    'name': 'actymath',
    'version': '0.1.1',
    'description': 'Actuarial Math and commutation functions for life insurance product - with a Pandas backend',
    'long_description': "# actymath\n\nActuarial formulae and commutation functions for life insurance products (with a fast Pandas backend)\n\n## Read this first\n\nThis started out as a package to build up the various actuarial formulae using the Pandas backend for speed.\n\nThe way it works is to create a 'grid' of actuarial calculation vectors in a pandas DataFrame that you can use for a single policy or a single cohort.\n\nWhen you ask for a particular actuarial formula or calculation to be created, it will spawn the columns needed to generate it.\n\nEverything is using Pandas in the backend, so you can use any normal Pandas machinery you like.\n\nThis is very much 'in development'.\n\n## Usage\n\n### Installation\n\nInstall using pip\n\n    pip install actymath\n\n### Getting started\n\nThis [getting started notebook](notebooks/01_getting_started.ipynb) illustrates how to use the package with a simple example.\n\n### Actuarial formula\n\nThe formula definitions are called **columns** in this package as they spawn columns in a pandas DataFrame.\n\nThese formulae can be explored in the [actymath/columns directory](https://github.com/ttamg/actymath/tree/main/actymath/columns).\n\n### Mortality tables\n\nCurrently only a few old standard mortality tables are implemented, but there is support for 1D and 2D mortality tables [here](https://github.com/ttamg/actymath/blob/main/actymath/tables.py).\n\n## Contributing\n\nFeel free to contribute or suggest improvements.\n\n- Add suggested improvements as a GitHub issue on this project\n\n- Pull requests also welcomed, particularly for any fixes, new tables or useful actuarial formulae\n\n### Developer setup\n\nClone this repository using\n\n    git clone git@github.com:ttamg/actymath.git\n\nDependencies use **poetry** so make sure you have [poetry already installed](https://python-poetry.org/docs/) on you development machine.\n\nWith poetry, you create a new virtual environment for yourself and activate it using\n\n    poetry shell\n\nTo install all the dependencies in your new virtual environment, use\n\n    poetry install\n\n### Running tests\n\nWe use **pytest** for all testing. Run the test pack using\n\n    pytest\n",
    'author': 'Matt Gosden',
    'author_email': 'mdgosden@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ttamg/actymath',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
