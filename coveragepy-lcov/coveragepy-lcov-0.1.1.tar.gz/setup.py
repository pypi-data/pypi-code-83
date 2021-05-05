# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coveragepy_lcov']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'coverage>=5.5,<6.0']

entry_points = \
{'console_scripts': ['coveragepy-lcov = coveragepy_lcov.cli:main']}

setup_kwargs = {
    'name': 'coveragepy-lcov',
    'version': '0.1.1',
    'description': 'A simple .coverage to LCOV converter',
    'long_description': '# coveragepy-lcov\n\nThis package provides a simple CLI for converting .coverage files to the LCOV format.\n\n# Usage\n\n```bash\npip install coveragepy-lcov\n\n# If the .coverage file is in your current working directory\ncoveragepy-lcov\n\n# Point to a different .coverage file path\ncoveragepy-lcov --data_file_path example/.coverage\n\n# Write the output to a different file path\ncoveragepy-lcov --output_file_path build/lcov.info\n\n# Use relative paths in the LCOV output\ncoveragepy-lcov --relative_path\n```\n\n# Configuration\n\n```text\nUsage: coveragepy-lcov [OPTIONS]\n\nOptions:\n  --data_file_path TEXT    Path to .coverage file\n  --output_file_path TEXT  lcov.info output file path\n  --config_file TEXT       Path to .coveragerc file\n  --relative_path          Use relative path in LCOV output\n  --preview                Preview LCOV output\n  --help                   Show this message and exit.\n```\n',
    'author': 'Chay Choong',
    'author_email': 'chaychoong@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chaychoong/coveragepy-lcov',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
