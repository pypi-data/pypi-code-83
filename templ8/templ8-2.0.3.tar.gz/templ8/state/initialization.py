import os
from dataclasses import dataclass
from typing import Any, Dict, List, Type, TypeVar, Union

from simple_pipes import pipe_call

from templ8.state.exceptions import InvalidInitialization
from templ8.state.rename import Rename

T = TypeVar("T", bound="Initialization")  # pylint: disable = C0103


@dataclass
class Initialization:
    cmd: str
    cwd: str

    @classmethod
    def parse(cls: Type[T], obj: Union[str, Dict[str, str]]) -> T:
        if isinstance(obj, str):
            return cls(cmd=obj, cwd=".")

        if not isinstance(obj, dict) or "cmd" not in obj:
            raise InvalidInitialization(obj)

        return cls(obj["cmd"], obj["cwd"] if "cwd" in obj else ".")

    def run(
        self, output_dir: str, renames: List[Rename], render_context: Dict[str, Any]
    ) -> None:
        pipe_call(
            self.cmd.split(" "),
            cwd=os.path.join(
                output_dir, Rename.resolve(self.cwd, renames, render_context)
            ),
        )
