import tempfile
from pathlib import Path

import pytest

PYPROJECT_TOML = """
[build-system]
requires = ['setuptools>=42', 'wheel']
build-backend = "setup_requirements"
"""

SETUP_CFG = """
[metadata]
name = fooproject
author = me

[options]
install_requires = flask
"""


@pytest.fixture
def requirements():
    return ['pytest', 'django==3.2']


@pytest.fixture
def project(requirements):
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / 'pyproject.toml').write_text(PYPROJECT_TOML)
        (tmp / 'setup.cfg').write_text(SETUP_CFG)

        req_text = '# comment\n'
        req_text += '\n'.join(requirements)
        (tmp / 'requirements.txt').write_text(req_text)

        yield tmp
