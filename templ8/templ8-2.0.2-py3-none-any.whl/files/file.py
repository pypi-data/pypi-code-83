import json
import os
from dataclasses import dataclass
from typing import Any, Dict, List

import yaml

from templ8.files.exceptions import FileParsingError, UnsupportedFormat
from templ8.state.rename import Rename
from templ8.utils.paths import path_ext


@dataclass
class File:
    root: str
    path: str

    @staticmethod
    def agnostic_parse(path: str) -> Dict[str, Any]:
        with open(path, "r") as stream:
            try:
                if path_ext(path) == ".json":
                    return json.load(stream)

                if path_ext(path) in [".yml", ".yaml"]:
                    return yaml.safe_load(stream)

            except (
                json.decoder.JSONDecodeError,
                yaml.scanner.ScannerError,
            ) as err:
                raise FileParsingError(path) from err

            raise UnsupportedFormat(path_ext(path))

    @property
    def source_path(self) -> str:
        return os.path.join(self.root, self.path)

    def resolve(self, renames: List[Rename], render_context: Dict[str, Any]) -> str:
        return Rename.resolve(self.path, renames, render_context)

    def output_path(
        self, output_dir: str, renames: List[Rename], render_context: Dict[str, Any]
    ) -> str:
        return os.path.join(output_dir, self.resolve(renames, render_context))
