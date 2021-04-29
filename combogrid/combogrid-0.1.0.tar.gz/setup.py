# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['combogrid']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.1,<4.0.0', 'pandas>=1.2.4,<2.0.0']

setup_kwargs = {
    'name': 'combogrid',
    'version': '0.1.0',
    'description': 'Draw a grid of combo charts (each with a line and bars)',
    'long_description': '# combogrid\n\n**combogrid** makes it easier to draw combo charts in a grid, using matplotlib\n\nCombo charts are useful for comparing two different \'y\' variables.\nGrids of charts (aka \'facet grids\') are useful for comparing data\nbetween groups.\n\nPerhaps you want to see how a single stock\'s price and volume changed day by day.\nAnd you are following multiple stocks, so you want one chart per stock.\n\n## Requirements\n* python 3.71 or above\n* pandas\n\n## Install\n```bash\npip install combogrid\n```\n\n## Help\n```python\nimport combogrid\nhelp(combogrid.plot)\n```\n\n\n## Use\n```python\nimport pandas as pd\nimport combogrid\ndf = pd.read_csv("sample.csv")\ndf["date"] = pd.to_datetime(df["date"])\nplt = combogrid.plot(df, "date", "volume", "price", "color")\nplt.show()\n```\n\n## Output\n![Sample image with a grid of combo charts](https://raw.githubusercontent.com/rahimnathwani/combogrid/main/sample.png)\n',
    'author': 'Rahim Nathwani',
    'author_email': 'rahim@encona.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rahimnathwani/combogrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
