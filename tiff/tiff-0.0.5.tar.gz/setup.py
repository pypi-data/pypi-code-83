# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tiff']

package_data = \
{'': ['*']}

install_requires = \
['geopy', 'numpy', 'pillow', 'pyproj', 'rasterio']

setup_kwargs = {
    'name': 'tiff',
    'version': '0.0.5',
    'description': 'GeoTiff utils package',
    'long_description': None,
    'author': 'Moleque',
    'author_email': 'molecada@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
