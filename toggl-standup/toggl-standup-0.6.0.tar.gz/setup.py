# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['togglstandup']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0',
 'crayons>=0.3.0,<0.4.0',
 'humanfriendly>=8.1,<9.0',
 'maya>=0.6.1,<0.7.0',
 'rich>=10.1.0,<11.0.0',
 'togglwrapper>=1.2.0,<2.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['standup = togglstandup:cli']}

setup_kwargs = {
    'name': 'toggl-standup',
    'version': '0.6.0',
    'description': 'Removes the pain of using Toggl with Geekbot',
    'long_description': '# Stand Up for Toggl\n\nThis tool helps generate my daily Geekbot stand up report in an format which I may copy and paste into Slack.\n\n## Usage\n\n```shell\n$ export TOGGL_API_KEY="PASTE_YOUR_KEY_HERE"\n\nUsage: standup [OPTIONS] SLANG_DATE\n\n  Standup tool to help with Toggl\n\nArguments:\n  SLANG_DATE  [required]\n\nOptions:\n  --api-key TEXT                  [default: ]\n  --show-duration / --no-show-duration\n                                  [default: False]\n  --show-time / --no-show-time    [default: False]\n  --timezone TEXT                 [default: US/Central]\n  --version\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n\n  --help                          Show this message and exit.\n```\n\n## To generate a report for yesterday\n\n```shell\n$ standup yesterday\n```\n',
    'author': 'Jeff Triplett',
    'author_email': 'jeff.triplett@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jefftriplett/toggl-standup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
