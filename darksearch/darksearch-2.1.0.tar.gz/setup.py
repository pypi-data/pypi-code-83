# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['darksearch']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25,<3.0']

entry_points = \
{'console_scripts': ['darksearch = darksearch.cli:main']}

setup_kwargs = {
    'name': 'darksearch',
    'version': '2.1.0',
    'description': 'Python API wrapper for DarkSearch (darksearch.io).',
    'long_description': '# DarkSearch\n\n[![PyPI](https://img.shields.io/pypi/v/darksearch?color=orange&logo=pypi&logoColor=orange)](https://pypi.org/project/darksearch/)\n[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?logo=python)](https://www.python.org/downloads/)\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/thehappydinoa/DarkSearch/test?label=tests)](https://github.com/thehappydinoa/DarkSearch/actions)\n[![License](https://img.shields.io/github/license/thehappydinoa/DarkSearch)](LICENSE)\n\nPython API wrapper for DarkSearch ([darksearch.io](https://darksearch.io/)).\n\n## Install\n\n```bash\npip install darksearch\n```\n\n## Cli\n\n```bash\ndarksearch --query "query" --page 1\n\ndarksearch --query "query" --pages 2\n\ndarksearch --query "query" --pages 2 --wait 2\n\ndarksearch --query "query" --json\n```\n\n## Usage\n\n```python\nimport darksearch\n\n """\n `timeout`, `headers`, and `proxies`  are optional\n timeout = 10\n proxies = {\n     "http": "http://127.0.0.1:8080"\n }\n headers = {\n     "User-Agent": "Chrome/57.0.2987.133"\n }\n """\n\nclient = darksearch.Client(timeout=30, headers=None, proxies=None)\n\nresults = client.search("query")\n\n """\n `results` is a JSON dict object like this\n {\n   "total": int,\n   "per_page": int,\n   "current_page": int,\n   "last_page": int,\n   "from": int,\n   "to": int,\n   "data": [\n       {\n           "title": string,\n           "link": string,\n           "description": string\n       }\n    ]\n}\n """\n\nresults = client.search("query", page=2)\n\n """\n `results` is a JSON dict object like this\n {\n   "total": int,\n   "per_page": int,\n   "current_page": 2,\n   "last_page": int,\n   "from": int,\n   "to": int,\n   "data": [\n       {\n           "title": string,\n           "link": string,\n           "description": string\n       }\n    ]\n}\n """\n\nresults = client.search("query", pages=2)\n\n """\n `results` is a list of JSON dict objects like this\n [\n {\n   "total": int,\n   "per_page": int,\n   "current_page": 1,\n   "last_page": int,\n   "from": int,\n   "to": int,\n   "data": [\n       {\n           "title": string,\n           "link": string,\n           "description": string\n       }\n    ]\n },\n ...\n ]\n """\n\nresults = client.search("query", pages=2, wait=2)\n\n """\n `wait` is the seconds between requests (DarkSearch\'s API is limited to 30 requests per minute.)\n `results` is a list of JSON dict objects\n [\n {\n   "total": int,\n   "per_page": int,\n   "current_page": 1,\n   "last_page": int,\n   "from": int,\n   "to": int,\n   "data": [\n       {\n           "title": string,\n           "link": string,\n           "description": string\n       }\n    ]\n },\n ...\n ]\n """\n\ncrawling_status = darksearch.crawling_status()\n\n """\n `crawling_status` is a integer of pages that have been indexed\n """\n```\n\n[Proxies Documentation](https://requests.readthedocs.io/en/master/user/advanced/#proxies)\n\n## Testing\n\n```bash\npytest\n```\n',
    'author': 'Aidan Holland',
    'author_email': 'thehappydinoa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thehappydinoa/DarkSearch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.0',
}


setup(**setup_kwargs)
