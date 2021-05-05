# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smqtk_image_io',
 'smqtk_image_io.impls',
 'smqtk_image_io.impls.image_reader',
 'smqtk_image_io.interfaces',
 'smqtk_image_io.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.5,<2.0.0',
 'pillow>=8.2.0,<9.0.0',
 'setuptools>=53',
 'smqtk-core>=0.16.0,<0.17.0',
 'smqtk-dataprovider>=0.15.0,<0.16.0']

setup_kwargs = {
    'name': 'smqtk-image-io',
    'version': '0.15.0',
    'description': 'SMQTK Image IO',
    'long_description': '# SMQTK - Image-IO\n\n## Intent\nThis package is intended to provide the interfaces and tools for working with image input.\n\nSpecifically, there are two readers used to interact with images. One uses GDAL and the other uses PIL\n\n## Documentation\n\nYou can build the sphinx documentation locally for the most\nup-to-date reference (see also: [Building the Documentation](\nhttps://smqtk.readthedocs.io/en/latest/installation.html#building-the-documentation)):\n```bash\n# Install dependencies\npoetry install\n# Navigate to the documentation root.\ncd docs\n# Build the docs.\npoetry run make html\n# Open in your favorite browser!\nfirefox _build/html/index.html\n```\n',
    'author': 'Kitware, Inc.',
    'author_email': 'smqtk-developers@kitware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
