import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Type, TypeVar

from walkmate import get_child_files

from templ8.files.exceptions import FileParsingError
from templ8.files.file import File
from templ8.files.static import Static
from templ8.files.template import Template
from templ8.state.exceptions import (CollectionsSourcePathError,
                                     InvalidMetadata, MissingCollectionsSource,
                                     MissingMetadata)
from templ8.state.initialization import Initialization
from templ8.state.rename import Rename
from templ8.utils.dataclasses import map_to_signature
from templ8.utils.functional import flatmap, refsort
from templ8.utils.paths import (full_listdir, get_module_path, is_path_head,
                                path_ext, path_head, path_name)

T = TypeVar("T", bound="Collection")  # pylint: disable = C0103


@dataclass
class Collection:
    path: str

    default_variables: Dict[str, Any] = field(default_factory=dict)
    default_protected: List[str] = field(default_factory=list)

    dynamic_folders: List[Rename] = field(default_factory=list)
    initialization: List[Initialization] = field(default_factory=list)

    @classmethod
    def gather(
        cls: Type[T],
        collection_sources: List[str] = field(default_factory=list),
        collections: List[str] = field(default_factory=list),
    ) -> List[T]:
        return sorted(
            map(
                cls.parse,
                filter(
                    lambda x: os.path.isdir(x)
                    and cls.has_metadata(x)
                    and path_head(x) in collections,
                    flatmap(
                        cls.discover_collections,
                        map(cls.resolve_collection_source, collection_sources),
                    ),
                ),
            ),
            key=refsort(collections, "name"),
        )

    @classmethod
    def parse(cls: Type[T], path: str) -> T:
        try:
            metadata = map_to_signature(cls, cls.parse_metadata(path))

            # Evaluate Rename and Initialization objects early so that their
            # properties can be printed by the reporter.
            return cls(
                path,
                metadata["default_variables"],
                metadata["default_protected"],
                list(map(Rename.parse, metadata["dynamic_folders"])),
                list(map(Initialization.parse, metadata["initialization"])),
            )

        except FileParsingError as err:
            raise InvalidMetadata(path) from err

    @staticmethod
    def discover_collections(
        collection_source: str,
    ) -> List[str]:
        return [
            os.path.join(collection_source, subdir)
            for subdir in os.listdir(collection_source)
        ]

    @staticmethod
    def resolve_collection_source(path: str) -> str:
        if is_path_head(path):
            try:
                return get_module_path(path)
            except ModuleNotFoundError as err:
                raise MissingCollectionsSource(path) from err

        if os.path.exists(path):
            return path

        raise CollectionsSourcePathError(path)

    @staticmethod
    def has_metadata(path: str) -> bool:
        return any(path_name(i) == "metadata" for i in os.listdir(path))

    @staticmethod
    def parse_metadata(path: str) -> Dict[str, Any]:
        try:
            return File.agnostic_parse(
                next(
                    filter(
                        lambda x: path_name(x) == "metadata",
                        full_listdir(path),
                    )
                )
            )
        except StopIteration as err:
            raise MissingMetadata(path) from err

    @property
    def name(self) -> str:
        return path_head(self.path)

    @property
    def file_paths(self) -> List[str]:
        return [os.path.relpath(file, self.path) for file in get_child_files(self.path)]

    @property
    def templates(self) -> List[Template]:
        return [
            Template(self.path, path)
            for path in self.file_paths
            if Template.is_template(path)
        ]

    @property
    def static_files(self) -> List[Static]:
        return [
            Static(self.path, path)
            for path in self.file_paths
            if path_ext(path) != ".j2" and path != "metadata.json"
        ]
