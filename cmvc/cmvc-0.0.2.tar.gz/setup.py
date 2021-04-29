# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmvc', 'cmvc.scripts']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'cmvc',
    'version': '0.0.2',
    'description': 'This is a voice conversion model implemented in PyTorch.',
    'long_description': '# CMVC\n論文のモデルを実装しています。\n現在forwardが通ることを確認しています。\n\nhttps://arxiv.org/abs/1904.04540\n',
    'author': 'kjun1',
    'author_email': 'p.k.maejima1211@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kjun1/CMVC',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
