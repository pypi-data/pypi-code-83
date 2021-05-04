# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['argo_dsl']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0', 'kubernetes>=12.0.1,<13.0.0', 'pydantic>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'argo-dsl',
    'version': '0.1.dev1',
    'description': 'Python DSL for argo workflow',
    'long_description': '# argo-dsl\nPython DSL for argo workflow\n',
    'author': 'ZhengYu, Xu',
    'author_email': 'zen-xu@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zen-xu/argo-dsl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
