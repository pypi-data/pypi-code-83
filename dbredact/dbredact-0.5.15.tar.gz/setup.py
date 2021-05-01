# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['app',
 'app.celery',
 'app.cli',
 'app.mail',
 'app.models.orm',
 'app.models.schemas',
 'app.models.schemas.discovery',
 'app.models.schemas.mssql',
 'app.models.schemas.oracle.redact',
 'app.redis',
 'app.routes',
 'app.routes.discovery',
 'app.routes.mssql',
 'app.routes.oracle',
 'app.routes.oracle.redact',
 'app.settings',
 'app.tasks',
 'app.tasks.discovery',
 'app.tasks.notification',
 'app.utils',
 'app.vendors',
 'app.vendors.mssql',
 'app.vendors.oracle']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'aiofiles>=0.6.0,<0.7.0',
 'aioredis>=1.3.1,<2.0.0',
 'alembic>=1.4.2,<2.0.0',
 'arq>=0.19,<0.20',
 'async-timeout>=3.0.1,<4.0.0',
 'celery>=5.0.5,<6.0.0',
 'click>=7.1.2,<8.0.0',
 'cryptography>=3.4.4,<4.0.0',
 'cx-Oracle>=8.1.0,<9.0.0',
 'email_validator>=1.1.0,<2.0.0',
 'fastapi-mail>=0.3.5,<0.4.0',
 'fastapi-pagination>=0.6.1,<0.7.0',
 'fastapi>=0.63.0,<0.64.0',
 'keyrings.alt>=4.0.2,<5.0.0',
 'mkdocs-material>=7.0.6,<8.0.0',
 'passlib>=1.7.4,<2.0.0',
 'psycopg2-binary>=2.8.5,<3.0.0',
 'pydash>=4.9.3,<5.0.0',
 'pymssql>=2.2.0,<3.0.0',
 'python-jose>=3.2.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'redis>=3.5.3,<4.0.0',
 'sentry-sdk>=0.14.3,<0.15.0',
 'sqlalchemy-utils>=0.36.5,<0.37.0',
 'starlette-context>=0.3.1,<0.4.0',
 'uvicorn>=0.11.5,<0.12.0']

entry_points = \
{'console_scripts': ['redact = app.cli:redact']}

setup_kwargs = {
    'name': 'dbredact',
    'version': '0.5.15',
    'description': 'Data Redaction Application',
    'long_description': '# DUCK\n\nOnline data masking and sensitve data discovery platform for common rdbms.\n\n## Commands\n`duck --help`\n\n\n## LICENCE\n\n[Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)\n![licence](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-nd.png)\n',
    'author': 'Ceyhun Kerti',
    'author_email': 'ceyhun.kerti@bluecolor.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bluecolor/redact',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
