"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AnalyzeDocumentResponseTypeDef

    data: AnalyzeDocumentResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from mypy_boto3_textract.literals import (
    BlockType,
    ContentClassifier,
    EntityType,
    JobStatus,
    RelationshipType,
    SelectionStatus,
    TextType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnalyzeDocumentResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadata",
    "S3ObjectTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "WarningTypeDef",
)


class AnalyzeDocumentResponseTypeDef(TypedDict, total=False):
    DocumentMetadata: "DocumentMetadataTypeDef"
    Blocks: List["BlockTypeDef"]
    HumanLoopActivationOutput: "HumanLoopActivationOutputTypeDef"
    AnalyzeDocumentModelVersion: str


BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": BlockType,
        "Confidence": float,
        "Text": str,
        "TextType": TextType,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": "GeometryTypeDef",
        "Id": str,
        "Relationships": List["RelationshipTypeDef"],
        "EntityTypes": List[EntityType],
        "SelectionStatus": SelectionStatus,
        "Page": int,
    },
    total=False,
)


class BoundingBoxTypeDef(TypedDict, total=False):
    Width: float
    Height: float
    Left: float
    Top: float


class DetectDocumentTextResponseTypeDef(TypedDict, total=False):
    DocumentMetadata: "DocumentMetadataTypeDef"
    Blocks: List["BlockTypeDef"]
    DetectDocumentTextModelVersion: str


class DocumentLocationTypeDef(TypedDict, total=False):
    S3Object: "S3ObjectTypeDef"


class DocumentMetadataTypeDef(TypedDict, total=False):
    Pages: int


class DocumentTypeDef(TypedDict, total=False):
    Bytes: Union[bytes, IO[bytes]]
    S3Object: "S3ObjectTypeDef"


class GeometryTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    Polygon: List["PointTypeDef"]


class GetDocumentAnalysisResponseTypeDef(TypedDict, total=False):
    DocumentMetadata: "DocumentMetadataTypeDef"
    JobStatus: JobStatus
    NextToken: str
    Blocks: List["BlockTypeDef"]
    Warnings: List["WarningTypeDef"]
    StatusMessage: str
    AnalyzeDocumentModelVersion: str


class GetDocumentTextDetectionResponseTypeDef(TypedDict, total=False):
    DocumentMetadata: "DocumentMetadataTypeDef"
    JobStatus: JobStatus
    NextToken: str
    Blocks: List["BlockTypeDef"]
    Warnings: List["WarningTypeDef"]
    StatusMessage: str
    DetectDocumentTextModelVersion: str


class HumanLoopActivationOutputTypeDef(TypedDict):
    HumanLoopArn: str
    HumanLoopActivationReasons: List[str]
    HumanLoopActivationConditionsEvaluationResults: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredHumanLoopConfigTypeDef(TypedDict):
    HumanLoopName: str
    FlowDefinitionArn: str


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, total=False):
    DataAttributes: "HumanLoopDataAttributesTypeDef"


class HumanLoopDataAttributesTypeDef(TypedDict, total=False):
    ContentClassifiers: List[ContentClassifier]


class NotificationChannelTypeDef(TypedDict):
    SNSTopicArn: str
    RoleArn: str


class _RequiredOutputConfigTypeDef(TypedDict):
    S3Bucket: str


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, total=False):
    S3Prefix: str


class PointTypeDef(TypedDict, total=False):
    X: float
    Y: float


RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef", {"Type": RelationshipType, "Ids": List[str]}, total=False
)


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3ObjectTypeDef(TypedDict, total=False):
    Bucket: str
    Name: str
    Version: str


class StartDocumentAnalysisResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartDocumentTextDetectionResponseTypeDef(TypedDict, total=False):
    JobId: str


class WarningTypeDef(TypedDict, total=False):
    ErrorCode: str
    Pages: List[int]
