"""
Type annotations for textract service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/literals.html)

Usage::

    ```python
    from mypy_boto3_textract.literals import BlockType

    data: BlockType = "CELL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BlockType",
    "ContentClassifier",
    "EntityType",
    "FeatureType",
    "JobStatus",
    "RelationshipType",
    "SelectionStatus",
    "TextType",
)


BlockType = Literal["CELL", "KEY_VALUE_SET", "LINE", "PAGE", "SELECTION_ELEMENT", "TABLE", "WORD"]
ContentClassifier = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
EntityType = Literal["KEY", "VALUE"]
FeatureType = Literal["FORMS", "TABLES"]
JobStatus = Literal["FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"]
RelationshipType = Literal["CHILD", "COMPLEX_FEATURES", "VALUE"]
SelectionStatus = Literal["NOT_SELECTED", "SELECTED"]
TextType = Literal["HANDWRITING", "PRINTED"]
