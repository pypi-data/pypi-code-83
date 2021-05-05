# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['html_dsl']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'html-dsl',
    'version': '0.4.0',
    'description': 'A HTML-DSL for Python',
    'long_description': 'html-dsl\n--------\nA HTML-DSL for Python\n\nUSE\n---\n\n\n>>> from html_dsl.elements import BaseHtmlElement, HTML, BODY, H1, P, DIV, SPAN\n>>> html = HTML[\n        BODY[\n            H1["Title"],\n            P(color="yellow")[\n                "Hello, World.", SPAN["something in span"], "Out of the span"\n            ],\n            P["This is the second paragraph."],\n            DIV[\n                DIV(_class="row")[\n                    DIV(_class="column", color="red")["col1"],\n                    DIV(_class="column", color="blue")["col2"],\n                    DIV(_class="column", color="green")["col3"],\n                ]\n            ],\n        ]\n    ]\n>>> print(html)\n<html>\n  <body>\n    <h1>\n    Title\n    </h1>\n    <p color="yellow">\n    Hello, World.\n      <span>\n      something in span\n      </span>\n    Out of the span\n    </p>\n    <p>\n    This is the second paragraph.\n    </p>\n    <div>\n      <div class="row">\n        <div color="red" class="column">\n        col1\n        </div>\n        <div color="blue" class="column">\n        col2\n        </div>\n        <div color="green" class="column">\n        col3\n        </div>\n      </div>\n    </div>\n  </body>\n</html>\n\nInstall\n-------\n\n.. code-block:: shell\n    \n    pip install html_dsl\n\n\nAuthor\n------\nYixian Du',
    'author': 'duyixian',
    'author_email': 'duyixian1234@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/duyixian1234/html_dsl',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
