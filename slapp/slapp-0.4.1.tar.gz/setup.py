# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slapp']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.12,<4.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'confuse>=1.4.0,<2.0.0',
 'marko>=1.0.1,<2.0.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['slapp = slapp.main:app']}

setup_kwargs = {
    'name': 'slapp',
    'version': '0.4.1',
    'description': 'Tool for easy deploying projects to git repo.',
    'long_description': '# Släpp\n\nTool for quick tagging and deploying releases to Git. Släpp automatically generates and pushes CHANGELOG file to your repo, based on your commit history.\n\n### Installation\n```bash\npip install slapp\n```\n\n### Quick start\n1. Init slapp config\n```bash\nslapp init\n```\n2. Edit slapp.yml file if needed\n3. Do some stuff in your repo and commit it with * \n```bash\ngit add . && git commit -m "* Added some cool features!"\n```\n4. Generate release tag and build auto-changelog in one command!\n```bash\nslapp release\n```\n\n### Release\n\nOnly [Semantic Versioning](https://semver.org) is supported, versions have to be without prefixes or postfixes. \n\nAdvanced usage of `release` command:\n```bash\nslapp release [OPTIONS] [MANUAL_VERSION]\n\nArguments:\n  [MANUAL_VERSION]  Manually added version name\n\nOptions:\n  -t, --type TEXT   Release type: major, minor, patch  [default: minor]\n  --dry / --no-dry  Do not perform any actions with git repo  [default: False]\n  --help            Show this message and exit.\n```\n\n### Versions\n\nYou can view all versions in repo by `versions` command:\n```bash\nslapp versions [OPTIONS]\n\nOptions:\n  -l, --last INTEGER  Show only last N versions.\n  -r, --reverse       Order versions by ascending.  [default: False]\n```\nFor example, you want to see the earliest three versions:\n```shell\nslapp versions -r -l 3\n```\n',
    'author': 'm.semenov',
    'author_email': '0rang3max@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
