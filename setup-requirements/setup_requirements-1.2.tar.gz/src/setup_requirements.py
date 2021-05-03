import os
import shutil
import tempfile
import zipfile
from pathlib import Path

from pkg_resources import parse_requirements
from setuptools import build_meta
from wheel import pkginfo

__all__ = [
    'get_requires_for_build_sdist',
    'get_requires_for_build_wheel',
    'prepare_metadata_for_build_wheel',
    'build_wheel',
    'build_sdist',
]


def zip_overwrite(path, info, contents):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        with zipfile.ZipFile(path) as src:
            with zipfile.ZipFile(tmp.name, 'w') as dst:
                for it in src.infolist():
                    if it.filename != info.filename:
                        buf = src.read(it)
                    else:
                        buf = contents
                    dst.writestr(it, buf)
        shutil.move(tmp.name, path)


class _BuildMetaBackend(build_meta._BuildMetaBackend):
    def build_wheel(self, wheel_directory, config_settings=None, metadata_directory=None):
        requirements_path = Path('requirements.txt')
        if not requirements_path.exists():
            raise ValueError('"requirements.txt" file must be present when using setup_requirements build backend')

        result_basename = super().build_wheel(
            wheel_directory, config_settings=config_settings, metadata_directory=metadata_directory
        )

        wheel_file = Path(wheel_directory) / result_basename

        with zipfile.ZipFile(wheel_file) as zf:
            metas = [f for f in zf.infolist() if os.path.basename(f.filename) == 'METADATA']
            assert len(metas) == 1, 'METADATA file not found in final wheel file'
            meta = metas[0]

            info = pkginfo.read_pkg_info_bytes(zf.read(meta))

            for requirement in parse_requirements(requirements_path.read_text()):
                info['Requires-Dist'] = str(requirement)

            with tempfile.NamedTemporaryFile() as tmp:
                pkginfo.write_pkg_info(tmp.name, info)
                tmp.seek(0)
                new_meta = tmp.read()

        zip_overwrite(wheel_file, meta, new_meta)

        return result_basename


_BACKEND = _BuildMetaBackend()

get_requires_for_build_wheel = _BACKEND.get_requires_for_build_wheel
get_requires_for_build_sdist = _BACKEND.get_requires_for_build_sdist
prepare_metadata_for_build_wheel = _BACKEND.prepare_metadata_for_build_wheel
build_wheel = _BACKEND.build_wheel
build_sdist = _BACKEND.build_sdist
