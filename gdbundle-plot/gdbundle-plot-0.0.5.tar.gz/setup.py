# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gdbundle_plot', 'gdbundle_plot.scripts']

package_data = \
{'': ['*']}

install_requires = \
['gdbundle>=0.0.3,<0.1.0']

setup_kwargs = {
    'name': 'gdbundle-plot',
    'version': '0.0.5',
    'description': 'Plot 1-D arrays',
    'long_description': '# gdbundle-plot\n\nThis is a [gdbundle](https://github.com/memfault/gdbundle) plugin used to plot 1-D arrays in a graph.\n\nC and Rust types can be parsed using the plugin.\n\nOne or several arrays can be plotted on the same graph.\n\n## Compatibility\n\n- GDB\n- LLDB: Not yet\n\n## Installation\n\n### Pip\n\n```shell\n$ pip install gdbundle-plot\n```\n\n### From source\n\nAfter setting up [gdbundle](https://github.com/memfault/gdbundle), install the package using:\n\n```shell\n$ poetry install\n```\n\nIf you\'ve decided to manually manage your packages using the `gdbundle(include=[])` argument,\nadd it to the list of plugins.\n\n```shell\n# .gdbinit\n\n[...]\nimport gdbundle\nplugins = ["plot"]\ngdbundle.init(include=plugins)\n```\n\n## Usage\n\n```\n(gdb) plot var1_name [var2_name ...]\n```\n',
    'author': 'Cyril Fougeray',
    'author_email': 'cyril.fougeray@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
