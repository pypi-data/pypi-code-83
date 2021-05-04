# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['datalakebundle']

package_data = \
{'': ['*'],
 'datalakebundle': ['_config/*',
                    'delta/*',
                    'notebook/*',
                    'notebook/decorator/*',
                    'notebook/decorator/tests/*',
                    'table/*',
                    'table/class_/*',
                    'table/create/*',
                    'table/delete/*',
                    'table/identifier/*',
                    'table/name/*',
                    'table/optimize/*',
                    'table/parameters/*',
                    'table/read/*',
                    'table/upsert/*',
                    'table/write/*',
                    'table/write/tests/*',
                    'test/*']}

install_requires = \
['console-bundle>=0.4.0,<0.5.0',
 'daipe-core>=0.8.0b1,<0.9.0',
 'injecta>=0.10.0,<0.11.0',
 'pyfony-bundles>=0.4.0,<0.5.0',
 'pyspark-bundle>=0.8.0b1,<0.9.0',
 'simpleeval>=0.9.10,<1.0.0']

entry_points = \
{'pyfony.bundle': ['create = datalakebundle.DataLakeBundle:DataLakeBundle']}

setup_kwargs = {
    'name': 'datalake-bundle',
    'version': '0.7.0a4',
    'description': 'DataLake tables management bundle for the Daipe Framework',
    'long_description': '# Datalake bundle\n\nThis bundle allows you to easily create and manage datalake(house) based on the [Daipe Framework](https://www.daipe.ai).  \n\n## Resources\n\n* [Documentation](https://docs.daipe.ai/data-pipelines-workflow/managing-datalake/)\n',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/daipe-ai/datalake-bundle',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
