# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magicenv']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'magicenv',
    'version': '0.1.2',
    'description': 'Simple way to parse common datatypes from env vars.',
    'long_description': '# magicenv\nSimple way to parse common datatypes from env vars.\n\n\n# Setup\n\n```bash\npip install magicenv\n```\n\n# Usage\n```python\nfrom magicenv import env\n\nDB_HOST = env(\'DB_HOST\', "localhost:1234")              # string var\nDB_NUM_TRANSACTIONS = env(\'DB_NUM_TRANSACTIONS\', 1234)  # int var\nENABLE_FEATURE_X = env(\'ENABLE_FEATURE_X\', True)  # bool var\n\nDB_SERVERS = env(\'DB_SERVERS\', [\'server1\', "server2"])  # interprets a comma separated string as a list\n\n```\n\n\n\n## env()\n\n```python\ndef env(key, default=None, return_type=None, list_element_type=str):\n```\n\n| Param             | Explanation                                                  |\n| ----------------- | ------------------------------------------------------------ |\n| key               | name of environment variable.                                |\n| default           | Optional - default value if key is not present in environment |\n| return_type       | Optional - specify return_type.                              |\n| list_element_type | Optional - cast/parse each element of a list with provided callable. Only used if the setting is a list. |\n\n\u200b        If key is not present in environment, and there is not provided a default value,\n\u200b        None will be returned.\n\n\n\n## Guidelines for settings in Environment\n\nA couple of conventions exist when designing\n environment variables for settings.\n\n 1. **All values are stored as strings in the environment variable**\n\n 2. **Booleans** \n  All boolean variables are encoded as one of "1", "True" or "true" if True,\n    all other values are interpreted as False     \n\n 3. **Lists are encoded as a comma separated string**\n    in example:  "a,b,c,   d"\n(intentionally put whitespace in there. It is allowed)\n      \n 4. **Default Values are preffered to be set to the same type as the setting.**\n\n  The type of the default value implicitly sets the datatype of the env var.\n  May be overriden by setting `return_type` explicitly.\n\n  * `list` -> `[]`, \n  * `str` -> `\'\'`\n  *  `int` -> `0` \n  * `bool` -> `True` or `False`',
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
