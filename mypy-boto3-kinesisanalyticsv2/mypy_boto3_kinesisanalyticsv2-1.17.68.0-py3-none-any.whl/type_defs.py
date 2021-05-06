"""
Type annotations for kinesisanalyticsv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.type_defs import AddApplicationCloudWatchLoggingOptionResponseTypeDef

    data: AddApplicationCloudWatchLoggingOptionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_kinesisanalyticsv2.literals import (
    ApplicationRestoreType,
    ApplicationStatus,
    CodeContentType,
    ConfigurationType,
    InputStartingPosition,
    LogLevel,
    MetricsLevel,
    RecordFormatType,
    RuntimeEnvironment,
    SnapshotStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddApplicationCloudWatchLoggingOptionResponseTypeDef",
    "AddApplicationInputProcessingConfigurationResponseTypeDef",
    "AddApplicationInputResponseTypeDef",
    "AddApplicationOutputResponseTypeDef",
    "AddApplicationReferenceDataSourceResponseTypeDef",
    "AddApplicationVpcConfigurationResponseTypeDef",
    "ApplicationCodeConfigurationDescriptionTypeDef",
    "ApplicationCodeConfigurationTypeDef",
    "ApplicationCodeConfigurationUpdateTypeDef",
    "ApplicationConfigurationDescriptionTypeDef",
    "ApplicationConfigurationTypeDef",
    "ApplicationConfigurationUpdateTypeDef",
    "ApplicationDetailTypeDef",
    "ApplicationMaintenanceConfigurationDescriptionTypeDef",
    "ApplicationMaintenanceConfigurationUpdateTypeDef",
    "ApplicationRestoreConfigurationTypeDef",
    "ApplicationSnapshotConfigurationDescriptionTypeDef",
    "ApplicationSnapshotConfigurationTypeDef",
    "ApplicationSnapshotConfigurationUpdateTypeDef",
    "ApplicationSummaryTypeDef",
    "CSVMappingParametersTypeDef",
    "CheckpointConfigurationDescriptionTypeDef",
    "CheckpointConfigurationTypeDef",
    "CheckpointConfigurationUpdateTypeDef",
    "CloudWatchLoggingOptionDescriptionTypeDef",
    "CloudWatchLoggingOptionTypeDef",
    "CloudWatchLoggingOptionUpdateTypeDef",
    "CodeContentDescriptionTypeDef",
    "CodeContentTypeDef",
    "CodeContentUpdateTypeDef",
    "CreateApplicationPresignedUrlResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DeleteApplicationCloudWatchLoggingOptionResponseTypeDef",
    "DeleteApplicationInputProcessingConfigurationResponseTypeDef",
    "DeleteApplicationOutputResponseTypeDef",
    "DeleteApplicationReferenceDataSourceResponseTypeDef",
    "DeleteApplicationVpcConfigurationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeApplicationSnapshotResponseTypeDef",
    "DestinationSchemaTypeDef",
    "DiscoverInputSchemaResponseTypeDef",
    "EnvironmentPropertiesTypeDef",
    "EnvironmentPropertyDescriptionsTypeDef",
    "EnvironmentPropertyUpdatesTypeDef",
    "FlinkApplicationConfigurationDescriptionTypeDef",
    "FlinkApplicationConfigurationTypeDef",
    "FlinkApplicationConfigurationUpdateTypeDef",
    "FlinkRunConfigurationTypeDef",
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
    "ListApplicationSnapshotsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MappingParametersTypeDef",
    "MonitoringConfigurationDescriptionTypeDef",
    "MonitoringConfigurationTypeDef",
    "MonitoringConfigurationUpdateTypeDef",
    "OutputDescriptionTypeDef",
    "OutputTypeDef",
    "OutputUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelismConfigurationDescriptionTypeDef",
    "ParallelismConfigurationTypeDef",
    "ParallelismConfigurationUpdateTypeDef",
    "PropertyGroupTypeDef",
    "RecordColumnTypeDef",
    "RecordFormatTypeDef",
    "ReferenceDataSourceDescriptionTypeDef",
    "ReferenceDataSourceTypeDef",
    "ReferenceDataSourceUpdateTypeDef",
    "ResponseMetadata",
    "RollbackApplicationResponseTypeDef",
    "RunConfigurationDescriptionTypeDef",
    "RunConfigurationTypeDef",
    "RunConfigurationUpdateTypeDef",
    "S3ApplicationCodeLocationDescriptionTypeDef",
    "S3ConfigurationTypeDef",
    "S3ContentLocationTypeDef",
    "S3ContentLocationUpdateTypeDef",
    "S3ReferenceDataSourceDescriptionTypeDef",
    "S3ReferenceDataSourceTypeDef",
    "S3ReferenceDataSourceUpdateTypeDef",
    "SnapshotDetailsTypeDef",
    "SourceSchemaTypeDef",
    "SqlApplicationConfigurationDescriptionTypeDef",
    "SqlApplicationConfigurationTypeDef",
    "SqlApplicationConfigurationUpdateTypeDef",
    "SqlRunConfigurationTypeDef",
    "TagTypeDef",
    "UpdateApplicationMaintenanceConfigurationResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VpcConfigurationDescriptionTypeDef",
    "VpcConfigurationTypeDef",
    "VpcConfigurationUpdateTypeDef",
)


class AddApplicationCloudWatchLoggingOptionResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List["CloudWatchLoggingOptionDescriptionTypeDef"]


class AddApplicationInputProcessingConfigurationResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    InputId: str
    InputProcessingConfigurationDescription: "InputProcessingConfigurationDescriptionTypeDef"


class AddApplicationInputResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    InputDescriptions: List["InputDescriptionTypeDef"]


class AddApplicationOutputResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    OutputDescriptions: List["OutputDescriptionTypeDef"]


class AddApplicationReferenceDataSourceResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    ReferenceDataSourceDescriptions: List["ReferenceDataSourceDescriptionTypeDef"]


class AddApplicationVpcConfigurationResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    VpcConfigurationDescription: "VpcConfigurationDescriptionTypeDef"


class _RequiredApplicationCodeConfigurationDescriptionTypeDef(TypedDict):
    CodeContentType: CodeContentType


class ApplicationCodeConfigurationDescriptionTypeDef(
    _RequiredApplicationCodeConfigurationDescriptionTypeDef, total=False
):
    CodeContentDescription: "CodeContentDescriptionTypeDef"


class _RequiredApplicationCodeConfigurationTypeDef(TypedDict):
    CodeContentType: CodeContentType


class ApplicationCodeConfigurationTypeDef(
    _RequiredApplicationCodeConfigurationTypeDef, total=False
):
    CodeContent: "CodeContentTypeDef"


class ApplicationCodeConfigurationUpdateTypeDef(TypedDict, total=False):
    CodeContentTypeUpdate: CodeContentType
    CodeContentUpdate: "CodeContentUpdateTypeDef"


class ApplicationConfigurationDescriptionTypeDef(TypedDict, total=False):
    SqlApplicationConfigurationDescription: "SqlApplicationConfigurationDescriptionTypeDef"
    ApplicationCodeConfigurationDescription: "ApplicationCodeConfigurationDescriptionTypeDef"
    RunConfigurationDescription: "RunConfigurationDescriptionTypeDef"
    FlinkApplicationConfigurationDescription: "FlinkApplicationConfigurationDescriptionTypeDef"
    EnvironmentPropertyDescriptions: "EnvironmentPropertyDescriptionsTypeDef"
    ApplicationSnapshotConfigurationDescription: "ApplicationSnapshotConfigurationDescriptionTypeDef"
    VpcConfigurationDescriptions: List["VpcConfigurationDescriptionTypeDef"]


class _RequiredApplicationConfigurationTypeDef(TypedDict):
    ApplicationCodeConfiguration: "ApplicationCodeConfigurationTypeDef"


class ApplicationConfigurationTypeDef(_RequiredApplicationConfigurationTypeDef, total=False):
    SqlApplicationConfiguration: "SqlApplicationConfigurationTypeDef"
    FlinkApplicationConfiguration: "FlinkApplicationConfigurationTypeDef"
    EnvironmentProperties: "EnvironmentPropertiesTypeDef"
    ApplicationSnapshotConfiguration: "ApplicationSnapshotConfigurationTypeDef"
    VpcConfigurations: List["VpcConfigurationTypeDef"]


class ApplicationConfigurationUpdateTypeDef(TypedDict, total=False):
    SqlApplicationConfigurationUpdate: "SqlApplicationConfigurationUpdateTypeDef"
    ApplicationCodeConfigurationUpdate: "ApplicationCodeConfigurationUpdateTypeDef"
    FlinkApplicationConfigurationUpdate: "FlinkApplicationConfigurationUpdateTypeDef"
    EnvironmentPropertyUpdates: "EnvironmentPropertyUpdatesTypeDef"
    ApplicationSnapshotConfigurationUpdate: "ApplicationSnapshotConfigurationUpdateTypeDef"
    VpcConfigurationUpdates: List["VpcConfigurationUpdateTypeDef"]


class _RequiredApplicationDetailTypeDef(TypedDict):
    ApplicationARN: str
    ApplicationName: str
    RuntimeEnvironment: RuntimeEnvironment
    ApplicationStatus: ApplicationStatus
    ApplicationVersionId: int


class ApplicationDetailTypeDef(_RequiredApplicationDetailTypeDef, total=False):
    ApplicationDescription: str
    ServiceExecutionRole: str
    CreateTimestamp: datetime
    LastUpdateTimestamp: datetime
    ApplicationConfigurationDescription: "ApplicationConfigurationDescriptionTypeDef"
    CloudWatchLoggingOptionDescriptions: List["CloudWatchLoggingOptionDescriptionTypeDef"]
    ApplicationMaintenanceConfigurationDescription: "ApplicationMaintenanceConfigurationDescriptionTypeDef"
    ApplicationVersionUpdatedFrom: int
    ApplicationVersionRolledBackFrom: int
    ConditionalToken: str


class ApplicationMaintenanceConfigurationDescriptionTypeDef(TypedDict):
    ApplicationMaintenanceWindowStartTime: str
    ApplicationMaintenanceWindowEndTime: str


class ApplicationMaintenanceConfigurationUpdateTypeDef(TypedDict):
    ApplicationMaintenanceWindowStartTimeUpdate: str


class _RequiredApplicationRestoreConfigurationTypeDef(TypedDict):
    ApplicationRestoreType: ApplicationRestoreType


class ApplicationRestoreConfigurationTypeDef(
    _RequiredApplicationRestoreConfigurationTypeDef, total=False
):
    SnapshotName: str


class ApplicationSnapshotConfigurationDescriptionTypeDef(TypedDict):
    SnapshotsEnabled: bool


class ApplicationSnapshotConfigurationTypeDef(TypedDict):
    SnapshotsEnabled: bool


class ApplicationSnapshotConfigurationUpdateTypeDef(TypedDict):
    SnapshotsEnabledUpdate: bool


class ApplicationSummaryTypeDef(TypedDict):
    ApplicationName: str
    ApplicationARN: str
    ApplicationStatus: ApplicationStatus
    ApplicationVersionId: int
    RuntimeEnvironment: RuntimeEnvironment


class CSVMappingParametersTypeDef(TypedDict):
    RecordRowDelimiter: str
    RecordColumnDelimiter: str


class CheckpointConfigurationDescriptionTypeDef(TypedDict, total=False):
    ConfigurationType: ConfigurationType
    CheckpointingEnabled: bool
    CheckpointInterval: int
    MinPauseBetweenCheckpoints: int


class _RequiredCheckpointConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationType


class CheckpointConfigurationTypeDef(_RequiredCheckpointConfigurationTypeDef, total=False):
    CheckpointingEnabled: bool
    CheckpointInterval: int
    MinPauseBetweenCheckpoints: int


class CheckpointConfigurationUpdateTypeDef(TypedDict, total=False):
    ConfigurationTypeUpdate: ConfigurationType
    CheckpointingEnabledUpdate: bool
    CheckpointIntervalUpdate: int
    MinPauseBetweenCheckpointsUpdate: int


class _RequiredCloudWatchLoggingOptionDescriptionTypeDef(TypedDict):
    LogStreamARN: str


class CloudWatchLoggingOptionDescriptionTypeDef(
    _RequiredCloudWatchLoggingOptionDescriptionTypeDef, total=False
):
    CloudWatchLoggingOptionId: str
    RoleARN: str


class CloudWatchLoggingOptionTypeDef(TypedDict):
    LogStreamARN: str


class _RequiredCloudWatchLoggingOptionUpdateTypeDef(TypedDict):
    CloudWatchLoggingOptionId: str


class CloudWatchLoggingOptionUpdateTypeDef(
    _RequiredCloudWatchLoggingOptionUpdateTypeDef, total=False
):
    LogStreamARNUpdate: str


class CodeContentDescriptionTypeDef(TypedDict, total=False):
    TextContent: str
    CodeMD5: str
    CodeSize: int
    S3ApplicationCodeLocationDescription: "S3ApplicationCodeLocationDescriptionTypeDef"


class CodeContentTypeDef(TypedDict, total=False):
    TextContent: str
    ZipFileContent: Union[bytes, IO[bytes]]
    S3ContentLocation: "S3ContentLocationTypeDef"


class CodeContentUpdateTypeDef(TypedDict, total=False):
    TextContentUpdate: str
    ZipFileContentUpdate: Union[bytes, IO[bytes]]
    S3ContentLocationUpdate: "S3ContentLocationUpdateTypeDef"


class CreateApplicationPresignedUrlResponseTypeDef(TypedDict, total=False):
    AuthorizedUrl: str


class CreateApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: "ApplicationDetailTypeDef"


class DeleteApplicationCloudWatchLoggingOptionResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int
    CloudWatchLoggingOptionDescriptions: List["CloudWatchLoggingOptionDescriptionTypeDef"]


class DeleteApplicationInputProcessingConfigurationResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int


class DeleteApplicationOutputResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int


class DeleteApplicationReferenceDataSourceResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int


class DeleteApplicationVpcConfigurationResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationVersionId: int


class DescribeApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: "ApplicationDetailTypeDef"


class DescribeApplicationSnapshotResponseTypeDef(TypedDict):
    SnapshotDetails: "SnapshotDetailsTypeDef"


class DestinationSchemaTypeDef(TypedDict):
    RecordFormatType: RecordFormatType


class DiscoverInputSchemaResponseTypeDef(TypedDict, total=False):
    InputSchema: "SourceSchemaTypeDef"
    ParsedInputRecords: List[List[str]]
    ProcessedInputRecords: List[str]
    RawInputRecords: List[str]


class EnvironmentPropertiesTypeDef(TypedDict):
    PropertyGroups: List["PropertyGroupTypeDef"]


class EnvironmentPropertyDescriptionsTypeDef(TypedDict, total=False):
    PropertyGroupDescriptions: List["PropertyGroupTypeDef"]


class EnvironmentPropertyUpdatesTypeDef(TypedDict):
    PropertyGroups: List["PropertyGroupTypeDef"]


class FlinkApplicationConfigurationDescriptionTypeDef(TypedDict, total=False):
    CheckpointConfigurationDescription: "CheckpointConfigurationDescriptionTypeDef"
    MonitoringConfigurationDescription: "MonitoringConfigurationDescriptionTypeDef"
    ParallelismConfigurationDescription: "ParallelismConfigurationDescriptionTypeDef"
    JobPlanDescription: str


class FlinkApplicationConfigurationTypeDef(TypedDict, total=False):
    CheckpointConfiguration: "CheckpointConfigurationTypeDef"
    MonitoringConfiguration: "MonitoringConfigurationTypeDef"
    ParallelismConfiguration: "ParallelismConfigurationTypeDef"


class FlinkApplicationConfigurationUpdateTypeDef(TypedDict, total=False):
    CheckpointConfigurationUpdate: "CheckpointConfigurationUpdateTypeDef"
    MonitoringConfigurationUpdate: "MonitoringConfigurationUpdateTypeDef"
    ParallelismConfigurationUpdate: "ParallelismConfigurationUpdateTypeDef"


class FlinkRunConfigurationTypeDef(TypedDict, total=False):
    AllowNonRestoredState: bool


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


class _RequiredInputLambdaProcessorDescriptionTypeDef(TypedDict):
    ResourceARN: str


class InputLambdaProcessorDescriptionTypeDef(
    _RequiredInputLambdaProcessorDescriptionTypeDef, total=False
):
    RoleARN: str


class InputLambdaProcessorTypeDef(TypedDict):
    ResourceARN: str


class InputLambdaProcessorUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class InputParallelismTypeDef(TypedDict, total=False):
    Count: int


class InputParallelismUpdateTypeDef(TypedDict):
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


class _RequiredKinesisFirehoseInputDescriptionTypeDef(TypedDict):
    ResourceARN: str


class KinesisFirehoseInputDescriptionTypeDef(
    _RequiredKinesisFirehoseInputDescriptionTypeDef, total=False
):
    RoleARN: str


class KinesisFirehoseInputTypeDef(TypedDict):
    ResourceARN: str


class KinesisFirehoseInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class _RequiredKinesisFirehoseOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str


class KinesisFirehoseOutputDescriptionTypeDef(
    _RequiredKinesisFirehoseOutputDescriptionTypeDef, total=False
):
    RoleARN: str


class KinesisFirehoseOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: "ResponseMetadata"


class KinesisFirehoseOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class _RequiredKinesisStreamsInputDescriptionTypeDef(TypedDict):
    ResourceARN: str


class KinesisStreamsInputDescriptionTypeDef(
    _RequiredKinesisStreamsInputDescriptionTypeDef, total=False
):
    RoleARN: str


class KinesisStreamsInputTypeDef(TypedDict):
    ResourceARN: str


class KinesisStreamsInputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class _RequiredKinesisStreamsOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str


class KinesisStreamsOutputDescriptionTypeDef(
    _RequiredKinesisStreamsOutputDescriptionTypeDef, total=False
):
    RoleARN: str


class KinesisStreamsOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: "ResponseMetadata"


class KinesisStreamsOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class _RequiredLambdaOutputDescriptionTypeDef(TypedDict):
    ResourceARN: str


class LambdaOutputDescriptionTypeDef(_RequiredLambdaOutputDescriptionTypeDef, total=False):
    RoleARN: str


class LambdaOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: "ResponseMetadata"


class LambdaOutputUpdateTypeDef(TypedDict):
    ResourceARNUpdate: str


class ListApplicationSnapshotsResponseTypeDef(TypedDict, total=False):
    SnapshotSummaries: List["SnapshotDetailsTypeDef"]
    NextToken: str


class _RequiredListApplicationsResponseTypeDef(TypedDict):
    ApplicationSummaries: List["ApplicationSummaryTypeDef"]


class ListApplicationsResponseTypeDef(_RequiredListApplicationsResponseTypeDef, total=False):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class MappingParametersTypeDef(TypedDict, total=False):
    JSONMappingParameters: "JSONMappingParametersTypeDef"
    CSVMappingParameters: "CSVMappingParametersTypeDef"


class MonitoringConfigurationDescriptionTypeDef(TypedDict, total=False):
    ConfigurationType: ConfigurationType
    MetricsLevel: MetricsLevel
    LogLevel: LogLevel


class _RequiredMonitoringConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationType


class MonitoringConfigurationTypeDef(_RequiredMonitoringConfigurationTypeDef, total=False):
    MetricsLevel: MetricsLevel
    LogLevel: LogLevel


class MonitoringConfigurationUpdateTypeDef(TypedDict, total=False):
    ConfigurationTypeUpdate: ConfigurationType
    MetricsLevelUpdate: MetricsLevel
    LogLevelUpdate: LogLevel


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


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParallelismConfigurationDescriptionTypeDef(TypedDict, total=False):
    ConfigurationType: ConfigurationType
    Parallelism: int
    ParallelismPerKPU: int
    CurrentParallelism: int
    AutoScalingEnabled: bool


class _RequiredParallelismConfigurationTypeDef(TypedDict):
    ConfigurationType: ConfigurationType


class ParallelismConfigurationTypeDef(_RequiredParallelismConfigurationTypeDef, total=False):
    Parallelism: int
    ParallelismPerKPU: int
    AutoScalingEnabled: bool


class ParallelismConfigurationUpdateTypeDef(TypedDict, total=False):
    ConfigurationTypeUpdate: ConfigurationType
    ParallelismUpdate: int
    ParallelismPerKPUUpdate: int
    AutoScalingEnabledUpdate: bool


class PropertyGroupTypeDef(TypedDict):
    PropertyGroupId: str
    PropertyMap: Dict[str, str]


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


class RollbackApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: "ApplicationDetailTypeDef"


class RunConfigurationDescriptionTypeDef(TypedDict, total=False):
    ApplicationRestoreConfigurationDescription: "ApplicationRestoreConfigurationTypeDef"
    FlinkRunConfigurationDescription: "FlinkRunConfigurationTypeDef"


class RunConfigurationTypeDef(TypedDict, total=False):
    FlinkRunConfiguration: "FlinkRunConfigurationTypeDef"
    SqlRunConfigurations: List["SqlRunConfigurationTypeDef"]
    ApplicationRestoreConfiguration: "ApplicationRestoreConfigurationTypeDef"


class RunConfigurationUpdateTypeDef(TypedDict, total=False):
    FlinkRunConfiguration: "FlinkRunConfigurationTypeDef"
    ApplicationRestoreConfiguration: "ApplicationRestoreConfigurationTypeDef"


class _RequiredS3ApplicationCodeLocationDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str


class S3ApplicationCodeLocationDescriptionTypeDef(
    _RequiredS3ApplicationCodeLocationDescriptionTypeDef, total=False
):
    ObjectVersion: str


class S3ConfigurationTypeDef(TypedDict):
    BucketARN: str
    FileKey: str


class _RequiredS3ContentLocationTypeDef(TypedDict):
    BucketARN: str
    FileKey: str


class S3ContentLocationTypeDef(_RequiredS3ContentLocationTypeDef, total=False):
    ObjectVersion: str


class S3ContentLocationUpdateTypeDef(TypedDict, total=False):
    BucketARNUpdate: str
    FileKeyUpdate: str
    ObjectVersionUpdate: str


class _RequiredS3ReferenceDataSourceDescriptionTypeDef(TypedDict):
    BucketARN: str
    FileKey: str


class S3ReferenceDataSourceDescriptionTypeDef(
    _RequiredS3ReferenceDataSourceDescriptionTypeDef, total=False
):
    ReferenceRoleARN: str


class S3ReferenceDataSourceTypeDef(TypedDict, total=False):
    BucketARN: str
    FileKey: str


class S3ReferenceDataSourceUpdateTypeDef(TypedDict, total=False):
    BucketARNUpdate: str
    FileKeyUpdate: str


class _RequiredSnapshotDetailsTypeDef(TypedDict):
    SnapshotName: str
    SnapshotStatus: SnapshotStatus
    ApplicationVersionId: int


class SnapshotDetailsTypeDef(_RequiredSnapshotDetailsTypeDef, total=False):
    SnapshotCreationTimestamp: datetime


class _RequiredSourceSchemaTypeDef(TypedDict):
    RecordFormat: "RecordFormatTypeDef"
    RecordColumns: List["RecordColumnTypeDef"]


class SourceSchemaTypeDef(_RequiredSourceSchemaTypeDef, total=False):
    RecordEncoding: str


class SqlApplicationConfigurationDescriptionTypeDef(TypedDict, total=False):
    InputDescriptions: List["InputDescriptionTypeDef"]
    OutputDescriptions: List["OutputDescriptionTypeDef"]
    ReferenceDataSourceDescriptions: List["ReferenceDataSourceDescriptionTypeDef"]


class SqlApplicationConfigurationTypeDef(TypedDict, total=False):
    Inputs: List["InputTypeDef"]
    Outputs: List["OutputTypeDef"]
    ReferenceDataSources: List["ReferenceDataSourceTypeDef"]


class SqlApplicationConfigurationUpdateTypeDef(TypedDict, total=False):
    InputUpdates: List["InputUpdateTypeDef"]
    OutputUpdates: List["OutputUpdateTypeDef"]
    ReferenceDataSourceUpdates: List["ReferenceDataSourceUpdateTypeDef"]


class SqlRunConfigurationTypeDef(TypedDict):
    InputId: str
    InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef"


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class UpdateApplicationMaintenanceConfigurationResponseTypeDef(TypedDict, total=False):
    ApplicationARN: str
    ApplicationMaintenanceConfigurationDescription: "ApplicationMaintenanceConfigurationDescriptionTypeDef"


class UpdateApplicationResponseTypeDef(TypedDict):
    ApplicationDetail: "ApplicationDetailTypeDef"


class VpcConfigurationDescriptionTypeDef(TypedDict):
    VpcConfigurationId: str
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class VpcConfigurationTypeDef(TypedDict):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class _RequiredVpcConfigurationUpdateTypeDef(TypedDict):
    VpcConfigurationId: str


class VpcConfigurationUpdateTypeDef(_RequiredVpcConfigurationUpdateTypeDef, total=False):
    SubnetIdUpdates: List[str]
    SecurityGroupIdUpdates: List[str]
