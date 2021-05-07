# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyuntype_cli', 'pyuntype_cli.utils']

package_data = \
{'': ['*']}

install_requires = \
['astor>=0.8.1,<0.9.0',
 'click>=7.1.2,<8.0.0',
 'loguru>=0.5.3,<0.6.0',
 'pydash>=5.0.0,<6.0.0']

entry_points = \
{'console_scripts': ['pyuntype = pyuntype_cli:main']}

setup_kwargs = {
    'name': 'pyuntype',
    'version': '0.0.3',
    'description': 'Programatically untype your Python code',
    'long_description': "# Python untype\n\nProgramatically untype your Python Projects.\n\n## Credits\n\nThe original idea and code of this project comes from the following [Stack OverFlow thread](https://stackoverflow.com/questions/42733877/remove-type-hints-in-python-source-programmatically).\n\n## Install\n\n```bash\npip install pyuntype\n```\n\n## Usage\n\nUse the following command to completely untype your Python Project located in the `src/` folder.\n\n```bash\npyuntype src/ dest/\n```\n\n### Option `gitmode` (bool)\n\nWhen `--gitmode=True`, the `src` directory should be a inside a Git repository. The goal to create a `dest` folder only with the files listed by `git ls-files` (and thus taking into account `.gitignore`)\n\n### Option `custom_typing_module` (str)\n\nIf you defined in your code a file with custom types, all imports from this file will be ignored, and this file won't be copied in your `dest` directory\n\n### Example:\n\nFor the Python CLI, we can use:\n\n```\npyuntype python python_untype --gitmode=True --custom_typing_module=custom_types\n```\n\n## Contribute\n\n### Development install\n\nFeel free to contribute by proposing merge requests to this project.\n\nThis project uses [Poetry](https://python-poetry.org/docs/basic-usage/) and can be installed in development mode with the following steps:\n\n- `git clone https://github.com/Escape-Technologies/pyuntype.git && cd pyuntype`\n- `poetry shell`\n- `poetry install`\n\n### Pre-commit\n\nThis project [Pre-Commit](https://pre-commit.com) to lint your code and make sure it is compliant to the rules we fixed.\n\n```bash\npre-commit install --hook-type commit-msg\n```\n\n### Testing --wip--\n\nThis project uses [PyTest](https://docs.pytest.org/en/6.2.x/) to unit test the code.\n",
    'author': 'Escape Technologies SAS',
    'author_email': 'ping@escape.tech',
    'maintainer': 'Antoine Carossio',
    'maintainer_email': 'antoine.carossio@me.com',
    'url': 'https://escape.tech/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
