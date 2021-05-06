# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfinra', 'pyfinra.financials', 'pyfinra.tools']

package_data = \
{'': ['*']}

install_requires = \
['finsymbols>=1.3.0,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'selenium>=3.141.0,<4.0.0']

setup_kwargs = {
    'name': 'pyfinra',
    'version': '0.1.8',
    'description': 'Unoffical Python Finra Wrapper',
    'long_description': '# Unoffical Python Finra Wrapper\n\n**warning this repository is still in alpha stage**\n\n## Requirements\n\n- Chromium\n- Chromedriver\n\n## Installation\n\n### PIP\n\n```Bash\npip install pyfinra\n```\n\n### Build your self with Python-Poetry\n\n```Bash\npoetry install\npoetry build\n```\n\n## Example\n\n```Python\nfrom pyfinra import Ticker\n\n\ngme = Ticker("Gme")\nprint(gme.quote())\nprint(gme.financials_balancesheet())\nprint(gme.financials_inc_statement())\nprint(gme.financials_cash_flow())\nprint(gme.financials_balancesheet(True))\nprint(gme.financials_inc_statement(True))\nprint(gme.financials_cash_flow(True))\n\n```\n\n## Testing\n\nNot implemented Yet!\n\n```Bash\npetry run pytest\n```\n',
    'author': 'Sören Michaels',
    'author_email': 'soeren.michaels@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BluhbergTerminal/PyFinra/tree/alpha',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
