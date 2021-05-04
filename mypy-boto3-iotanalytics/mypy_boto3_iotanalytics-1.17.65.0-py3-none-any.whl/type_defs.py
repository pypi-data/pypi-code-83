"""
Type annotations for iotanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotanalytics.type_defs import AddAttributesActivityTypeDef

    data: AddAttributesActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_iotanalytics.literals import (
    ChannelStatus,
    ComputeType,
    DatasetActionType,
    DatasetContentState,
    DatasetStatus,
    DatastoreStatus,
    FileFormatType,
    ReprocessingStatus,
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
    "AddAttributesActivityTypeDef",
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageResponseTypeDef",
    "ChannelActivityTypeDef",
    "ChannelMessagesTypeDef",
    "ChannelStatisticsTypeDef",
    "ChannelStorageSummaryTypeDef",
    "ChannelStorageTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ColumnTypeDef",
    "ContainerDatasetActionTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDatasetContentResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "CreatePipelineResponseTypeDef",
    "CustomerManagedChannelS3StorageSummaryTypeDef",
    "CustomerManagedChannelS3StorageTypeDef",
    "CustomerManagedDatastoreS3StorageSummaryTypeDef",
    "CustomerManagedDatastoreS3StorageTypeDef",
    "DatasetActionSummaryTypeDef",
    "DatasetActionTypeDef",
    "DatasetContentDeliveryDestinationTypeDef",
    "DatasetContentDeliveryRuleTypeDef",
    "DatasetContentStatusTypeDef",
    "DatasetContentSummaryTypeDef",
    "DatasetContentVersionValueTypeDef",
    "DatasetEntryTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTriggerTypeDef",
    "DatasetTypeDef",
    "DatastoreActivityTypeDef",
    "DatastoreStatisticsTypeDef",
    "DatastoreStorageSummaryTypeDef",
    "DatastoreStorageTypeDef",
    "DatastoreSummaryTypeDef",
    "DatastoreTypeDef",
    "DeltaTimeSessionWindowConfigurationTypeDef",
    "DeltaTimeTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDatastoreResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePipelineResponseTypeDef",
    "DeviceRegistryEnrichActivityTypeDef",
    "DeviceShadowEnrichActivityTypeDef",
    "EstimatedResourceSizeTypeDef",
    "FileFormatConfigurationTypeDef",
    "FilterActivityTypeDef",
    "GetDatasetContentResponseTypeDef",
    "GlueConfigurationTypeDef",
    "IotEventsDestinationConfigurationTypeDef",
    "LambdaActivityTypeDef",
    "LateDataRuleConfigurationTypeDef",
    "LateDataRuleTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDatasetContentsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDatastoresResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MathActivityTypeDef",
    "MessageTypeDef",
    "OutputFileUriValueTypeDef",
    "PaginatorConfigTypeDef",
    "ParquetConfigurationTypeDef",
    "PipelineActivityTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "QueryFilterTypeDef",
    "RemoveAttributesActivityTypeDef",
    "ReprocessingSummaryTypeDef",
    "ResourceConfigurationTypeDef",
    "RetentionPeriodTypeDef",
    "RunPipelineActivityResponseTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SampleChannelDataResponseTypeDef",
    "ScheduleTypeDef",
    "SchemaDefinitionTypeDef",
    "SelectAttributesActivityTypeDef",
    "SqlQueryDatasetActionTypeDef",
    "StartPipelineReprocessingResponseTypeDef",
    "TagTypeDef",
    "TriggeringDatasetTypeDef",
    "VariableTypeDef",
    "VersioningConfigurationTypeDef",
)

_RequiredAddAttributesActivityTypeDef = TypedDict(
    "_RequiredAddAttributesActivityTypeDef", {"name": str, "attributes": Dict[str, str]}
)
_OptionalAddAttributesActivityTypeDef = TypedDict(
    "_OptionalAddAttributesActivityTypeDef", {"next": str}, total=False
)


class AddAttributesActivityTypeDef(
    _RequiredAddAttributesActivityTypeDef, _OptionalAddAttributesActivityTypeDef
):
    pass


class BatchPutMessageErrorEntryTypeDef(TypedDict, total=False):
    messageId: str
    errorCode: str
    errorMessage: str


class BatchPutMessageResponseTypeDef(TypedDict, total=False):
    batchPutMessageErrorEntries: List["BatchPutMessageErrorEntryTypeDef"]


_RequiredChannelActivityTypeDef = TypedDict(
    "_RequiredChannelActivityTypeDef", {"name": str, "channelName": str}
)
_OptionalChannelActivityTypeDef = TypedDict(
    "_OptionalChannelActivityTypeDef", {"next": str}, total=False
)


class ChannelActivityTypeDef(_RequiredChannelActivityTypeDef, _OptionalChannelActivityTypeDef):
    pass


class ChannelMessagesTypeDef(TypedDict, total=False):
    s3Paths: List[str]


class ChannelStatisticsTypeDef(TypedDict, total=False):
    size: "EstimatedResourceSizeTypeDef"


class ChannelStorageSummaryTypeDef(TypedDict, total=False):
    serviceManagedS3: Dict[str, Any]
    customerManagedS3: "CustomerManagedChannelS3StorageSummaryTypeDef"


class ChannelStorageTypeDef(TypedDict, total=False):
    serviceManagedS3: Dict[str, Any]
    customerManagedS3: "CustomerManagedChannelS3StorageTypeDef"


class ChannelSummaryTypeDef(TypedDict, total=False):
    channelName: str
    channelStorage: "ChannelStorageSummaryTypeDef"
    status: ChannelStatus
    creationTime: datetime
    lastUpdateTime: datetime
    lastMessageArrivalTime: datetime


class ChannelTypeDef(TypedDict, total=False):
    name: str
    storage: "ChannelStorageTypeDef"
    arn: str
    status: ChannelStatus
    retentionPeriod: "RetentionPeriodTypeDef"
    creationTime: datetime
    lastUpdateTime: datetime
    lastMessageArrivalTime: datetime


ColumnTypeDef = TypedDict("ColumnTypeDef", {"name": str, "type": str})


class _RequiredContainerDatasetActionTypeDef(TypedDict):
    image: str
    executionRoleArn: str
    resourceConfiguration: "ResourceConfigurationTypeDef"


class ContainerDatasetActionTypeDef(_RequiredContainerDatasetActionTypeDef, total=False):
    variables: List["VariableTypeDef"]


class CreateChannelResponseTypeDef(TypedDict, total=False):
    channelName: str
    channelArn: str
    retentionPeriod: "RetentionPeriodTypeDef"


class CreateDatasetContentResponseTypeDef(TypedDict, total=False):
    versionId: str


class CreateDatasetResponseTypeDef(TypedDict, total=False):
    datasetName: str
    datasetArn: str
    retentionPeriod: "RetentionPeriodTypeDef"


class CreateDatastoreResponseTypeDef(TypedDict, total=False):
    datastoreName: str
    datastoreArn: str
    retentionPeriod: "RetentionPeriodTypeDef"


class CreatePipelineResponseTypeDef(TypedDict, total=False):
    pipelineName: str
    pipelineArn: str


class CustomerManagedChannelS3StorageSummaryTypeDef(TypedDict, total=False):
    bucket: str
    keyPrefix: str
    roleArn: str


class _RequiredCustomerManagedChannelS3StorageTypeDef(TypedDict):
    bucket: str
    roleArn: str


class CustomerManagedChannelS3StorageTypeDef(
    _RequiredCustomerManagedChannelS3StorageTypeDef, total=False
):
    keyPrefix: str


class CustomerManagedDatastoreS3StorageSummaryTypeDef(TypedDict, total=False):
    bucket: str
    keyPrefix: str
    roleArn: str


class _RequiredCustomerManagedDatastoreS3StorageTypeDef(TypedDict):
    bucket: str
    roleArn: str


class CustomerManagedDatastoreS3StorageTypeDef(
    _RequiredCustomerManagedDatastoreS3StorageTypeDef, total=False
):
    keyPrefix: str


class DatasetActionSummaryTypeDef(TypedDict, total=False):
    actionName: str
    actionType: DatasetActionType


class DatasetActionTypeDef(TypedDict, total=False):
    actionName: str
    queryAction: "SqlQueryDatasetActionTypeDef"
    containerAction: "ContainerDatasetActionTypeDef"


class DatasetContentDeliveryDestinationTypeDef(TypedDict, total=False):
    iotEventsDestinationConfiguration: "IotEventsDestinationConfigurationTypeDef"
    s3DestinationConfiguration: "S3DestinationConfigurationTypeDef"


class _RequiredDatasetContentDeliveryRuleTypeDef(TypedDict):
    destination: "DatasetContentDeliveryDestinationTypeDef"


class DatasetContentDeliveryRuleTypeDef(_RequiredDatasetContentDeliveryRuleTypeDef, total=False):
    entryName: str


class DatasetContentStatusTypeDef(TypedDict, total=False):
    state: DatasetContentState
    reason: str


class DatasetContentSummaryTypeDef(TypedDict, total=False):
    version: str
    status: "DatasetContentStatusTypeDef"
    creationTime: datetime
    scheduleTime: datetime
    completionTime: datetime


class DatasetContentVersionValueTypeDef(TypedDict):
    datasetName: str


class DatasetEntryTypeDef(TypedDict, total=False):
    entryName: str
    dataURI: str


class DatasetSummaryTypeDef(TypedDict, total=False):
    datasetName: str
    status: DatasetStatus
    creationTime: datetime
    lastUpdateTime: datetime
    triggers: List["DatasetTriggerTypeDef"]
    actions: List["DatasetActionSummaryTypeDef"]


class DatasetTriggerTypeDef(TypedDict, total=False):
    schedule: "ScheduleTypeDef"
    dataset: "TriggeringDatasetTypeDef"


class DatasetTypeDef(TypedDict, total=False):
    name: str
    arn: str
    actions: List["DatasetActionTypeDef"]
    triggers: List["DatasetTriggerTypeDef"]
    contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"]
    status: DatasetStatus
    creationTime: datetime
    lastUpdateTime: datetime
    retentionPeriod: "RetentionPeriodTypeDef"
    versioningConfiguration: "VersioningConfigurationTypeDef"
    lateDataRules: List["LateDataRuleTypeDef"]


class DatastoreActivityTypeDef(TypedDict):
    name: str
    datastoreName: str


class DatastoreStatisticsTypeDef(TypedDict, total=False):
    size: "EstimatedResourceSizeTypeDef"


class DatastoreStorageSummaryTypeDef(TypedDict, total=False):
    serviceManagedS3: Dict[str, Any]
    customerManagedS3: "CustomerManagedDatastoreS3StorageSummaryTypeDef"


class DatastoreStorageTypeDef(TypedDict, total=False):
    serviceManagedS3: Dict[str, Any]
    customerManagedS3: "CustomerManagedDatastoreS3StorageTypeDef"


class DatastoreSummaryTypeDef(TypedDict, total=False):
    datastoreName: str
    datastoreStorage: "DatastoreStorageSummaryTypeDef"
    status: DatastoreStatus
    creationTime: datetime
    lastUpdateTime: datetime
    lastMessageArrivalTime: datetime
    fileFormatType: FileFormatType


class DatastoreTypeDef(TypedDict, total=False):
    name: str
    storage: "DatastoreStorageTypeDef"
    arn: str
    status: DatastoreStatus
    retentionPeriod: "RetentionPeriodTypeDef"
    creationTime: datetime
    lastUpdateTime: datetime
    lastMessageArrivalTime: datetime
    fileFormatConfiguration: "FileFormatConfigurationTypeDef"


class DeltaTimeSessionWindowConfigurationTypeDef(TypedDict):
    timeoutInMinutes: int


class DeltaTimeTypeDef(TypedDict):
    offsetSeconds: int
    timeExpression: str


class DescribeChannelResponseTypeDef(TypedDict, total=False):
    channel: "ChannelTypeDef"
    statistics: "ChannelStatisticsTypeDef"


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    dataset: "DatasetTypeDef"


class DescribeDatastoreResponseTypeDef(TypedDict, total=False):
    datastore: "DatastoreTypeDef"
    statistics: "DatastoreStatisticsTypeDef"


class DescribeLoggingOptionsResponseTypeDef(TypedDict, total=False):
    loggingOptions: "LoggingOptionsTypeDef"


class DescribePipelineResponseTypeDef(TypedDict, total=False):
    pipeline: "PipelineTypeDef"


_RequiredDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceRegistryEnrichActivityTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalDeviceRegistryEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceRegistryEnrichActivityTypeDef", {"next": str}, total=False
)


class DeviceRegistryEnrichActivityTypeDef(
    _RequiredDeviceRegistryEnrichActivityTypeDef, _OptionalDeviceRegistryEnrichActivityTypeDef
):
    pass


_RequiredDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_RequiredDeviceShadowEnrichActivityTypeDef",
    {"name": str, "attribute": str, "thingName": str, "roleArn": str},
)
_OptionalDeviceShadowEnrichActivityTypeDef = TypedDict(
    "_OptionalDeviceShadowEnrichActivityTypeDef", {"next": str}, total=False
)


class DeviceShadowEnrichActivityTypeDef(
    _RequiredDeviceShadowEnrichActivityTypeDef, _OptionalDeviceShadowEnrichActivityTypeDef
):
    pass


class EstimatedResourceSizeTypeDef(TypedDict, total=False):
    estimatedSizeInBytes: float
    estimatedOn: datetime


class FileFormatConfigurationTypeDef(TypedDict, total=False):
    jsonConfiguration: Dict[str, Any]
    parquetConfiguration: "ParquetConfigurationTypeDef"


_RequiredFilterActivityTypeDef = TypedDict(
    "_RequiredFilterActivityTypeDef", {"name": str, "filter": str}
)
_OptionalFilterActivityTypeDef = TypedDict(
    "_OptionalFilterActivityTypeDef", {"next": str}, total=False
)


class FilterActivityTypeDef(_RequiredFilterActivityTypeDef, _OptionalFilterActivityTypeDef):
    pass


class GetDatasetContentResponseTypeDef(TypedDict, total=False):
    entries: List["DatasetEntryTypeDef"]
    timestamp: datetime
    status: "DatasetContentStatusTypeDef"


class GlueConfigurationTypeDef(TypedDict):
    tableName: str
    databaseName: str


class IotEventsDestinationConfigurationTypeDef(TypedDict):
    inputName: str
    roleArn: str


_RequiredLambdaActivityTypeDef = TypedDict(
    "_RequiredLambdaActivityTypeDef", {"name": str, "lambdaName": str, "batchSize": int}
)
_OptionalLambdaActivityTypeDef = TypedDict(
    "_OptionalLambdaActivityTypeDef", {"next": str}, total=False
)


class LambdaActivityTypeDef(_RequiredLambdaActivityTypeDef, _OptionalLambdaActivityTypeDef):
    pass


class LateDataRuleConfigurationTypeDef(TypedDict, total=False):
    deltaTimeSessionWindowConfiguration: "DeltaTimeSessionWindowConfigurationTypeDef"


class _RequiredLateDataRuleTypeDef(TypedDict):
    ruleConfiguration: "LateDataRuleConfigurationTypeDef"


class LateDataRuleTypeDef(_RequiredLateDataRuleTypeDef, total=False):
    ruleName: str


class ListChannelsResponseTypeDef(TypedDict, total=False):
    channelSummaries: List["ChannelSummaryTypeDef"]
    nextToken: str


class ListDatasetContentsResponseTypeDef(TypedDict, total=False):
    datasetContentSummaries: List["DatasetContentSummaryTypeDef"]
    nextToken: str


class ListDatasetsResponseTypeDef(TypedDict, total=False):
    datasetSummaries: List["DatasetSummaryTypeDef"]
    nextToken: str


class ListDatastoresResponseTypeDef(TypedDict, total=False):
    datastoreSummaries: List["DatastoreSummaryTypeDef"]
    nextToken: str


class ListPipelinesResponseTypeDef(TypedDict, total=False):
    pipelineSummaries: List["PipelineSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class LoggingOptionsTypeDef(TypedDict):
    roleArn: str
    level: Literal["ERROR"]
    enabled: bool


_RequiredMathActivityTypeDef = TypedDict(
    "_RequiredMathActivityTypeDef", {"name": str, "attribute": str, "math": str}
)
_OptionalMathActivityTypeDef = TypedDict("_OptionalMathActivityTypeDef", {"next": str}, total=False)


class MathActivityTypeDef(_RequiredMathActivityTypeDef, _OptionalMathActivityTypeDef):
    pass


class MessageTypeDef(TypedDict):
    messageId: str
    payload: Union[bytes, IO[bytes]]


class OutputFileUriValueTypeDef(TypedDict):
    fileName: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParquetConfigurationTypeDef(TypedDict, total=False):
    schemaDefinition: "SchemaDefinitionTypeDef"


PipelineActivityTypeDef = TypedDict(
    "PipelineActivityTypeDef",
    {
        "channel": "ChannelActivityTypeDef",
        "lambda": "LambdaActivityTypeDef",
        "datastore": "DatastoreActivityTypeDef",
        "addAttributes": "AddAttributesActivityTypeDef",
        "removeAttributes": "RemoveAttributesActivityTypeDef",
        "selectAttributes": "SelectAttributesActivityTypeDef",
        "filter": "FilterActivityTypeDef",
        "math": "MathActivityTypeDef",
        "deviceRegistryEnrich": "DeviceRegistryEnrichActivityTypeDef",
        "deviceShadowEnrich": "DeviceShadowEnrichActivityTypeDef",
    },
    total=False,
)


class PipelineSummaryTypeDef(TypedDict, total=False):
    pipelineName: str
    reprocessingSummaries: List["ReprocessingSummaryTypeDef"]
    creationTime: datetime
    lastUpdateTime: datetime


class PipelineTypeDef(TypedDict, total=False):
    name: str
    arn: str
    activities: List["PipelineActivityTypeDef"]
    reprocessingSummaries: List["ReprocessingSummaryTypeDef"]
    creationTime: datetime
    lastUpdateTime: datetime


class QueryFilterTypeDef(TypedDict, total=False):
    deltaTime: "DeltaTimeTypeDef"


_RequiredRemoveAttributesActivityTypeDef = TypedDict(
    "_RequiredRemoveAttributesActivityTypeDef", {"name": str, "attributes": List[str]}
)
_OptionalRemoveAttributesActivityTypeDef = TypedDict(
    "_OptionalRemoveAttributesActivityTypeDef", {"next": str}, total=False
)


class RemoveAttributesActivityTypeDef(
    _RequiredRemoveAttributesActivityTypeDef, _OptionalRemoveAttributesActivityTypeDef
):
    pass


ReprocessingSummaryTypeDef = TypedDict(
    "ReprocessingSummaryTypeDef",
    {"id": str, "status": ReprocessingStatus, "creationTime": datetime},
    total=False,
)


class ResourceConfigurationTypeDef(TypedDict):
    computeType: ComputeType
    volumeSizeInGB: int


class RetentionPeriodTypeDef(TypedDict, total=False):
    unlimited: bool
    numberOfDays: int


class RunPipelineActivityResponseTypeDef(TypedDict, total=False):
    payloads: List[Union[bytes, IO[bytes]]]
    logResult: str


class _RequiredS3DestinationConfigurationTypeDef(TypedDict):
    bucket: str
    key: str
    roleArn: str


class S3DestinationConfigurationTypeDef(_RequiredS3DestinationConfigurationTypeDef, total=False):
    glueConfiguration: "GlueConfigurationTypeDef"


class SampleChannelDataResponseTypeDef(TypedDict, total=False):
    payloads: List[Union[bytes, IO[bytes]]]


class ScheduleTypeDef(TypedDict, total=False):
    expression: str


class SchemaDefinitionTypeDef(TypedDict, total=False):
    columns: List["ColumnTypeDef"]


_RequiredSelectAttributesActivityTypeDef = TypedDict(
    "_RequiredSelectAttributesActivityTypeDef", {"name": str, "attributes": List[str]}
)
_OptionalSelectAttributesActivityTypeDef = TypedDict(
    "_OptionalSelectAttributesActivityTypeDef", {"next": str}, total=False
)


class SelectAttributesActivityTypeDef(
    _RequiredSelectAttributesActivityTypeDef, _OptionalSelectAttributesActivityTypeDef
):
    pass


class _RequiredSqlQueryDatasetActionTypeDef(TypedDict):
    sqlQuery: str


class SqlQueryDatasetActionTypeDef(_RequiredSqlQueryDatasetActionTypeDef, total=False):
    filters: List["QueryFilterTypeDef"]


class StartPipelineReprocessingResponseTypeDef(TypedDict, total=False):
    reprocessingId: str


class TagTypeDef(TypedDict):
    key: str
    value: str


class TriggeringDatasetTypeDef(TypedDict):
    name: str


class _RequiredVariableTypeDef(TypedDict):
    name: str


class VariableTypeDef(_RequiredVariableTypeDef, total=False):
    stringValue: str
    doubleValue: float
    datasetContentVersionValue: "DatasetContentVersionValueTypeDef"
    outputFileUriValue: "OutputFileUriValueTypeDef"


class VersioningConfigurationTypeDef(TypedDict, total=False):
    unlimited: bool
    maxVersions: int
