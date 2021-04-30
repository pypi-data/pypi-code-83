# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kolore']

package_data = \
{'': ['*'], 'kolore': ['resources/krita/*']}

install_requires = \
['Pillow>=8.1.0,<9.0.0', 'PyYAML>=5.4.1,<6.0.0', 'click>=7.1.2,<8.0.0']

entry_points = \
{'console_scripts': ['kolore = kolore.cli:parse']}

setup_kwargs = {
    'name': 'kolore',
    'version': '0.1.13',
    'description': 'Your tiny swiss-army knife for color palettes.',
    'long_description': '<div align="center">\n    <a href="https://pypi.org/project/kolore/" target="_blank" rel="noopener noreferrer">\n        <img width="200" src="https://gitlab.com/AlvarBer/kolore/-/raw/master/radical_180.png" alt="Logo">\n    </a>\n</div>\n\n# Kolore\n\nYour tiny swiss-army knife for color palettes.\n\n![Krita palette](https://gitlab.com/AlvarBer/kolore/-/raw/master/palette_demo.png)\n\n## Install\n\n`pip install kolore`\n\n## Usage\n\nConvert between various palette files, such as krita to unity\n\n`kolore --in palette.colors --out palette.kpl`\n\nTo create a palette png from a krita palette file\n\n`kolore --in palette.kpl --out palette.png`\n\nYou can also set the size of the generated image\n\n`kolore --in palette.colors --out result.png --width 200 --height 100`\n\nGet general help with\n\n`kolore --help`\n\n## Supported formats\n\n### Input\n\n* Krita palette files (`.kpl`)\n* Unity color preset library (`.colors`)\n\n### Output\n\n* Krita palette files (`.kpl`)\n* Unity color preset library (`.colors`)\n* PNG images (`.png`)\n\n## Pitfalls\n\nHDR colors from unity are not supported!\n\nThis is just a prototype, please report any bugs.\n',
    'author': 'AlvarBer',
    'author_email': 'git@alvarber.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/AlvarBer/kolore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
