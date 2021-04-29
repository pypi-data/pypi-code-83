# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prm']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['prm = prm.prm:main']}

setup_kwargs = {
    'name': 'prm',
    'version': '0.1.4',
    'description': 'pip repository manager',
    'long_description': 'PRM\n---\npip repository manager\n\nUse\n---\n\n.. code-block:: shell\n\n    $ prm list\n    pypi                https://pypi.org/simple\n\n    douban              https://pypi.douban.com/simple\n\n    tencent             https://mirrors.cloud.tencent.com/pypi/simple\n\n    aliyun              https://mirrors.aliyun.com/pypi/simple/\n    $ prm show\n\n    Current: https://mirrors.cloud.tencent.com/pypi/simple\n    $ prm use pypi\n\n    Setting to pypi\n    $ prm show\n\n    Current: https://pypi.org/simple\n    $ prm --help\n\n    Usage: prm [OPTIONS] COMMAND [ARGS]...\n\n    Options:\n      --help  Show this message and exit.\n\n    Commands:\n      list\n      show\n      use\n\n\n\nInstall\n-------\n\n.. code-block:: shell\n    \n    pip install prm\n\n\nAuthor\n------\nYixian Du\n',
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
