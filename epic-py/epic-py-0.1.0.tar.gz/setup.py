# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epic_py', 'epic_py.domain']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.1,<1.9.0', 'requests>=2.25.1,<2.26.0']

setup_kwargs = {
    'name': 'epic-py',
    'version': '0.1.0',
    'description': 'ePIC API in Python',
    'long_description': '# epic-py package\n\nThis is the Python client for ePIC API `version >= 3.0.0`.\n\n## Features\n\n### Get a PID\n\nTo get a PID and its values, simply call the `get` method. It returns a `Pid` object which contains `prefix`, `suffix`,\nand its values in `data` variable. Note that if `username` and `password` are not provided, the client can only get the\nPID and its public readable values.\n\n### Create a PID\n\nTo create a PID, a `Pid` object must first be created with proper `data`, which is a list of `PidData` (handle values).\nPlease see the example usage below for more details.\n\nThere are 2 ways to create a PID:\n\n1. Call the `create` method: this method will throw an error in case the PID has already existed.\n1. Call the `create_or_update` method: as the name suggested, if the PID has already existed, it will be updated\n   instead. This update overwrites the PID with new data.\n\n### Update a PID\n\nTo update a PID, a `Pid` object must first be created with proper `prefix`, `suffix`, and `data`. `data` is a list\nof `PidData` (handle values).\n\nSame as create, there are 2 ways to update a PID:\n\n1. Call the `update` method: this method will throw an error in case the PID does not exist.\n1. Call the `create_or_update` method: if the PID already exists, it will be updated. This update overwrites the PID\n   with new data.\n\n### Delete a PID\n\nTo delete a PID, simply call the `delete` method and pass the PID string as a parameter. This command does not guarantee\nthat the PID will be deleted. It depends on the policies of each prefix. Usually, the `no-delete` policy is enforced. If\nthat is the case, trying to delete a PID will lead to an error.\n\n## Example usage\n\nSuppose one wants to create a PID with its content as follows:\n\n```json\n[\n  {\n    "parsed_data": "Test Publisher",\n    "type": "publisher"\n  },\n  {\n    "parsed_data": "2021",\n    "type": "publicationYear",\n    "privs": "rw--"\n  },\n  {\n    "parsed_data": {\n      "identifier-Attribute": "DOI",\n      "identifier-Value": "10.123.456/789"\n    },\n    "type": "identifier"\n  },\n  {\n    "parsed_data": {\n      "resourceType-Value": "test"\n    },\n    "type": "resourceType"\n  },\n  {\n    "parsed_data": {\n      "creator": {\n        "creatorName": "Triet Doan"\n      }\n    },\n    "type": "creators"\n  },\n  {\n    "parsed_data": {\n      "title": {\n        "title-Value": "Test title"\n      }\n    },\n    "type": "titles"\n  }\n]\n```\n\nThe following example code can be used:\n\n```python\nfrom epic_py import EpicAPI, PidData, Pid\n\npublisher = PidData(type=\'publisher\', parsed_data=\'Test Publisher\')\npublication_year = PidData(type=\'publicationYear\', parsed_data=\'2021\', privs=\'rw--\')\nidentifier = PidData(type=\'identifier\',\n                     parsed_data={"identifier-Attribute": "DOI", "identifier-Value": "10.123.456/789"})\nresource_type = PidData(type=\'resourceType\', parsed_data={"resourceType-Value": "test"})\ncreators = PidData(type=\'creators\', parsed_data={"creator": {"creatorName": "Triet Doan"}})\ntitles = PidData(type=\'titles\', parsed_data={"title": {"title-Value": "Test title"}})\n\n# Create the PID object\nprefix = \'my_prefix\'\npid = Pid(prefix=prefix, data=[publisher, publication_year, identifier, resource_type, creators, titles])\n\n# Create the client\nepic_api = EpicAPI(\'<host>\', \'<username>\', \'<password>\')\n\n# Create the PID\npid = epic_api.create(pid)\n\n# Get the PID\npid_response = epic_api.get(pid.pid_str)\n\n# Delete the PID\nepic_api.delete(pid.pid_str)\n```',
    'author': 'Triet Doan',
    'author_email': 'triet.doan@gwdg.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.gwdg.de/epic/epic-python-library',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
