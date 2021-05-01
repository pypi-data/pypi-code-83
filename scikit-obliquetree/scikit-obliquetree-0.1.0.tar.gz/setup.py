# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scikit_obliquetree']

package_data = \
{'': ['*']}

install_requires = \
['rich>=9.8.2,<10.0.0', 'typer[all]>=0.3.2,<0.4.0']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1.6.0,<2.0.0']}

entry_points = \
{'console_scripts': ['scikit-obliquetree = scikit_obliquetree.__main__:app']}

setup_kwargs = {
    'name': 'scikit-obliquetree',
    'version': '0.1.0',
    'description': 'Oblique Decision Tree in Python',
    'long_description': '# scikit-obliquetree\n\n<div align="center">\n\n[![Build status](https://github.com/zhenlingcn/scikit-obliquetree/workflows/build/badge.svg?branch=master&event=push)](https://github.com/zhenlingcn/scikit-obliquetree/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/scikit-obliquetree.svg)](https://pypi.org/project/scikit-obliquetree/)\n[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/zhenlingcn/scikit-obliquetree/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/zhenlingcn/scikit-obliquetree/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/zhenlingcn/scikit-obliquetree/releases)\n[![License](https://img.shields.io/github/license/zhenlingcn/scikit-obliquetree)](https://github.com/zhenlingcn/scikit-obliquetree/blob/master/LICENSE)\n\nOblique Decision Tree in Python\n\n</div>\n\n## Introduction\n\nThe oblique decision tree is a popular choice in the machine learning domain for improving the performance of traditional decision tree algorithms. In contrast to the traditional decision tree, which uses an axis-parallel split point to determine whether a data point should be assigned to the left or right branch of a decision tree, the oblique decision tree uses a hyper-plane based on all data point features. \n\nNumerous works in the machine learning domain have shown that oblique decision trees can achieve exceptional performance in a wide range of domains. However, there is still a lack of a package that has implemented oblique decision tree algorithms, which stymies the development of this domain. As a result, the goal of this project is to solve this problem by implementing some well-known algorithms in this domain. We hope that by doing so, these algorithms will serve as a baseline for machine learning practitioners to compare newly designed algorithms to existing algorithms.\n\n\n## 🚀 Features\n* A simple scikit-learn interface for oblique decision tree algorithms\n* A general gradient boosting estimator that can be used to improve arbitrary base estimators\n\n## Installation\n\n```bash\npip install -U scikit-obliquetree\n```\n\nor install with `Poetry`\n\n```bash\npoetry add scikit-obliquetree\n```\n\nThen you can run\n\n```bash\nscikit-obliquetree --help\n```\n\n```bash\nscikit-obliquetree --name Roman\n```\n\nor if installed with `Poetry`:\n\n```bash\npoetry run scikit-obliquetree --help\n```\n\n```bash\npoetry run scikit-obliquetree --name Roman\n```\n\n## Example\nExample of usage:\n```python\nfrom sklearn.datasets import load_boston\nfrom sklearn.ensemble import BaggingRegressor\nfrom sklearn.model_selection import cross_val_score\n\nfrom scikit_obliquetree.HHCART import HouseHolderCART\nfrom scikit_obliquetree.segmentor import MSE, MeanSegmentor\n\nX, y = load_boston(return_X_y=True)\nreg = BaggingRegressor(\n    HouseHolderCART(MSE(), MeanSegmentor(), max_depth=3),\n    n_estimators=100,\n    n_jobs=-1,\n)\nprint(\'CV Score\', cross_val_score(reg, X, y))\n```\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/zhenlingcn/scikit-obliquetree)](https://github.com/zhenlingcn/scikit-obliquetree/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `Apache Software License 2.0` license. See [LICENSE](https://github.com/zhenlingcn/scikit-obliquetree/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```\n@misc{scikit-obliquetree,\n  author = {ECNU},\n  title = {Oblique Decision Tree in Python},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/zhenlingcn/scikit-obliquetree}}\n}\n```\n\n## Credits\n\nThis project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template).\n',
    'author': 'ECNU',
    'author_email': 'zhenlingcn@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/zhenlingcn/scikit-obliquetree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
