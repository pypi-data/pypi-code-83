"""
Type annotations for dynamodbstreams service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_dynamodbstreams.literals import KeyType, OperationType, StreamStatus, StreamViewType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "ListStreamsOutputTypeDef",
    "RecordTypeDef",
    "ResponseMetadata",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "StreamRecordTypeDef",
    "StreamTypeDef",
)


class AttributeValueTypeDef(TypedDict, total=False):
    S: str
    N: str
    B: Union[bytes, IO[bytes]]
    SS: List[str]
    NS: List[str]
    BS: List[Union[bytes, IO[bytes]]]
    M: Dict[str, Dict[str, Any]]
    L: List[Dict[str, Any]]
    NULL: bool
    BOOL: bool


class DescribeStreamOutputTypeDef(TypedDict):
    StreamDescription: "StreamDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetRecordsOutputTypeDef(TypedDict):
    Records: List["RecordTypeDef"]
    NextShardIterator: str
    ResponseMetadata: "ResponseMetadata"


class GetShardIteratorOutputTypeDef(TypedDict):
    ShardIterator: str
    ResponseMetadata: "ResponseMetadata"


IdentityTypeDef = TypedDict("IdentityTypeDef", {"PrincipalId": str, "Type": str}, total=False)


class KeySchemaElementTypeDef(TypedDict):
    AttributeName: str
    KeyType: KeyType


class ListStreamsOutputTypeDef(TypedDict):
    Streams: List["StreamTypeDef"]
    LastEvaluatedStreamArn: str
    ResponseMetadata: "ResponseMetadata"


class RecordTypeDef(TypedDict, total=False):
    eventID: str
    eventName: OperationType
    eventVersion: str
    eventSource: str
    awsRegion: str
    dynamodb: "StreamRecordTypeDef"
    userIdentity: "IdentityTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SequenceNumberRangeTypeDef(TypedDict, total=False):
    StartingSequenceNumber: str
    EndingSequenceNumber: str


class ShardTypeDef(TypedDict, total=False):
    ShardId: str
    SequenceNumberRange: "SequenceNumberRangeTypeDef"
    ParentShardId: str


class StreamDescriptionTypeDef(TypedDict, total=False):
    StreamArn: str
    StreamLabel: str
    StreamStatus: StreamStatus
    StreamViewType: StreamViewType
    CreationRequestDateTime: datetime
    TableName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Shards: List["ShardTypeDef"]
    LastEvaluatedShardId: str


class StreamRecordTypeDef(TypedDict, total=False):
    ApproximateCreationDateTime: datetime
    Keys: Dict[str, "AttributeValueTypeDef"]
    NewImage: Dict[str, "AttributeValueTypeDef"]
    OldImage: Dict[str, "AttributeValueTypeDef"]
    SequenceNumber: str
    SizeBytes: int
    StreamViewType: StreamViewType


class StreamTypeDef(TypedDict, total=False):
    StreamArn: str
    TableName: str
    StreamLabel: str
