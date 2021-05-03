"""
Type annotations for dms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_dms.literals import (
    AuthMechanismValue,
    AuthTypeValue,
    CharLengthSemantics,
    CompressionTypeValue,
    DataFormatValue,
    DatePartitionDelimiterValue,
    DatePartitionSequenceValue,
    DmsSslModeValue,
    EncodingTypeValue,
    EncryptionModeValue,
    EndpointSettingTypeValue,
    KafkaSecurityProtocol,
    MessageFormatValue,
    MigrationTypeValue,
    NestingLevelValue,
    ParquetVersionValue,
    RefreshSchemasStatusTypeValue,
    ReplicationEndpointTypeValue,
    SafeguardPolicy,
    TargetDbType,
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
    "AccountQuotaTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "FilterTypeDef",
    "IBMDb2SettingsTypeDef",
    "ImportCertificateResponseTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadTablesResponseTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "S3SettingsTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TestConnectionResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)


class AccountQuotaTypeDef(TypedDict, total=False):
    AccountQuotaName: str
    Used: int
    Max: int


class ApplyPendingMaintenanceActionResponseTypeDef(TypedDict, total=False):
    ResourcePendingMaintenanceActions: "ResourcePendingMaintenanceActionsTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class CancelReplicationTaskAssessmentRunResponseTypeDef(TypedDict, total=False):
    ReplicationTaskAssessmentRun: "ReplicationTaskAssessmentRunTypeDef"


class CertificateTypeDef(TypedDict, total=False):
    CertificateIdentifier: str
    CertificateCreationDate: datetime
    CertificatePem: str
    CertificateWallet: Union[bytes, IO[bytes]]
    CertificateArn: str
    CertificateOwner: str
    ValidFromDate: datetime
    ValidToDate: datetime
    SigningAlgorithm: str
    KeyLength: int


class ConnectionTypeDef(TypedDict, total=False):
    ReplicationInstanceArn: str
    EndpointArn: str
    Status: str
    LastFailureMessage: str
    EndpointIdentifier: str
    ReplicationInstanceIdentifier: str


class CreateEndpointResponseTypeDef(TypedDict, total=False):
    Endpoint: "EndpointTypeDef"


class CreateEventSubscriptionResponseTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class CreateReplicationInstanceResponseTypeDef(TypedDict, total=False):
    ReplicationInstance: "ReplicationInstanceTypeDef"


class CreateReplicationSubnetGroupResponseTypeDef(TypedDict, total=False):
    ReplicationSubnetGroup: "ReplicationSubnetGroupTypeDef"


class CreateReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class DeleteCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: "CertificateTypeDef"


class DeleteConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class DeleteEndpointResponseTypeDef(TypedDict, total=False):
    Endpoint: "EndpointTypeDef"


class DeleteEventSubscriptionResponseTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class DeleteReplicationInstanceResponseTypeDef(TypedDict, total=False):
    ReplicationInstance: "ReplicationInstanceTypeDef"


class DeleteReplicationTaskAssessmentRunResponseTypeDef(TypedDict, total=False):
    ReplicationTaskAssessmentRun: "ReplicationTaskAssessmentRunTypeDef"


class DeleteReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class DescribeAccountAttributesResponseTypeDef(TypedDict, total=False):
    AccountQuotas: List["AccountQuotaTypeDef"]
    UniqueAccountIdentifier: str


class DescribeApplicableIndividualAssessmentsResponseTypeDef(TypedDict, total=False):
    IndividualAssessmentNames: List[str]
    Marker: str


class DescribeCertificatesResponseTypeDef(TypedDict, total=False):
    Marker: str
    Certificates: List["CertificateTypeDef"]


class DescribeConnectionsResponseTypeDef(TypedDict, total=False):
    Marker: str
    Connections: List["ConnectionTypeDef"]


class DescribeEndpointSettingsResponseTypeDef(TypedDict, total=False):
    Marker: str
    EndpointSettings: List["EndpointSettingTypeDef"]


class DescribeEndpointTypesResponseTypeDef(TypedDict, total=False):
    Marker: str
    SupportedEndpointTypes: List["SupportedEndpointTypeTypeDef"]


class DescribeEndpointsResponseTypeDef(TypedDict, total=False):
    Marker: str
    Endpoints: List["EndpointTypeDef"]


class DescribeEventCategoriesResponseTypeDef(TypedDict, total=False):
    EventCategoryGroupList: List["EventCategoryGroupTypeDef"]


class DescribeEventSubscriptionsResponseTypeDef(TypedDict, total=False):
    Marker: str
    EventSubscriptionsList: List["EventSubscriptionTypeDef"]


class DescribeEventsResponseTypeDef(TypedDict, total=False):
    Marker: str
    Events: List["EventTypeDef"]


class DescribeOrderableReplicationInstancesResponseTypeDef(TypedDict, total=False):
    OrderableReplicationInstances: List["OrderableReplicationInstanceTypeDef"]
    Marker: str


class DescribePendingMaintenanceActionsResponseTypeDef(TypedDict, total=False):
    PendingMaintenanceActions: List["ResourcePendingMaintenanceActionsTypeDef"]
    Marker: str


class DescribeRefreshSchemasStatusResponseTypeDef(TypedDict, total=False):
    RefreshSchemasStatus: "RefreshSchemasStatusTypeDef"


class DescribeReplicationInstanceTaskLogsResponseTypeDef(TypedDict, total=False):
    ReplicationInstanceArn: str
    ReplicationInstanceTaskLogs: List["ReplicationInstanceTaskLogTypeDef"]
    Marker: str


class DescribeReplicationInstancesResponseTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationInstances: List["ReplicationInstanceTypeDef"]


class DescribeReplicationSubnetGroupsResponseTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationSubnetGroups: List["ReplicationSubnetGroupTypeDef"]


class DescribeReplicationTaskAssessmentResultsResponseTypeDef(TypedDict, total=False):
    Marker: str
    BucketName: str
    ReplicationTaskAssessmentResults: List["ReplicationTaskAssessmentResultTypeDef"]


class DescribeReplicationTaskAssessmentRunsResponseTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationTaskAssessmentRuns: List["ReplicationTaskAssessmentRunTypeDef"]


class DescribeReplicationTaskIndividualAssessmentsResponseTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationTaskIndividualAssessments: List["ReplicationTaskIndividualAssessmentTypeDef"]


class DescribeReplicationTasksResponseTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationTasks: List["ReplicationTaskTypeDef"]


class DescribeSchemasResponseTypeDef(TypedDict, total=False):
    Marker: str
    Schemas: List[str]


class DescribeTableStatisticsResponseTypeDef(TypedDict, total=False):
    ReplicationTaskArn: str
    TableStatistics: List["TableStatisticsTypeDef"]
    Marker: str


class DmsTransferSettingsTypeDef(TypedDict, total=False):
    ServiceAccessRoleArn: str
    BucketName: str


class DocDbSettingsTypeDef(TypedDict, total=False):
    Username: str
    Password: str
    ServerName: str
    Port: int
    DatabaseName: str
    NestingLevel: NestingLevelValue
    ExtractDocId: bool
    DocsToInvestigate: int
    KmsKeyId: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class DynamoDbSettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: str


class _RequiredElasticsearchSettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: str
    EndpointUri: str


class ElasticsearchSettingsTypeDef(_RequiredElasticsearchSettingsTypeDef, total=False):
    FullLoadErrorPercentage: int
    ErrorRetryDuration: int


EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": str,
        "Type": EndpointSettingTypeValue,
        "EnumValues": List[str],
        "Sensitive": bool,
        "Units": str,
        "Applicability": str,
        "IntValueMin": int,
        "IntValueMax": int,
    },
    total=False,
)


class EndpointTypeDef(TypedDict, total=False):
    EndpointIdentifier: str
    EndpointType: ReplicationEndpointTypeValue
    EngineName: str
    EngineDisplayName: str
    Username: str
    ServerName: str
    Port: int
    DatabaseName: str
    ExtraConnectionAttributes: str
    Status: str
    KmsKeyId: str
    EndpointArn: str
    CertificateArn: str
    SslMode: DmsSslModeValue
    ServiceAccessRoleArn: str
    ExternalTableDefinition: str
    ExternalId: str
    DynamoDbSettings: "DynamoDbSettingsTypeDef"
    S3Settings: "S3SettingsTypeDef"
    DmsTransferSettings: "DmsTransferSettingsTypeDef"
    MongoDbSettings: "MongoDbSettingsTypeDef"
    KinesisSettings: "KinesisSettingsTypeDef"
    KafkaSettings: "KafkaSettingsTypeDef"
    ElasticsearchSettings: "ElasticsearchSettingsTypeDef"
    NeptuneSettings: "NeptuneSettingsTypeDef"
    RedshiftSettings: "RedshiftSettingsTypeDef"
    PostgreSQLSettings: "PostgreSQLSettingsTypeDef"
    MySQLSettings: "MySQLSettingsTypeDef"
    OracleSettings: "OracleSettingsTypeDef"
    SybaseSettings: "SybaseSettingsTypeDef"
    MicrosoftSQLServerSettings: "MicrosoftSQLServerSettingsTypeDef"
    IBMDb2Settings: "IBMDb2SettingsTypeDef"
    DocDbSettings: "DocDbSettingsTypeDef"


class EventCategoryGroupTypeDef(TypedDict, total=False):
    SourceType: str
    EventCategories: List[str]


class EventSubscriptionTypeDef(TypedDict, total=False):
    CustomerAwsId: str
    CustSubscriptionId: str
    SnsTopicArn: str
    Status: str
    SubscriptionCreationTime: str
    SourceType: str
    SourceIdsList: List[str]
    EventCategoriesList: List[str]
    Enabled: bool


class EventTypeDef(TypedDict, total=False):
    SourceIdentifier: str
    SourceType: Literal["replication-instance"]
    Message: str
    EventCategories: List[str]
    Date: datetime


class FilterTypeDef(TypedDict):
    Name: str
    Values: List[str]


class IBMDb2SettingsTypeDef(TypedDict, total=False):
    DatabaseName: str
    Password: str
    Port: int
    ServerName: str
    SetDataCaptureChanges: bool
    CurrentLsn: str
    MaxKBytesPerRead: int
    Username: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class ImportCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: "CertificateTypeDef"


class KafkaSettingsTypeDef(TypedDict, total=False):
    Broker: str
    Topic: str
    MessageFormat: MessageFormatValue
    IncludeTransactionDetails: bool
    IncludePartitionValue: bool
    PartitionIncludeSchemaTable: bool
    IncludeTableAlterOperations: bool
    IncludeControlDetails: bool
    MessageMaxBytes: int
    IncludeNullAndEmpty: bool
    SecurityProtocol: KafkaSecurityProtocol
    SslClientCertificateArn: str
    SslClientKeyArn: str
    SslClientKeyPassword: str
    SslCaCertificateArn: str
    SaslUsername: str
    SaslPassword: str


class KinesisSettingsTypeDef(TypedDict, total=False):
    StreamArn: str
    MessageFormat: MessageFormatValue
    ServiceAccessRoleArn: str
    IncludeTransactionDetails: bool
    IncludePartitionValue: bool
    PartitionIncludeSchemaTable: bool
    IncludeTableAlterOperations: bool
    IncludeControlDetails: bool
    IncludeNullAndEmpty: bool


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class MicrosoftSQLServerSettingsTypeDef(TypedDict, total=False):
    Port: int
    BcpPacketSize: int
    DatabaseName: str
    ControlTablesFileGroup: str
    Password: str
    QuerySingleAlwaysOnNode: bool
    ReadBackupOnly: bool
    SafeguardPolicy: SafeguardPolicy
    ServerName: str
    Username: str
    UseBcpFullLoad: bool
    UseThirdPartyBackupDevice: bool
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class ModifyEndpointResponseTypeDef(TypedDict, total=False):
    Endpoint: "EndpointTypeDef"


class ModifyEventSubscriptionResponseTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ModifyReplicationInstanceResponseTypeDef(TypedDict, total=False):
    ReplicationInstance: "ReplicationInstanceTypeDef"


class ModifyReplicationSubnetGroupResponseTypeDef(TypedDict, total=False):
    ReplicationSubnetGroup: "ReplicationSubnetGroupTypeDef"


class ModifyReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class MongoDbSettingsTypeDef(TypedDict, total=False):
    Username: str
    Password: str
    ServerName: str
    Port: int
    DatabaseName: str
    AuthType: AuthTypeValue
    AuthMechanism: AuthMechanismValue
    NestingLevel: NestingLevelValue
    ExtractDocId: str
    DocsToInvestigate: str
    AuthSource: str
    KmsKeyId: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class MoveReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class MySQLSettingsTypeDef(TypedDict, total=False):
    AfterConnectScript: str
    CleanSourceMetadataOnMismatch: bool
    DatabaseName: str
    EventsPollInterval: int
    TargetDbType: TargetDbType
    MaxFileSize: int
    ParallelLoadThreads: int
    Password: str
    Port: int
    ServerName: str
    ServerTimezone: str
    Username: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class _RequiredNeptuneSettingsTypeDef(TypedDict):
    S3BucketName: str
    S3BucketFolder: str


class NeptuneSettingsTypeDef(_RequiredNeptuneSettingsTypeDef, total=False):
    ServiceAccessRoleArn: str
    ErrorRetryDuration: int
    MaxFileSize: int
    MaxRetryCount: int
    IamAuthEnabled: bool


class OracleSettingsTypeDef(TypedDict, total=False):
    AddSupplementalLogging: bool
    ArchivedLogDestId: int
    AdditionalArchivedLogDestId: int
    AllowSelectNestedTables: bool
    ParallelAsmReadThreads: int
    ReadAheadBlocks: int
    AccessAlternateDirectly: bool
    UseAlternateFolderForOnline: bool
    OraclePathPrefix: str
    UsePathPrefix: str
    ReplacePathPrefix: bool
    EnableHomogenousTablespace: bool
    DirectPathNoLog: bool
    ArchivedLogsOnly: bool
    AsmPassword: str
    AsmServer: str
    AsmUser: str
    CharLengthSemantics: CharLengthSemantics
    DatabaseName: str
    DirectPathParallelLoad: bool
    FailTasksOnLobTruncation: bool
    NumberDatatypeScale: int
    Password: str
    Port: int
    ReadTableSpaceName: bool
    RetryInterval: int
    SecurityDbEncryption: str
    SecurityDbEncryptionName: str
    ServerName: str
    SpatialDataOptionToGeoJsonFunctionName: str
    Username: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str
    SecretsManagerOracleAsmAccessRoleArn: str
    SecretsManagerOracleAsmSecretId: str


class OrderableReplicationInstanceTypeDef(TypedDict, total=False):
    EngineVersion: str
    ReplicationInstanceClass: str
    StorageType: str
    MinAllocatedStorage: int
    MaxAllocatedStorage: int
    DefaultAllocatedStorage: int
    IncludedAllocatedStorage: int
    AvailabilityZones: List[str]
    ReleaseStatus: Literal["beta"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PendingMaintenanceActionTypeDef(TypedDict, total=False):
    Action: str
    AutoAppliedAfterDate: datetime
    ForcedApplyDate: datetime
    OptInStatus: str
    CurrentApplyDate: datetime
    Description: str


class PostgreSQLSettingsTypeDef(TypedDict, total=False):
    AfterConnectScript: str
    CaptureDdls: bool
    MaxFileSize: int
    DatabaseName: str
    DdlArtifactsSchema: str
    ExecuteTimeout: int
    FailTasksOnLobTruncation: bool
    Password: str
    Port: int
    ServerName: str
    Username: str
    SlotName: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class RebootReplicationInstanceResponseTypeDef(TypedDict, total=False):
    ReplicationInstance: "ReplicationInstanceTypeDef"


class RedshiftSettingsTypeDef(TypedDict, total=False):
    AcceptAnyDate: bool
    AfterConnectScript: str
    BucketFolder: str
    BucketName: str
    CaseSensitiveNames: bool
    CompUpdate: bool
    ConnectionTimeout: int
    DatabaseName: str
    DateFormat: str
    EmptyAsNull: bool
    EncryptionMode: EncryptionModeValue
    ExplicitIds: bool
    FileTransferUploadStreams: int
    LoadTimeout: int
    MaxFileSize: int
    Password: str
    Port: int
    RemoveQuotes: bool
    ReplaceInvalidChars: str
    ReplaceChars: str
    ServerName: str
    ServiceAccessRoleArn: str
    ServerSideEncryptionKmsKeyId: str
    TimeFormat: str
    TrimBlanks: bool
    TruncateColumns: bool
    Username: str
    WriteBufferSize: int
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class RefreshSchemasResponseTypeDef(TypedDict, total=False):
    RefreshSchemasStatus: "RefreshSchemasStatusTypeDef"


class RefreshSchemasStatusTypeDef(TypedDict, total=False):
    EndpointArn: str
    ReplicationInstanceArn: str
    Status: RefreshSchemasStatusTypeValue
    LastRefreshDate: datetime
    LastFailureMessage: str


class ReloadTablesResponseTypeDef(TypedDict, total=False):
    ReplicationTaskArn: str


class ReplicationInstanceTaskLogTypeDef(TypedDict, total=False):
    ReplicationTaskName: str
    ReplicationTaskArn: str
    ReplicationInstanceTaskLogSize: int


class ReplicationInstanceTypeDef(TypedDict, total=False):
    ReplicationInstanceIdentifier: str
    ReplicationInstanceClass: str
    ReplicationInstanceStatus: str
    AllocatedStorage: int
    InstanceCreateTime: datetime
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    AvailabilityZone: str
    ReplicationSubnetGroup: "ReplicationSubnetGroupTypeDef"
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "ReplicationPendingModifiedValuesTypeDef"
    MultiAZ: bool
    EngineVersion: str
    AutoMinorVersionUpgrade: bool
    KmsKeyId: str
    ReplicationInstanceArn: str
    ReplicationInstancePublicIpAddress: str
    ReplicationInstancePrivateIpAddress: str
    ReplicationInstancePublicIpAddresses: List[str]
    ReplicationInstancePrivateIpAddresses: List[str]
    PubliclyAccessible: bool
    SecondaryAvailabilityZone: str
    FreeUntil: datetime
    DnsNameServers: str


class ReplicationPendingModifiedValuesTypeDef(TypedDict, total=False):
    ReplicationInstanceClass: str
    AllocatedStorage: int
    MultiAZ: bool
    EngineVersion: str


class ReplicationSubnetGroupTypeDef(TypedDict, total=False):
    ReplicationSubnetGroupIdentifier: str
    ReplicationSubnetGroupDescription: str
    VpcId: str
    SubnetGroupStatus: str
    Subnets: List["SubnetTypeDef"]


class ReplicationTaskAssessmentResultTypeDef(TypedDict, total=False):
    ReplicationTaskIdentifier: str
    ReplicationTaskArn: str
    ReplicationTaskLastAssessmentDate: datetime
    AssessmentStatus: str
    AssessmentResultsFile: str
    AssessmentResults: str
    S3ObjectUrl: str


class ReplicationTaskAssessmentRunProgressTypeDef(TypedDict, total=False):
    IndividualAssessmentCount: int
    IndividualAssessmentCompletedCount: int


class ReplicationTaskAssessmentRunTypeDef(TypedDict, total=False):
    ReplicationTaskAssessmentRunArn: str
    ReplicationTaskArn: str
    Status: str
    ReplicationTaskAssessmentRunCreationDate: datetime
    AssessmentProgress: "ReplicationTaskAssessmentRunProgressTypeDef"
    LastFailureMessage: str
    ServiceAccessRoleArn: str
    ResultLocationBucket: str
    ResultLocationFolder: str
    ResultEncryptionMode: str
    ResultKmsKeyArn: str
    AssessmentRunName: str


class ReplicationTaskIndividualAssessmentTypeDef(TypedDict, total=False):
    ReplicationTaskIndividualAssessmentArn: str
    ReplicationTaskAssessmentRunArn: str
    IndividualAssessmentName: str
    Status: str
    ReplicationTaskIndividualAssessmentStartDate: datetime


class ReplicationTaskStatsTypeDef(TypedDict, total=False):
    FullLoadProgressPercent: int
    ElapsedTimeMillis: int
    TablesLoaded: int
    TablesLoading: int
    TablesQueued: int
    TablesErrored: int
    FreshStartDate: datetime
    StartDate: datetime
    StopDate: datetime
    FullLoadStartDate: datetime
    FullLoadFinishDate: datetime


class ReplicationTaskTypeDef(TypedDict, total=False):
    ReplicationTaskIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ReplicationInstanceArn: str
    MigrationType: MigrationTypeValue
    TableMappings: str
    ReplicationTaskSettings: str
    Status: str
    LastFailureMessage: str
    StopReason: str
    ReplicationTaskCreationDate: datetime
    ReplicationTaskStartDate: datetime
    CdcStartPosition: str
    CdcStopPosition: str
    RecoveryCheckpoint: str
    ReplicationTaskArn: str
    ReplicationTaskStats: "ReplicationTaskStatsTypeDef"
    TaskData: str
    TargetReplicationInstanceArn: str


class ResourcePendingMaintenanceActionsTypeDef(TypedDict, total=False):
    ResourceIdentifier: str
    PendingMaintenanceActionDetails: List["PendingMaintenanceActionTypeDef"]


class S3SettingsTypeDef(TypedDict, total=False):
    ServiceAccessRoleArn: str
    ExternalTableDefinition: str
    CsvRowDelimiter: str
    CsvDelimiter: str
    BucketFolder: str
    BucketName: str
    CompressionType: CompressionTypeValue
    EncryptionMode: EncryptionModeValue
    ServerSideEncryptionKmsKeyId: str
    DataFormat: DataFormatValue
    EncodingType: EncodingTypeValue
    DictPageSizeLimit: int
    RowGroupLength: int
    DataPageSize: int
    ParquetVersion: ParquetVersionValue
    EnableStatistics: bool
    IncludeOpForFullLoad: bool
    CdcInsertsOnly: bool
    TimestampColumnName: str
    ParquetTimestampInMillisecond: bool
    CdcInsertsAndUpdates: bool
    DatePartitionEnabled: bool
    DatePartitionSequence: DatePartitionSequenceValue
    DatePartitionDelimiter: DatePartitionDelimiterValue
    UseCsvNoSupValue: bool
    CsvNoSupValue: str
    PreserveTransactions: bool
    CdcPath: str


class StartReplicationTaskAssessmentResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class StartReplicationTaskAssessmentRunResponseTypeDef(TypedDict, total=False):
    ReplicationTaskAssessmentRun: "ReplicationTaskAssessmentRunTypeDef"


class StartReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class StopReplicationTaskResponseTypeDef(TypedDict, total=False):
    ReplicationTask: "ReplicationTaskTypeDef"


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AvailabilityZoneTypeDef"
    SubnetStatus: str


class SupportedEndpointTypeTypeDef(TypedDict, total=False):
    EngineName: str
    SupportsCDC: bool
    EndpointType: ReplicationEndpointTypeValue
    ReplicationInstanceEngineMinimumVersion: str
    EngineDisplayName: str


class SybaseSettingsTypeDef(TypedDict, total=False):
    DatabaseName: str
    Password: str
    Port: int
    ServerName: str
    Username: str
    SecretsManagerAccessRoleArn: str
    SecretsManagerSecretId: str


class TableStatisticsTypeDef(TypedDict, total=False):
    SchemaName: str
    TableName: str
    Inserts: int
    Deletes: int
    Updates: int
    Ddls: int
    FullLoadRows: int
    FullLoadCondtnlChkFailedRows: int
    FullLoadErrorRows: int
    FullLoadStartTime: datetime
    FullLoadEndTime: datetime
    FullLoadReloaded: bool
    LastUpdateTime: datetime
    TableState: str
    ValidationPendingRecords: int
    ValidationFailedRecords: int
    ValidationSuspendedRecords: int
    ValidationState: str
    ValidationStateDetails: str


class TableToReloadTypeDef(TypedDict):
    SchemaName: str
    TableName: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TestConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class VpcSecurityGroupMembershipTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
