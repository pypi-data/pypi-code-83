"""
Type annotations for dynamodb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.type_defs import ArchivalSummaryTypeDef

    data: ArchivalSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Set, Union

from mypy_boto3_dynamodb.literals import (
    AttributeAction,
    BackupStatus,
    BackupType,
    BatchStatementErrorCodeEnum,
    BillingMode,
    ComparisonOperator,
    ContinuousBackupsStatus,
    ContributorInsightsStatus,
    DestinationStatus,
    ExportFormat,
    ExportStatus,
    GlobalTableStatus,
    IndexStatus,
    KeyType,
    PointInTimeRecoveryStatus,
    ProjectionType,
    ReplicaStatus,
    ReturnValuesOnConditionCheckFailure,
    S3SseAlgorithm,
    ScalarAttributeType,
    SSEStatus,
    SSEType,
    StreamViewType,
    TableStatus,
    TimeToLiveStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchivalSummaryTypeDef",
    "AttributeDefinitionTypeDef",
    "AttributeValueUpdateTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "BatchGetItemOutputTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementRequestTypeDef",
    "BatchStatementResponseTypeDef",
    "BatchWriteItemOutputTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionCheckTypeDef",
    "ConditionTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateBackupOutputTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "CreateReplicaActionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteBackupOutputTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteItemOutputTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTableOutputTypeDef",
    "DeleteTypeDef",
    "DescribeBackupOutputTypeDef",
    "DescribeContinuousBackupsOutputTypeDef",
    "DescribeContributorInsightsOutputTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeExportOutputTypeDef",
    "DescribeGlobalTableOutputTypeDef",
    "DescribeGlobalTableSettingsOutputTypeDef",
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeTableOutputTypeDef",
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    "DescribeTimeToLiveOutputTypeDef",
    "EndpointTypeDef",
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "ExpectedAttributeValueTypeDef",
    "ExportDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "FailureExceptionTypeDef",
    "GetItemOutputTypeDef",
    "GetTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "GlobalTableDescriptionTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "GlobalTableTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeySchemaElementTypeDef",
    "KeysAndAttributesTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListBackupsOutputTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ListTablesOutputTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "LocalSecondaryIndexTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterizedStatementTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "ProvisionedThroughputTypeDef",
    "PutItemOutputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "QueryOutputTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "ReplicaTypeDef",
    "ReplicaUpdateTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "ResponseMetadata",
    "RestoreSummaryTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "ScanOutputTypeDef",
    "SourceTableDetailsTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "StreamSpecificationTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "TableDescriptionTypeDef",
    "TagTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "TransactGetItemTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateItemOutputTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "UpdateTypeDef",
    "WaiterConfigTypeDef",
    "WriteRequestTypeDef",
)


class ArchivalSummaryTypeDef(TypedDict, total=False):
    ArchivalDateTime: datetime
    ArchivalReason: str
    ArchivalBackupArn: str


class AttributeDefinitionTypeDef(TypedDict):
    AttributeName: str
    AttributeType: ScalarAttributeType


class AttributeValueUpdateTypeDef(TypedDict, total=False):
    Value: Union[
        bytes,
        bytearray,
        str,
        int,
        Decimal,
        bool,
        Set[int],
        Set[Decimal],
        Set[str],
        Set[bytes],
        Set[bytearray],
        List[Any],
        Dict[str, Any],
        None,
    ]
    Action: AttributeAction


class AutoScalingPolicyDescriptionTypeDef(TypedDict, total=False):
    PolicyName: str
    TargetTrackingScalingPolicyConfiguration: "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef"


class _RequiredAutoScalingPolicyUpdateTypeDef(TypedDict):
    TargetTrackingScalingPolicyConfiguration: "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"


class AutoScalingPolicyUpdateTypeDef(_RequiredAutoScalingPolicyUpdateTypeDef, total=False):
    PolicyName: str


class AutoScalingSettingsDescriptionTypeDef(TypedDict, total=False):
    MinimumUnits: int
    MaximumUnits: int
    AutoScalingDisabled: bool
    AutoScalingRoleArn: str
    ScalingPolicies: List["AutoScalingPolicyDescriptionTypeDef"]


class AutoScalingSettingsUpdateTypeDef(TypedDict, total=False):
    MinimumUnits: int
    MaximumUnits: int
    AutoScalingDisabled: bool
    AutoScalingRoleArn: str
    ScalingPolicyUpdate: "AutoScalingPolicyUpdateTypeDef"


class _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(TypedDict):
    TargetValue: float


class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef, total=False
):
    DisableScaleIn: bool
    ScaleInCooldown: int
    ScaleOutCooldown: int


class _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(TypedDict):
    TargetValue: float


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef, total=False
):
    DisableScaleIn: bool
    ScaleInCooldown: int
    ScaleOutCooldown: int


class BackupDescriptionTypeDef(TypedDict, total=False):
    BackupDetails: "BackupDetailsTypeDef"
    SourceTableDetails: "SourceTableDetailsTypeDef"
    SourceTableFeatureDetails: "SourceTableFeatureDetailsTypeDef"


class _RequiredBackupDetailsTypeDef(TypedDict):
    BackupArn: str
    BackupName: str
    BackupStatus: BackupStatus
    BackupType: BackupType
    BackupCreationDateTime: datetime


class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, total=False):
    BackupSizeBytes: int
    BackupExpiryDateTime: datetime


class BackupSummaryTypeDef(TypedDict, total=False):
    TableName: str
    TableId: str
    TableArn: str
    BackupArn: str
    BackupName: str
    BackupCreationDateTime: datetime
    BackupExpiryDateTime: datetime
    BackupStatus: BackupStatus
    BackupType: BackupType
    BackupSizeBytes: int


class BatchExecuteStatementOutputTypeDef(TypedDict):
    Responses: List["BatchStatementResponseTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetItemOutputTypeDef(TypedDict):
    Responses: Dict[
        str,
        List[
            Dict[
                str,
                Union[
                    bytes,
                    bytearray,
                    str,
                    int,
                    Decimal,
                    bool,
                    Set[int],
                    Set[Decimal],
                    Set[str],
                    Set[bytes],
                    Set[bytearray],
                    List[Any],
                    Dict[str, Any],
                    None,
                ],
            ]
        ],
    ]
    UnprocessedKeys: Dict[str, "KeysAndAttributesTypeDef"]
    ConsumedCapacity: List["ConsumedCapacityTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchStatementErrorTypeDef(TypedDict, total=False):
    Code: BatchStatementErrorCodeEnum
    Message: str


class _RequiredBatchStatementRequestTypeDef(TypedDict):
    Statement: str


class BatchStatementRequestTypeDef(_RequiredBatchStatementRequestTypeDef, total=False):
    Parameters: List[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ]
    ]
    ConsistentRead: bool


class BatchStatementResponseTypeDef(TypedDict, total=False):
    Error: "BatchStatementErrorTypeDef"
    TableName: str
    Item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]


class BatchWriteItemOutputTypeDef(TypedDict):
    UnprocessedItems: Dict[str, List["WriteRequestTypeDef"]]
    ItemCollectionMetrics: Dict[str, List["ItemCollectionMetricsTypeDef"]]
    ConsumedCapacity: List["ConsumedCapacityTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BillingModeSummaryTypeDef(TypedDict, total=False):
    BillingMode: BillingMode
    LastUpdateToPayPerRequestDateTime: datetime


class CapacityTypeDef(TypedDict, total=False):
    ReadCapacityUnits: float
    WriteCapacityUnits: float
    CapacityUnits: float


class _RequiredConditionCheckTypeDef(TypedDict):
    Key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    TableName: str
    ConditionExpression: str


class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, total=False):
    ExpressionAttributeNames: Dict[str, str]
    ExpressionAttributeValues: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ReturnValuesOnConditionCheckFailure: ReturnValuesOnConditionCheckFailure


class _RequiredConditionTypeDef(TypedDict):
    ComparisonOperator: ComparisonOperator


class ConditionTypeDef(_RequiredConditionTypeDef, total=False):
    AttributeValueList: List[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ]
    ]


class ConsumedCapacityTypeDef(TypedDict, total=False):
    TableName: str
    CapacityUnits: float
    ReadCapacityUnits: float
    WriteCapacityUnits: float
    Table: "CapacityTypeDef"
    LocalSecondaryIndexes: Dict[str, "CapacityTypeDef"]
    GlobalSecondaryIndexes: Dict[str, "CapacityTypeDef"]


class _RequiredContinuousBackupsDescriptionTypeDef(TypedDict):
    ContinuousBackupsStatus: ContinuousBackupsStatus


class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, total=False
):
    PointInTimeRecoveryDescription: "PointInTimeRecoveryDescriptionTypeDef"


class ContributorInsightsSummaryTypeDef(TypedDict, total=False):
    TableName: str
    IndexName: str
    ContributorInsightsStatus: ContributorInsightsStatus


class CreateBackupOutputTypeDef(TypedDict):
    BackupDetails: "BackupDetailsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredCreateGlobalSecondaryIndexActionTypeDef(TypedDict):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"


class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef, total=False
):
    ProvisionedThroughput: "ProvisionedThroughputTypeDef"


class CreateGlobalTableOutputTypeDef(TypedDict):
    GlobalTableDescription: "GlobalTableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateReplicaActionTypeDef(TypedDict):
    RegionName: str


class _RequiredCreateReplicationGroupMemberActionTypeDef(TypedDict):
    RegionName: str


class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef, total=False
):
    KMSMasterKeyId: str
    ProvisionedThroughputOverride: "ProvisionedThroughputOverrideTypeDef"
    GlobalSecondaryIndexes: List["ReplicaGlobalSecondaryIndexTypeDef"]


class CreateTableOutputTypeDef(TypedDict):
    TableDescription: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteBackupOutputTypeDef(TypedDict):
    BackupDescription: "BackupDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteGlobalSecondaryIndexActionTypeDef(TypedDict):
    IndexName: str


class DeleteItemOutputTypeDef(TypedDict):
    Attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ItemCollectionMetrics: "ItemCollectionMetricsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteReplicaActionTypeDef(TypedDict):
    RegionName: str


class DeleteReplicationGroupMemberActionTypeDef(TypedDict):
    RegionName: str


class DeleteRequestTypeDef(TypedDict):
    Key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]


class DeleteTableOutputTypeDef(TypedDict):
    TableDescription: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredDeleteTypeDef(TypedDict):
    Key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    TableName: str


class DeleteTypeDef(_RequiredDeleteTypeDef, total=False):
    ConditionExpression: str
    ExpressionAttributeNames: Dict[str, str]
    ExpressionAttributeValues: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ReturnValuesOnConditionCheckFailure: ReturnValuesOnConditionCheckFailure


class DescribeBackupOutputTypeDef(TypedDict):
    BackupDescription: "BackupDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeContinuousBackupsOutputTypeDef(TypedDict):
    ContinuousBackupsDescription: "ContinuousBackupsDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeContributorInsightsOutputTypeDef(TypedDict):
    TableName: str
    IndexName: str
    ContributorInsightsRuleList: List[str]
    ContributorInsightsStatus: ContributorInsightsStatus
    LastUpdateDateTime: datetime
    FailureException: "FailureExceptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeEndpointsResponseTypeDef(TypedDict):
    Endpoints: List["EndpointTypeDef"]


class DescribeExportOutputTypeDef(TypedDict):
    ExportDescription: "ExportDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGlobalTableOutputTypeDef(TypedDict):
    GlobalTableDescription: "GlobalTableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGlobalTableSettingsOutputTypeDef(TypedDict):
    GlobalTableName: str
    ReplicaSettings: List["ReplicaSettingsDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeKinesisStreamingDestinationOutputTypeDef(TypedDict):
    TableName: str
    KinesisDataStreamDestinations: List["KinesisDataStreamDestinationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeLimitsOutputTypeDef(TypedDict):
    AccountMaxReadCapacityUnits: int
    AccountMaxWriteCapacityUnits: int
    TableMaxReadCapacityUnits: int
    TableMaxWriteCapacityUnits: int
    ResponseMetadata: "ResponseMetadata"


class DescribeTableOutputTypeDef(TypedDict):
    Table: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeTableReplicaAutoScalingOutputTypeDef(TypedDict):
    TableAutoScalingDescription: "TableAutoScalingDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeTimeToLiveOutputTypeDef(TypedDict):
    TimeToLiveDescription: "TimeToLiveDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class EndpointTypeDef(TypedDict):
    Address: str
    CachePeriodInMinutes: int


class ExecuteStatementOutputTypeDef(TypedDict):
    Items: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ]
    ]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ExecuteTransactionOutputTypeDef(TypedDict):
    Responses: List["ItemResponseTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ExpectedAttributeValueTypeDef(TypedDict, total=False):
    Value: Union[
        bytes,
        bytearray,
        str,
        int,
        Decimal,
        bool,
        Set[int],
        Set[Decimal],
        Set[str],
        Set[bytes],
        Set[bytearray],
        List[Any],
        Dict[str, Any],
        None,
    ]
    Exists: bool
    ComparisonOperator: ComparisonOperator
    AttributeValueList: List[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ]
    ]


class ExportDescriptionTypeDef(TypedDict, total=False):
    ExportArn: str
    ExportStatus: ExportStatus
    StartTime: datetime
    EndTime: datetime
    ExportManifest: str
    TableArn: str
    TableId: str
    ExportTime: datetime
    ClientToken: str
    S3Bucket: str
    S3BucketOwner: str
    S3Prefix: str
    S3SseAlgorithm: S3SseAlgorithm
    S3SseKmsKeyId: str
    FailureCode: str
    FailureMessage: str
    ExportFormat: ExportFormat
    BilledSizeBytes: int
    ItemCount: int


class ExportSummaryTypeDef(TypedDict, total=False):
    ExportArn: str
    ExportStatus: ExportStatus


class ExportTableToPointInTimeOutputTypeDef(TypedDict):
    ExportDescription: "ExportDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class FailureExceptionTypeDef(TypedDict, total=False):
    ExceptionName: str
    ExceptionDescription: str


class GetItemOutputTypeDef(TypedDict):
    Item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredGetTypeDef(TypedDict):
    Key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    TableName: str


class GetTypeDef(_RequiredGetTypeDef, total=False):
    ProjectionExpression: str
    ExpressionAttributeNames: Dict[str, str]


class GlobalSecondaryIndexAutoScalingUpdateTypeDef(TypedDict, total=False):
    IndexName: str
    ProvisionedWriteCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef"


class GlobalSecondaryIndexDescriptionTypeDef(TypedDict, total=False):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"
    IndexStatus: IndexStatus
    Backfilling: bool
    ProvisionedThroughput: "ProvisionedThroughputDescriptionTypeDef"
    IndexSizeBytes: int
    ItemCount: int
    IndexArn: str


class GlobalSecondaryIndexInfoTypeDef(TypedDict, total=False):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"
    ProvisionedThroughput: "ProvisionedThroughputTypeDef"


class _RequiredGlobalSecondaryIndexTypeDef(TypedDict):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"


class GlobalSecondaryIndexTypeDef(_RequiredGlobalSecondaryIndexTypeDef, total=False):
    ProvisionedThroughput: "ProvisionedThroughputTypeDef"


class GlobalSecondaryIndexUpdateTypeDef(TypedDict, total=False):
    Update: "UpdateGlobalSecondaryIndexActionTypeDef"
    Create: "CreateGlobalSecondaryIndexActionTypeDef"
    Delete: "DeleteGlobalSecondaryIndexActionTypeDef"


class GlobalTableDescriptionTypeDef(TypedDict, total=False):
    ReplicationGroup: List["ReplicaDescriptionTypeDef"]
    GlobalTableArn: str
    CreationDateTime: datetime
    GlobalTableStatus: GlobalTableStatus
    GlobalTableName: str


class _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(TypedDict):
    IndexName: str


class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef, total=False
):
    ProvisionedWriteCapacityUnits: int
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef"


class GlobalTableTypeDef(TypedDict, total=False):
    GlobalTableName: str
    ReplicationGroup: List["ReplicaTypeDef"]


class ItemCollectionMetricsTypeDef(TypedDict, total=False):
    ItemCollectionKey: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    SizeEstimateRangeGB: List[float]


class ItemResponseTypeDef(TypedDict, total=False):
    Item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]


class KeySchemaElementTypeDef(TypedDict):
    AttributeName: str
    KeyType: KeyType


class _RequiredKeysAndAttributesTypeDef(TypedDict):
    Keys: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ]
    ]


class KeysAndAttributesTypeDef(_RequiredKeysAndAttributesTypeDef, total=False):
    AttributesToGet: List[str]
    ConsistentRead: bool
    ProjectionExpression: str
    ExpressionAttributeNames: Dict[str, str]


class KinesisDataStreamDestinationTypeDef(TypedDict, total=False):
    StreamArn: str
    DestinationStatus: DestinationStatus
    DestinationStatusDescription: str


class KinesisStreamingDestinationOutputTypeDef(TypedDict):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatus
    ResponseMetadata: "ResponseMetadata"


class ListBackupsOutputTypeDef(TypedDict):
    BackupSummaries: List["BackupSummaryTypeDef"]
    LastEvaluatedBackupArn: str
    ResponseMetadata: "ResponseMetadata"


class ListContributorInsightsOutputTypeDef(TypedDict):
    ContributorInsightsSummaries: List["ContributorInsightsSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListExportsOutputTypeDef(TypedDict):
    ExportSummaries: List["ExportSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListGlobalTablesOutputTypeDef(TypedDict):
    GlobalTables: List["GlobalTableTypeDef"]
    LastEvaluatedGlobalTableName: str
    ResponseMetadata: "ResponseMetadata"


class ListTablesOutputTypeDef(TypedDict):
    TableNames: List[str]
    LastEvaluatedTableName: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsOfResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class LocalSecondaryIndexDescriptionTypeDef(TypedDict, total=False):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"
    IndexSizeBytes: int
    ItemCount: int
    IndexArn: str


class LocalSecondaryIndexInfoTypeDef(TypedDict, total=False):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"


class LocalSecondaryIndexTypeDef(TypedDict):
    IndexName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    Projection: "ProjectionTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredParameterizedStatementTypeDef(TypedDict):
    Statement: str


class ParameterizedStatementTypeDef(_RequiredParameterizedStatementTypeDef, total=False):
    Parameters: List[
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ]
    ]


class PointInTimeRecoveryDescriptionTypeDef(TypedDict, total=False):
    PointInTimeRecoveryStatus: PointInTimeRecoveryStatus
    EarliestRestorableDateTime: datetime
    LatestRestorableDateTime: datetime


class PointInTimeRecoverySpecificationTypeDef(TypedDict):
    PointInTimeRecoveryEnabled: bool


class ProjectionTypeDef(TypedDict, total=False):
    ProjectionType: ProjectionType
    NonKeyAttributes: List[str]


class ProvisionedThroughputDescriptionTypeDef(TypedDict, total=False):
    LastIncreaseDateTime: datetime
    LastDecreaseDateTime: datetime
    NumberOfDecreasesToday: int
    ReadCapacityUnits: int
    WriteCapacityUnits: int


class ProvisionedThroughputOverrideTypeDef(TypedDict, total=False):
    ReadCapacityUnits: int


class ProvisionedThroughputTypeDef(TypedDict):
    ReadCapacityUnits: int
    WriteCapacityUnits: int


class PutItemOutputTypeDef(TypedDict):
    Attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ItemCollectionMetrics: "ItemCollectionMetricsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PutRequestTypeDef(TypedDict):
    Item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]


class _RequiredPutTypeDef(TypedDict):
    Item: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    TableName: str


class PutTypeDef(_RequiredPutTypeDef, total=False):
    ConditionExpression: str
    ExpressionAttributeNames: Dict[str, str]
    ExpressionAttributeValues: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ReturnValuesOnConditionCheckFailure: ReturnValuesOnConditionCheckFailure


class QueryOutputTypeDef(TypedDict):
    Items: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ]
    ]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ReplicaAutoScalingDescriptionTypeDef(TypedDict, total=False):
    RegionName: str
    GlobalSecondaryIndexes: List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"]
    ReplicaProvisionedReadCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ReplicaProvisionedWriteCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ReplicaStatus: ReplicaStatus


class _RequiredReplicaAutoScalingUpdateTypeDef(TypedDict):
    RegionName: str


class ReplicaAutoScalingUpdateTypeDef(_RequiredReplicaAutoScalingUpdateTypeDef, total=False):
    ReplicaGlobalSecondaryIndexUpdates: List["ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"]
    ReplicaProvisionedReadCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef"


class ReplicaDescriptionTypeDef(TypedDict, total=False):
    RegionName: str
    ReplicaStatus: ReplicaStatus
    ReplicaStatusDescription: str
    ReplicaStatusPercentProgress: str
    KMSMasterKeyId: str
    ProvisionedThroughputOverride: "ProvisionedThroughputOverrideTypeDef"
    GlobalSecondaryIndexes: List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"]
    ReplicaInaccessibleDateTime: datetime


class ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef(TypedDict, total=False):
    IndexName: str
    IndexStatus: IndexStatus
    ProvisionedReadCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ProvisionedWriteCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"


class ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef(TypedDict, total=False):
    IndexName: str
    ProvisionedReadCapacityAutoScalingUpdate: "AutoScalingSettingsUpdateTypeDef"


class ReplicaGlobalSecondaryIndexDescriptionTypeDef(TypedDict, total=False):
    IndexName: str
    ProvisionedThroughputOverride: "ProvisionedThroughputOverrideTypeDef"


class _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(TypedDict):
    IndexName: str


class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef, total=False
):
    IndexStatus: IndexStatus
    ProvisionedReadCapacityUnits: int
    ProvisionedReadCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ProvisionedWriteCapacityUnits: int
    ProvisionedWriteCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"


class _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(TypedDict):
    IndexName: str


class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef, total=False
):
    ProvisionedReadCapacityUnits: int
    ProvisionedReadCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef"


class _RequiredReplicaGlobalSecondaryIndexTypeDef(TypedDict):
    IndexName: str


class ReplicaGlobalSecondaryIndexTypeDef(_RequiredReplicaGlobalSecondaryIndexTypeDef, total=False):
    ProvisionedThroughputOverride: "ProvisionedThroughputOverrideTypeDef"


class _RequiredReplicaSettingsDescriptionTypeDef(TypedDict):
    RegionName: str


class ReplicaSettingsDescriptionTypeDef(_RequiredReplicaSettingsDescriptionTypeDef, total=False):
    ReplicaStatus: ReplicaStatus
    ReplicaBillingModeSummary: "BillingModeSummaryTypeDef"
    ReplicaProvisionedReadCapacityUnits: int
    ReplicaProvisionedReadCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ReplicaProvisionedWriteCapacityUnits: int
    ReplicaProvisionedWriteCapacityAutoScalingSettings: "AutoScalingSettingsDescriptionTypeDef"
    ReplicaGlobalSecondaryIndexSettings: List[
        "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
    ]


class _RequiredReplicaSettingsUpdateTypeDef(TypedDict):
    RegionName: str


class ReplicaSettingsUpdateTypeDef(_RequiredReplicaSettingsUpdateTypeDef, total=False):
    ReplicaProvisionedReadCapacityUnits: int
    ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate: "AutoScalingSettingsUpdateTypeDef"
    ReplicaGlobalSecondaryIndexSettingsUpdate: List[
        "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"
    ]


class ReplicaTypeDef(TypedDict, total=False):
    RegionName: str


class ReplicaUpdateTypeDef(TypedDict, total=False):
    Create: "CreateReplicaActionTypeDef"
    Delete: "DeleteReplicaActionTypeDef"


class ReplicationGroupUpdateTypeDef(TypedDict, total=False):
    Create: "CreateReplicationGroupMemberActionTypeDef"
    Update: "UpdateReplicationGroupMemberActionTypeDef"
    Delete: "DeleteReplicationGroupMemberActionTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredRestoreSummaryTypeDef(TypedDict):
    RestoreDateTime: datetime
    RestoreInProgress: bool


class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, total=False):
    SourceBackupArn: str
    SourceTableArn: str


class RestoreTableFromBackupOutputTypeDef(TypedDict):
    TableDescription: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class RestoreTableToPointInTimeOutputTypeDef(TypedDict):
    TableDescription: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SSEDescriptionTypeDef(TypedDict, total=False):
    Status: SSEStatus
    SSEType: SSEType
    KMSMasterKeyArn: str
    InaccessibleEncryptionDateTime: datetime


class SSESpecificationTypeDef(TypedDict, total=False):
    Enabled: bool
    SSEType: SSEType
    KMSMasterKeyId: str


class ScanOutputTypeDef(TypedDict):
    Items: List[
        Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ]
    ]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredSourceTableDetailsTypeDef(TypedDict):
    TableName: str
    TableId: str
    KeySchema: List["KeySchemaElementTypeDef"]
    TableCreationDateTime: datetime
    ProvisionedThroughput: "ProvisionedThroughputTypeDef"


class SourceTableDetailsTypeDef(_RequiredSourceTableDetailsTypeDef, total=False):
    TableArn: str
    TableSizeBytes: int
    ItemCount: int
    BillingMode: BillingMode


class SourceTableFeatureDetailsTypeDef(TypedDict, total=False):
    LocalSecondaryIndexes: List["LocalSecondaryIndexInfoTypeDef"]
    GlobalSecondaryIndexes: List["GlobalSecondaryIndexInfoTypeDef"]
    StreamDescription: "StreamSpecificationTypeDef"
    TimeToLiveDescription: "TimeToLiveDescriptionTypeDef"
    SSEDescription: "SSEDescriptionTypeDef"


class _RequiredStreamSpecificationTypeDef(TypedDict):
    StreamEnabled: bool


class StreamSpecificationTypeDef(_RequiredStreamSpecificationTypeDef, total=False):
    StreamViewType: StreamViewType


class TableAutoScalingDescriptionTypeDef(TypedDict, total=False):
    TableName: str
    TableStatus: TableStatus
    Replicas: List["ReplicaAutoScalingDescriptionTypeDef"]


class TableDescriptionTypeDef(TypedDict, total=False):
    AttributeDefinitions: List["AttributeDefinitionTypeDef"]
    TableName: str
    KeySchema: List["KeySchemaElementTypeDef"]
    TableStatus: TableStatus
    CreationDateTime: datetime
    ProvisionedThroughput: "ProvisionedThroughputDescriptionTypeDef"
    TableSizeBytes: int
    ItemCount: int
    TableArn: str
    TableId: str
    BillingModeSummary: "BillingModeSummaryTypeDef"
    LocalSecondaryIndexes: List["LocalSecondaryIndexDescriptionTypeDef"]
    GlobalSecondaryIndexes: List["GlobalSecondaryIndexDescriptionTypeDef"]
    StreamSpecification: "StreamSpecificationTypeDef"
    LatestStreamLabel: str
    LatestStreamArn: str
    GlobalTableVersion: str
    Replicas: List["ReplicaDescriptionTypeDef"]
    RestoreSummary: "RestoreSummaryTypeDef"
    SSEDescription: "SSEDescriptionTypeDef"
    ArchivalSummary: "ArchivalSummaryTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TimeToLiveDescriptionTypeDef(TypedDict, total=False):
    TimeToLiveStatus: TimeToLiveStatus
    AttributeName: str


class TimeToLiveSpecificationTypeDef(TypedDict):
    Enabled: bool
    AttributeName: str


class TransactGetItemTypeDef(TypedDict):
    Get: "GetTypeDef"


class TransactGetItemsOutputTypeDef(TypedDict):
    ConsumedCapacity: List["ConsumedCapacityTypeDef"]
    Responses: List["ItemResponseTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class TransactWriteItemTypeDef(TypedDict, total=False):
    ConditionCheck: "ConditionCheckTypeDef"
    Put: "PutTypeDef"
    Delete: "DeleteTypeDef"
    Update: "UpdateTypeDef"


class TransactWriteItemsOutputTypeDef(TypedDict):
    ConsumedCapacity: List["ConsumedCapacityTypeDef"]
    ItemCollectionMetrics: Dict[str, List["ItemCollectionMetricsTypeDef"]]
    ResponseMetadata: "ResponseMetadata"


class UpdateContinuousBackupsOutputTypeDef(TypedDict):
    ContinuousBackupsDescription: "ContinuousBackupsDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateContributorInsightsOutputTypeDef(TypedDict):
    TableName: str
    IndexName: str
    ContributorInsightsStatus: ContributorInsightsStatus
    ResponseMetadata: "ResponseMetadata"


class UpdateGlobalSecondaryIndexActionTypeDef(TypedDict):
    IndexName: str
    ProvisionedThroughput: "ProvisionedThroughputTypeDef"


class UpdateGlobalTableOutputTypeDef(TypedDict):
    GlobalTableDescription: "GlobalTableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateGlobalTableSettingsOutputTypeDef(TypedDict):
    GlobalTableName: str
    ReplicaSettings: List["ReplicaSettingsDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UpdateItemOutputTypeDef(TypedDict):
    Attributes: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ConsumedCapacity: "ConsumedCapacityTypeDef"
    ItemCollectionMetrics: "ItemCollectionMetricsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredUpdateReplicationGroupMemberActionTypeDef(TypedDict):
    RegionName: str


class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef, total=False
):
    KMSMasterKeyId: str
    ProvisionedThroughputOverride: "ProvisionedThroughputOverrideTypeDef"
    GlobalSecondaryIndexes: List["ReplicaGlobalSecondaryIndexTypeDef"]


class UpdateTableOutputTypeDef(TypedDict):
    TableDescription: "TableDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateTableReplicaAutoScalingOutputTypeDef(TypedDict):
    TableAutoScalingDescription: "TableAutoScalingDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateTimeToLiveOutputTypeDef(TypedDict):
    TimeToLiveSpecification: "TimeToLiveSpecificationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredUpdateTypeDef(TypedDict):
    Key: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    UpdateExpression: str
    TableName: str


class UpdateTypeDef(_RequiredUpdateTypeDef, total=False):
    ConditionExpression: str
    ExpressionAttributeNames: Dict[str, str]
    ExpressionAttributeValues: Dict[
        str,
        Union[
            bytes,
            bytearray,
            str,
            int,
            Decimal,
            bool,
            Set[int],
            Set[Decimal],
            Set[str],
            Set[bytes],
            Set[bytearray],
            List[Any],
            Dict[str, Any],
            None,
        ],
    ]
    ReturnValuesOnConditionCheckFailure: ReturnValuesOnConditionCheckFailure


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WriteRequestTypeDef(TypedDict, total=False):
    PutRequest: "PutRequestTypeDef"
    DeleteRequest: "DeleteRequestTypeDef"
