import os
from dataclasses import dataclass
from functools import reduce
from typing import Any, Dict, List, Type, TypeVar, Union

from templ8.state.exceptions import (InvalidDynamicFolder, InvalidRename,
                                     MissingRename)
from templ8.utils.paths import path_tail, leads_path

T = TypeVar("T", bound="Rename")  # pylint: disable = C0103


@dataclass
class Rename:
    segment: str
    token: str

    @classmethod
    def parse(cls: Type[T], obj: Union[str, Dict[str, str]]) -> T:
        if isinstance(obj, str):
            return cls(segment=obj, token=obj)

        if not isinstance(obj, dict) or "segment" not in obj:
            raise InvalidDynamicFolder(obj)

        return cls(obj["segment"], obj["token"] if "token" in obj else obj["segment"])

    @staticmethod
    def resolve(path: str, renames: List[T], render_context: Dict[str, Any]) -> str:
        return reduce(lambda acc, x: x.apply(acc, render_context), renames, path)

    def lookup(self, render_context: Dict[str, Any]) -> str:
        if self.token not in render_context:
            raise MissingRename(self.token)

        rename_value = render_context[self.token]

        if not isinstance(rename_value, str) or len(rename_value) == 0:
            raise InvalidRename(rename_value)

        return rename_value

    def apply(self, path: str, render_context: Dict[str, Any]) -> str:
        print(self.segment, path, leads_path(self.segment, path))
        return (
            path.replace(
                self.segment,
                os.path.join(path_tail(self.segment), self.lookup(render_context)),
                1,
            )
            if leads_path(self.segment, path)
            else path
        )
