# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['kanye']
install_requires = \
['requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'kanye',
    'version': '0.1.0',
    'description': 'kanye.rest API quotes',
    'long_description': '# 🐍 Python kanye.rest API bindings\n\n**🙌 Simplest API bindings for kanye.rest**\n\n## Usage\n\n```python\n>>> import kanye\n>>> kanye.quote()\n"My memories are from the future"\n```\n\n\n## Install\n\n```bash\npip install kanye\n```\n',
    'author': 'Ilkhomidin Baxoraliev',
    'author_email': 'itilhomidin@yandex.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ilhomidin/kanye',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
