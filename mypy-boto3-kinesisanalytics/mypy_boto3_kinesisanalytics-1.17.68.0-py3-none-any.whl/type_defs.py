"""
Type annotations for kinesisanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.type_defs import ApplicationDetailTypeDef

    data: ApplicationDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_kinesisanalytics.literals import (
    ApplicationStatus,
    InputStartingPosition,
    RecordFormatType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationDetailTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationUpdateTypeDef",
    "CSVMappingParametersTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "InputConfigurationTypeDef",
    "InputDescriptionTypeDef",
    "InputLambdaProcessorDescriptionTypeDef",
    "InputLambdaProcessorTypeDef",
    "InputLambdaProcessorUpdateTypeDef",
    "InputParallelismTypeDef",
    "InputParallelismUpdateTypeDef",
    "InputProcessingConfigurationDescriptionTypeDef",
    "InputProcessingConfigurationTypeDef",
    "InputProcessingConfigurationUpdateTypeDef",
    "InputSchemaUpdateTypeDef",
    "InputStartingPositionConfigurationTypeDef",
    "InputTypeDef",
    "InputUpdateTypeDef",
    "JSONMappingParametersTypeDef",
    "KinesisFirehoseInputDescriptionTypeDef",
    "KinesisFirehoseInputTypeDef",
    "KinesisFirehoseInputUpdateTypeDef",
    "KinesisFirehoseOutputDescriptionTypeDef",
    "KinesisFirehoseOutputTypeDef",
    "KinesisFirehoseOutputUpdateTypeDef",
    "KinesisStreamsInputDescriptionTypeDef",
    "KinesisStreamsInputTypeDef",
    "KinesisStreamsInputUpdateTypeDef",
    "KinesisStreamsOutputDescriptionTypeDef",
    "KinesisStreamsOutputTypeDef",
    "KinesisStreamsOutputUpdateTypeDef",
    "LambdaOutputDescriptionTypeDef",
    "LambdaOutputTypeDef",
    "LambdaOutputUpdateTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadata",
    "S3ConfigurationTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SourceSchemaTypeDef",
    "TagTypeDef",
)


class _RequiredApplicationDetailTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatus
    ApplicationVersionId: int


class ApplicationDetailTypeDef(_RequiredApplicationDetailTypeDef, total=False):
    ApplicationDescription: str
    CreateTimestamp: datetime
    LastUpdateTimestamp: datetime
    InputDescriptions: List["InputDescriptionTypeDef"]
    OutputDescriptions: List["OutputDescriptionTypeDef"]
    ReferenceDataSourceDescriptions: List["ReferenceDataSourceDescriptionTypeDef"]
    CloudWatchLoggingOptionDescriptions: List["CloudWatchLoggingOptionDescriptionTypeDef"]
    ApplicationCode: str


class ApplicationSummaryTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatus


class ApplicationUpdateTypeDef(TypedDict, total=False):
    InputUpdates: List["InputUpdateTypeDef"]
    ApplicationCodeUpdate: str
    OutputUpdates: List["OutputUpdateTypeDef"]
    ReferenceDataSourceUpdates: List["ReferenceDataSourceUpdateTypeDef"]
    CloudWatchLoggingOptionUpdates: List["CloudWatchLoggingOptionUpdateTypeDef"]


class CSVMappingParametersTypeDef(TypedDict):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str


class _RequiredCloudWatchLoggingOptionDescriptionTypeDef(TypedDict):
    LogStreamARN: str
    RoleARN: str


class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef, total=False
):
    CloudWatchLoggingOptionId: str


class CloudWatchLoggingOptionTypeDef(TypedDict):
    LogStreamARN: str
    RoleARN: str


class _RequiredCloudWatchLoggingOptionUpdateTypeDef(TypedDict):
    CloudWatchLoggingOptionId: str


class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, total=False
):
    LogStreamARNUpdate: str
    RoleARNUpdate: str


class CreateApplicationResponseTypeDef(TypedDict):
    ApplicationSummary: "ApplicationSummaryTypeDef"


class DescribeApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: "ApplicationDetailTypeDef"


class DestinationSchemaTypeDef(TypedDict):
    RecordFormatType: RecordFormatType


class DiscoverInputSchemaResponseTypeDef(TypedDict, total=False):
    InputSchema: "SourceSchemaTypeDef"
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]


class InputConfigurationTypeDef(TypedDict):
    Id: str
    InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef"


class InputDescriptionTypeDef(TypedDict, total=False):
    InputId: str
    NamePrefix: str
    InAppStreamNames: List[str]
    InputProcessingConfigurationDescription: "InputProcessingConfigurationDescriptionTypeDef"
    KinesisStreamsInputDescription: "KinesisStreamsInputDescriptionTypeDef"
    KinesisFirehoseInputDescription: "KinesisFirehoseInputDescriptionTypeDef"
    InputSchema: "SourceSchemaTypeDef"
    InputParallelism: "InputParallelismTypeDef"
    InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef"


class InputLambdaProcessorDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class InputLambdaProcessorTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str


class InputLambdaProcessorUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class InputParallelismTypeDef(TypedDict, total=False):
    Count: int


class InputParallelismUpdateTypeDef(TypedDict, total=False):
    CountUpdate: int


class InputProcessingConfigurationDescriptionTypeDef(TypedDict, total=False):
    InputLambdaProcessorDescription: "InputLambdaProcessorDescriptionTypeDef"


class InputProcessingConfigurationTypeDef(TypedDict):
    InputLambdaProcessor: "InputLambdaProcessorTypeDef"


class InputProcessingConfigurationUpdateTypeDef(TypedDict):
    InputLambdaProcessorUpdate: "InputLambdaProcessorUpdateTypeDef"


class InputSchemaUpdateTypeDef(TypedDict, total=False):
    RecordFormatUpdate: "RecordFormatTypeDef"
    RecordEncodingUpdate: str
    RecordColumnUpdates: List["RecordColumnTypeDef"]


class InputStartingPositionConfigurationTypeDef(TypedDict, total=False):
    InputStartingPosition: InputStartingPosition


class _RequiredInputTypeDef(TypedDict):
    NamePrefix: str
    InputSchema: "SourceSchemaTypeDef"


class InputTypeDef(_RequiredInputTypeDef, total=False):
    InputProcessingConfiguration: "InputProcessingConfigurationTypeDef"
    KinesisStreamsInput: "KinesisStreamsInputTypeDef"
    KinesisFirehoseInput: "KinesisFirehoseInputTypeDef"
    InputParallelism: "InputParallelismTypeDef"


class _RequiredInputUpdateTypeDef(TypedDict):
    InputId: str


class InputUpdateTypeDef(_RequiredInputUpdateTypeDef, total=False):
    NamePrefixUpdate: str
    InputProcessingConfigurationUpdate: "InputProcessingConfigurationUpdateTypeDef"
    KinesisStreamsInputUpdate: "KinesisStreamsInputUpdateTypeDef"
    KinesisFirehoseInputUpdate: "KinesisFirehoseInputUpdateTypeDef"
    InputSchemaUpdate: "InputSchemaUpdateTypeDef"
    InputParallelismUpdate: "InputParallelismUpdateTypeDef"


class JSONMappingParametersTypeDef(TypedDict):
    RecordRowPath: str


class KinesisFirehoseInputDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class KinesisFirehoseInputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str


class KinesisFirehoseInputUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class KinesisFirehoseOutputDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class KinesisFirehoseOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str
    ResponseMetadata: "ResponseMetadata"


class KinesisFirehoseOutputUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class KinesisStreamsInputDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class KinesisStreamsInputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str


class KinesisStreamsInputUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class KinesisStreamsOutputDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class KinesisStreamsOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str
    ResponseMetadata: "ResponseMetadata"


class KinesisStreamsOutputUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class LambdaOutputDescriptionTypeDef(TypedDict, total=False):
    ResourceARN: str
    RoleARN: str


class LambdaOutputTypeDef(TypedDict):
    ResourceARN: str
    RoleARN: str
    ResponseMetadata: "ResponseMetadata"


class LambdaOutputUpdateTypeDef(TypedDict, total=False):
    ResourceARNUpdate: str
    RoleARNUpdate: str


class ListApplicationsResponseTypeDef(TypedDict):
    ApplicationSummaries: List["ApplicationSummaryTypeDef"]
    HasMoreApplications: bool


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class MappingParametersTypeDef(TypedDict, total=False):
    JSONMappingParameters: "JSONMappingParametersTypeDef"
    CSVMappingParameters: "CSVMappingParametersTypeDef"


class OutputDescriptionTypeDef(TypedDict, total=False):
    OutputId: str
    Name: str
    KinesisStreamsOutputDescription: "KinesisStreamsOutputDescriptionTypeDef"
    KinesisFirehoseOutputDescription: "KinesisFirehoseOutputDescriptionTypeDef"
    LambdaOutputDescription: "LambdaOutputDescriptionTypeDef"
    DestinationSchema: "DestinationSchemaTypeDef"


class OutputTypeDef(TypedDict):
    Name: str
    KinesisStreamsOutput: "KinesisStreamsOutputTypeDef"
    KinesisFirehoseOutput: "KinesisFirehoseOutputTypeDef"
    LambdaOutput: "LambdaOutputTypeDef"
    DestinationSchema: "DestinationSchemaTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredOutputUpdateTypeDef(TypedDict):
    OutputId: str


class OutputUpdateTypeDef(_RequiredOutputUpdateTypeDef, total=False):
    NameUpdate: str
    KinesisStreamsOutputUpdate: "KinesisStreamsOutputUpdateTypeDef"
    KinesisFirehoseOutputUpdate: "KinesisFirehoseOutputUpdateTypeDef"
    LambdaOutputUpdate: "LambdaOutputUpdateTypeDef"
    DestinationSchemaUpdate: "DestinationSchemaTypeDef"


_RequiredRecordColumnTypeDef = TypedDict(
    "_RequiredRecordColumnTypeDef", {"Name": str, "SqlType": str}
)
_OptionalRecordColumnTypeDef = TypedDict(
    "_OptionalRecordColumnTypeDef", {"Mapping": str}, total=False
)


class RecordColumnTypeDef(_RequiredRecordColumnTypeDef, _OptionalRecordColumnTypeDef):
    pass


class _RequiredRecordFormatTypeDef(TypedDict):
    RecordFormatType: RecordFormatType


class RecordFormatTypeDef(_RequiredRecordFormatTypeDef, total=False):
    MappingParameters: "MappingParametersTypeDef"


class _RequiredReferenceDataSourceDescriptionTypeDef(TypedDict):
    ReferenceId: str
    TableName: str
    S3ReferenceDataSourceDescription: "S3ReferenceDataSourceDescriptionTypeDef"


class ReferenceDataSourceDescriptionTypeDef(
    _RequiredReferenceDataSourceDescriptionTypeDef, total=False
):
    ReferenceSchema: "SourceSchemaTypeDef"


class _RequiredReferenceDataSourceTypeDef(TypedDict):
    TableName: str
    ReferenceSchema: "SourceSchemaTypeDef"


class ReferenceDataSourceTypeDef(_RequiredReferenceDataSourceTypeDef, total=False):
    S3ReferenceDataSource: "S3ReferenceDataSourceTypeDef"


class _RequiredReferenceDataSourceUpdateTypeDef(TypedDict):
    ReferenceId: str


class ReferenceDataSourceUpdateTypeDef(_RequiredReferenceDataSourceUpdateTypeDef, total=False):
    TableNameUpdate: str
    S3ReferenceDataSourceUpdate: "S3ReferenceDataSourceUpdateTypeDef"
    ReferenceSchemaUpdate: "SourceSchemaTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3ConfigurationTypeDef(TypedDict):
    RoleARN: str
    BucketARN: str
    FileKey: str


class S3ReferenceDataSourceDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str


class S3ReferenceDataSourceTypeDef(TypedDict):
    BucketARN: str
    FileKey: str
    ReferenceRoleARN: str


class S3ReferenceDataSourceUpdateTypeDef(TypedDict, total=False):
    BucketARNUpdate: str
    FileKeyUpdate: str
    ReferenceRoleARNUpdate: str


class _RequiredSourceSchemaTypeDef(TypedDict):
    RecordFormat: "RecordFormatTypeDef"
    RecordColumns: List["RecordColumnTypeDef"]


class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, total=False):
    RecordEncoding: str


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str
