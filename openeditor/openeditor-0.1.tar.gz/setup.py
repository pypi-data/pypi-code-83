# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['openeditor']
setup_kwargs = {
    'name': 'openeditor',
    'version': '0.1',
    'description': 'Edit files with your $EDITOR, like git commit does.',
    'long_description': '# `openeditor`\nEdit files with your `$EDITOR`, like git commit does.\n\n## Usage\n```\n# Let user edit file\ns = openeditor.edit_file("path/to/my/file.txt")\nprint("The file now contains:\\n" + s)\n\n# Use a temp file\ns = openeditor.edit_file("path/to/my/file.txt")\nprint("The file now contains:\\n" + s) \n```\n\n`openeditor.edit_file("path/to/my/file.txt")` to let user edit `path/to/my/file.txt` in the configured editor and return ',
    'author': 'Azat Akhmetov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/metov/openeditor',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
