import os
from pathlib import Path
from urllib.parse import unquote, urlparse
from typing import Any, Callable, List


def find_file(root: Path, name: str) -> List[Path]:
    """Finds files of the specified name in the specified path (recursive)

    Args:
        root (Path): path to search in
        name (str): name to search for (supports globs)

    Returns:
        List[Path]: list of full paths to matching files
    """
    res = []
    for path in root.rglob(name):
        pr = path.resolve()
        if pr.is_file():
            res.append(pr)
    return res


def last_index_where(l: List[Any], where: Callable[[Any], bool]) -> int:
    idx = -1
    for i, v in enumerate(l):
        if where(v):
            idx = i
    return idx


def uri_to_path(uri: str) -> Path:
    p = urlparse(uri)
    final_path = os.path.abspath(os.path.join(p.netloc, unquote(p.path)))
    return Path(final_path)
