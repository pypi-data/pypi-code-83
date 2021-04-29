# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exec_wrapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'exec-wrapper',
    'version': '0.1.0',
    'description': 'Allows creating executable wrappers for any executable',
    'long_description': "exec-wrapper\n===\n\nAllows creating executable wrappers for any executable.\nTested on Linux, Windows.\n\nExample\n---\n```python\nimport os\nimport subprocess\nfrom exec_wrapper import write_exec_wrapper\n\nwrapper = '/tmp/ssh-wrapper'\nwrite_exec_wrapper(wrapper, ['ssh', '-i', 'my-key', '-o', 'BatchMode=yes'])\n\nsubprocess.run(['git', 'fetch', '...'], env={**os.environ, 'GIT_SSH': wrapper})\n```\n",
    'author': 'xppt',
    'author_email': '21246102+xppt@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
