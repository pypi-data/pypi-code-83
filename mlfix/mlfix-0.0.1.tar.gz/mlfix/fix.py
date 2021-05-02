from pathlib import Path
import yaml
from typing import Dict, Any
from mlfix.path_utils import (
    find_file,
    last_index_where,
    uri_to_path,
)

FILENAMES = ["meta.yaml"]
KEYS_TO_FIX = ["artifact_location", "artifact_uri"]


def _fix_path_in_uri(uri: str, mlruns_name: str, new_path_to_store: Path) -> str:
    """
    returns fixed uri
    """
    path = uri_to_path(uri)
    path_parts = list(path.parts)
    im = last_index_where(path_parts, lambda x: x == mlruns_name)
    assert im >= 0
    # create new path
    new_path = new_path_to_store.resolve().absolute().joinpath(*path_parts[im + 1 :])
    # to uri
    return new_path.as_uri()


def fix_meta(path_to_store: Path, mlruns_name: str) -> bool:
    """
    path_to_store - path to artifact store to fix
    mlruns_name - name of the former mlruns folder (the one present in yaml files)
    returns True if any of the files was changed
    """
    assert (
        path_to_store.exists() and path_to_store.is_dir()
    ), f"path_to_store: {path_to_store.resolve()} must be a real folder"
    # find files
    files_to_fix = []
    for fn in FILENAMES:
        files_to_fix.extend(find_file(path_to_store, fn))

    # read each file, replace found key with fixed path and overwrite file
    changed = False
    for fp in files_to_fix:
        with open(fp, "r+") as f:
            contents: Dict[str, Any] = yaml.full_load(f)
            changed = False
            for k in KEYS_TO_FIX:
                if k in contents:
                    contents[k] = _fix_path_in_uri(
                        contents[k], mlruns_name, path_to_store
                    )
                    changed = True
            if changed:
                # save new version of this file
                f.seek(0)
                yaml.dump(contents, f)
    return changed
