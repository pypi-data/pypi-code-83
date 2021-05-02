from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

from templ8.files.file import File
from templ8.user.exceptions import MissingOutputDir
from templ8.utils.dataclasses import map_to_signature
from templ8.utils.dicts import collapse_dict
from templ8.utils.paths import abs_from_root

T = TypeVar("T", bound="Inputs")  # pylint: disable = C0103


@dataclass
class Inputs:
    input_file: str
    output_dir: str

    clear_top_level: bool = False
    logical_grouping: bool = False

    collection_sources: List[str] = field(default_factory=list)
    collections: List[str] = field(default_factory=list)

    includes: List[str] = field(default_factory=list)
    protected: List[str] = field(default_factory=list)

    render_context: Dict[str, Any] = field(default_factory=dict)
    loader_paths: List[str] = field(default_factory=list)

    @classmethod
    def from_file(cls: Type[T], input_file: str) -> T:
        input_config = map_to_signature(cls, File.agnostic_parse(input_file))

        if "output_dir" not in input_config:
            raise MissingOutputDir()

        if input_config["logical_grouping"]:
            input_config["render_context"] = collapse_dict(
                input_config["render_context"]
            )

        input_config["loader_paths"] = [
            abs_from_root(input_file, i) for i in input_config["loader_paths"]
        ]

        return cls(input_file=input_file, **input_config)
