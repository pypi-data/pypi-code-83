# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyconnect']

package_data = \
{'': ['*']}

install_requires = \
['avro-python3>=1.10.0,<2.0.0',
 'confluent-kafka[avro]>=1.6.1,<2.0.0',
 'loguru',
 'pycodestyle',
 'pydantic>=1.6.1,<2.0.0',
 'pyyaml>=5.3.1,<6.0.0']

setup_kwargs = {
    'name': 'pyconnect',
    'version': '0.5.1',
    'description': 'A Python implementation of "Kafka Connect"-like functionality',
    'long_description': None,
    'author': 'real.digital',
    'author_email': 'opensource@real-digital.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
