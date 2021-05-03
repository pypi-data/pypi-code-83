"""
Type annotations for firehose service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/type_defs.html)

Usage::

    ```python
    from mypy_boto3_firehose.type_defs import BufferingHintsTypeDef

    data: BufferingHintsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_firehose.literals import (
    CompressionFormat,
    ContentEncoding,
    DeliveryStreamEncryptionStatus,
    DeliveryStreamFailureType,
    DeliveryStreamStatus,
    DeliveryStreamType,
    ElasticsearchIndexRotationPeriod,
    ElasticsearchS3BackupMode,
    HECEndpointType,
    HttpEndpointS3BackupMode,
    KeyType,
    OrcCompression,
    OrcFormatVersion,
    ParquetCompression,
    ParquetWriterVersion,
    ProcessorParameterName,
    RedshiftS3BackupMode,
    S3BackupMode,
    SplunkS3BackupMode,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BufferingHintsTypeDef",
    "CloudWatchLoggingOptionsTypeDef",
    "CopyCommandTypeDef",
    "CreateDeliveryStreamOutputTypeDef",
    "DataFormatConversionConfigurationTypeDef",
    "DeliveryStreamDescriptionTypeDef",
    "DeliveryStreamEncryptionConfigurationInputTypeDef",
    "DeliveryStreamEncryptionConfigurationTypeDef",
    "DescribeDeliveryStreamOutputTypeDef",
    "DeserializerTypeDef",
    "DestinationDescriptionTypeDef",
    "ElasticsearchBufferingHintsTypeDef",
    "ElasticsearchDestinationConfigurationTypeDef",
    "ElasticsearchDestinationDescriptionTypeDef",
    "ElasticsearchDestinationUpdateTypeDef",
    "ElasticsearchRetryOptionsTypeDef",
    "EncryptionConfigurationTypeDef",
    "ExtendedS3DestinationConfigurationTypeDef",
    "ExtendedS3DestinationDescriptionTypeDef",
    "ExtendedS3DestinationUpdateTypeDef",
    "FailureDescriptionTypeDef",
    "HiveJsonSerDeTypeDef",
    "HttpEndpointBufferingHintsTypeDef",
    "HttpEndpointCommonAttributeTypeDef",
    "HttpEndpointConfigurationTypeDef",
    "HttpEndpointDescriptionTypeDef",
    "HttpEndpointDestinationConfigurationTypeDef",
    "HttpEndpointDestinationDescriptionTypeDef",
    "HttpEndpointDestinationUpdateTypeDef",
    "HttpEndpointRequestConfigurationTypeDef",
    "HttpEndpointRetryOptionsTypeDef",
    "InputFormatConfigurationTypeDef",
    "KMSEncryptionConfigTypeDef",
    "KinesisStreamSourceConfigurationTypeDef",
    "KinesisStreamSourceDescriptionTypeDef",
    "ListDeliveryStreamsOutputTypeDef",
    "ListTagsForDeliveryStreamOutputTypeDef",
    "OpenXJsonSerDeTypeDef",
    "OrcSerDeTypeDef",
    "OutputFormatConfigurationTypeDef",
    "ParquetSerDeTypeDef",
    "ProcessingConfigurationTypeDef",
    "ProcessorParameterTypeDef",
    "ProcessorTypeDef",
    "PutRecordBatchOutputTypeDef",
    "PutRecordBatchResponseEntryTypeDef",
    "PutRecordOutputTypeDef",
    "RecordTypeDef",
    "RedshiftDestinationConfigurationTypeDef",
    "RedshiftDestinationDescriptionTypeDef",
    "RedshiftDestinationUpdateTypeDef",
    "RedshiftRetryOptionsTypeDef",
    "ResponseMetadata",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationDescriptionTypeDef",
    "S3DestinationUpdateTypeDef",
    "SchemaConfigurationTypeDef",
    "SerializerTypeDef",
    "SourceDescriptionTypeDef",
    "SplunkDestinationConfigurationTypeDef",
    "SplunkDestinationDescriptionTypeDef",
    "SplunkDestinationUpdateTypeDef",
    "SplunkRetryOptionsTypeDef",
    "TagTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
)


class BufferingHintsTypeDef(TypedDict, total=False):
    SizeInMBs: int
    IntervalInSeconds: int


class CloudWatchLoggingOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    LogGroupName: str
    LogStreamName: str


class _RequiredCopyCommandTypeDef(TypedDict):
    DataTableName: str


class CopyCommandTypeDef(_RequiredCopyCommandTypeDef, total=False):
    DataTableColumns: str
    CopyOptions: str


class CreateDeliveryStreamOutputTypeDef(TypedDict):
    DeliveryStreamARN: str
    ResponseMetadata: "ResponseMetadata"


class DataFormatConversionConfigurationTypeDef(TypedDict, total=False):
    SchemaConfiguration: "SchemaConfigurationTypeDef"
    InputFormatConfiguration: "InputFormatConfigurationTypeDef"
    OutputFormatConfiguration: "OutputFormatConfigurationTypeDef"
    Enabled: bool


class _RequiredDeliveryStreamDescriptionTypeDef(TypedDict):
    DeliveryStreamName: str
    DeliveryStreamARN: str
    DeliveryStreamStatus: DeliveryStreamStatus
    DeliveryStreamType: DeliveryStreamType
    VersionId: str
    Destinations: List["DestinationDescriptionTypeDef"]
    HasMoreDestinations: bool


class DeliveryStreamDescriptionTypeDef(_RequiredDeliveryStreamDescriptionTypeDef, total=False):
    FailureDescription: "FailureDescriptionTypeDef"
    DeliveryStreamEncryptionConfiguration: "DeliveryStreamEncryptionConfigurationTypeDef"
    CreateTimestamp: datetime
    LastUpdateTimestamp: datetime
    Source: "SourceDescriptionTypeDef"


class _RequiredDeliveryStreamEncryptionConfigurationInputTypeDef(TypedDict):
    KeyType: KeyType


class DeliveryStreamEncryptionConfigurationInputTypeDef(
    _RequiredDeliveryStreamEncryptionConfigurationInputTypeDef, total=False
):
    KeyARN: str


class DeliveryStreamEncryptionConfigurationTypeDef(TypedDict, total=False):
    KeyARN: str
    KeyType: KeyType
    Status: DeliveryStreamEncryptionStatus
    FailureDescription: "FailureDescriptionTypeDef"


class DescribeDeliveryStreamOutputTypeDef(TypedDict):
    DeliveryStreamDescription: "DeliveryStreamDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeserializerTypeDef(TypedDict, total=False):
    OpenXJsonSerDe: "OpenXJsonSerDeTypeDef"
    HiveJsonSerDe: "HiveJsonSerDeTypeDef"


class _RequiredDestinationDescriptionTypeDef(TypedDict):
    DestinationId: str


class DestinationDescriptionTypeDef(_RequiredDestinationDescriptionTypeDef, total=False):
    S3DestinationDescription: "S3DestinationDescriptionTypeDef"
    ExtendedS3DestinationDescription: "ExtendedS3DestinationDescriptionTypeDef"
    RedshiftDestinationDescription: "RedshiftDestinationDescriptionTypeDef"
    ElasticsearchDestinationDescription: "ElasticsearchDestinationDescriptionTypeDef"
    SplunkDestinationDescription: "SplunkDestinationDescriptionTypeDef"
    HttpEndpointDestinationDescription: "HttpEndpointDestinationDescriptionTypeDef"


class ElasticsearchBufferingHintsTypeDef(TypedDict, total=False):
    IntervalInSeconds: int
    SizeInMBs: int


class _RequiredElasticsearchDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    IndexName: str
    S3Configuration: "S3DestinationConfigurationTypeDef"


class ElasticsearchDestinationConfigurationTypeDef(
    _RequiredElasticsearchDestinationConfigurationTypeDef, total=False
):
    DomainARN: str
    ClusterEndpoint: str
    TypeName: str
    IndexRotationPeriod: ElasticsearchIndexRotationPeriod
    BufferingHints: "ElasticsearchBufferingHintsTypeDef"
    RetryOptions: "ElasticsearchRetryOptionsTypeDef"
    S3BackupMode: ElasticsearchS3BackupMode
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    VpcConfiguration: "VpcConfigurationTypeDef"


class ElasticsearchDestinationDescriptionTypeDef(TypedDict, total=False):
    RoleARN: str
    DomainARN: str
    ClusterEndpoint: str
    IndexName: str
    TypeName: str
    IndexRotationPeriod: ElasticsearchIndexRotationPeriod
    BufferingHints: "ElasticsearchBufferingHintsTypeDef"
    RetryOptions: "ElasticsearchRetryOptionsTypeDef"
    S3BackupMode: ElasticsearchS3BackupMode
    S3DestinationDescription: "S3DestinationDescriptionTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    VpcConfigurationDescription: "VpcConfigurationDescriptionTypeDef"


class ElasticsearchDestinationUpdateTypeDef(TypedDict, total=False):
    RoleARN: str
    DomainARN: str
    ClusterEndpoint: str
    IndexName: str
    TypeName: str
    IndexRotationPeriod: ElasticsearchIndexRotationPeriod
    BufferingHints: "ElasticsearchBufferingHintsTypeDef"
    RetryOptions: "ElasticsearchRetryOptionsTypeDef"
    S3Update: "S3DestinationUpdateTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class ElasticsearchRetryOptionsTypeDef(TypedDict, total=False):
    DurationInSeconds: int


class EncryptionConfigurationTypeDef(TypedDict, total=False):
    NoEncryptionConfig: Literal["NoEncryption"]
    KMSEncryptionConfig: "KMSEncryptionConfigTypeDef"


class _RequiredExtendedS3DestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str


class ExtendedS3DestinationConfigurationTypeDef(
    _RequiredExtendedS3DestinationConfigurationTypeDef, total=False
):
    Prefix: str
    ErrorOutputPrefix: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: S3BackupMode
    S3BackupConfiguration: "S3DestinationConfigurationTypeDef"
    DataFormatConversionConfiguration: "DataFormatConversionConfigurationTypeDef"


class _RequiredExtendedS3DestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"


class ExtendedS3DestinationDescriptionTypeDef(
    _RequiredExtendedS3DestinationDescriptionTypeDef, total=False
):
    Prefix: str
    ErrorOutputPrefix: str
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: S3BackupMode
    S3BackupDescription: "S3DestinationDescriptionTypeDef"
    DataFormatConversionConfiguration: "DataFormatConversionConfigurationTypeDef"


class ExtendedS3DestinationUpdateTypeDef(TypedDict, total=False):
    RoleARN: str
    BucketARN: str
    Prefix: str
    ErrorOutputPrefix: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: S3BackupMode
    S3BackupUpdate: "S3DestinationUpdateTypeDef"
    DataFormatConversionConfiguration: "DataFormatConversionConfigurationTypeDef"


FailureDescriptionTypeDef = TypedDict(
    "FailureDescriptionTypeDef", {"Type": DeliveryStreamFailureType, "Details": str}
)


class HiveJsonSerDeTypeDef(TypedDict, total=False):
    TimestampFormats: List[str]


class HttpEndpointBufferingHintsTypeDef(TypedDict, total=False):
    SizeInMBs: int
    IntervalInSeconds: int


class HttpEndpointCommonAttributeTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: str


class _RequiredHttpEndpointConfigurationTypeDef(TypedDict):
    Url: str


class HttpEndpointConfigurationTypeDef(_RequiredHttpEndpointConfigurationTypeDef, total=False):
    Name: str
    AccessKey: str


class HttpEndpointDescriptionTypeDef(TypedDict, total=False):
    Url: str
    Name: str


class _RequiredHttpEndpointDestinationConfigurationTypeDef(TypedDict):
    EndpointConfiguration: "HttpEndpointConfigurationTypeDef"
    S3Configuration: "S3DestinationConfigurationTypeDef"


class HttpEndpointDestinationConfigurationTypeDef(
    _RequiredHttpEndpointDestinationConfigurationTypeDef, total=False
):
    BufferingHints: "HttpEndpointBufferingHintsTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    RequestConfiguration: "HttpEndpointRequestConfigurationTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    RoleARN: str
    RetryOptions: "HttpEndpointRetryOptionsTypeDef"
    S3BackupMode: HttpEndpointS3BackupMode


class HttpEndpointDestinationDescriptionTypeDef(TypedDict, total=False):
    EndpointConfiguration: "HttpEndpointDescriptionTypeDef"
    BufferingHints: "HttpEndpointBufferingHintsTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    RequestConfiguration: "HttpEndpointRequestConfigurationTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    RoleARN: str
    RetryOptions: "HttpEndpointRetryOptionsTypeDef"
    S3BackupMode: HttpEndpointS3BackupMode
    S3DestinationDescription: "S3DestinationDescriptionTypeDef"


class HttpEndpointDestinationUpdateTypeDef(TypedDict, total=False):
    EndpointConfiguration: "HttpEndpointConfigurationTypeDef"
    BufferingHints: "HttpEndpointBufferingHintsTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"
    RequestConfiguration: "HttpEndpointRequestConfigurationTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    RoleARN: str
    RetryOptions: "HttpEndpointRetryOptionsTypeDef"
    S3BackupMode: HttpEndpointS3BackupMode
    S3Update: "S3DestinationUpdateTypeDef"


class HttpEndpointRequestConfigurationTypeDef(TypedDict, total=False):
    ContentEncoding: ContentEncoding
    CommonAttributes: List["HttpEndpointCommonAttributeTypeDef"]


class HttpEndpointRetryOptionsTypeDef(TypedDict, total=False):
    DurationInSeconds: int


class InputFormatConfigurationTypeDef(TypedDict, total=False):
    Deserializer: "DeserializerTypeDef"


class KMSEncryptionConfigTypeDef(TypedDict):
    AWSKMSKeyARN: str


class KinesisStreamSourceConfigurationTypeDef(TypedDict):
    KinesisStreamARN: str
    RoleARN: str


class KinesisStreamSourceDescriptionTypeDef(TypedDict, total=False):
    KinesisStreamARN: str
    RoleARN: str
    DeliveryStartTimestamp: datetime


class ListDeliveryStreamsOutputTypeDef(TypedDict):
    DeliveryStreamNames: List[str]
    HasMoreDeliveryStreams: bool
    ResponseMetadata: "ResponseMetadata"


class ListTagsForDeliveryStreamOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    HasMoreTags: bool
    ResponseMetadata: "ResponseMetadata"


class OpenXJsonSerDeTypeDef(TypedDict, total=False):
    ConvertDotsInJsonKeysToUnderscores: bool
    CaseInsensitive: bool
    ColumnToJsonKeyMappings: Dict[str, str]


class OrcSerDeTypeDef(TypedDict, total=False):
    StripeSizeBytes: int
    BlockSizeBytes: int
    RowIndexStride: int
    EnablePadding: bool
    PaddingTolerance: float
    Compression: OrcCompression
    BloomFilterColumns: List[str]
    BloomFilterFalsePositiveProbability: float
    DictionaryKeyThreshold: float
    FormatVersion: OrcFormatVersion


class OutputFormatConfigurationTypeDef(TypedDict, total=False):
    Serializer: "SerializerTypeDef"


class ParquetSerDeTypeDef(TypedDict, total=False):
    BlockSizeBytes: int
    PageSizeBytes: int
    Compression: ParquetCompression
    EnableDictionaryCompression: bool
    MaxPaddingBytes: int
    WriterVersion: ParquetWriterVersion


class ProcessingConfigurationTypeDef(TypedDict, total=False):
    Enabled: bool
    Processors: List["ProcessorTypeDef"]


class ProcessorParameterTypeDef(TypedDict):
    ParameterName: ProcessorParameterName
    ParameterValue: str


_RequiredProcessorTypeDef = TypedDict("_RequiredProcessorTypeDef", {"Type": Literal["Lambda"]})
_OptionalProcessorTypeDef = TypedDict(
    "_OptionalProcessorTypeDef", {"Parameters": List["ProcessorParameterTypeDef"]}, total=False
)


class ProcessorTypeDef(_RequiredProcessorTypeDef, _OptionalProcessorTypeDef):
    pass


class PutRecordBatchOutputTypeDef(TypedDict):
    FailedPutCount: int
    Encrypted: bool
    RequestResponses: List["PutRecordBatchResponseEntryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PutRecordBatchResponseEntryTypeDef(TypedDict, total=False):
    RecordId: str
    ErrorCode: str
    ErrorMessage: str


class PutRecordOutputTypeDef(TypedDict):
    RecordId: str
    Encrypted: bool
    ResponseMetadata: "ResponseMetadata"


class RecordTypeDef(TypedDict):
    Data: Union[bytes, IO[bytes]]


class _RequiredRedshiftDestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: "CopyCommandTypeDef"
    Username: str
    Password: str
    S3Configuration: "S3DestinationConfigurationTypeDef"


class RedshiftDestinationConfigurationTypeDef(
    _RequiredRedshiftDestinationConfigurationTypeDef, total=False
):
    RetryOptions: "RedshiftRetryOptionsTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: RedshiftS3BackupMode
    S3BackupConfiguration: "S3DestinationConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class _RequiredRedshiftDestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: "CopyCommandTypeDef"
    Username: str
    S3DestinationDescription: "S3DestinationDescriptionTypeDef"


class RedshiftDestinationDescriptionTypeDef(
    _RequiredRedshiftDestinationDescriptionTypeDef, total=False
):
    RetryOptions: "RedshiftRetryOptionsTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: RedshiftS3BackupMode
    S3BackupDescription: "S3DestinationDescriptionTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class RedshiftDestinationUpdateTypeDef(TypedDict, total=False):
    RoleARN: str
    ClusterJDBCURL: str
    CopyCommand: "CopyCommandTypeDef"
    Username: str
    Password: str
    RetryOptions: "RedshiftRetryOptionsTypeDef"
    S3Update: "S3DestinationUpdateTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    S3BackupMode: RedshiftS3BackupMode
    S3BackupUpdate: "S3DestinationUpdateTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class RedshiftRetryOptionsTypeDef(TypedDict, total=False):
    DurationInSeconds: int


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredS3DestinationConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str


class S3DestinationConfigurationTypeDef(_RequiredS3DestinationConfigurationTypeDef, total=False):
    Prefix: str
    ErrorOutputPrefix: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class _RequiredS3DestinationDescriptionTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"


class S3DestinationDescriptionTypeDef(_RequiredS3DestinationDescriptionTypeDef, total=False):
    Prefix: str
    ErrorOutputPrefix: str
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class S3DestinationUpdateTypeDef(TypedDict, total=False):
    RoleARN: str
    BucketARN: str
    Prefix: str
    ErrorOutputPrefix: str
    BufferingHints: "BufferingHintsTypeDef"
    CompressionFormat: CompressionFormat
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class SchemaConfigurationTypeDef(TypedDict, total=False):
    RoleARN: str
    CatalogId: str
    DatabaseName: str
    TableName: str
    Region: str
    VersionId: str


class SerializerTypeDef(TypedDict, total=False):
    ParquetSerDe: "ParquetSerDeTypeDef"
    OrcSerDe: "OrcSerDeTypeDef"


class SourceDescriptionTypeDef(TypedDict, total=False):
    KinesisStreamSourceDescription: "KinesisStreamSourceDescriptionTypeDef"


class _RequiredSplunkDestinationConfigurationTypeDef(TypedDict):
    HECEndpoint: str
    HECEndpointType: HECEndpointType
    HECToken: str
    S3Configuration: "S3DestinationConfigurationTypeDef"


class SplunkDestinationConfigurationTypeDef(
    _RequiredSplunkDestinationConfigurationTypeDef, total=False
):
    HECAcknowledgmentTimeoutInSeconds: int
    RetryOptions: "SplunkRetryOptionsTypeDef"
    S3BackupMode: SplunkS3BackupMode
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class SplunkDestinationDescriptionTypeDef(TypedDict, total=False):
    HECEndpoint: str
    HECEndpointType: HECEndpointType
    HECToken: str
    HECAcknowledgmentTimeoutInSeconds: int
    RetryOptions: "SplunkRetryOptionsTypeDef"
    S3BackupMode: SplunkS3BackupMode
    S3DestinationDescription: "S3DestinationDescriptionTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class SplunkDestinationUpdateTypeDef(TypedDict, total=False):
    HECEndpoint: str
    HECEndpointType: HECEndpointType
    HECToken: str
    HECAcknowledgmentTimeoutInSeconds: int
    RetryOptions: "SplunkRetryOptionsTypeDef"
    S3BackupMode: SplunkS3BackupMode
    S3Update: "S3DestinationUpdateTypeDef"
    ProcessingConfiguration: "ProcessingConfigurationTypeDef"
    CloudWatchLoggingOptions: "CloudWatchLoggingOptionsTypeDef"


class SplunkRetryOptionsTypeDef(TypedDict, total=False):
    DurationInSeconds: int


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class VpcConfigurationDescriptionTypeDef(TypedDict):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
    VpcId: str


class VpcConfigurationTypeDef(TypedDict):
    SubnetIds: List[str]
    RoleARN: str
    SecurityGroupIds: List[str]
