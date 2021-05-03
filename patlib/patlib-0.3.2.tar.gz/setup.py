# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['patlib']

package_data = \
{'': ['*']}

extras_require = \
{'misc': ['pyyaml', 'toml', 'tabulate', 'tqdm', 'pandas'],
 'mydev': ['ipython>=7.20,<8.0',
           'pyqt5!=5.15.3',
           'pre-commit',
           'line_profiler',
           'see',
           'pytest',
           'pytest-sugar',
           'pytest-clarity',
           'ipdb',
           'pudb',
           'pysnooper']}

setup_kwargs = {
    'name': 'patlib',
    'version': '0.3.2',
    'description': 'A collection of tools.',
    'long_description': '# patlib\n\nPurposes:\n\n- Share tools across my projects, such as DAPPER.\n- Define optional dependencies to setup my dev. environments by\n  "inheriting" from here. The aim is that I only need to keep\n  pylib up to date (e.g. pinning buggy Jedi or pdbpp),\n  rather than the `pyproject.toml` of each and every project.\n\n  ```toml\n  [tool.poetry.dev-dependencies]\n  # Either:\n  patlib = {version = "==0.2.8", extras = ["mydev", "misc"]}\n  # Or:\n  patlib = {path = "../../py/patlib", extras = ["mydev", "misc"], develop=true}\n  ```\n\n  NB: Maybe this is a bad idea; maybe I will forget to include e.g.\n  numpy when publishing the other project.\n\n- Provide pylab replacement\n\n\nPoetry workflow\n\n- Init project\n- Abandom project (tmp)\n- Resume project\n- Publish/realease PyPI/GitHub\n- Add dependencies (by poetry or pyproject.toml)\n- Update dependencies\n- Virtual env management\n- Pre-commit, Lint, Test, CI, Docs\n',
    'author': 'patricknraanes',
    'author_email': 'patrick.n.raanes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
