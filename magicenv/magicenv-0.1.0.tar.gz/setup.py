# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magicenv']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'magicenv',
    'version': '0.1.0',
    'description': 'Simple way to parse common datatypes from env vars.',
    'long_description': '# magicenv\nSimple way to parse common datatypes from env vars.\n\n\n# Setup\n\n```bash\npip install magicenv\n```\n\n# Usage\n```python\nfrom magicenv import env\n\nDB_HOST = env(\'DB_HOST\', "localhost:1234")              # string var\nDB_NUM_TRANSACTIONS = env(\'DB_NUM_TRANSACTIONS\', 1234)  # int var\nENABLE_FEATURE_X = env(\'ENABLE_FEATURE_X\', True)  # bool var\n\nDB_SERVERS = env(\'DB_SERVERS\', [\'server1\', "server2"])  # interprets a comma separated string as a list\n\n```',
    'author': 'technocake',
    'author_email': 'robin.garen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/technocake/magicenv',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
