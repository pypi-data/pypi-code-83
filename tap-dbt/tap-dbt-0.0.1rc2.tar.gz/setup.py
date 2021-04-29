# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_dbt', 'tap_dbt.tests']

package_data = \
{'': ['*'], 'tap_dbt': ['schemas/*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'singer-sdk>=0.1.2,<0.2.0']

entry_points = \
{'console_scripts': ['tap-dbt = tap_dbt.tap:cli']}

setup_kwargs = {
    'name': 'tap-dbt',
    'version': '0.0.1rc2',
    'description': 'Singer tap for dbt, built with the Singer SDK.',
    'long_description': '# tap-dbt\n\n[![PyPI](https://img.shields.io/pypi/v/tap-dbt.svg)](https://pypi.org/project/tap-dbt/)\n[![Python versions](https://img.shields.io/pypi/pyversions/tap-dbt.svg)](https://pypi.org/project/tap-dbt/)\n[![Super-Linter](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/superlinter.yml/badge.svg)](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/superlinter.yml)\n[![TestPyPI](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/test-pypi.yml/badge.svg)](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/test-pypi.yml)\n[![Test Tap](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/test-tap.yml/badge.svg)](https://github.com/edgarrmondragon/tap-dbt/actions/workflows/test-tap.yml)\n\n`tap-dbt` is a Singer tap for the [dbt Cloud API][dbtcloud].\n\nBuilt with the [Singer SDK][sdk].\n\n- [Installation](#Installation)\n- [Configuration](#Configuration)\n  - [Inputs](#Inputs)\n  - [JSON example](#JSON-example)\n  - [Environment variables example](#Environment-variables-example)\n- [Usage](#Usage)\n\n## Installation\n\n```shell\npip install tap-dbt\n```\n\n## Configuration\n\nVisit the [API docs][apidocs] for instructions on how to get your API key.\n\nYou can pass configuration using environment variables with the `TAP_DBT_` prefix followed by the uppercased field name\n\n```shell\ntap-dbt --config=ENV\n```\n\nor a JSON file\n\n```shell\ntap-dbt --config=config.json\n```\n\n### Inputs\n\n| Field         | Description                      | Type           | Required | Default                                          |\n|---------------|----------------------------------|----------------|----------|--------------------------------------------------|\n| `api_key`     | API key for the dbt Cloud API    | `string`       | yes      |                                                  |\n| `account_ids` | dbt Cloud account IDs            | `list(string)` | yes      |                                                  |\n| `user_agent`  | User-Agent to make requests with | `string`       | no       | `tap-dbt/0.1.0 Singer Tap for the dbt Cloud API` |\n| `base_url`    | Base URL for the dbt Cloud API   | `string`       | no       | `https://cloud.getdbt.com/api/v2`                |\n\n### JSON example\n\n```json\n{\n  "api_key": "da39a3ee5e6b4b0d3255bfef95601890afd80709",\n  "account_ids": [51341],\n  "user_agent": "tap-dbt/0.1.0 Singer Tap for the dbt Cloud API",\n  "base_url": "https://my-dbt-cloud-api.com"\n}\n```\n\n### Environment variables example\n\n```dotenv\nTAP_DBT_API_KEY=da39a3ee5e6b4b0d3255bfef95601890afd80709\nTAP_DBT_ACCOUNT_IDS=[51341]\nTAP_DBT_USER_AGENT=\'tap-dbt/0.1.0 Singer Tap for the dbt Cloud API\'\nTAP_DBT_BASE_URL=https://my-dbt-cloud-api.com"\n```\n\nA full list of supported settings and capabilities for this tap is available by running:\n\n```shell\ntap-dbt --about --format json\n```\n\n## Usage\n\nYou can easily run `tap-dbt` by itself or in a pipeline using [Meltano][meltano].\n\n### Executing the Tap Directly\n\n```shell\ntap-dbt --version\ntap-dbt --help\ntap-dbt --config .secrets/example.json --discover > ./catalog/json\n```\n\n[dbtcloud]: https://cloud.getdbt.com\n[sdk]: https://gitlab.com/meltano/singer-sdk\n[apidocs]: https://docs.getdbt.com/dbt-cloud/api#section/Authentication\n[meltano]: https://gitlab.com/meltano/singer-sdk/-/blob/main/www.meltano.com\n[click]: click.palletsprojects.com/\n',
    'author': 'Edgar Ramírez Mondragón',
    'author_email': 'edgarrm358@sample.com',
    'maintainer': 'Edgar Ramírez Mondragón',
    'maintainer_email': 'edgarrm358@sample.com',
    'url': 'https://github.com/edgarrmondragon/tap-dbt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.9',
}


setup(**setup_kwargs)
