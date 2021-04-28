# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_mockforce', 'simple_mockforce.query_algorithms']

package_data = \
{'': ['*']}

install_requires = \
['decorator>=5.0.7,<6.0.0',
 'python-soql-parser>=0.1.0,<0.2.0',
 'responses>=0.13.2,<0.14.0']

setup_kwargs = {
    'name': 'simple-mockforce',
    'version': '0.1.5',
    'description': "A companion package for simple-salesforce that enables the testing of code that interacts with Salesforce's API",
    'long_description': '# Introduction\n\nThis library was inspired by [moto](https://github.com/spulec/moto) and mimics some of its design. Mainly,\nno `simple-salesforce` code is patched; instead, the HTTP calls it makes are intercepted, and state is\nstored in an in-memory, virtual Salesforce instance, which is just a globally instantiated class that\nis created at the run-time of a test-suite.\n\n# Installation\n\n`pip install simple-mockforce`\n\nor, with poetry\n\n`poetry add simple-mockforce`\n\n# Usage\n\nTo patch calls to the Salesforce API and instead interact with the "virtual"\nSalesforce instance provided by this library, add the following:\n\n```python\nimport os\n\nfrom simple_mockforce import mock_salesforce\n\nfrom simple_salesforce import Salesforce\n\n\n@mock_salesforce\ndef test_api():\n    salesforce = Salesforce(\n        username=os.getenv["SFDC_USERNAME"],\n        password=os.getenv["SFDC_PASSWORD"],\n        security_token=os.getenv["SFDC_SECURITY_TOKEN"]\n    )\n\n    salesforce.Account.create({"Name": "Test Account"})\n```\n\nTo reset state, you can call `create_new_virtual_instance`,\nensuring there\'s no pollution between tests\n\n```python\nfrom simple_mockforce.virtual import virtual_salesforce\n\n\n@mock_salesforce\ndef test_api_again():\n    # This will wipe away the account created in the above step\n    virtual_salesforce.create_new_virtual_instance()\n```\n\nAnd that\'s about it!\n\n# Caveats\n\n## Case sensitivity\n\nUnlike a real Salesforce instance, the virtual instance will not handle case-insensitive\ndependent code for you. You must remain consistent with your casing of object and field\nnames in all aspects of the code.\n\n## Missing endpoints\n\nThe following features are currently not supported:\n\n- the describe API\n- bulk queries\n- SOSL searches\n\n## Queries\n\nSOQL is only partially supported as of now. Please refer to the README\nfor [python-soql-parser](https://github.com/Kicksaw-Consulting/python-soql-parser#notable-unsupported-features)\nto see what\'s not yet implemented.\n\nYou should only expect this library to be able to mock the most basic of queries.\nWhile there are plans to, mocking query calls which traverse object relationships\nor that use SOQL-specific where-clause tokens are not yet supported.\n\nNotable mentions:\n\n- be explicit with direction in `ORDER BY` clauses, i.e., always supply `DESC` or `ASC`\n\n## Error handling\n\nError handling is only mocked to a degree, and for some calls it isn\'t at all.\nThis is because the virtual Salesforce instance does not yet enforce any of\nthe server-side validation when working with a real API.\n\nThis means that the virtual instance is much more permissive and loose than a\nreal Salesforce instance would be.\n\nThere are plans to read the XML consumed by the meta API in order to enforce\nmore rigidity inside the virtual instance, but this is not yet implemented.\n\n## All HTTP traffic is blocked\n\nWhen using `@mock_salesforce`, do note that the `requests` library is being\npatched with `responses`, so any calls you make to any other APIs will fail\nunless you patch them yourself, or patch the code which invokes.\n',
    'author': 'Alex Drozd',
    'author_email': 'drozdster@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Kicksaw-Consulting/simple-mockforce',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
