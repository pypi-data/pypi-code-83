# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yamlflow',
 'yamlflow.cli',
 'yamlflow.cli.commands',
 'yamlflow.dockerfiles.core.scripts']

package_data = \
{'': ['*'],
 'yamlflow': ['dockerfiles/app/*',
              'dockerfiles/backend/sklearn-cpu/*',
              'dockerfiles/backend/torch-cpu/*',
              'dockerfiles/core/*']}

install_requires = \
['click>=7.0.0,<8.0.0', 'docker>=5.0.0,<6.0.0', 'pyyaml>=5.4.1,<6.0.0']

entry_points = \
{'console_scripts': ['yamlflow = yamlflow.cli:main']}

setup_kwargs = {
    'name': 'yamlflow',
    'version': '0.0.9',
    'description': 'Yet Another ML flow',
    'long_description': "# yamlflow\nYet Another ML flow\n\nWe follow `convention over configuration` (also known as coding by convention) software design paradigm.\n\nHere are some of the features the `yamlflow` provides.\n\n\n1. Build and publish your ML solution as a RESTful Web Service `with yaml`.\n    \n    + You don't need to write web realated code, or dockerfiles.\n    \n    + You don't need to benchmark which python web server or framework is best in terms of performance.\n    \n    + WE do it for you. All the best, packed in.\n\n\n## Metrics for inference\n\n+ Throughput\n (How many requests can server process in some interval of time)\n\n+ Latency\n (How long does it take to get a prediction for a single request)\n\n## Python REST API\n\n```\nasync\n    - web-server(ASGI): Uvicorn, Hypercorn, Daphne\n    - web-(micro)framework: Starlete, ...\n    - API-framework: FastAPI, ...\n\nsync\n    - web-server(WSGI): gunicorn, uWSGI, Gevent, Twisted Web\n    - web-(micro)framework: Flask\n    - API-framework: None\n```\n\n\n### Project structure \n```\n.\n├── model\n│   ├── ...\n│   ├── pipeline.py\n│   └── requirements.txt\n├── service\n│   ├── objects\n│   ├── config.py\n│   └── predictor.py\n├── train\n│   ├── ...\n│   ├── train.py\n│   └── requirements.txt\n├── README.md\n└── yamlflow.yaml\n```\n\n#### example `yamlflow.yaml`\n```yaml\nkind: Service\nmeta:\n  registry: your.docker.registry\n  user: dockerusername\nproject:\n  name: ml-project\n  version: 0.1.0\nbackend:\n  runtime: torch\n  device: cpu\nport: 8002\n```\n\n### Installation guide\n```bash\npip install yamlflow\n```\n\n### User guide\n```bash\nyamlflow init\nyamlflow build\nyamlflow run\n```\n\n### Developer guide\n```\npyenv install 3.8.6\npoetry env use ~/.pyenv/versions/3.8.6/bin/python\npoetry shell\npoetry install\n```\n",
    'author': 'Sevak Harutyunyan',
    'author_email': 'sevak.g.harutyunyan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sevakharutyunyan/yamlflow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
