# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylineage']

package_data = \
{'': ['*'], 'pylineage': ['templates/*']}

install_requires = \
['graphviz>=0.16,<0.17',
 'networkx>=2.5.1,<3.0.0',
 'pydot>=1.4.2,<2.0.0',
 'regex>=2021.4.4,<2022.0.0']

setup_kwargs = {
    'name': 'pylineage',
    'version': '0.1.4',
    'description': 'Data Lineage for Python',
    'long_description': '[![PyPI - Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://pypi.org/project/pylineage/)\n[![PyPI - PyPi](https://img.shields.io/pypi/v/pylineage)](https://pypi.org/project/pylineage/)\n[![PyPI - License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/jasperpaalman/pylineage/blob/master/LICENSE)\n\n# pylineage\nThis package provides simple tools for parsing and visualizing your .sql scripts.\n\n## Installation\n\nThe package is distributed through PyPI, and can be installed with\n\n```bash\npip install pylineage\n```\n\nIn order to create a lineage graph you should also install and add [Graphviz](https://graphviz.org/download/) to your Path. \n\n## SQL Parser\n\nIndividual basic .sql scripts can be parsed by running\n\n```python\nfrom pylineage import SqlParser\n\nparser = SqlParser()\nquery = """\n\nSELECT column1\n     , column2 AS c2\nFROM my_table t\nWHERE column1 = 1\n\n"""\n\nparsed = parser.parse(query)\n```\n\nThe output looks as follows\n\n```python\n>>> parsed\n\n{\n  "select": [{ "content": "column1" }, { "content": "column2", "alias": "c2" }],\n  "from": { "content": "my_table", "alias": "t" },\n  "where": ["column1 = 1"]\n}\n```\n\nCurrently the parser supports the clauses\n\n| Clause           |\n|------------------|\n| SELECT           |\n| FROM             |\n| LEFT JOIN        |\n| LEFT OUTER JOIN  |\n| RIGHT JOIN       |\n| RIGHT OUTER JOIN |\n| FULL JOIN        |\n| FULL OUTER JOIN  |\n| JOIN             |\n| INNER JOIN       |\n| WHERE            |\n| QUALIFY          |\n| GROUP BY         |\n| ORDER BY         |\n| HAVING           |\n## Lineage Graph\n\nBased on the SQL parser, a lineage graph can be constructed. \nWe start off with the main constructor:\n\n```python\n\nfrom pylineage import LineageGraph\n\nlineage_graph = LineageGraph()\n```\n\nSubsequently, there are two options of adding SQL scripts: (1) as individual input strings or (2) as directory.\n\n```python\n\nlineage_graph.extend_graph_from_input_string("CREATE TABLE my_view AS SELECT column1 FROM my_table")\n\nlineage_graph.extend_graph_from_directory("/data")\n\n```\n\nThe graph can be cleared at any time by running\n\n```python\nlineage_graph.clear_graph()\n```\n\nOne purpose of parsing and visualizing is to obtain execution order. This can be obtained by running\n\n```python\nlineage_graph.get_execution_order()\n```\n\n**NOTE**</br>\nAny inner query that is not a part of a source clause (FROM / JOIN) is not included as a node in the graph. As such, statements like the one below are not taken into account.\n\n```sql\n...\nWHERE column not in (\n  SELECT column\n  FROM table2\n)\n```\n\nFinally the Lineage Graph can be accessed by directly checking\n\n```python\nlineage_graph.graph\n```\n\nor by running it in interactive mode:\n\n```python\nlineage_graph.serve_graph()\n```\n\nThe interactive mode offers convenient highlighting and dragging capabilities.\n\n<img src="images/interactive_graph.gif" width="80%"/>',
    'author': 'jasperpaalman',
    'author_email': 'jasper_paalman@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jasperpaalman/pylineage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
