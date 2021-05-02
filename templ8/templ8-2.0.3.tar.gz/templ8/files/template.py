import os
import re
from dataclasses import dataclass
from functools import reduce
from typing import Any, Dict, List

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from jinja2schema import infer, to_json_schema

from templ8.files.file import File
from templ8.state.rename import Rename
from templ8.utils.dicts import merge_dicts
from templ8.utils.lifecycle import lifecycle_stage
from templ8.utils.paths import path_ext, path_head, path_tail
from templ8.utils.strings import handle, kebab_to_snake, quote


@dataclass
class Template(File):
    custom_filters = {
        "kebab_to_snake": kebab_to_snake,
        "pad_in": lambda x, n: "".join([" "] * n) + x,
        "to_handle": handle,
        "to_lifecycle_stage": lifecycle_stage,
        "to_quote": quote,
        "without_ends": lambda x: x[1:-1],
        "without_first": lambda x: x[1:],
        "without_last": lambda x: x[:-1],
    }

    @staticmethod
    def is_template(path: str) -> bool:
        return path_ext(path) == ".j2"

    @property
    def schema(self) -> Dict[str, Any]:
        custom_tokens = [
            r"{% include .* %}",
            *[rf"(\| ?)?{i}(\(.*\))?" for i in self.custom_filters],
        ]

        with open(self.source_path, "r") as stream:
            return to_json_schema(
                infer(
                    reduce(
                        lambda acc, x: re.sub(x, "", acc),
                        custom_tokens,
                        stream.read(),
                    )
                )
            )

    def resolve(self, renames: List[Rename], render_context: Dict[str, Any]) -> str:
        return Rename.resolve(self.path[:-3], renames, render_context)

    def parse(
        self,
        render_context: Dict[str, Any],
        loader_paths: List[str],
    ) -> str:
        loader_paths = [os.getcwd(), *loader_paths, path_tail(self.source_path)]

        env = Environment(
            loader=FileSystemLoader(loader_paths),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined,
        )

        env.filters = merge_dicts(env.filters, self.custom_filters)
        return env.get_template(path_head(self.source_path)).render(**render_context)
