"""
Type annotations for kinesis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import ChildShardTypeDef

    data: ChildShardTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_kinesis.literals import (
    ConsumerStatus,
    EncryptionType,
    MetricsName,
    ShardFilterType,
    ShardIteratorType,
    StreamStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "EnhancedMetricsTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "HashKeyRangeTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListShardsOutputTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordOutputTypeDef",
    "PutRecordsOutputTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RecordTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadata",
    "SequenceNumberRangeTypeDef",
    "ShardFilterTypeDef",
    "ShardTypeDef",
    "StartingPositionTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "SubscribeToShardOutputTypeDef",
    "TagTypeDef",
    "UpdateShardCountOutputTypeDef",
    "WaiterConfigTypeDef",
)


class ChildShardTypeDef(TypedDict):
    ShardId: str
    ParentShards: List[str]
    HashKeyRange: "HashKeyRangeTypeDef"


class ConsumerDescriptionTypeDef(TypedDict):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatus
    ConsumerCreationTimestamp: datetime
    StreamARN: str


class ConsumerTypeDef(TypedDict):
    ConsumerName: str
    ConsumerARN: str
    ConsumerStatus: ConsumerStatus
    ConsumerCreationTimestamp: datetime


class DescribeLimitsOutputTypeDef(TypedDict):
    ShardLimit: int
    OpenShardCount: int
    ResponseMetadata: "ResponseMetadata"


class DescribeStreamConsumerOutputTypeDef(TypedDict):
    ConsumerDescription: "ConsumerDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStreamOutputTypeDef(TypedDict):
    StreamDescription: "StreamDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStreamSummaryOutputTypeDef(TypedDict):
    StreamDescriptionSummary: "StreamDescriptionSummaryTypeDef"
    ResponseMetadata: "ResponseMetadata"


class EnhancedMetricsTypeDef(TypedDict, total=False):
    ShardLevelMetrics: List[MetricsName]


class EnhancedMonitoringOutputTypeDef(TypedDict):
    StreamName: str
    CurrentShardLevelMetrics: List[MetricsName]
    DesiredShardLevelMetrics: List[MetricsName]
    ResponseMetadata: "ResponseMetadata"


class GetRecordsOutputTypeDef(TypedDict):
    Records: List["RecordTypeDef"]
    NextShardIterator: str
    MillisBehindLatest: int
    ChildShards: List["ChildShardTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetShardIteratorOutputTypeDef(TypedDict):
    ShardIterator: str
    ResponseMetadata: "ResponseMetadata"


class HashKeyRangeTypeDef(TypedDict):
    StartingHashKey: str
    EndingHashKey: str


class InternalFailureExceptionTypeDef(TypedDict, total=False):
    message: str


class KMSAccessDeniedExceptionTypeDef(TypedDict, total=False):
    message: str


class KMSDisabledExceptionTypeDef(TypedDict, total=False):
    message: str


class KMSInvalidStateExceptionTypeDef(TypedDict, total=False):
    message: str


class KMSNotFoundExceptionTypeDef(TypedDict, total=False):
    message: str


class KMSOptInRequiredTypeDef(TypedDict, total=False):
    message: str


class KMSThrottlingExceptionTypeDef(TypedDict, total=False):
    message: str


class ListShardsOutputTypeDef(TypedDict):
    Shards: List["ShardTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStreamConsumersOutputTypeDef(TypedDict):
    Consumers: List["ConsumerTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStreamsOutputTypeDef(TypedDict):
    StreamNames: List[str]
    HasMoreStreams: bool
    ResponseMetadata: "ResponseMetadata"


class ListTagsForStreamOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    HasMoreTags: bool
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutRecordOutputTypeDef(TypedDict):
    ShardId: str
    SequenceNumber: str
    EncryptionType: EncryptionType
    ResponseMetadata: "ResponseMetadata"


class PutRecordsOutputTypeDef(TypedDict):
    FailedRecordCount: int
    Records: List["PutRecordsResultEntryTypeDef"]
    EncryptionType: EncryptionType
    ResponseMetadata: "ResponseMetadata"


class _RequiredPutRecordsRequestEntryTypeDef(TypedDict):
    Data: Union[bytes, IO[bytes]]
    PartitionKey: str


class PutRecordsRequestEntryTypeDef(_RequiredPutRecordsRequestEntryTypeDef, total=False):
    ExplicitHashKey: str


class PutRecordsResultEntryTypeDef(TypedDict, total=False):
    SequenceNumber: str
    ShardId: str
    ErrorCode: str
    ErrorMessage: str


class _RequiredRecordTypeDef(TypedDict):
    SequenceNumber: str
    Data: Union[bytes, IO[bytes]]
    PartitionKey: str


class RecordTypeDef(_RequiredRecordTypeDef, total=False):
    ApproximateArrivalTimestamp: datetime
    EncryptionType: EncryptionType


class RegisterStreamConsumerOutputTypeDef(TypedDict):
    Consumer: "ConsumerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ResourceInUseExceptionTypeDef(TypedDict, total=False):
    message: str


class ResourceNotFoundExceptionTypeDef(TypedDict, total=False):
    message: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredSequenceNumberRangeTypeDef(TypedDict):
    StartingSequenceNumber: str


class SequenceNumberRangeTypeDef(_RequiredSequenceNumberRangeTypeDef, total=False):
    EndingSequenceNumber: str


_RequiredShardFilterTypeDef = TypedDict("_RequiredShardFilterTypeDef", {"Type": ShardFilterType})
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef", {"ShardId": str, "Timestamp": datetime}, total=False
)


class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass


class _RequiredShardTypeDef(TypedDict):
    ShardId: str
    HashKeyRange: "HashKeyRangeTypeDef"
    SequenceNumberRange: "SequenceNumberRangeTypeDef"


class ShardTypeDef(_RequiredShardTypeDef, total=False):
    ParentShardId: str
    AdjacentParentShardId: str


_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef", {"Type": ShardIteratorType}
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef", {"SequenceNumber": str, "Timestamp": datetime}, total=False
)


class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass


class _RequiredStreamDescriptionSummaryTypeDef(TypedDict):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatus
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List["EnhancedMetricsTypeDef"]
    OpenShardCount: int


class StreamDescriptionSummaryTypeDef(_RequiredStreamDescriptionSummaryTypeDef, total=False):
    EncryptionType: EncryptionType
    KeyId: str
    ConsumerCount: int


class _RequiredStreamDescriptionTypeDef(TypedDict):
    StreamName: str
    StreamARN: str
    StreamStatus: StreamStatus
    Shards: List["ShardTypeDef"]
    HasMoreShards: bool
    RetentionPeriodHours: int
    StreamCreationTimestamp: datetime
    EnhancedMonitoring: List["EnhancedMetricsTypeDef"]


class StreamDescriptionTypeDef(_RequiredStreamDescriptionTypeDef, total=False):
    EncryptionType: EncryptionType
    KeyId: str


class _RequiredSubscribeToShardEventStreamTypeDef(TypedDict):
    SubscribeToShardEvent: "SubscribeToShardEventTypeDef"


class SubscribeToShardEventStreamTypeDef(_RequiredSubscribeToShardEventStreamTypeDef, total=False):
    ResourceNotFoundException: "ResourceNotFoundExceptionTypeDef"
    ResourceInUseException: "ResourceInUseExceptionTypeDef"
    KMSDisabledException: "KMSDisabledExceptionTypeDef"
    KMSInvalidStateException: "KMSInvalidStateExceptionTypeDef"
    KMSAccessDeniedException: "KMSAccessDeniedExceptionTypeDef"
    KMSNotFoundException: "KMSNotFoundExceptionTypeDef"
    KMSOptInRequired: "KMSOptInRequiredTypeDef"
    KMSThrottlingException: "KMSThrottlingExceptionTypeDef"
    InternalFailureException: "InternalFailureExceptionTypeDef"


class _RequiredSubscribeToShardEventTypeDef(TypedDict):
    Records: List["RecordTypeDef"]
    ContinuationSequenceNumber: str
    MillisBehindLatest: int


class SubscribeToShardEventTypeDef(_RequiredSubscribeToShardEventTypeDef, total=False):
    ChildShards: List["ChildShardTypeDef"]


class SubscribeToShardOutputTypeDef(TypedDict):
    EventStream: "SubscribeToShardEventStreamTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class UpdateShardCountOutputTypeDef(TypedDict):
    StreamName: str
    CurrentShardCount: int
    TargetShardCount: int
    ResponseMetadata: "ResponseMetadata"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
