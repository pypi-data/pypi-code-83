from inspect import cleandoc
from typing import Any, Set


class CollectionsSourcePathError(Exception):
    def __init__(self, collection_source: str) -> None:
        super().__init__(f"Path: {collection_source} does not exist.")


class MissingCollectionsSource(Exception):
    def __init__(self, collection_source: str) -> None:
        super().__init__(f"Module: {collection_source} was not found.")


class MissingMetadata(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Could not find metadata: {path}")


class InvalidMetadata(Exception):
    def __init__(self, path: str) -> None:
        super().__init__(f"Could not parse metadata: {path}")


class MissingCollections(Exception):
    def __init__(self, missing_collections: Set[str]) -> None:
        super().__init__(
            cleandoc(
                f"""
                Specified collections were not found when gathering templates:
                {missing_collections}
                """
            )
        )


class MissingIncludes(Exception):
    def __init__(self, missing_includes: Set[str]) -> None:
        super().__init__(
            cleandoc(
                f"""
                Specified includes were not found when gathering templates:
                {missing_includes}
                """
            )
        )


class MissingRenderContext(Exception):
    def __init__(self, missing_context: Set[str]) -> None:
        super().__init__(f"Missing required variables: {missing_context}")


class MissingRename(Exception):
    def __init__(self, token: str) -> None:
        super().__init__(f"Token: {token} cannot be found in the given render context")


class InvalidRename(Exception):
    def __init__(self, rename_value: str) -> None:
        super().__init__(f"Rename value: {rename_value} is not a non-empty string")


class InvalidDynamicFolder(Exception):
    def __init__(self, obj: Any) -> None:
        super().__init__(
            f"Dynamic folder objects must be dictionaries with a segment field. Received: {obj}"
        )


class InvalidInitialization(Exception):
    def __init__(self, obj: Any) -> None:
        super().__init__(
            f"Initialization objects must be dictionaries with a cmd field. Received: {obj}"
        )
