# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roman_discovery', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'roman-discovery',
    'version': '0.2.0',
    'description': 'Discover packages and classes in a python project.',
    'long_description': '# Roman Discovery\n\nThe package scans the project to execute some actions with found modules and objects. It\'s specifically helpful for frameworks that define resources on the fly with decorators and expect you to import all necessary modules.\n\nFor example, it can be helpful for Flask to load all your blueprints, initialize extensions, and import SQLAlchemy models.\n\n## Install\n\n```shell\npip install roman-discovery\n```\n\n## Usage with Flask\n\nUsing within the opinionated Flask structure was the initial purpose of the package. Use `roman_discovery.discover()` with\n`roman_discovery.flask.get_flask_rules()`.\n\nThe function expects the following project structure.\n\n```\nmyproject\n\n  app.py\n  config.py\n  services.py\n\n  foo/\n    controllers.py\n    models.py\n    cli.py\n\n  bar/\n    controllers/\n      api.py\n      admin.py\n    models/\n      users.py\n      projects.py\n    cli/\n      user_commands.py\n      project_commands.py\n```\n\nWith this structure, it will do the following.\n\n- Scan controllers.py and controllers/ to find blueprints and attach the blueprints to the flask application.\n- Import all files in models.py and models/ to help flask-migrate find all the SQLAlchemy models to create migrations.\n- Scan cli.py and cli/ to find flask.cli.AppGroup instances and attach them to Flask\'s CLI.\n- Scan top-level services.py, find all the instances that have `init_app()` methods, and call `obj.init_app(app=flask_app)` for each of them.\n\nAn example of your top-level app.py\n\n```python\n# file: myproject/app.py\nfrom flask import Flask\nfrom roman_discovery import discover\nfrom roman_discovery.flask import get_flask_rules\n\n\ndef app() -> Flask:\n    flask_app = Flask(__name__, instance_relative_config=True)\n    flask_app.config.from_object("myproject.config")\n    flask_rules = get_flask_rules("myproject", flask_app)\n    discover("myproject", flask_rules)\n    return flask_app\n```\n\nAn example of your top-level services.py\n\n```python\n# file: myproject/services.py\n\nfrom flask_sqlalchemy import SQLAlchemy\nfrom flask_migrate import Migrate\nfrom flask_mail import Mail\n\ndb = SQLAlchemy()\nmigrate = Migrate(db=db)\nmail = Mail()\n```\n\n\n## Usage with anything else\n\nYou can create your own discovery rules with the `discover()` function, `ModuleRule` and `ObjectRule`. Optionally, you can take advantage of custom matchers, defined in `roman_discovery.matchers`.\n\nFor example, that\'s how you print all modules and all callable objects within the `roman_discovery` itself.\n\n```python\nfrom roman_discovery import discover, ModuleRule, ObjectRule\n\nmodule_printer = ModuleRule(\n    name="module printer",\n    module_matches=lambda module_name: True,\n    module_action=lambda module_name: print(f"Found module {module_name}"),\n)\n\nobject_printer = ObjectRule(\n    name="object printer",\n    module_matches=lambda module_name: True,\n    object_matches=callable,\n    object_action=lambda obj: print(f"Found callable object {obj!r}"),\n)\n\ndiscover("roman_discovery", rules=[module_printer, object_printer])\n```\n\n\n## Why the "roman" prefix?\n\nI use it as my own "pseudo-namespace." If I ever abandon the project, at least the package doesn\'t occupy a common name.\n',
    'author': 'Roman Imankulov',
    'author_email': 'roman.imankulov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imankulov/roman_discovery',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7.8,<4.0',
}


setup(**setup_kwargs)
