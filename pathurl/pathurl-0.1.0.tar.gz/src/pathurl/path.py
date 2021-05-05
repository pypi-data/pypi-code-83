from typing import List


class Path:
    __slots__ = ["_path"]

    def __init__(self, path: str = ""):
        self._path = path

    def __str__(self):
        return self._path

    @property
    def is_absolute(self) -> bool:
        return not self._path or self._path.startswith("/")

    @property
    def segments(self) -> List[str]:
        split = self._path.split("/")
        if self.is_absolute:
            return split[1:]
        return split
