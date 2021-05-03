from pathlib import Path
from urllib import request
from urllib.error import HTTPError

import toml
from pytest import fixture, raises  # type: ignore

from assertion import __version__


@fixture
def pyproject_version(scope="session"):
    t = toml.load((Path(__file__) / "../../pyproject.toml").resolve())
    return t["project"]["version"]


def test_version_consistency(pyproject_version):
    assert __version__ == pyproject_version, "version mismatch"


def test_pypi_collision():
    with raises(HTTPError, match="404"):
        request.urlopen(f"https://pypi.org/project/assertion/{__version__}/")
