import os
from dataclasses import dataclass
from typing import Any, Dict, List, Set, TypeVar

from backports.cached_property import cached_property

from templ8.state.collection import Collection
from templ8.state.exceptions import (MissingCollections, MissingIncludes,
                                     MissingRenderContext)
from templ8.state.rename import Rename
from templ8.user.inputs import Inputs
from templ8.utils.dicts import deep_merge_dicts, merge_dicts
from templ8.utils.paths import abs_from_root, path_head
from templ8.utils.time import timestamp

T = TypeVar("T", bound="Loader")  # pylint: disable = C0103


@dataclass
class Loader:
    inputs: Inputs

    @property
    def collection_sources(self) -> List[str]:
        return [
            *self.inputs.collection_sources,
            os.path.normpath(os.path.join(__file__, "..", "..", "core")),
        ]

    @cached_property
    def collections(self) -> List[Collection]:
        return Collection.gather(
            self.collection_sources,
            self.inputs.collections,
        )

    @cached_property
    def render_context(self) -> Dict[str, Any]:
        return merge_dicts(
            timestamp(),
            *map(lambda x: x.default_variables, self.collections),
            self.inputs.render_context,
        )

    @property
    def loader_paths(self) -> List[str]:
        return self.inputs.loader_paths

    @property
    def output_dir(self) -> str:
        return abs_from_root(self.inputs.input_file, self.inputs.output_dir)

    # TODO Includes are unable to specify which collections' dynamic folders to use.
    @property
    def includes(self) -> List[str]:
        dynamic_folders = [
            dynamic_folder
            for collection in self.collections
            for dynamic_folder in collection.dynamic_folders
        ]
        return [
            Rename.resolve(
                path,
                dynamic_folders,
                self.render_context,
            )
            for path in self.inputs.includes
        ]

    @property
    def protected(self) -> List[str]:
        return [
            path_head(self.inputs.input_file),
            *self.inputs.protected,
            *[
                Rename.resolve(
                    path,
                    collection.dynamic_folders,
                    self.render_context,
                )
                for collection in self.collections
                for path in collection.default_protected
            ],
        ]

    @property
    def schema(self) -> Dict[str, Any]:
        return deep_merge_dicts(
            *[
                template.schema
                for collection in self.collections
                for template in collection.templates
            ]
        )

    @property
    def collection_names(self) -> List[str]:
        return [i.name for i in self.collections]

    @property
    def file_paths(self) -> List[str]:
        return [
            file.resolve(collection.dynamic_folders, self.render_context)
            for collection in self.collections
            for file in [*collection.static_files, *collection.templates]
        ]

    @property
    def missing_collections(self) -> Set[str]:
        return set(self.inputs.collections) - set(self.collection_names)

    @property
    def missing_includes(self) -> Set[str]:
        return set(self.inputs.includes) - set(self.file_paths)

    @property
    def missing_context(self) -> Set[str]:
        required_context = self.schema["required"] if "required" in self.schema else []
        rename_tokens = [
            rename.token
            for collection in self.collections
            for rename in collection.dynamic_folders
        ]
        return (set(required_context) | set(rename_tokens)) - set(self.render_context)

    def introspect(self) -> None:
        if self.missing_collections:
            raise MissingCollections(self.missing_collections)

        if self.missing_context:
            raise MissingRenderContext(self.missing_context)

        if self.missing_includes:
            raise MissingIncludes(self.missing_includes)
