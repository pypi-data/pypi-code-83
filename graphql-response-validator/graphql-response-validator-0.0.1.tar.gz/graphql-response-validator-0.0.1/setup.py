# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['graphql_response_validator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'graphql-response-validator',
    'version': '0.0.1',
    'description': 'A tool for validating GraphQL responses against their respective queries',
    'long_description': 'graphql-response-validator\n==========================\n\n|Build| |Coverage| |Version| |Python versions| |License|\n\nA tool for validating GraphQL responses against their respective queries.\n\nThis package is work-in-progress.\n\n.. |Build| image:: https://github.com/schemathesis/graphql-response-validator/workflows/build/badge.svg\n   :target: https://github.com/schemathesis/graphql-response-validator/actions\n.. |Coverage| image:: https://codecov.io/gh/schemathesis/graphql-response-validator/branch/main/graph/badge.svg\n   :target: https://codecov.io/gh/schemathesis/graphql-response-validator/branch/main\n   :alt: codecov.io status for main branch\n.. |Version| image:: https://img.shields.io/pypi/v/graphql-response-validator.svg\n   :target: https://pypi.org/project/graphql-response-validator/\n.. |Python versions| image:: https://img.shields.io/pypi/pyversions/graphql-response-validator.svg\n   :target: https://pypi.org/project/graphql-response-validator/\n.. |License| image:: https://img.shields.io/pypi/l/graphql-response-validator.svg\n   :target: https://opensource.org/licenses/MIT\n',
    'author': 'Dmitry Dygalo',
    'author_email': 'dadygalo@gmail.com',
    'maintainer': 'Dmitry Dygalo',
    'maintainer_email': 'dadygalo@gmail.com',
    'url': 'https://github.com/schemathesis/graphql-response-validator',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
