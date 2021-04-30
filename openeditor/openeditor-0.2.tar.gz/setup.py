# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['openeditor']
setup_kwargs = {
    'name': 'openeditor',
    'version': '0.2',
    'description': 'Edit files with your $EDITOR, like git commit does.',
    'long_description': '# `openeditor`\nEdit files with your `$EDITOR`, like git commit does.\n\n## Usage\nInstall with: `pip install openeditor`\n\n```\n# Let user edit file\ns = openeditor.edit_file("path/to/my/file.txt")\nprint("The file now contains:\\n" + s)\n\n# Use a temp file\ns = openeditor.edit_file(\n    "# Please edit this file, save and close editor when done", \n    "path/to/my/file.txt"\n)\nprint("The file now contains:\\n" + s) \n```\n\nThe editor is obtained from, in order of precedence:\n\n* `$VISUAL`\n* `$EDITOR`\n\nIf none of these provide a useful editor, an exception will be thrown.\n',
    'author': 'Azat Akhmetov',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/metov/openeditor',
    'package_dir': package_dir,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
