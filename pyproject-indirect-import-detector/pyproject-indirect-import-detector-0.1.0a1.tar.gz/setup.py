# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyproject_indirect_import_detector']

package_data = \
{'': ['*']}

install_requires = \
['result>=0.6.0,<0.7.0',
 'setuptools>=56.0.0,<57.0.0',
 'stdlib-list>=0.8.0,<0.9.0',
 'termcolor>=1.1.0,<2.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['pyproject-indirect-import-detector = '
                     'pyproject_indirect_import_detector.main:_main']}

setup_kwargs = {
    'name': 'pyproject-indirect-import-detector',
    'version': '0.1.0a1',
    'description': 'CI tool to detect indirect import',
    'long_description': '# `pyproject-indirect-import-detector`: Indirect import detector\n\n[![PyPI](https://img.shields.io/pypi/v/pyproject-indirect-import-detector.svg)](https://pypi.org/project/pyproject-indirect-import-detector)\n[![Project License](https://img.shields.io/pypi/l/pyproject-indirect-import-detector.svg)](https://pypi.org/project/pyproject-indirect-import-detector)\n[![Supported Python versions](https://img.shields.io/badge/python-3.9-1081c2.svg)](https://pypi.org/project/nitpick/)\n[![CircleCI](https://circleci.com/gh/kenoss/pyproject-indirect-import-detector.svg?style=svg)](https://app.circleci.com/pipelines/github/kenoss/pyproject-indirect-import-detector)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Motivation\n\nIndirect import is bad.\n\n- The biggest reason is requirements are not protected by [semantic versioning](https://semver.org/).\n- Virtual environment is not strictly synced with `pyproject.toml` nor `poetry.lock` by `poetry`, so far.  It is possible that you delete a dependency but it still remains in the virtual environment.  This means, tests can accidentally pass.\n- FYI, indirect import is not allowed in rust/cargo.\n\n## Limitation\n\nCurrently, this tool only suuport `pyproject.toml` using `poetry`.\n[PEP 631](https://www.python.org/dev/peps/pep-0631/) support is planed if python community agree this motivation and use this tool.\n\n## How to use\n\n### Install\n\n```\npoetry add --dev pyproject-indirect-import-detector\n```\n\nNote that this tool is intended to use in the virtual environment created by `poetry install`.  See also: [Why only works in venv?](#why-only-works-in-venv)\n\n### Usage\n\n```\npoetry run pyproject-indirect-import-detector -v\n```\n\nSee also [CI config](.circleci/config.yml), especially the job `check-indirect-import`.\n\n### Configuration\n\nYou can configure by `pyproject.toml` as the following:\n\n```\n[tool.pyproject-indirect-import-detector]\nexclude_modules = [\n    "dataclasses",           # If you use compat trick like https://github.com/PyCQA/isort/blob/5.8.0/isort/_future/__init__.py#L3-L7 .\n    "tests",                 # If your test suite make `tests` module importable and use it like https://github.com/andreoliwa/nitpick/blob/v0.26.0/tests/test_json.py#L6 .\n    "dummy_module_for_test", # If you use dummy modules in tests like https://github.com/PyCQA/isort/blob/5.8.0/tests/unit/example_crlf_file.py#L1-L2 .\n]\n```\n\n## FAQ\n\n### It failes with not reasonable errors.\n\nReport an issue and let me know your case.\nThe core logic is not yet well-tested with real packages.\nWe need edge cases.\n\n### Why only works in venv?\n\nThis tool makes a correspondence from [package names to module names](src/pyproject_indirect_import_detector/domain.py).\nThis use [`importlib`](https://docs.python.org/3/library/importlib.html) and requires an environment that has all packages installed.\nThis tool is designed to be used in CI.  So, runnable under `poetry run` is enough.\n\n### Why installable with `python >= 3.6` and runnable only in `python >= 3.9`?\n\nSee the comment in [pyproject.toml](./pyproject.toml).\nI tried to make it runnable in old pythons, but the cost is high.\nThis tool is designed to be used in CI.  So, this restriction is reasonable.\n\n## How to develop\n\n### How to release\n\n1. Bump version, PR and merge.\n2. `git tag <version>` then `git push origin <version>`.\n3. CI will pubish the package to PyPI: https://pypi.org/project/pyproject-indirect-import-detector/\n',
    'author': 'keno',
    'author_email': 'keno.ss57@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kenoss/pyproject-indirect-import-detector',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
