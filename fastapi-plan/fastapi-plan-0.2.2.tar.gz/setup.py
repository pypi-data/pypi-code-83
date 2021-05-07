# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_plan',
 'fastapi_plan.template.hooks',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.api',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.api.routers',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.core',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.crud',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.models',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.schemas',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.tests',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.tests.api',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.tests.crud',
 'fastapi_plan.template.{{cookiecutter.project_name}}.app.tests.utils']

package_data = \
{'': ['*'],
 'fastapi_plan': ['template/*',
                  'template/{{cookiecutter.project_name}}/*',
                  'template/{{cookiecutter.project_name}}/config/*'],
 'fastapi_plan.template.{{cookiecutter.project_name}}.app': ['migrations/models/*']}

install_requires = \
['cookiecutter>=1.7.2,<2.0.0']

entry_points = \
{'console_scripts': ['fastapi-plan = fastapi_plan:main']}

setup_kwargs = {
    'name': 'fastapi-plan',
    'version': '0.2.2',
    'description': 'Dead simple template manager for FastAPI applications',
    'long_description': '# Project description\n\n[![GitHub license](https://img.shields.io/github/license/rafsaf/fastapi-plan)](https://github.com/rafsaf/fastapi-plan/blob/master/LICENSE)\n![PyPI](https://img.shields.io/pypi/v/fastapi-plan)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fastapi-plan)\n![example workflow](https://github.com/rafsaf/fastapi-plan/actions/workflows/python-package.yml/badge.svg)\n\n## about\n\ndead simple but powerful template manager for FastAPI applications.\n\n## quickstart\n\nNOTE: you will need [docker](https://www.docker.com/get-started) and optional but recommended [poetry](https://python-poetry.org/docs/) installed!\n\ninstall via pip (or poetry):\n\n```bash\npip install fastapi-plan\n```\n\ninitialize new FastAPI project:\n\n```bash\nfastapi-plan\n```\n\nenter project name and other information and after noticing SUCCESS your project is ready, enter project with `cd project_name` and continue installing dependencies:\n\n```bash\npoetry install\n\n# optional if you selected "requirements.txt" (with venv installed)\npip install -r requirements.txt\n```\n\nsince we wanna use uvicorn in development, create only postgres container using docker-compose:\n\n```bash\ndocker-compose up -d db\n```\n\nnow run aerich migrations and configure tortoise (and add first superuser)\n\n```bash\naerich upgrade\npython app/initial_data.py\n```\n\nfinally you can run this command to start uvicorn server\n\n```bash\nuvicorn app.main:app --reload\n```\n\n## short project structure\n\n```\n|── app\n|    ├── api                                 # endpoints/dependecies\n|    |\n|    ├── core                                # settings and security algorithms\n|    |\n|    ├── crud                                # CRUD operations\n|    |\n|    ├── migrations                          # for aerich migrations\n|    |\n|    ├── models                              # tortoise models\n|    |\n|    ├── schemas                             # pandatic schemas\n|    |\n|    ├── tests                               # tests\n|    |\n|    ├── initial.sh                          # initial shell script used by docker\n|    ├── initial_data.py                     # init database and add first superuser\n|    ├── main.py                             # main fastapi application file\n|\n├── config                                   # nginx server config file\n|\n├── .env                                     # .env file with settings\n|\n├── Dockerfile                               # dockerfile for web app\n|\n├── aerich.ini                               # aerich (migrations) configuration\n|\n├── docker-compose.yml                       # puts it all together\n|\n├── pytest.ini                               # Pytest configurations\n|\n├── pyproject.toml                           # python dependencies (poetry)\n|\n├── poetry.lock                              # python dependencies (poetry)\n|\n├── (optional) requirements.txt              # python dependencies (pip)\n```\n\n## why such a structure of the project\n',
    'author': 'rafsaf',
    'author_email': 'rafal.safin12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafsaf/fastapi-template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
