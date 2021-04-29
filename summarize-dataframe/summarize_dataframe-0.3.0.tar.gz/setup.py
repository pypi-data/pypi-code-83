# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['summarize_dataframe']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'summarize-dataframe',
    'version': '0.3.0',
    'description': 'A package to provide summary data about pandas DataFrame',
    'long_description': '# Summarize dataframe\n\n## Feature\n\nThis python library permits to get some statistic about your pandas DataFrame. It returns the number of rows and columns\nand the frequency of each datatype present in the DataFrame\n\n## Usage\n\nTo install the package, run:\n\n```bash\npip install summarize-dataframe\n```\n\nIt has been tested for Python `3.7`, `3.8` and `3.9`\n\n## Developers\n\nTo run the tests:\n\ninstall first [poetry]() and run:\n\n```bash\npoetry install\n```\n\nNext run:\n\n```\npoetry run pytest\n```\n\nor:\n\n```bash\ntox\n```\n\n## About\n\nFaouzi Braza\n',
    'author': 'fbraza',
    'author_email': 'fbraza@tutanota.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fbraza/summarize_dataframe',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
