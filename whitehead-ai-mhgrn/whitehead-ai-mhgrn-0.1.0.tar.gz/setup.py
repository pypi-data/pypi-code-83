# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['whitehead_ai_mhgrn',
 'whitehead_ai_mhgrn.modeling',
 'whitehead_ai_mhgrn.utils',
 'whitehead_ai_mhgrn.utils.tasks.plain_qa']

package_data = \
{'': ['*'], 'whitehead_ai_mhgrn': ['data/csqa/*', 'scripts/*']}

setup_kwargs = {
    'name': 'whitehead-ai-mhgrn',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Diwank Singh Tomer',
    'author_email': 'diwank.singh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
