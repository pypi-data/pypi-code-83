from setuptools.build_meta import (
    build_sdist as orig_build_sdist,
    build_wheel as orig_build_wheel,
)
from literary.commands.build import LiteraryBuildApp
import shutil
import pathlib
import os


def _find_jupyter_path():
    jupyter_path = pathlib.Path(shutil.which("jupyter"))
    return jupyter_path.parent.parent / "share" / "jupyter"


def _patch_jupyter_path():
    paths = os.environ.get('JUPYTER_PATH', '').split(os.path.sep)
    paths = [str(_find_jupyter_path())] + paths
    os.environ['JUPYTER_PATH'] = os.path.sep.join(paths)


def _build_literary():
    _patch_jupyter_path()
    
    LiteraryBuildApp.launch_instance(argv=[])


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    _build_literary()
    return orig_build_wheel(
        wheel_directory,
        config_settings=config_settings,
        metadata_directory=metadata_directory,
    )


def build_sdist(sdist_directory, config_settings=None):
    _build_literary()
    return orig_build_sdist(sdist_directory, config_settings=config_settings)
