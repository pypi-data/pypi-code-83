# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rrshare',
 'rrshare.RQSetting',
 'rrshare.rqFactor',
 'rrshare.rqFetch',
 'rrshare.rqSU',
 'rrshare.rqUpdate',
 'rrshare.rqUtil',
 'rrshare.rqWeb',
 'rrshare.sql']

package_data = \
{'': ['*'], 'rrshare': ['templates/*'], 'rrshare.rqWeb': ['templates/*']}

install_requires = \
['Flask>=1.1.2,<2.0.0',
 'click>=7.1.2,<8.0.0',
 'dash>=1.20.0,<2.0.0',
 'easyquotation>=0.7.4,<0.8.0',
 'jqdatasdk>=1.8.9,<2.0.0',
 'motor>=2.4.0,<3.0.0',
 'psycopg2-binary>=2.8.6,<3.0.0',
 'psycopg2>=2.8.6,<3.0.0',
 'pyecharts>=1.9.0,<2.0.0',
 'streamlit>=0.80.0,<0.81.0',
 'tushare>=1.2.62,<2.0.0',
 'zenlog>=1.1,<2.0']

entry_points = \
{'console_scripts': ['record-data = rrshare.record_all_data:main',
                     'rrshare = rrshare.cli:main']}

setup_kwargs = {
    'name': 'rrshare',
    'version': '2.4.30',
    'description': 'stock data & anlysis',
    'long_description': None,
    'author': 'rome',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
