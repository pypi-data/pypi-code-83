"""
Type annotations for glue service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glue.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_glue.literals import (
    BackfillErrorCode,
    CatalogEncryptionMode,
    CloudWatchEncryptionMode,
    ColumnStatisticsType,
    Comparator,
    Compatibility,
    ConnectionPropertyKey,
    ConnectionType,
    CrawlerLineageSettings,
    CrawlerState,
    CrawlState,
    CsvHeaderOption,
    DeleteBehavior,
    JobBookmarksEncryptionMode,
    JobRunState,
    LastCrawlStatus,
    Logical,
    MLUserDataEncryptionModeString,
    NodeType,
    PartitionIndexStatus,
    Permission,
    PrincipalType,
    RecrawlBehavior,
    RegistryStatus,
    ResourceType,
    S3EncryptionMode,
    ScheduleState,
    SchemaStatus,
    SchemaVersionStatus,
    Sort,
    SortDirectionType,
    TaskRunSortColumnType,
    TaskStatusType,
    TaskType,
    TransformSortColumnType,
    TransformStatusType,
    TriggerState,
    TriggerType,
    UpdateBehavior,
    WorkerType,
    WorkflowRunStatus,
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
    "ActionTypeDef",
    "BackfillErrorTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "BatchGetJobsResponseTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CatalogEntryTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnTypeDef",
    "ConditionTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationMetricsTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesResponseTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsResponseTypeDef",
    "GetJobsResponseTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "GetMLTransformResponseTypeDef",
    "GetMLTransformsResponseTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "GetTableResponseTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsResponseTypeDef",
    "GetTablesResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersResponseTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "GluePolicyTypeDef",
    "GlueTableTypeDef",
    "GrokClassifierTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JsonClassifierTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MongoDBTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "OrderTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PredecessorTypeDef",
    "PredicateTypeDef",
    "PrincipalPermissionsTypeDef",
    "PropertyPredicateTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "RecrawlPolicyTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResourceUriTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "S3EncryptionTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
    "SchemaIdTypeDef",
    "SchemaListItemTypeDef",
    "SchemaReferenceTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SchemaVersionNumberTypeDef",
    "SearchTablesResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoTypeDef",
    "SortCriterionTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopTriggerResponseTypeDef",
    "StorageDescriptorTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableInputTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TaskRunTypeDef",
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
)


class ActionTypeDef(TypedDict, total=False):
    JobName: str
    Arguments: Dict[str, str]
    Timeout: int
    SecurityConfiguration: str
    NotificationProperty: "NotificationPropertyTypeDef"
    CrawlerName: str


class BackfillErrorTypeDef(TypedDict, total=False):
    Code: BackfillErrorCode
    Partitions: List["PartitionValueListTypeDef"]


class BatchCreatePartitionResponseTypeDef(TypedDict, total=False):
    Errors: List["PartitionErrorTypeDef"]


class BatchDeleteConnectionResponseTypeDef(TypedDict, total=False):
    Succeeded: List[str]
    Errors: Dict[str, "ErrorDetailTypeDef"]


class BatchDeletePartitionResponseTypeDef(TypedDict, total=False):
    Errors: List["PartitionErrorTypeDef"]


class BatchDeleteTableResponseTypeDef(TypedDict, total=False):
    Errors: List["TableErrorTypeDef"]


class BatchDeleteTableVersionResponseTypeDef(TypedDict, total=False):
    Errors: List["TableVersionErrorTypeDef"]


class BatchGetCrawlersResponseTypeDef(TypedDict, total=False):
    Crawlers: List["CrawlerTypeDef"]
    CrawlersNotFound: List[str]


class BatchGetDevEndpointsResponseTypeDef(TypedDict, total=False):
    DevEndpoints: List["DevEndpointTypeDef"]
    DevEndpointsNotFound: List[str]


class BatchGetJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobTypeDef"]
    JobsNotFound: List[str]


class BatchGetPartitionResponseTypeDef(TypedDict, total=False):
    Partitions: List["PartitionTypeDef"]
    UnprocessedKeys: List["PartitionValueListTypeDef"]


class BatchGetTriggersResponseTypeDef(TypedDict, total=False):
    Triggers: List["TriggerTypeDef"]
    TriggersNotFound: List[str]


class BatchGetWorkflowsResponseTypeDef(TypedDict, total=False):
    Workflows: List["WorkflowTypeDef"]
    MissingWorkflows: List[str]


class BatchStopJobRunErrorTypeDef(TypedDict, total=False):
    JobName: str
    JobRunId: str
    ErrorDetail: "ErrorDetailTypeDef"


class BatchStopJobRunResponseTypeDef(TypedDict, total=False):
    SuccessfulSubmissions: List["BatchStopJobRunSuccessfulSubmissionTypeDef"]
    Errors: List["BatchStopJobRunErrorTypeDef"]


class BatchStopJobRunSuccessfulSubmissionTypeDef(TypedDict, total=False):
    JobName: str
    JobRunId: str


class BatchUpdatePartitionFailureEntryTypeDef(TypedDict, total=False):
    PartitionValueList: List[str]
    ErrorDetail: "ErrorDetailTypeDef"


class BatchUpdatePartitionRequestEntryTypeDef(TypedDict):
    PartitionValueList: List[str]
    PartitionInput: "PartitionInputTypeDef"


class BatchUpdatePartitionResponseTypeDef(TypedDict, total=False):
    Errors: List["BatchUpdatePartitionFailureEntryTypeDef"]


class BinaryColumnStatisticsDataTypeDef(TypedDict):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int


class BooleanColumnStatisticsDataTypeDef(TypedDict):
    NumberOfTrues: int
    NumberOfFalses: int
    NumberOfNulls: int


class CancelMLTaskRunResponseTypeDef(TypedDict, total=False):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusType


class CatalogEntryTypeDef(TypedDict):
    DatabaseName: str
    TableName: str


class CatalogImportStatusTypeDef(TypedDict, total=False):
    ImportCompleted: bool
    ImportTime: datetime
    ImportedBy: str


class CatalogTargetTypeDef(TypedDict):
    DatabaseName: str
    Tables: List[str]


class CheckSchemaVersionValidityResponseTypeDef(TypedDict, total=False):
    Valid: bool
    Error: str


class ClassifierTypeDef(TypedDict, total=False):
    GrokClassifier: "GrokClassifierTypeDef"
    XMLClassifier: "XMLClassifierTypeDef"
    JsonClassifier: "JsonClassifierTypeDef"
    CsvClassifier: "CsvClassifierTypeDef"


class CloudWatchEncryptionTypeDef(TypedDict, total=False):
    CloudWatchEncryptionMode: CloudWatchEncryptionMode
    KmsKeyArn: str


class _RequiredCodeGenEdgeTypeDef(TypedDict):
    Source: str
    Target: str


class CodeGenEdgeTypeDef(_RequiredCodeGenEdgeTypeDef, total=False):
    TargetParameter: str


class _RequiredCodeGenNodeArgTypeDef(TypedDict):
    Name: str
    Value: str


class CodeGenNodeArgTypeDef(_RequiredCodeGenNodeArgTypeDef, total=False):
    Param: bool


class _RequiredCodeGenNodeTypeDef(TypedDict):
    Id: str
    NodeType: str
    Args: List["CodeGenNodeArgTypeDef"]


class CodeGenNodeTypeDef(_RequiredCodeGenNodeTypeDef, total=False):
    LineNumber: int


class ColumnErrorTypeDef(TypedDict, total=False):
    ColumnName: str
    Error: "ErrorDetailTypeDef"


class ColumnImportanceTypeDef(TypedDict, total=False):
    ColumnName: str
    Importance: float


_RequiredColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredColumnStatisticsDataTypeDef", {"Type": ColumnStatisticsType}
)
_OptionalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalColumnStatisticsDataTypeDef",
    {
        "BooleanColumnStatisticsData": "BooleanColumnStatisticsDataTypeDef",
        "DateColumnStatisticsData": "DateColumnStatisticsDataTypeDef",
        "DecimalColumnStatisticsData": "DecimalColumnStatisticsDataTypeDef",
        "DoubleColumnStatisticsData": "DoubleColumnStatisticsDataTypeDef",
        "LongColumnStatisticsData": "LongColumnStatisticsDataTypeDef",
        "StringColumnStatisticsData": "StringColumnStatisticsDataTypeDef",
        "BinaryColumnStatisticsData": "BinaryColumnStatisticsDataTypeDef",
    },
    total=False,
)


class ColumnStatisticsDataTypeDef(
    _RequiredColumnStatisticsDataTypeDef, _OptionalColumnStatisticsDataTypeDef
):
    pass


class ColumnStatisticsErrorTypeDef(TypedDict, total=False):
    ColumnStatistics: "ColumnStatisticsTypeDef"
    Error: "ErrorDetailTypeDef"


class ColumnStatisticsTypeDef(TypedDict):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: datetime
    StatisticsData: "ColumnStatisticsDataTypeDef"


_RequiredColumnTypeDef = TypedDict("_RequiredColumnTypeDef", {"Name": str})
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {"Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


class ConditionTypeDef(TypedDict, total=False):
    LogicalOperator: Literal["EQUALS"]
    JobName: str
    State: JobRunState
    CrawlerName: str
    CrawlState: CrawlState


class ConfusionMatrixTypeDef(TypedDict, total=False):
    NumTruePositives: int
    NumFalsePositives: int
    NumTrueNegatives: int
    NumFalseNegatives: int


class _RequiredConnectionInputTypeDef(TypedDict):
    Name: str
    ConnectionType: ConnectionType
    ConnectionProperties: Dict[ConnectionPropertyKey, str]


class ConnectionInputTypeDef(_RequiredConnectionInputTypeDef, total=False):
    Description: str
    MatchCriteria: List[str]
    PhysicalConnectionRequirements: "PhysicalConnectionRequirementsTypeDef"


class _RequiredConnectionPasswordEncryptionTypeDef(TypedDict):
    ReturnConnectionPasswordEncrypted: bool


class ConnectionPasswordEncryptionTypeDef(
    _RequiredConnectionPasswordEncryptionTypeDef, total=False
):
    AwsKmsKeyId: str


class ConnectionTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    ConnectionType: ConnectionType
    MatchCriteria: List[str]
    ConnectionProperties: Dict[ConnectionPropertyKey, str]
    PhysicalConnectionRequirements: "PhysicalConnectionRequirementsTypeDef"
    CreationTime: datetime
    LastUpdatedTime: datetime
    LastUpdatedBy: str


class ConnectionsListTypeDef(TypedDict, total=False):
    Connections: List[str]


class CrawlTypeDef(TypedDict, total=False):
    State: CrawlState
    StartedOn: datetime
    CompletedOn: datetime
    ErrorMessage: str
    LogGroup: str
    LogStream: str


class CrawlerMetricsTypeDef(TypedDict, total=False):
    CrawlerName: str
    TimeLeftSeconds: float
    StillEstimating: bool
    LastRuntimeSeconds: float
    MedianRuntimeSeconds: float
    TablesCreated: int
    TablesUpdated: int
    TablesDeleted: int


class CrawlerNodeDetailsTypeDef(TypedDict, total=False):
    Crawls: List["CrawlTypeDef"]


class CrawlerTargetsTypeDef(TypedDict, total=False):
    S3Targets: List["S3TargetTypeDef"]
    JdbcTargets: List["JdbcTargetTypeDef"]
    MongoDBTargets: List["MongoDBTargetTypeDef"]
    DynamoDBTargets: List["DynamoDBTargetTypeDef"]
    CatalogTargets: List["CatalogTargetTypeDef"]


class CrawlerTypeDef(TypedDict, total=False):
    Name: str
    Role: str
    Targets: "CrawlerTargetsTypeDef"
    DatabaseName: str
    Description: str
    Classifiers: List[str]
    RecrawlPolicy: "RecrawlPolicyTypeDef"
    SchemaChangePolicy: "SchemaChangePolicyTypeDef"
    LineageConfiguration: "LineageConfigurationTypeDef"
    State: CrawlerState
    TablePrefix: str
    Schedule: "ScheduleTypeDef"
    CrawlElapsedTime: int
    CreationTime: datetime
    LastUpdated: datetime
    LastCrawl: "LastCrawlInfoTypeDef"
    Version: int
    Configuration: str
    CrawlerSecurityConfiguration: str


class _RequiredCreateCsvClassifierRequestTypeDef(TypedDict):
    Name: str


class CreateCsvClassifierRequestTypeDef(_RequiredCreateCsvClassifierRequestTypeDef, total=False):
    Delimiter: str
    QuoteSymbol: str
    ContainsHeader: CsvHeaderOption
    Header: List[str]
    DisableValueTrimming: bool
    AllowSingleColumn: bool


class CreateDevEndpointResponseTypeDef(TypedDict, total=False):
    EndpointName: str
    Status: str
    SecurityGroupIds: List[str]
    SubnetId: str
    RoleArn: str
    YarnEndpointAddress: str
    ZeppelinRemoteSparkInterpreterPort: int
    NumberOfNodes: int
    WorkerType: WorkerType
    GlueVersion: str
    NumberOfWorkers: int
    AvailabilityZone: str
    VpcId: str
    ExtraPythonLibsS3Path: str
    ExtraJarsS3Path: str
    FailureReason: str
    SecurityConfiguration: str
    CreatedTimestamp: datetime
    Arguments: Dict[str, str]


class _RequiredCreateGrokClassifierRequestTypeDef(TypedDict):
    Classification: str
    Name: str
    GrokPattern: str


class CreateGrokClassifierRequestTypeDef(_RequiredCreateGrokClassifierRequestTypeDef, total=False):
    CustomPatterns: str


class CreateJobResponseTypeDef(TypedDict, total=False):
    Name: str


class CreateJsonClassifierRequestTypeDef(TypedDict):
    Name: str
    JsonPath: str


class CreateMLTransformResponseTypeDef(TypedDict, total=False):
    TransformId: str


class CreateRegistryResponseTypeDef(TypedDict, total=False):
    RegistryArn: str
    RegistryName: str
    Description: str
    Tags: Dict[str, str]


class CreateSchemaResponseTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: Literal["AVRO"]
    Compatibility: Compatibility
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatus
    Tags: Dict[str, str]
    SchemaVersionId: str
    SchemaVersionStatus: SchemaVersionStatus


class CreateScriptResponseTypeDef(TypedDict, total=False):
    PythonScript: str
    ScalaCode: str


class CreateSecurityConfigurationResponseTypeDef(TypedDict, total=False):
    Name: str
    CreatedTimestamp: datetime


class CreateTriggerResponseTypeDef(TypedDict, total=False):
    Name: str


class CreateWorkflowResponseTypeDef(TypedDict, total=False):
    Name: str


class _RequiredCreateXMLClassifierRequestTypeDef(TypedDict):
    Classification: str
    Name: str


class CreateXMLClassifierRequestTypeDef(_RequiredCreateXMLClassifierRequestTypeDef, total=False):
    RowTag: str


class _RequiredCsvClassifierTypeDef(TypedDict):
    Name: str


class CsvClassifierTypeDef(_RequiredCsvClassifierTypeDef, total=False):
    CreationTime: datetime
    LastUpdated: datetime
    Version: int
    Delimiter: str
    QuoteSymbol: str
    ContainsHeader: CsvHeaderOption
    Header: List[str]
    DisableValueTrimming: bool
    AllowSingleColumn: bool


class DataCatalogEncryptionSettingsTypeDef(TypedDict, total=False):
    EncryptionAtRest: "EncryptionAtRestTypeDef"
    ConnectionPasswordEncryption: "ConnectionPasswordEncryptionTypeDef"


class DataLakePrincipalTypeDef(TypedDict, total=False):
    DataLakePrincipalIdentifier: str


class DatabaseIdentifierTypeDef(TypedDict, total=False):
    CatalogId: str
    DatabaseName: str


class _RequiredDatabaseInputTypeDef(TypedDict):
    Name: str


class DatabaseInputTypeDef(_RequiredDatabaseInputTypeDef, total=False):
    Description: str
    LocationUri: str
    Parameters: Dict[str, str]
    CreateTableDefaultPermissions: List["PrincipalPermissionsTypeDef"]
    TargetDatabase: "DatabaseIdentifierTypeDef"


class _RequiredDatabaseTypeDef(TypedDict):
    Name: str


class DatabaseTypeDef(_RequiredDatabaseTypeDef, total=False):
    Description: str
    LocationUri: str
    Parameters: Dict[str, str]
    CreateTime: datetime
    CreateTableDefaultPermissions: List["PrincipalPermissionsTypeDef"]
    TargetDatabase: "DatabaseIdentifierTypeDef"
    CatalogId: str


class _RequiredDateColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int


class DateColumnStatisticsDataTypeDef(_RequiredDateColumnStatisticsDataTypeDef, total=False):
    MinimumValue: datetime
    MaximumValue: datetime


class _RequiredDecimalColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int


class DecimalColumnStatisticsDataTypeDef(_RequiredDecimalColumnStatisticsDataTypeDef, total=False):
    MinimumValue: "DecimalNumberTypeDef"
    MaximumValue: "DecimalNumberTypeDef"


class DecimalNumberTypeDef(TypedDict):
    UnscaledValue: Union[bytes, IO[bytes]]
    Scale: int


class DeleteJobResponseTypeDef(TypedDict, total=False):
    JobName: str


class DeleteMLTransformResponseTypeDef(TypedDict, total=False):
    TransformId: str


class DeleteRegistryResponseTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str
    Status: RegistryStatus


class DeleteSchemaResponseTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaName: str
    Status: SchemaStatus


class DeleteSchemaVersionsResponseTypeDef(TypedDict, total=False):
    SchemaVersionErrors: List["SchemaVersionErrorItemTypeDef"]


class DeleteTriggerResponseTypeDef(TypedDict, total=False):
    Name: str


class DeleteWorkflowResponseTypeDef(TypedDict, total=False):
    Name: str


class DevEndpointCustomLibrariesTypeDef(TypedDict, total=False):
    ExtraPythonLibsS3Path: str
    ExtraJarsS3Path: str


class DevEndpointTypeDef(TypedDict, total=False):
    EndpointName: str
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str
    YarnEndpointAddress: str
    PrivateAddress: str
    ZeppelinRemoteSparkInterpreterPort: int
    PublicAddress: str
    Status: str
    WorkerType: WorkerType
    GlueVersion: str
    NumberOfWorkers: int
    NumberOfNodes: int
    AvailabilityZone: str
    VpcId: str
    ExtraPythonLibsS3Path: str
    ExtraJarsS3Path: str
    FailureReason: str
    LastUpdateStatus: str
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    PublicKey: str
    PublicKeys: List[str]
    SecurityConfiguration: str
    Arguments: Dict[str, str]


class _RequiredDoubleColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int


class DoubleColumnStatisticsDataTypeDef(_RequiredDoubleColumnStatisticsDataTypeDef, total=False):
    MinimumValue: float
    MaximumValue: float


class DynamoDBTargetTypeDef(TypedDict, total=False):
    Path: str
    scanAll: bool
    scanRate: float


class EdgeTypeDef(TypedDict, total=False):
    SourceId: str
    DestinationId: str


class _RequiredEncryptionAtRestTypeDef(TypedDict):
    CatalogEncryptionMode: CatalogEncryptionMode


class EncryptionAtRestTypeDef(_RequiredEncryptionAtRestTypeDef, total=False):
    SseAwsKmsKeyId: str


class EncryptionConfigurationTypeDef(TypedDict, total=False):
    S3Encryption: List["S3EncryptionTypeDef"]
    CloudWatchEncryption: "CloudWatchEncryptionTypeDef"
    JobBookmarksEncryption: "JobBookmarksEncryptionTypeDef"


class ErrorDetailTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str


class ErrorDetailsTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str


class _RequiredEvaluationMetricsTypeDef(TypedDict):
    TransformType: Literal["FIND_MATCHES"]


class EvaluationMetricsTypeDef(_RequiredEvaluationMetricsTypeDef, total=False):
    FindMatchesMetrics: "FindMatchesMetricsTypeDef"


class ExecutionPropertyTypeDef(TypedDict, total=False):
    MaxConcurrentRuns: int


class ExportLabelsTaskRunPropertiesTypeDef(TypedDict, total=False):
    OutputS3Path: str


class FindMatchesMetricsTypeDef(TypedDict, total=False):
    AreaUnderPRCurve: float
    Precision: float
    Recall: float
    F1: float
    ConfusionMatrix: "ConfusionMatrixTypeDef"
    ColumnImportances: List["ColumnImportanceTypeDef"]


class FindMatchesParametersTypeDef(TypedDict, total=False):
    PrimaryKeyColumnName: str
    PrecisionRecallTradeoff: float
    AccuracyCostTradeoff: float
    EnforceProvidedLabels: bool


class FindMatchesTaskRunPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobRunId: str


class GetCatalogImportStatusResponseTypeDef(TypedDict, total=False):
    ImportStatus: "CatalogImportStatusTypeDef"


class GetClassifierResponseTypeDef(TypedDict, total=False):
    Classifier: "ClassifierTypeDef"


class GetClassifiersResponseTypeDef(TypedDict, total=False):
    Classifiers: List["ClassifierTypeDef"]
    NextToken: str


class GetColumnStatisticsForPartitionResponseTypeDef(TypedDict, total=False):
    ColumnStatisticsList: List["ColumnStatisticsTypeDef"]
    Errors: List["ColumnErrorTypeDef"]


class GetColumnStatisticsForTableResponseTypeDef(TypedDict, total=False):
    ColumnStatisticsList: List["ColumnStatisticsTypeDef"]
    Errors: List["ColumnErrorTypeDef"]


class GetConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class GetConnectionsFilterTypeDef(TypedDict, total=False):
    MatchCriteria: List[str]
    ConnectionType: ConnectionType


class GetConnectionsResponseTypeDef(TypedDict, total=False):
    ConnectionList: List["ConnectionTypeDef"]
    NextToken: str


class GetCrawlerMetricsResponseTypeDef(TypedDict, total=False):
    CrawlerMetricsList: List["CrawlerMetricsTypeDef"]
    NextToken: str


class GetCrawlerResponseTypeDef(TypedDict, total=False):
    Crawler: "CrawlerTypeDef"


class GetCrawlersResponseTypeDef(TypedDict, total=False):
    Crawlers: List["CrawlerTypeDef"]
    NextToken: str


class GetDataCatalogEncryptionSettingsResponseTypeDef(TypedDict, total=False):
    DataCatalogEncryptionSettings: "DataCatalogEncryptionSettingsTypeDef"


class GetDatabaseResponseTypeDef(TypedDict, total=False):
    Database: "DatabaseTypeDef"


class _RequiredGetDatabasesResponseTypeDef(TypedDict):
    DatabaseList: List["DatabaseTypeDef"]


class GetDatabasesResponseTypeDef(_RequiredGetDatabasesResponseTypeDef, total=False):
    NextToken: str


class GetDataflowGraphResponseTypeDef(TypedDict, total=False):
    DagNodes: List["CodeGenNodeTypeDef"]
    DagEdges: List["CodeGenEdgeTypeDef"]


class GetDevEndpointResponseTypeDef(TypedDict, total=False):
    DevEndpoint: "DevEndpointTypeDef"


class GetDevEndpointsResponseTypeDef(TypedDict, total=False):
    DevEndpoints: List["DevEndpointTypeDef"]
    NextToken: str


class GetJobBookmarkResponseTypeDef(TypedDict, total=False):
    JobBookmarkEntry: "JobBookmarkEntryTypeDef"


class GetJobResponseTypeDef(TypedDict, total=False):
    Job: "JobTypeDef"


class GetJobRunResponseTypeDef(TypedDict, total=False):
    JobRun: "JobRunTypeDef"


class GetJobRunsResponseTypeDef(TypedDict, total=False):
    JobRuns: List["JobRunTypeDef"]
    NextToken: str


class GetJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobTypeDef"]
    NextToken: str


class GetMLTaskRunResponseTypeDef(TypedDict, total=False):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusType
    LogGroupName: str
    Properties: "TaskRunPropertiesTypeDef"
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int


class GetMLTaskRunsResponseTypeDef(TypedDict, total=False):
    TaskRuns: List["TaskRunTypeDef"]
    NextToken: str


class GetMLTransformResponseTypeDef(TypedDict, total=False):
    TransformId: str
    Name: str
    Description: str
    Status: TransformStatusType
    CreatedOn: datetime
    LastModifiedOn: datetime
    InputRecordTables: List["GlueTableTypeDef"]
    Parameters: "TransformParametersTypeDef"
    EvaluationMetrics: "EvaluationMetricsTypeDef"
    LabelCount: int
    Schema: List["SchemaColumnTypeDef"]
    Role: str
    GlueVersion: str
    MaxCapacity: float
    WorkerType: WorkerType
    NumberOfWorkers: int
    Timeout: int
    MaxRetries: int
    TransformEncryption: "TransformEncryptionTypeDef"


class _RequiredGetMLTransformsResponseTypeDef(TypedDict):
    Transforms: List["MLTransformTypeDef"]


class GetMLTransformsResponseTypeDef(_RequiredGetMLTransformsResponseTypeDef, total=False):
    NextToken: str


GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef", {"Mapping": List["MappingEntryTypeDef"]}
)


class GetPartitionIndexesResponseTypeDef(TypedDict, total=False):
    PartitionIndexDescriptorList: List["PartitionIndexDescriptorTypeDef"]
    NextToken: str


class GetPartitionResponseTypeDef(TypedDict, total=False):
    Partition: "PartitionTypeDef"


class GetPartitionsResponseTypeDef(TypedDict, total=False):
    Partitions: List["PartitionTypeDef"]
    NextToken: str


class GetPlanResponseTypeDef(TypedDict, total=False):
    PythonScript: str
    ScalaCode: str


class GetRegistryResponseTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatus
    CreatedTime: str
    UpdatedTime: str


class GetResourcePoliciesResponseTypeDef(TypedDict, total=False):
    GetResourcePoliciesResponseList: List["GluePolicyTypeDef"]
    NextToken: str


class GetResourcePolicyResponseTypeDef(TypedDict, total=False):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime


class GetSchemaByDefinitionResponseTypeDef(TypedDict, total=False):
    SchemaVersionId: str
    SchemaArn: str
    DataFormat: Literal["AVRO"]
    Status: SchemaVersionStatus
    CreatedTime: str


class GetSchemaResponseTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: Literal["AVRO"]
    Compatibility: Compatibility
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatus
    CreatedTime: str
    UpdatedTime: str


class GetSchemaVersionResponseTypeDef(TypedDict, total=False):
    SchemaVersionId: str
    SchemaDefinition: str
    DataFormat: Literal["AVRO"]
    SchemaArn: str
    VersionNumber: int
    Status: SchemaVersionStatus
    CreatedTime: str


class GetSchemaVersionsDiffResponseTypeDef(TypedDict, total=False):
    Diff: str


class GetSecurityConfigurationResponseTypeDef(TypedDict, total=False):
    SecurityConfiguration: "SecurityConfigurationTypeDef"


class GetSecurityConfigurationsResponseTypeDef(TypedDict, total=False):
    SecurityConfigurations: List["SecurityConfigurationTypeDef"]
    NextToken: str


class GetTableResponseTypeDef(TypedDict, total=False):
    Table: "TableTypeDef"


class GetTableVersionResponseTypeDef(TypedDict, total=False):
    TableVersion: "TableVersionTypeDef"


class GetTableVersionsResponseTypeDef(TypedDict, total=False):
    TableVersions: List["TableVersionTypeDef"]
    NextToken: str


class GetTablesResponseTypeDef(TypedDict, total=False):
    TableList: List["TableTypeDef"]
    NextToken: str


class GetTagsResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class GetTriggerResponseTypeDef(TypedDict, total=False):
    Trigger: "TriggerTypeDef"


class GetTriggersResponseTypeDef(TypedDict, total=False):
    Triggers: List["TriggerTypeDef"]
    NextToken: str


class GetUserDefinedFunctionResponseTypeDef(TypedDict, total=False):
    UserDefinedFunction: "UserDefinedFunctionTypeDef"


class GetUserDefinedFunctionsResponseTypeDef(TypedDict, total=False):
    UserDefinedFunctions: List["UserDefinedFunctionTypeDef"]
    NextToken: str


class GetWorkflowResponseTypeDef(TypedDict, total=False):
    Workflow: "WorkflowTypeDef"


class GetWorkflowRunPropertiesResponseTypeDef(TypedDict, total=False):
    RunProperties: Dict[str, str]


class GetWorkflowRunResponseTypeDef(TypedDict, total=False):
    Run: "WorkflowRunTypeDef"


class GetWorkflowRunsResponseTypeDef(TypedDict, total=False):
    Runs: List["WorkflowRunTypeDef"]
    NextToken: str


class GluePolicyTypeDef(TypedDict, total=False):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime


class _RequiredGlueTableTypeDef(TypedDict):
    DatabaseName: str
    TableName: str


class GlueTableTypeDef(_RequiredGlueTableTypeDef, total=False):
    CatalogId: str
    ConnectionName: str


class _RequiredGrokClassifierTypeDef(TypedDict):
    Name: str
    Classification: str
    GrokPattern: str


class GrokClassifierTypeDef(_RequiredGrokClassifierTypeDef, total=False):
    CreationTime: datetime
    LastUpdated: datetime
    Version: int
    CustomPatterns: str


class ImportLabelsTaskRunPropertiesTypeDef(TypedDict, total=False):
    InputS3Path: str
    Replace: bool


class JdbcTargetTypeDef(TypedDict, total=False):
    ConnectionName: str
    Path: str
    Exclusions: List[str]


class JobBookmarkEntryTypeDef(TypedDict, total=False):
    JobName: str
    Version: int
    Run: int
    Attempt: int
    PreviousRunId: str
    RunId: str
    JobBookmark: str


class JobBookmarksEncryptionTypeDef(TypedDict, total=False):
    JobBookmarksEncryptionMode: JobBookmarksEncryptionMode
    KmsKeyArn: str


class JobCommandTypeDef(TypedDict, total=False):
    Name: str
    ScriptLocation: str
    PythonVersion: str


class JobNodeDetailsTypeDef(TypedDict, total=False):
    JobRuns: List["JobRunTypeDef"]


class JobRunTypeDef(TypedDict, total=False):
    Id: str
    Attempt: int
    PreviousRunId: str
    TriggerName: str
    JobName: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    JobRunState: JobRunState
    Arguments: Dict[str, str]
    ErrorMessage: str
    PredecessorRuns: List["PredecessorTypeDef"]
    AllocatedCapacity: int
    ExecutionTime: int
    Timeout: int
    MaxCapacity: float
    WorkerType: WorkerType
    NumberOfWorkers: int
    SecurityConfiguration: str
    LogGroupName: str
    NotificationProperty: "NotificationPropertyTypeDef"
    GlueVersion: str


class JobTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    LogUri: str
    Role: str
    CreatedOn: datetime
    LastModifiedOn: datetime
    ExecutionProperty: "ExecutionPropertyTypeDef"
    Command: "JobCommandTypeDef"
    DefaultArguments: Dict[str, str]
    NonOverridableArguments: Dict[str, str]
    Connections: "ConnectionsListTypeDef"
    MaxRetries: int
    AllocatedCapacity: int
    Timeout: int
    MaxCapacity: float
    WorkerType: WorkerType
    NumberOfWorkers: int
    SecurityConfiguration: str
    NotificationProperty: "NotificationPropertyTypeDef"
    GlueVersion: str


class JobUpdateTypeDef(TypedDict, total=False):
    Description: str
    LogUri: str
    Role: str
    ExecutionProperty: "ExecutionPropertyTypeDef"
    Command: "JobCommandTypeDef"
    DefaultArguments: Dict[str, str]
    NonOverridableArguments: Dict[str, str]
    Connections: "ConnectionsListTypeDef"
    MaxRetries: int
    AllocatedCapacity: int
    Timeout: int
    MaxCapacity: float
    WorkerType: WorkerType
    NumberOfWorkers: int
    SecurityConfiguration: str
    NotificationProperty: "NotificationPropertyTypeDef"
    GlueVersion: str


class _RequiredJsonClassifierTypeDef(TypedDict):
    Name: str
    JsonPath: str


class JsonClassifierTypeDef(_RequiredJsonClassifierTypeDef, total=False):
    CreationTime: datetime
    LastUpdated: datetime
    Version: int


KeySchemaElementTypeDef = TypedDict("KeySchemaElementTypeDef", {"Name": str, "Type": str})


class LabelingSetGenerationTaskRunPropertiesTypeDef(TypedDict, total=False):
    OutputS3Path: str


class LastCrawlInfoTypeDef(TypedDict, total=False):
    Status: LastCrawlStatus
    ErrorMessage: str
    LogGroup: str
    LogStream: str
    MessagePrefix: str
    StartTime: datetime


class LineageConfigurationTypeDef(TypedDict, total=False):
    CrawlerLineageSettings: CrawlerLineageSettings


class ListCrawlersResponseTypeDef(TypedDict, total=False):
    CrawlerNames: List[str]
    NextToken: str


class ListDevEndpointsResponseTypeDef(TypedDict, total=False):
    DevEndpointNames: List[str]
    NextToken: str


class ListJobsResponseTypeDef(TypedDict, total=False):
    JobNames: List[str]
    NextToken: str


class _RequiredListMLTransformsResponseTypeDef(TypedDict):
    TransformIds: List[str]


class ListMLTransformsResponseTypeDef(_RequiredListMLTransformsResponseTypeDef, total=False):
    NextToken: str


class ListRegistriesResponseTypeDef(TypedDict, total=False):
    Registries: List["RegistryListItemTypeDef"]
    NextToken: str


class ListSchemaVersionsResponseTypeDef(TypedDict, total=False):
    Schemas: List["SchemaVersionListItemTypeDef"]
    NextToken: str


class ListSchemasResponseTypeDef(TypedDict, total=False):
    Schemas: List["SchemaListItemTypeDef"]
    NextToken: str


class ListTriggersResponseTypeDef(TypedDict, total=False):
    TriggerNames: List[str]
    NextToken: str


class ListWorkflowsResponseTypeDef(TypedDict, total=False):
    Workflows: List[str]
    NextToken: str


class LocationTypeDef(TypedDict, total=False):
    Jdbc: List["CodeGenNodeArgTypeDef"]
    S3: List["CodeGenNodeArgTypeDef"]
    DynamoDB: List["CodeGenNodeArgTypeDef"]


class _RequiredLongColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int


class LongColumnStatisticsDataTypeDef(_RequiredLongColumnStatisticsDataTypeDef, total=False):
    MinimumValue: int
    MaximumValue: int


class MLTransformTypeDef(TypedDict, total=False):
    TransformId: str
    Name: str
    Description: str
    Status: TransformStatusType
    CreatedOn: datetime
    LastModifiedOn: datetime
    InputRecordTables: List["GlueTableTypeDef"]
    Parameters: "TransformParametersTypeDef"
    EvaluationMetrics: "EvaluationMetricsTypeDef"
    LabelCount: int
    Schema: List["SchemaColumnTypeDef"]
    Role: str
    GlueVersion: str
    MaxCapacity: float
    WorkerType: WorkerType
    NumberOfWorkers: int
    Timeout: int
    MaxRetries: int
    TransformEncryption: "TransformEncryptionTypeDef"


class _RequiredMLUserDataEncryptionTypeDef(TypedDict):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeString


class MLUserDataEncryptionTypeDef(_RequiredMLUserDataEncryptionTypeDef, total=False):
    KmsKeyId: str


class MappingEntryTypeDef(TypedDict, total=False):
    SourceTable: str
    SourcePath: str
    SourceType: str
    TargetTable: str
    TargetPath: str
    TargetType: str


class MetadataInfoTypeDef(TypedDict, total=False):
    MetadataValue: str
    CreatedTime: str
    OtherMetadataValueList: List["OtherMetadataValueListItemTypeDef"]


class MetadataKeyValuePairTypeDef(TypedDict, total=False):
    MetadataKey: str
    MetadataValue: str


class MongoDBTargetTypeDef(TypedDict, total=False):
    ConnectionName: str
    Path: str
    ScanAll: bool


NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NodeType,
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": "TriggerNodeDetailsTypeDef",
        "JobDetails": "JobNodeDetailsTypeDef",
        "CrawlerDetails": "CrawlerNodeDetailsTypeDef",
    },
    total=False,
)


class NotificationPropertyTypeDef(TypedDict, total=False):
    NotifyDelayAfter: int


class OrderTypeDef(TypedDict):
    Column: str
    SortOrder: int


class OtherMetadataValueListItemTypeDef(TypedDict, total=False):
    MetadataValue: str
    CreatedTime: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartitionErrorTypeDef(TypedDict, total=False):
    PartitionValues: List[str]
    ErrorDetail: "ErrorDetailTypeDef"


class _RequiredPartitionIndexDescriptorTypeDef(TypedDict):
    IndexName: str
    Keys: List["KeySchemaElementTypeDef"]
    IndexStatus: PartitionIndexStatus


class PartitionIndexDescriptorTypeDef(_RequiredPartitionIndexDescriptorTypeDef, total=False):
    BackfillErrors: List["BackfillErrorTypeDef"]


class PartitionIndexTypeDef(TypedDict):
    Keys: List[str]
    IndexName: str


class PartitionInputTypeDef(TypedDict, total=False):
    Values: List[str]
    LastAccessTime: datetime
    StorageDescriptor: "StorageDescriptorTypeDef"
    Parameters: Dict[str, str]
    LastAnalyzedTime: datetime


class PartitionTypeDef(TypedDict, total=False):
    Values: List[str]
    DatabaseName: str
    TableName: str
    CreationTime: datetime
    LastAccessTime: datetime
    StorageDescriptor: "StorageDescriptorTypeDef"
    Parameters: Dict[str, str]
    LastAnalyzedTime: datetime
    CatalogId: str


class PartitionValueListTypeDef(TypedDict):
    Values: List[str]


class PhysicalConnectionRequirementsTypeDef(TypedDict, total=False):
    SubnetId: str
    SecurityGroupIdList: List[str]
    AvailabilityZone: str


class PredecessorTypeDef(TypedDict, total=False):
    JobName: str
    RunId: str


class PredicateTypeDef(TypedDict, total=False):
    Logical: Logical
    Conditions: List["ConditionTypeDef"]


class PrincipalPermissionsTypeDef(TypedDict, total=False):
    Principal: "DataLakePrincipalTypeDef"
    Permissions: List[Permission]


class PropertyPredicateTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    Comparator: Comparator


class PutResourcePolicyResponseTypeDef(TypedDict, total=False):
    PolicyHash: str


class PutSchemaVersionMetadataResponseTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str


class QuerySchemaVersionMetadataResponseTypeDef(TypedDict, total=False):
    MetadataInfoMap: Dict[str, "MetadataInfoTypeDef"]
    SchemaVersionId: str
    NextToken: str


class RecrawlPolicyTypeDef(TypedDict, total=False):
    RecrawlBehavior: RecrawlBehavior


class RegisterSchemaVersionResponseTypeDef(TypedDict, total=False):
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatus


class RegistryIdTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str


class RegistryListItemTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatus
    CreatedTime: str
    UpdatedTime: str


class RemoveSchemaVersionMetadataResponseTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str


class ResetJobBookmarkResponseTypeDef(TypedDict, total=False):
    JobBookmarkEntry: "JobBookmarkEntryTypeDef"


class ResourceUriTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    Uri: str


class ResumeWorkflowRunResponseTypeDef(TypedDict, total=False):
    RunId: str
    NodeIds: List[str]


class S3EncryptionTypeDef(TypedDict, total=False):
    S3EncryptionMode: S3EncryptionMode
    KmsKeyArn: str


class S3TargetTypeDef(TypedDict, total=False):
    Path: str
    Exclusions: List[str]
    ConnectionName: str


class ScheduleTypeDef(TypedDict, total=False):
    ScheduleExpression: str
    State: ScheduleState


class SchemaChangePolicyTypeDef(TypedDict, total=False):
    UpdateBehavior: UpdateBehavior
    DeleteBehavior: DeleteBehavior


class SchemaColumnTypeDef(TypedDict, total=False):
    Name: str
    DataType: str


class SchemaIdTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaName: str
    RegistryName: str


class SchemaListItemTypeDef(TypedDict, total=False):
    RegistryName: str
    SchemaName: str
    SchemaArn: str
    Description: str
    SchemaStatus: SchemaStatus
    CreatedTime: str
    UpdatedTime: str


class SchemaReferenceTypeDef(TypedDict, total=False):
    SchemaId: "SchemaIdTypeDef"
    SchemaVersionId: str
    SchemaVersionNumber: int


class SchemaVersionErrorItemTypeDef(TypedDict, total=False):
    VersionNumber: int
    ErrorDetails: "ErrorDetailsTypeDef"


class SchemaVersionListItemTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatus
    CreatedTime: str


class SchemaVersionNumberTypeDef(TypedDict, total=False):
    LatestVersion: bool
    VersionNumber: int


class SearchTablesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    TableList: List["TableTypeDef"]


class SecurityConfigurationTypeDef(TypedDict, total=False):
    Name: str
    CreatedTimeStamp: datetime
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"


class SegmentTypeDef(TypedDict):
    SegmentNumber: int
    TotalSegments: int


class SerDeInfoTypeDef(TypedDict, total=False):
    Name: str
    SerializationLibrary: str
    Parameters: Dict[str, str]


class SkewedInfoTypeDef(TypedDict, total=False):
    SkewedColumnNames: List[str]
    SkewedColumnValues: List[str]
    SkewedColumnValueLocationMaps: Dict[str, str]


class SortCriterionTypeDef(TypedDict, total=False):
    FieldName: str
    Sort: Sort


class StartExportLabelsTaskRunResponseTypeDef(TypedDict, total=False):
    TaskRunId: str


class StartImportLabelsTaskRunResponseTypeDef(TypedDict, total=False):
    TaskRunId: str


class StartJobRunResponseTypeDef(TypedDict, total=False):
    JobRunId: str


class StartMLEvaluationTaskRunResponseTypeDef(TypedDict, total=False):
    TaskRunId: str


class StartMLLabelingSetGenerationTaskRunResponseTypeDef(TypedDict, total=False):
    TaskRunId: str


class StartTriggerResponseTypeDef(TypedDict, total=False):
    Name: str


class StartWorkflowRunResponseTypeDef(TypedDict, total=False):
    RunId: str


class StopTriggerResponseTypeDef(TypedDict, total=False):
    Name: str


class StorageDescriptorTypeDef(TypedDict, total=False):
    Columns: List["ColumnTypeDef"]
    Location: str
    InputFormat: str
    OutputFormat: str
    Compressed: bool
    NumberOfBuckets: int
    SerdeInfo: "SerDeInfoTypeDef"
    BucketColumns: List[str]
    SortColumns: List["OrderTypeDef"]
    Parameters: Dict[str, str]
    SkewedInfo: "SkewedInfoTypeDef"
    StoredAsSubDirectories: bool
    SchemaReference: "SchemaReferenceTypeDef"


class StringColumnStatisticsDataTypeDef(TypedDict):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int
    NumberOfDistinctValues: int


class TableErrorTypeDef(TypedDict, total=False):
    TableName: str
    ErrorDetail: "ErrorDetailTypeDef"


class TableIdentifierTypeDef(TypedDict, total=False):
    CatalogId: str
    DatabaseName: str
    Name: str


class _RequiredTableInputTypeDef(TypedDict):
    Name: str


class TableInputTypeDef(_RequiredTableInputTypeDef, total=False):
    Description: str
    Owner: str
    LastAccessTime: datetime
    LastAnalyzedTime: datetime
    Retention: int
    StorageDescriptor: "StorageDescriptorTypeDef"
    PartitionKeys: List["ColumnTypeDef"]
    ViewOriginalText: str
    ViewExpandedText: str
    TableType: str
    Parameters: Dict[str, str]
    TargetTable: "TableIdentifierTypeDef"


class _RequiredTableTypeDef(TypedDict):
    Name: str


class TableTypeDef(_RequiredTableTypeDef, total=False):
    DatabaseName: str
    Description: str
    Owner: str
    CreateTime: datetime
    UpdateTime: datetime
    LastAccessTime: datetime
    LastAnalyzedTime: datetime
    Retention: int
    StorageDescriptor: "StorageDescriptorTypeDef"
    PartitionKeys: List["ColumnTypeDef"]
    ViewOriginalText: str
    ViewExpandedText: str
    TableType: str
    Parameters: Dict[str, str]
    CreatedBy: str
    IsRegisteredWithLakeFormation: bool
    TargetTable: "TableIdentifierTypeDef"
    CatalogId: str


class TableVersionErrorTypeDef(TypedDict, total=False):
    TableName: str
    VersionId: str
    ErrorDetail: "ErrorDetailTypeDef"


class TableVersionTypeDef(TypedDict, total=False):
    Table: "TableTypeDef"
    VersionId: str


class TaskRunFilterCriteriaTypeDef(TypedDict, total=False):
    TaskRunType: TaskType
    Status: TaskStatusType
    StartedBefore: datetime
    StartedAfter: datetime


class TaskRunPropertiesTypeDef(TypedDict, total=False):
    TaskType: TaskType
    ImportLabelsTaskRunProperties: "ImportLabelsTaskRunPropertiesTypeDef"
    ExportLabelsTaskRunProperties: "ExportLabelsTaskRunPropertiesTypeDef"
    LabelingSetGenerationTaskRunProperties: "LabelingSetGenerationTaskRunPropertiesTypeDef"
    FindMatchesTaskRunProperties: "FindMatchesTaskRunPropertiesTypeDef"


class TaskRunSortCriteriaTypeDef(TypedDict):
    Column: TaskRunSortColumnType
    SortDirection: SortDirectionType


class TaskRunTypeDef(TypedDict, total=False):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusType
    LogGroupName: str
    Properties: "TaskRunPropertiesTypeDef"
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int


class TransformEncryptionTypeDef(TypedDict, total=False):
    MlUserDataEncryption: "MLUserDataEncryptionTypeDef"
    TaskRunSecurityConfigurationName: str


class TransformFilterCriteriaTypeDef(TypedDict, total=False):
    Name: str
    TransformType: Literal["FIND_MATCHES"]
    Status: TransformStatusType
    GlueVersion: str
    CreatedBefore: datetime
    CreatedAfter: datetime
    LastModifiedBefore: datetime
    LastModifiedAfter: datetime
    Schema: List["SchemaColumnTypeDef"]


class _RequiredTransformParametersTypeDef(TypedDict):
    TransformType: Literal["FIND_MATCHES"]


class TransformParametersTypeDef(_RequiredTransformParametersTypeDef, total=False):
    FindMatchesParameters: "FindMatchesParametersTypeDef"


class TransformSortCriteriaTypeDef(TypedDict):
    Column: TransformSortColumnType
    SortDirection: SortDirectionType


class TriggerNodeDetailsTypeDef(TypedDict, total=False):
    Trigger: "TriggerTypeDef"


TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": TriggerType,
        "State": TriggerState,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
    },
    total=False,
)


class TriggerUpdateTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    Schedule: str
    Actions: List["ActionTypeDef"]
    Predicate: "PredicateTypeDef"


class UpdateColumnStatisticsForPartitionResponseTypeDef(TypedDict, total=False):
    Errors: List["ColumnStatisticsErrorTypeDef"]


class UpdateColumnStatisticsForTableResponseTypeDef(TypedDict, total=False):
    Errors: List["ColumnStatisticsErrorTypeDef"]


class _RequiredUpdateCsvClassifierRequestTypeDef(TypedDict):
    Name: str


class UpdateCsvClassifierRequestTypeDef(_RequiredUpdateCsvClassifierRequestTypeDef, total=False):
    Delimiter: str
    QuoteSymbol: str
    ContainsHeader: CsvHeaderOption
    Header: List[str]
    DisableValueTrimming: bool
    AllowSingleColumn: bool


class _RequiredUpdateGrokClassifierRequestTypeDef(TypedDict):
    Name: str


class UpdateGrokClassifierRequestTypeDef(_RequiredUpdateGrokClassifierRequestTypeDef, total=False):
    Classification: str
    GrokPattern: str
    CustomPatterns: str


class UpdateJobResponseTypeDef(TypedDict, total=False):
    JobName: str


class _RequiredUpdateJsonClassifierRequestTypeDef(TypedDict):
    Name: str


class UpdateJsonClassifierRequestTypeDef(_RequiredUpdateJsonClassifierRequestTypeDef, total=False):
    JsonPath: str


class UpdateMLTransformResponseTypeDef(TypedDict, total=False):
    TransformId: str


class UpdateRegistryResponseTypeDef(TypedDict, total=False):
    RegistryName: str
    RegistryArn: str


class UpdateSchemaResponseTypeDef(TypedDict, total=False):
    SchemaArn: str
    SchemaName: str
    RegistryName: str


class UpdateTriggerResponseTypeDef(TypedDict, total=False):
    Trigger: "TriggerTypeDef"


class UpdateWorkflowResponseTypeDef(TypedDict, total=False):
    Name: str


class _RequiredUpdateXMLClassifierRequestTypeDef(TypedDict):
    Name: str


class UpdateXMLClassifierRequestTypeDef(_RequiredUpdateXMLClassifierRequestTypeDef, total=False):
    Classification: str
    RowTag: str


class UserDefinedFunctionInputTypeDef(TypedDict, total=False):
    FunctionName: str
    ClassName: str
    OwnerName: str
    OwnerType: PrincipalType
    ResourceUris: List["ResourceUriTypeDef"]


class UserDefinedFunctionTypeDef(TypedDict, total=False):
    FunctionName: str
    DatabaseName: str
    ClassName: str
    OwnerName: str
    OwnerType: PrincipalType
    CreateTime: datetime
    ResourceUris: List["ResourceUriTypeDef"]
    CatalogId: str


class WorkflowGraphTypeDef(TypedDict, total=False):
    Nodes: List["NodeTypeDef"]
    Edges: List["EdgeTypeDef"]


class WorkflowRunStatisticsTypeDef(TypedDict, total=False):
    TotalActions: int
    TimeoutActions: int
    FailedActions: int
    StoppedActions: int
    SucceededActions: int
    RunningActions: int


class WorkflowRunTypeDef(TypedDict, total=False):
    Name: str
    WorkflowRunId: str
    PreviousRunId: str
    WorkflowRunProperties: Dict[str, str]
    StartedOn: datetime
    CompletedOn: datetime
    Status: WorkflowRunStatus
    ErrorMessage: str
    Statistics: "WorkflowRunStatisticsTypeDef"
    Graph: "WorkflowGraphTypeDef"


class WorkflowTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    DefaultRunProperties: Dict[str, str]
    CreatedOn: datetime
    LastModifiedOn: datetime
    LastRun: "WorkflowRunTypeDef"
    Graph: "WorkflowGraphTypeDef"
    MaxConcurrentRuns: int


class _RequiredXMLClassifierTypeDef(TypedDict):
    Name: str
    Classification: str


class XMLClassifierTypeDef(_RequiredXMLClassifierTypeDef, total=False):
    CreationTime: datetime
    LastUpdated: datetime
    Version: int
    RowTag: str
