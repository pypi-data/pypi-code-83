# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_models_parser']

package_data = \
{'': ['*']}

install_requires = \
['parsimonious>=0.8.1,<0.9.0']

setup_kwargs = {
    'name': 'py-models-parser',
    'version': '0.1.0',
    'description': '',
    'long_description': '\nPy-Models-Parser\n----------------\n\nIt\'s as second Parser that done by me, first is a https://github.com/xnuinside/simple-ddl-parser for SQL DDL with different dialects.\nPy-Models-Parser supports now ORM Sqlalchemy, Gino, Tortoise; Pydantic, Python Enum models & in nearest feature I plan to add Dataclasses & pure pyton classes. And next will be added other ORMs models.\n\nPy-Models-Parser written with PEG parser and it\'s python implementation - parsimonious.\nPy-Models-Parser take as input different Python code with Models and provide output in standard form:\n\n.. code-block:: python\n\n\n       [\n           \'name\': \'ModelName\',\n           \'parents\': [\'BaseModel\'], # class parents that defined in (), for example: `class MaterialType(str, Enum):` parents - str, Enum\n           \'attrs\':\n       {\n           \'type\': \'integer\',\n           \'name\': \'attr_name\',\n           \'default\': \'default_value\',\n           \'properties\': {\n               ...\n           }\n       },\n       \'properties\': {\n           \'table_name\': ...\n       }\n       ]\n\nFor ORM models \'attrs\' contains Columns of course.\n\n3 keys - \'type\', \'name\', \'default\' exists in parse result \'attrs\' of all Models\n\'properties\' key contains additional information for attribut or column depend on Model type, for example, in ORM models it can contains \'foreign_key\' key if this column used ForeignKey, or \'server_default\' if it is a SqlAlchemy model or GinoORM.\n\nModel level \'properties\' contains information relative to model, for example, if it ORM model - table_name\n\nNOTE: it\'s is a text parser, so it don\'t import or load your code, parser work with source code as text, not objects in Python. So to run parser you DO NOT NEED install dependencies for models, that you tries to parse - only models.\n\nHow to install\n--------------\n\n.. code-block:: bash\n\n\n       pip install py-models-parser\n\nHow to use\n----------\n\nLibrary detect automaticaly that type of models you tries to parse. You can check a lot of examples in test/ folder on the GitHub\n\nYou can parse models from python string:\n\n.. code-block:: python\n\n\n   from py_models_parser.core import parse\n\n   models_str =  """from gino import Gino\n\n   db = Gino()\n\n\n   class OrderItems(db.Model):\n\n       __tablename__ = \'order_items\'\n\n       product_no = db.Column(db.Integer(), db.ForeignKey(\'products.product_no\'), ondelete="RESTRICT", primary_key=True)\n       order_id = db.Column(db.Integer(), db.ForeignKey(\'orders.order_id\'), ondelete="CASCADE", primary_key=True)\n       type = db.Column(db.Integer(), db.ForeignKey(\'types.type_id\'), ondelete="RESTRICT", onupdate="CASCADE")\n\n       """\n   result = parse(models_str)\n\nIt will produce the result:\n\n.. code-block:: python\n\n\n       [\n           {\n               "attrs": [\n                   {\n                       "default": None,\n                       "name": "product_no",\n                       "properties": {\n                           "foreign_key": "\'products.product_no\'",\n                           "ondelete": \'"RESTRICT"\',\n                           "primary_key": "True",\n                       },\n                       "type": "db.Integer()",\n                   },\n                   {\n                       "default": None,\n                       "name": "order_id",\n                       "properties": {\n                           "foreign_key": "\'orders.order_id\'",\n                           "ondelete": \'"CASCADE"\',\n                           "primary_key": "True",\n                       },\n                       "type": "db.Integer()",\n                   },\n                   {\n                       "default": None,\n                       "name": "type",\n                       "properties": {\n                           "foreign_key": "\'types.type_id\'",\n                           "ondelete": \'"RESTRICT"\',\n                           "onupdate": \'"CASCADE"\',\n                       },\n                       "type": "db.Integer()",\n                   },\n               ],\n               "name": "OrderItems",\n               "parents": ["db.Model"],\n               "properties": {"table_name": "\'order_items\'"},\n           }\n       ]\n\nTODO: in next Release\n---------------------\n\n\n#. Parse from file method\n#. Add cli\n#. Add more tests for supported models (and fix existed not covered cases): Pydantic, Enums, Dataclasses, SQLAlchemy Models, GinoORM models, TortoiseORM models \n#. Add support for pure Python classes\n#. Add support for pure SQLAlchemy Core Tables\n\nChangelog\n---------\n\n**v0.1.0**\n\n\n#. Added base parser logic & tests for Pydantic, Enums, SQLAlchemy Models, GinoORM models, TortoiseORM models \n',
    'author': 'Iuliia Volkova',
    'author_email': 'xnuinside@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xnuinside/omymodels',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
