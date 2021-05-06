# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dyndns_updater']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'dnspython>=2.1.0,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'schedule>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'dyndns-updater',
    'version': '0.1.1',
    'description': 'standalone DNS updater for Gandi',
    'long_description': '# dynDNS_updater\nstandalone DNS updater for Gandi\n\nThe main purpose of **dynDNS_updater** is to keep the DNS records pointing to your servers up to date **without any system dependencies** (except python, of course) nor any fancy web services to identify their public IPv4 / IPv6\n\n## Usage\n\n```yaml\nip_identifier: cloudflare\ndelta : 900\ndns_providers: \n  - gandi: GKDNzPZsdHB8vxA56voERCiC\n    somedomain.io:\n      tower: A\n      tower6: AAAA\n      tower2: AAAA\n```\n\n## Features\n\nTypes of records\n\n* A\n* AAAA\n\n### Supported DNS provider\n\n|      Name | API root                         |\n| --------: | :------------------------------- |\n| **Gandi** | https://api.gandi.net/v5/livedns |\n\n## Developpers \n\n### Onboarding\n\n* [poetry]()\n* []()\n\n```bash\ngit clone https://github.com/zar3bski/dynDNS_updater.git\ncd dynDNS_updater\npoetry install \n```\n',
    'author': 'David Zarebski',
    'author_email': 'zarebskidavid@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zar3bski/dynDNS_updater',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
