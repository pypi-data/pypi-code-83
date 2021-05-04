# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['openapi_annotations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'openapi-annotations',
    'version': '0.1.2',
    'description': 'Generate OpenApi with code-first annotations. Use type-hint info and docstrings to document your API. This is an experimental library!',
    'long_description': '# OpenAPI Python annotations\n\nGenerate OpenApi with code-first annotations. Use type-hint info and docstrings to document your API. This is an experimental library!\n\n## Getting Started\n\n### Install the package\n\n```\npip install openapi-annotations\n```\n\n### Document a model\n\n\n```python\nfrom openapi_annotations import api_model, api_property, StringFormats\n\n\n@api_model\nclass Event:\n    """The first model from this API."""\n\n    @property\n    def id(self) -> str:\n        return self._id\n\n    @id.setter\n    @api_property(data_format=StringFormats.Uuid, nullable=True)\n    def id(self, value: str):\n        """The id of the object."""\n        self._id = value\n\n    @property\n    def documented_property(self) -> str:\n        return self._documented_property\n\n    @documented_property.setter\n    @api_property()\n    def documented_property(self, value: str):\n        """Property documentation."""\n        self._documented_property = value\n```\n\n\n### Document a route\n\n\n```python\nfrom openapi_annotations import api_route, api_response\nfrom http import HTTPStatus\nfrom .models import Event # My custom model\n\n\n@api_response(HTTPStatus.CREATED, Event)\n@api_response(HTTPStatus.BAD_REQUEST)\n@api_response(HTTPStatus.INTERNAL_SERVER_ERROR)\n@api_route(Methods.Post, f\'events/{{eventId}}\', Event)\ndef events_post(body=None):\n    """Creates a new event and returns it."""\n    result = {}\n    return json.dumps(result), 201\n\n```\n\n\n### View the swagger:\n\n```python\nimport .controllers # Make sure you import all files containing annotations\nfrom openapi_annotations import get_spec\nimport json\n\nwith open(\'./openapi.json\', \'w\') as file:\n    file.write(json.dumps(spec, indent=4))\n```\n',
    'author': 'Mathias Colpaert',
    'author_email': 'mathias.colpaert@trensition.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mathi123/openapi-annotation',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
