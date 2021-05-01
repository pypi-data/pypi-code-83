# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['marleu_pytest', 'marleu_pytest.greetings']

package_data = \
{'': ['*']}

install_requires = \
['click']

entry_points = \
{'console_scripts': ['marleu-pytest = marleu_pytest.entrypoint:hello']}

setup_kwargs = {
    'name': 'marleu-pytest',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Martin Leuthold',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
