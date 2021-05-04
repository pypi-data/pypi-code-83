import shutil
from pathlib import Path

from .configured_notion import Notion


def copy_config_dir_to_package_dir(dir_path: str):
    tgt_dir_path = Path(__path__[0]) / Path("config")
    if tgt_dir_path.exists():
        shutil.rmtree(str(tgt_dir_path))
    shutil.copytree(dir_path, str(tgt_dir_path), dirs_exist_ok=True)
