import os
import subprocess
import zipfile

from wheel import pkginfo


def _get_wheel_metadata(project):
    files = list(project.glob('*.whl'))
    assert len(files) == 1
    wheel = files[0]

    with zipfile.ZipFile(wheel) as zf:
        metas = [f for f in zf.namelist() if os.path.basename(f) == 'METADATA']
        assert len(metas) == 1
        meta = metas[0]
        return zf.read(meta)


def test_success(project, requirements):
    subprocess.check_call(['pip', 'wheel', '--no-build-isolation', '--no-deps', '.'], cwd=project)
    meta = _get_wheel_metadata(project)
    info = pkginfo.read_pkg_info_bytes(meta)
    assert info.get_all('Requires-Dist') == ['flask'] + requirements


def test_requirements_file_needed(project):
    (project / 'requirements.txt').unlink()
    cmd = subprocess.run(
        ['pip', 'wheel', '--no-build-isolation', '--no-deps', '.'], cwd=project, capture_output=True, text=True
    )
    assert cmd.returncode != 0
    assert (
        """ValueError: "requirements.txt" file must be present when using setup_requirements build backend"""
        in cmd.stderr
    )
