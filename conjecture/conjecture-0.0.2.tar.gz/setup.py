# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['conjecture']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'conjecture',
    'version': '0.0.2',
    'description': 'A pythonic assertion library',
    'long_description': '# Conjecture\n\nA pythonic assertion library.\n\n## 🛠 Installing\n\n### Poetry\n\n```\npoetry add conjecture\n```\n\n### pip\n\n```\npip install conjecture\n```\n\n## 🎓 Usage\n\n\n### Basic\n\nA basic assertion.\n\n```pycon\n>>> import conjecture\n>>> assert 5 == conjecture.has(lambda v: v < 10)\n>>> assert 5 == conjecture.has(lambda v: v > 10)\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n```\n\n### Combined conjectures\n\nMatching all conditions.\n\n```pycon\n>>> import conjecture\n>>> assert 5 == conjecture.has(lambda v: v <= 5) & conjecture.has(lambda v: v => 5)\n>>> assert 6 == conjecture.has(lambda v: v <= 5) & conjecture.has(lambda v: v => 5)\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n>>> assert 5 == conjecture.all_of(\n...     conjecture.has(lambda v: v <= 5),\n...     conjecture.has(lambda v: v => 5)\n... )\n>>> assert 6 == conjecture.all_of(\n...     conjecture.has(lambda v: v <= 5),\n...     conjecture.has(lambda v: v => 5)\n... )\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n```\n\nMatching any conditions.\n\n```pycon\n>>> import conjecture\n>>> assert 0 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)\n>>> assert 5 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)\n>>> assert 6 == conjecture.has(lambda v: v == 5) | conjecture.has(lambda v: v == 0)\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n>>> assert 5 == conjecture.any_of(\n...     conjecture.has(lambda v: v == 5),\n...     conjecture.has(lambda v: v == 0)\n... )\n>>> assert 6 == conjecture.any_of(\n...     conjecture.has(lambda v: v == 5),\n...     conjecture.has(lambda v: v == 0)\n... )\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n```\n\n### Negation\n\nA negative assertion.\n\n```pycon\n>>> import conjecture\n>>> assert 5 != conjecture.has(lambda v: v == 10)\n>>> assert 5 == ~conjecture.has(lambda v: v == 10)\n>>> assert 10 == ~conjecture.has(lambda v: v == 10)\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\nAssertionError\n```\n\n## ⚖️ Licence\n\nThis project is licensed under the [MIT licence](http://dan.mit-license.org/).\n\nAll documentation and images are licenced under the \n[Creative Commons Attribution-ShareAlike 4.0 International License][cc_by_sa].\n\n[cc_by_sa]: https://creativecommons.org/licenses/by-sa/4.0/\n\n## 📝 Meta\n\nThis project uses [Semantic Versioning](http://semver.org/).',
    'author': 'Daniel Knell',
    'author_email': 'contact@danielknell.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/artisanofcode/python-conjecture',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
