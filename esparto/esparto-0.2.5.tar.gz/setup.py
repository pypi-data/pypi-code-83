# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['esparto']

package_data = \
{'': ['*'], 'esparto': ['resources/css/*', 'resources/jinja/*']}

install_requires = \
['Pillow<9.0.0', 'Pillow>=7.0.0', 'jinja2>=2.10.1,<3.0.0', 'markdown>=3.1,<4.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses'],
 'extras': ['beautifulsoup4>=4.7', 'weasyprint>=51']}

setup_kwargs = {
    'name': 'esparto',
    'version': '0.2.5',
    'description': 'Simple HTML and PDF document generator for Python.',
    'long_description': 'esparto\n=======\n\n[![image](https://img.shields.io/pypi/v/esparto.svg)](https://pypi.python.org/pypi/esparto)\n[![Build Status](https://travis-ci.com/domvwt/esparto.svg?branch=main)](https://travis-ci.com/domvwt/esparto)\n[![codecov](https://codecov.io/gh/domvwt/esparto/branch/main/graph/badge.svg?token=35J8NZCUYC)](https://codecov.io/gh/domvwt/esparto)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=domvwt_esparto&metric=alert_status)](https://sonarcloud.io/dashboard?id=domvwt_esparto)\n\nEsparto is a simple HTML and PDF document generator for Python. Its primary use is for generating shareable single page reports\nwith content from popular analytics and data science libraries.\n\nFull documentation and examples are available at [domvwt.github.io/esparto/](https://domvwt.github.io/esparto/).\n\n## Overview\nThe library features a streamlined API that defines pages in terms of\nsections, rows, and columns; and an intelligent wrapping system that automatically\nconverts Python objects into content.\n\nWe use the grid system and components from [Bootstrap](https://getbootstrap.com/) to ensure\ndocuments adapt to the viewing device and appear immediately familiar and accessible.\nNo knowledge of Bootstrap or web development is required to use the library, however, as these\ndetails are conveniently abstracted.\n\nAt publishing time, the completed document is passed to [Jinja2](https://palletsprojects.com/p/jinja/)\nand fed into an HTML template with all style details and dependencies captured inline.\n\nEsparto supports content rendering within Jupyter Notebooks, allowing users to interactively\nand iteratively build documents without disrupting their workflow.\n\nPDF conversion is provided by [Weasyprint](https://weasyprint.org/).\n\n### Features\n* Lightweight API\n* No CSS or HTML required\n* Device responsive display\n* Self contained / inline dependencies\n* Jupyter Notebook support\n* Printer friendly formatting\n* PDF output\n* MIT License\n\n### Supported Content\n* Markdown\n* Images\n* Pandas DataFrames\n* Plots from:\n    * Matplotlib\n    * Bokeh\n    * Plotly\n',
    'author': 'Dominic Thorn',
    'author_email': 'dominic.thorn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://domvwt.github.io/esparto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
