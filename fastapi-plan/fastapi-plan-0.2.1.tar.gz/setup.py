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
    'version': '0.2.1',
    'description': 'Dead simple template manager for FastAPI applications',
    'long_description': '# fastapi-plan\nDead simple template manager for FastAPI applications\n',
    'author': 'rafsaf',
    'author_email': 'rafal.safin12@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rafsaf/fastapi-template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
