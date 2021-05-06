# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['idp_layout_spec', 'idp_layout_spec.utils']

package_data = \
{'': ['*']}

install_requires = \
['cached-property>=1.5.2,<2.0.0',
 'graphic-coloring-engine>=0.1.5,<0.2.0',
 'pydantic>=1.8.1,<2.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'idp-layout-spec',
    'version': '0.1.4',
    'description': 'idp 稿件数据结构',
    'long_description': None,
    'author': 'zheduan.yin',
    'author_email': 'zheduan.yin@arkie.cn',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.10,<4.0.0',
}


setup(**setup_kwargs)
