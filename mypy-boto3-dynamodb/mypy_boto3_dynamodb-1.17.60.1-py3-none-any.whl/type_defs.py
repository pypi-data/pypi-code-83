"""
Main interface for dynamodb service type definitions.

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
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyUpdateTypeDef",
    "AutoScalingSettingsDescriptionTypeDef",
    "AutoScalingSettingsUpdateTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    "BackupDescriptionTypeDef",
    "BackupDetailsTypeDef",
    "BackupSummaryTypeDef",
    "BatchStatementErrorTypeDef",
    "BatchStatementResponseTypeDef",
    "BillingModeSummaryTypeDef",
    "CapacityTypeDef",
    "ConditionCheckTypeDef",
    "ConsumedCapacityTypeDef",
    "ContinuousBackupsDescriptionTypeDef",
    "ContributorInsightsSummaryTypeDef",
    "CreateGlobalSecondaryIndexActionTypeDef",
    "CreateReplicaActionTypeDef",
    "CreateReplicationGroupMemberActionTypeDef",
    "DeleteGlobalSecondaryIndexActionTypeDef",
    "DeleteReplicaActionTypeDef",
    "DeleteReplicationGroupMemberActionTypeDef",
    "DeleteRequestTypeDef",
    "DeleteTypeDef",
    "EndpointTypeDef",
    "ExportDescriptionTypeDef",
    "ExportSummaryTypeDef",
    "FailureExceptionTypeDef",
    "GetTypeDef",
    "GlobalSecondaryIndexDescriptionTypeDef",
    "GlobalSecondaryIndexInfoTypeDef",
    "GlobalTableDescriptionTypeDef",
    "GlobalTableTypeDef",
    "ItemCollectionMetricsTypeDef",
    "ItemResponseTypeDef",
    "KeySchemaElementTypeDef",
    "KeysAndAttributesTypeDef",
    "KinesisDataStreamDestinationTypeDef",
    "LocalSecondaryIndexDescriptionTypeDef",
    "LocalSecondaryIndexInfoTypeDef",
    "PointInTimeRecoveryDescriptionTypeDef",
    "ProjectionTypeDef",
    "ProvisionedThroughputDescriptionTypeDef",
    "ProvisionedThroughputOverrideTypeDef",
    "ProvisionedThroughputTypeDef",
    "PutRequestTypeDef",
    "PutTypeDef",
    "ReplicaAutoScalingDescriptionTypeDef",
    "ReplicaDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    "ReplicaGlobalSecondaryIndexTypeDef",
    "ReplicaSettingsDescriptionTypeDef",
    "ReplicaTypeDef",
    "ResponseMetadata",
    "RestoreSummaryTypeDef",
    "SSEDescriptionTypeDef",
    "SourceTableDetailsTypeDef",
    "SourceTableFeatureDetailsTypeDef",
    "StreamSpecificationTypeDef",
    "TableAutoScalingDescriptionTypeDef",
    "TableDescriptionTypeDef",
    "TagTypeDef",
    "TimeToLiveDescriptionTypeDef",
    "TimeToLiveSpecificationTypeDef",
    "UpdateGlobalSecondaryIndexActionTypeDef",
    "UpdateReplicationGroupMemberActionTypeDef",
    "UpdateTypeDef",
    "WriteRequestTypeDef",
    "AttributeValueUpdateTypeDef",
    "BatchExecuteStatementOutputTypeDef",
    "BatchGetItemOutputTypeDef",
    "BatchStatementRequestTypeDef",
    "BatchWriteItemOutputTypeDef",
    "ConditionTypeDef",
    "CreateBackupOutputTypeDef",
    "CreateGlobalTableOutputTypeDef",
    "CreateTableOutputTypeDef",
    "DeleteBackupOutputTypeDef",
    "DeleteItemOutputTypeDef",
    "DeleteTableOutputTypeDef",
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
    "ExecuteStatementOutputTypeDef",
    "ExecuteTransactionOutputTypeDef",
    "ExpectedAttributeValueTypeDef",
    "ExportTableToPointInTimeOutputTypeDef",
    "GetItemOutputTypeDef",
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    "GlobalSecondaryIndexTypeDef",
    "GlobalSecondaryIndexUpdateTypeDef",
    "GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    "KinesisStreamingDestinationOutputTypeDef",
    "ListBackupsOutputTypeDef",
    "ListContributorInsightsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListGlobalTablesOutputTypeDef",
    "ListTablesOutputTypeDef",
    "ListTagsOfResourceOutputTypeDef",
    "LocalSecondaryIndexTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterizedStatementTypeDef",
    "PointInTimeRecoverySpecificationTypeDef",
    "PutItemOutputTypeDef",
    "QueryOutputTypeDef",
    "ReplicaAutoScalingUpdateTypeDef",
    "ReplicaSettingsUpdateTypeDef",
    "ReplicaUpdateTypeDef",
    "ReplicationGroupUpdateTypeDef",
    "RestoreTableFromBackupOutputTypeDef",
    "RestoreTableToPointInTimeOutputTypeDef",
    "SSESpecificationTypeDef",
    "ScanOutputTypeDef",
    "TransactGetItemTypeDef",
    "TransactGetItemsOutputTypeDef",
    "TransactWriteItemTypeDef",
    "TransactWriteItemsOutputTypeDef",
    "UpdateContinuousBackupsOutputTypeDef",
    "UpdateContributorInsightsOutputTypeDef",
    "UpdateGlobalTableOutputTypeDef",
    "UpdateGlobalTableSettingsOutputTypeDef",
    "UpdateItemOutputTypeDef",
    "UpdateTableOutputTypeDef",
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    "UpdateTimeToLiveOutputTypeDef",
    "WaiterConfigTypeDef",
)

ArchivalSummaryTypeDef = TypedDict(
    "ArchivalSummaryTypeDef",
    {"ArchivalDateTime": datetime, "ArchivalReason": str, "ArchivalBackupArn": str},
    total=False,
)

AttributeDefinitionTypeDef = TypedDict(
    "AttributeDefinitionTypeDef", {"AttributeName": str, "AttributeType": ScalarAttributeType}
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "PolicyName": str,
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    },
    total=False,
)

_RequiredAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingPolicyUpdateTypeDef",
    {
        "TargetTrackingScalingPolicyConfiguration": "AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef"
    },
)
_OptionalAutoScalingPolicyUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingPolicyUpdateTypeDef", {"PolicyName": str}, total=False
)


class AutoScalingPolicyUpdateTypeDef(
    _RequiredAutoScalingPolicyUpdateTypeDef, _OptionalAutoScalingPolicyUpdateTypeDef
):
    pass


AutoScalingSettingsDescriptionTypeDef = TypedDict(
    "AutoScalingSettingsDescriptionTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicies": List["AutoScalingPolicyDescriptionTypeDef"],
    },
    total=False,
)

AutoScalingSettingsUpdateTypeDef = TypedDict(
    "AutoScalingSettingsUpdateTypeDef",
    {
        "MinimumUnits": int,
        "MaximumUnits": int,
        "AutoScalingDisabled": bool,
        "AutoScalingRoleArn": str,
        "ScalingPolicyUpdate": "AutoScalingPolicyUpdateTypeDef",
    },
    total=False,
)

_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {"TargetValue": float},
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int},
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef,
):
    pass


_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {"TargetValue": float},
)
_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef = TypedDict(
    "_OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef",
    {"DisableScaleIn": bool, "ScaleInCooldown": int, "ScaleOutCooldown": int},
    total=False,
)


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(
    _RequiredAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
    _OptionalAutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef,
):
    pass


BackupDescriptionTypeDef = TypedDict(
    "BackupDescriptionTypeDef",
    {
        "BackupDetails": "BackupDetailsTypeDef",
        "SourceTableDetails": "SourceTableDetailsTypeDef",
        "SourceTableFeatureDetails": "SourceTableFeatureDetailsTypeDef",
    },
    total=False,
)

_RequiredBackupDetailsTypeDef = TypedDict(
    "_RequiredBackupDetailsTypeDef",
    {
        "BackupArn": str,
        "BackupName": str,
        "BackupStatus": BackupStatus,
        "BackupType": BackupType,
        "BackupCreationDateTime": datetime,
    },
)
_OptionalBackupDetailsTypeDef = TypedDict(
    "_OptionalBackupDetailsTypeDef",
    {"BackupSizeBytes": int, "BackupExpiryDateTime": datetime},
    total=False,
)


class BackupDetailsTypeDef(_RequiredBackupDetailsTypeDef, _OptionalBackupDetailsTypeDef):
    pass


BackupSummaryTypeDef = TypedDict(
    "BackupSummaryTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "TableArn": str,
        "BackupArn": str,
        "BackupName": str,
        "BackupCreationDateTime": datetime,
        "BackupExpiryDateTime": datetime,
        "BackupStatus": BackupStatus,
        "BackupType": BackupType,
        "BackupSizeBytes": int,
    },
    total=False,
)

BatchStatementErrorTypeDef = TypedDict(
    "BatchStatementErrorTypeDef", {"Code": BatchStatementErrorCodeEnum, "Message": str}, total=False
)

BatchStatementResponseTypeDef = TypedDict(
    "BatchStatementResponseTypeDef",
    {
        "Error": "BatchStatementErrorTypeDef",
        "TableName": str,
        "Item": Dict[
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
        ],
    },
    total=False,
)

BillingModeSummaryTypeDef = TypedDict(
    "BillingModeSummaryTypeDef",
    {"BillingMode": BillingMode, "LastUpdateToPayPerRequestDateTime": datetime},
    total=False,
)

CapacityTypeDef = TypedDict(
    "CapacityTypeDef",
    {"ReadCapacityUnits": float, "WriteCapacityUnits": float, "CapacityUnits": float},
    total=False,
)

_RequiredConditionCheckTypeDef = TypedDict(
    "_RequiredConditionCheckTypeDef",
    {
        "Key": Dict[
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
        ],
        "TableName": str,
        "ConditionExpression": str,
    },
)
_OptionalConditionCheckTypeDef = TypedDict(
    "_OptionalConditionCheckTypeDef",
    {
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
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
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailure,
    },
    total=False,
)


class ConditionCheckTypeDef(_RequiredConditionCheckTypeDef, _OptionalConditionCheckTypeDef):
    pass


ConsumedCapacityTypeDef = TypedDict(
    "ConsumedCapacityTypeDef",
    {
        "TableName": str,
        "CapacityUnits": float,
        "ReadCapacityUnits": float,
        "WriteCapacityUnits": float,
        "Table": "CapacityTypeDef",
        "LocalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
        "GlobalSecondaryIndexes": Dict[str, "CapacityTypeDef"],
    },
    total=False,
)

_RequiredContinuousBackupsDescriptionTypeDef = TypedDict(
    "_RequiredContinuousBackupsDescriptionTypeDef",
    {"ContinuousBackupsStatus": ContinuousBackupsStatus},
)
_OptionalContinuousBackupsDescriptionTypeDef = TypedDict(
    "_OptionalContinuousBackupsDescriptionTypeDef",
    {"PointInTimeRecoveryDescription": "PointInTimeRecoveryDescriptionTypeDef"},
    total=False,
)


class ContinuousBackupsDescriptionTypeDef(
    _RequiredContinuousBackupsDescriptionTypeDef, _OptionalContinuousBackupsDescriptionTypeDef
):
    pass


ContributorInsightsSummaryTypeDef = TypedDict(
    "ContributorInsightsSummaryTypeDef",
    {"TableName": str, "IndexName": str, "ContributorInsightsStatus": ContributorInsightsStatus},
    total=False,
)

_RequiredCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_RequiredCreateGlobalSecondaryIndexActionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalCreateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "_OptionalCreateGlobalSecondaryIndexActionTypeDef",
    {"ProvisionedThroughput": "ProvisionedThroughputTypeDef"},
    total=False,
)


class CreateGlobalSecondaryIndexActionTypeDef(
    _RequiredCreateGlobalSecondaryIndexActionTypeDef,
    _OptionalCreateGlobalSecondaryIndexActionTypeDef,
):
    pass


CreateReplicaActionTypeDef = TypedDict("CreateReplicaActionTypeDef", {"RegionName": str})

_RequiredCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredCreateReplicationGroupMemberActionTypeDef", {"RegionName": str}
)
_OptionalCreateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalCreateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)


class CreateReplicationGroupMemberActionTypeDef(
    _RequiredCreateReplicationGroupMemberActionTypeDef,
    _OptionalCreateReplicationGroupMemberActionTypeDef,
):
    pass


DeleteGlobalSecondaryIndexActionTypeDef = TypedDict(
    "DeleteGlobalSecondaryIndexActionTypeDef", {"IndexName": str}
)

DeleteReplicaActionTypeDef = TypedDict("DeleteReplicaActionTypeDef", {"RegionName": str})

DeleteReplicationGroupMemberActionTypeDef = TypedDict(
    "DeleteReplicationGroupMemberActionTypeDef", {"RegionName": str}
)

DeleteRequestTypeDef = TypedDict(
    "DeleteRequestTypeDef",
    {
        "Key": Dict[
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
    },
)

_RequiredDeleteTypeDef = TypedDict(
    "_RequiredDeleteTypeDef",
    {
        "Key": Dict[
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
        ],
        "TableName": str,
    },
)
_OptionalDeleteTypeDef = TypedDict(
    "_OptionalDeleteTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
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
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailure,
    },
    total=False,
)


class DeleteTypeDef(_RequiredDeleteTypeDef, _OptionalDeleteTypeDef):
    pass


EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "CachePeriodInMinutes": int})

ExportDescriptionTypeDef = TypedDict(
    "ExportDescriptionTypeDef",
    {
        "ExportArn": str,
        "ExportStatus": ExportStatus,
        "StartTime": datetime,
        "EndTime": datetime,
        "ExportManifest": str,
        "TableArn": str,
        "TableId": str,
        "ExportTime": datetime,
        "ClientToken": str,
        "S3Bucket": str,
        "S3BucketOwner": str,
        "S3Prefix": str,
        "S3SseAlgorithm": S3SseAlgorithm,
        "S3SseKmsKeyId": str,
        "FailureCode": str,
        "FailureMessage": str,
        "ExportFormat": ExportFormat,
        "BilledSizeBytes": int,
        "ItemCount": int,
    },
    total=False,
)

ExportSummaryTypeDef = TypedDict(
    "ExportSummaryTypeDef", {"ExportArn": str, "ExportStatus": ExportStatus}, total=False
)

FailureExceptionTypeDef = TypedDict(
    "FailureExceptionTypeDef", {"ExceptionName": str, "ExceptionDescription": str}, total=False
)

_RequiredGetTypeDef = TypedDict(
    "_RequiredGetTypeDef",
    {
        "Key": Dict[
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
        ],
        "TableName": str,
    },
)
_OptionalGetTypeDef = TypedDict(
    "_OptionalGetTypeDef",
    {"ProjectionExpression": str, "ExpressionAttributeNames": Dict[str, str]},
    total=False,
)


class GetTypeDef(_RequiredGetTypeDef, _OptionalGetTypeDef):
    pass


GlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "GlobalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexStatus": IndexStatus,
        "Backfilling": bool,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

GlobalSecondaryIndexInfoTypeDef = TypedDict(
    "GlobalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
    total=False,
)

GlobalTableDescriptionTypeDef = TypedDict(
    "GlobalTableDescriptionTypeDef",
    {
        "ReplicationGroup": List["ReplicaDescriptionTypeDef"],
        "GlobalTableArn": str,
        "CreationDateTime": datetime,
        "GlobalTableStatus": GlobalTableStatus,
        "GlobalTableName": str,
    },
    total=False,
)

GlobalTableTypeDef = TypedDict(
    "GlobalTableTypeDef",
    {"GlobalTableName": str, "ReplicationGroup": List["ReplicaTypeDef"]},
    total=False,
)

ItemCollectionMetricsTypeDef = TypedDict(
    "ItemCollectionMetricsTypeDef",
    {
        "ItemCollectionKey": Dict[
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
        ],
        "SizeEstimateRangeGB": List[float],
    },
    total=False,
)

ItemResponseTypeDef = TypedDict(
    "ItemResponseTypeDef",
    {
        "Item": Dict[
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
    },
    total=False,
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef", {"AttributeName": str, "KeyType": KeyType}
)

_RequiredKeysAndAttributesTypeDef = TypedDict(
    "_RequiredKeysAndAttributesTypeDef",
    {
        "Keys": List[
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
    },
)
_OptionalKeysAndAttributesTypeDef = TypedDict(
    "_OptionalKeysAndAttributesTypeDef",
    {
        "AttributesToGet": List[str],
        "ConsistentRead": bool,
        "ProjectionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
    },
    total=False,
)


class KeysAndAttributesTypeDef(
    _RequiredKeysAndAttributesTypeDef, _OptionalKeysAndAttributesTypeDef
):
    pass


KinesisDataStreamDestinationTypeDef = TypedDict(
    "KinesisDataStreamDestinationTypeDef",
    {"StreamArn": str, "DestinationStatus": DestinationStatus, "DestinationStatusDescription": str},
    total=False,
)

LocalSecondaryIndexDescriptionTypeDef = TypedDict(
    "LocalSecondaryIndexDescriptionTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
        "IndexSizeBytes": int,
        "ItemCount": int,
        "IndexArn": str,
    },
    total=False,
)

LocalSecondaryIndexInfoTypeDef = TypedDict(
    "LocalSecondaryIndexInfoTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
    total=False,
)

PointInTimeRecoveryDescriptionTypeDef = TypedDict(
    "PointInTimeRecoveryDescriptionTypeDef",
    {
        "PointInTimeRecoveryStatus": PointInTimeRecoveryStatus,
        "EarliestRestorableDateTime": datetime,
        "LatestRestorableDateTime": datetime,
    },
    total=False,
)

ProjectionTypeDef = TypedDict(
    "ProjectionTypeDef",
    {"ProjectionType": ProjectionType, "NonKeyAttributes": List[str]},
    total=False,
)

ProvisionedThroughputDescriptionTypeDef = TypedDict(
    "ProvisionedThroughputDescriptionTypeDef",
    {
        "LastIncreaseDateTime": datetime,
        "LastDecreaseDateTime": datetime,
        "NumberOfDecreasesToday": int,
        "ReadCapacityUnits": int,
        "WriteCapacityUnits": int,
    },
    total=False,
)

ProvisionedThroughputOverrideTypeDef = TypedDict(
    "ProvisionedThroughputOverrideTypeDef", {"ReadCapacityUnits": int}, total=False
)

ProvisionedThroughputTypeDef = TypedDict(
    "ProvisionedThroughputTypeDef", {"ReadCapacityUnits": int, "WriteCapacityUnits": int}
)

PutRequestTypeDef = TypedDict(
    "PutRequestTypeDef",
    {
        "Item": Dict[
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
    },
)

_RequiredPutTypeDef = TypedDict(
    "_RequiredPutTypeDef",
    {
        "Item": Dict[
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
        ],
        "TableName": str,
    },
)
_OptionalPutTypeDef = TypedDict(
    "_OptionalPutTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
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
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailure,
    },
    total=False,
)


class PutTypeDef(_RequiredPutTypeDef, _OptionalPutTypeDef):
    pass


ReplicaAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaAutoScalingDescriptionTypeDef",
    {
        "RegionName": str,
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef"],
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaStatus": ReplicaStatus,
    },
    total=False,
)

ReplicaDescriptionTypeDef = TypedDict(
    "ReplicaDescriptionTypeDef",
    {
        "RegionName": str,
        "ReplicaStatus": ReplicaStatus,
        "ReplicaStatusDescription": str,
        "ReplicaStatusPercentProgress": str,
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexDescriptionTypeDef"],
        "ReplicaInaccessibleDateTime": datetime,
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef",
    {
        "IndexName": str,
        "IndexStatus": IndexStatus,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

ReplicaGlobalSecondaryIndexDescriptionTypeDef = TypedDict(
    "ReplicaGlobalSecondaryIndexDescriptionTypeDef",
    {"IndexName": str, "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef"},
    total=False,
)

_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef", {"IndexName": str}
)
_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef",
    {
        "IndexStatus": IndexStatus,
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef,
):
    pass


_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef", {"IndexName": str}
)
_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedReadCapacityUnits": int,
        "ProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalReplicaGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


_RequiredReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredReplicaGlobalSecondaryIndexTypeDef", {"IndexName": str}
)
_OptionalReplicaGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalReplicaGlobalSecondaryIndexTypeDef",
    {"ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef"},
    total=False,
)


class ReplicaGlobalSecondaryIndexTypeDef(
    _RequiredReplicaGlobalSecondaryIndexTypeDef, _OptionalReplicaGlobalSecondaryIndexTypeDef
):
    pass


_RequiredReplicaSettingsDescriptionTypeDef = TypedDict(
    "_RequiredReplicaSettingsDescriptionTypeDef", {"RegionName": str}
)
_OptionalReplicaSettingsDescriptionTypeDef = TypedDict(
    "_OptionalReplicaSettingsDescriptionTypeDef",
    {
        "ReplicaStatus": ReplicaStatus,
        "ReplicaBillingModeSummary": "BillingModeSummaryTypeDef",
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaProvisionedWriteCapacityUnits": int,
        "ReplicaProvisionedWriteCapacityAutoScalingSettings": "AutoScalingSettingsDescriptionTypeDef",
        "ReplicaGlobalSecondaryIndexSettings": List[
            "ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef"
        ],
    },
    total=False,
)


class ReplicaSettingsDescriptionTypeDef(
    _RequiredReplicaSettingsDescriptionTypeDef, _OptionalReplicaSettingsDescriptionTypeDef
):
    pass


ReplicaTypeDef = TypedDict("ReplicaTypeDef", {"RegionName": str}, total=False)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRestoreSummaryTypeDef = TypedDict(
    "_RequiredRestoreSummaryTypeDef", {"RestoreDateTime": datetime, "RestoreInProgress": bool}
)
_OptionalRestoreSummaryTypeDef = TypedDict(
    "_OptionalRestoreSummaryTypeDef", {"SourceBackupArn": str, "SourceTableArn": str}, total=False
)


class RestoreSummaryTypeDef(_RequiredRestoreSummaryTypeDef, _OptionalRestoreSummaryTypeDef):
    pass


SSEDescriptionTypeDef = TypedDict(
    "SSEDescriptionTypeDef",
    {
        "Status": SSEStatus,
        "SSEType": SSEType,
        "KMSMasterKeyArn": str,
        "InaccessibleEncryptionDateTime": datetime,
    },
    total=False,
)

_RequiredSourceTableDetailsTypeDef = TypedDict(
    "_RequiredSourceTableDetailsTypeDef",
    {
        "TableName": str,
        "TableId": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableCreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputTypeDef",
    },
)
_OptionalSourceTableDetailsTypeDef = TypedDict(
    "_OptionalSourceTableDetailsTypeDef",
    {"TableArn": str, "TableSizeBytes": int, "ItemCount": int, "BillingMode": BillingMode},
    total=False,
)


class SourceTableDetailsTypeDef(
    _RequiredSourceTableDetailsTypeDef, _OptionalSourceTableDetailsTypeDef
):
    pass


SourceTableFeatureDetailsTypeDef = TypedDict(
    "SourceTableFeatureDetailsTypeDef",
    {
        "LocalSecondaryIndexes": List["LocalSecondaryIndexInfoTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexInfoTypeDef"],
        "StreamDescription": "StreamSpecificationTypeDef",
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
    },
    total=False,
)

_RequiredStreamSpecificationTypeDef = TypedDict(
    "_RequiredStreamSpecificationTypeDef", {"StreamEnabled": bool}
)
_OptionalStreamSpecificationTypeDef = TypedDict(
    "_OptionalStreamSpecificationTypeDef", {"StreamViewType": StreamViewType}, total=False
)


class StreamSpecificationTypeDef(
    _RequiredStreamSpecificationTypeDef, _OptionalStreamSpecificationTypeDef
):
    pass


TableAutoScalingDescriptionTypeDef = TypedDict(
    "TableAutoScalingDescriptionTypeDef",
    {
        "TableName": str,
        "TableStatus": TableStatus,
        "Replicas": List["ReplicaAutoScalingDescriptionTypeDef"],
    },
    total=False,
)

TableDescriptionTypeDef = TypedDict(
    "TableDescriptionTypeDef",
    {
        "AttributeDefinitions": List["AttributeDefinitionTypeDef"],
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "TableStatus": TableStatus,
        "CreationDateTime": datetime,
        "ProvisionedThroughput": "ProvisionedThroughputDescriptionTypeDef",
        "TableSizeBytes": int,
        "ItemCount": int,
        "TableArn": str,
        "TableId": str,
        "BillingModeSummary": "BillingModeSummaryTypeDef",
        "LocalSecondaryIndexes": List["LocalSecondaryIndexDescriptionTypeDef"],
        "GlobalSecondaryIndexes": List["GlobalSecondaryIndexDescriptionTypeDef"],
        "StreamSpecification": "StreamSpecificationTypeDef",
        "LatestStreamLabel": str,
        "LatestStreamArn": str,
        "GlobalTableVersion": str,
        "Replicas": List["ReplicaDescriptionTypeDef"],
        "RestoreSummary": "RestoreSummaryTypeDef",
        "SSEDescription": "SSEDescriptionTypeDef",
        "ArchivalSummary": "ArchivalSummaryTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TimeToLiveDescriptionTypeDef = TypedDict(
    "TimeToLiveDescriptionTypeDef",
    {"TimeToLiveStatus": TimeToLiveStatus, "AttributeName": str},
    total=False,
)

TimeToLiveSpecificationTypeDef = TypedDict(
    "TimeToLiveSpecificationTypeDef", {"Enabled": bool, "AttributeName": str}
)

UpdateGlobalSecondaryIndexActionTypeDef = TypedDict(
    "UpdateGlobalSecondaryIndexActionTypeDef",
    {"IndexName": str, "ProvisionedThroughput": "ProvisionedThroughputTypeDef"},
)

_RequiredUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_RequiredUpdateReplicationGroupMemberActionTypeDef", {"RegionName": str}
)
_OptionalUpdateReplicationGroupMemberActionTypeDef = TypedDict(
    "_OptionalUpdateReplicationGroupMemberActionTypeDef",
    {
        "KMSMasterKeyId": str,
        "ProvisionedThroughputOverride": "ProvisionedThroughputOverrideTypeDef",
        "GlobalSecondaryIndexes": List["ReplicaGlobalSecondaryIndexTypeDef"],
    },
    total=False,
)


class UpdateReplicationGroupMemberActionTypeDef(
    _RequiredUpdateReplicationGroupMemberActionTypeDef,
    _OptionalUpdateReplicationGroupMemberActionTypeDef,
):
    pass


_RequiredUpdateTypeDef = TypedDict(
    "_RequiredUpdateTypeDef",
    {
        "Key": Dict[
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
        ],
        "UpdateExpression": str,
        "TableName": str,
    },
)
_OptionalUpdateTypeDef = TypedDict(
    "_OptionalUpdateTypeDef",
    {
        "ConditionExpression": str,
        "ExpressionAttributeNames": Dict[str, str],
        "ExpressionAttributeValues": Dict[
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
        ],
        "ReturnValuesOnConditionCheckFailure": ReturnValuesOnConditionCheckFailure,
    },
    total=False,
)


class UpdateTypeDef(_RequiredUpdateTypeDef, _OptionalUpdateTypeDef):
    pass


WriteRequestTypeDef = TypedDict(
    "WriteRequestTypeDef",
    {"PutRequest": "PutRequestTypeDef", "DeleteRequest": "DeleteRequestTypeDef"},
    total=False,
)

AttributeValueUpdateTypeDef = TypedDict(
    "AttributeValueUpdateTypeDef",
    {
        "Value": Union[
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
        "Action": AttributeAction,
    },
    total=False,
)

BatchExecuteStatementOutputTypeDef = TypedDict(
    "BatchExecuteStatementOutputTypeDef",
    {"Responses": List["BatchStatementResponseTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

BatchGetItemOutputTypeDef = TypedDict(
    "BatchGetItemOutputTypeDef",
    {
        "Responses": Dict[
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
        ],
        "UnprocessedKeys": Dict[str, "KeysAndAttributesTypeDef"],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredBatchStatementRequestTypeDef = TypedDict(
    "_RequiredBatchStatementRequestTypeDef", {"Statement": str}
)
_OptionalBatchStatementRequestTypeDef = TypedDict(
    "_OptionalBatchStatementRequestTypeDef",
    {
        "Parameters": List[
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
        ],
        "ConsistentRead": bool,
    },
    total=False,
)


class BatchStatementRequestTypeDef(
    _RequiredBatchStatementRequestTypeDef, _OptionalBatchStatementRequestTypeDef
):
    pass


BatchWriteItemOutputTypeDef = TypedDict(
    "BatchWriteItemOutputTypeDef",
    {
        "UnprocessedItems": Dict[str, List["WriteRequestTypeDef"]],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredConditionTypeDef = TypedDict(
    "_RequiredConditionTypeDef", {"ComparisonOperator": ComparisonOperator}
)
_OptionalConditionTypeDef = TypedDict(
    "_OptionalConditionTypeDef",
    {
        "AttributeValueList": List[
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
    },
    total=False,
)


class ConditionTypeDef(_RequiredConditionTypeDef, _OptionalConditionTypeDef):
    pass


CreateBackupOutputTypeDef = TypedDict(
    "CreateBackupOutputTypeDef",
    {"BackupDetails": "BackupDetailsTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateGlobalTableOutputTypeDef = TypedDict(
    "CreateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateTableOutputTypeDef = TypedDict(
    "CreateTableOutputTypeDef",
    {"TableDescription": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteBackupOutputTypeDef = TypedDict(
    "DeleteBackupOutputTypeDef",
    {"BackupDescription": "BackupDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteItemOutputTypeDef = TypedDict(
    "DeleteItemOutputTypeDef",
    {
        "Attributes": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteTableOutputTypeDef = TypedDict(
    "DeleteTableOutputTypeDef",
    {"TableDescription": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeBackupOutputTypeDef = TypedDict(
    "DescribeBackupOutputTypeDef",
    {"BackupDescription": "BackupDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeContinuousBackupsOutputTypeDef = TypedDict(
    "DescribeContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeContributorInsightsOutputTypeDef = TypedDict(
    "DescribeContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsRuleList": List[str],
        "ContributorInsightsStatus": ContributorInsightsStatus,
        "LastUpdateDateTime": datetime,
        "FailureException": "FailureExceptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef", {"Endpoints": List["EndpointTypeDef"]}
)

DescribeExportOutputTypeDef = TypedDict(
    "DescribeExportOutputTypeDef",
    {"ExportDescription": "ExportDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeGlobalTableOutputTypeDef = TypedDict(
    "DescribeGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeGlobalTableSettingsOutputTypeDef = TypedDict(
    "DescribeGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeKinesisStreamingDestinationOutputTypeDef = TypedDict(
    "DescribeKinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "KinesisDataStreamDestinations": List["KinesisDataStreamDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "AccountMaxReadCapacityUnits": int,
        "AccountMaxWriteCapacityUnits": int,
        "TableMaxReadCapacityUnits": int,
        "TableMaxWriteCapacityUnits": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTableOutputTypeDef = TypedDict(
    "DescribeTableOutputTypeDef",
    {"Table": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "DescribeTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTimeToLiveOutputTypeDef = TypedDict(
    "DescribeTimeToLiveOutputTypeDef",
    {
        "TimeToLiveDescription": "TimeToLiveDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ExecuteStatementOutputTypeDef = TypedDict(
    "ExecuteStatementOutputTypeDef",
    {
        "Items": List[
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
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ExecuteTransactionOutputTypeDef = TypedDict(
    "ExecuteTransactionOutputTypeDef",
    {"Responses": List["ItemResponseTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ExpectedAttributeValueTypeDef = TypedDict(
    "ExpectedAttributeValueTypeDef",
    {
        "Value": Union[
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
        "Exists": bool,
        "ComparisonOperator": ComparisonOperator,
        "AttributeValueList": List[
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
        ],
    },
    total=False,
)

ExportTableToPointInTimeOutputTypeDef = TypedDict(
    "ExportTableToPointInTimeOutputTypeDef",
    {"ExportDescription": "ExportDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetItemOutputTypeDef = TypedDict(
    "GetItemOutputTypeDef",
    {
        "Item": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GlobalSecondaryIndexAutoScalingUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexAutoScalingUpdateTypeDef",
    {
        "IndexName": str,
        "ProvisionedWriteCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)

_RequiredGlobalSecondaryIndexTypeDef = TypedDict(
    "_RequiredGlobalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)
_OptionalGlobalSecondaryIndexTypeDef = TypedDict(
    "_OptionalGlobalSecondaryIndexTypeDef",
    {"ProvisionedThroughput": "ProvisionedThroughputTypeDef"},
    total=False,
)


class GlobalSecondaryIndexTypeDef(
    _RequiredGlobalSecondaryIndexTypeDef, _OptionalGlobalSecondaryIndexTypeDef
):
    pass


GlobalSecondaryIndexUpdateTypeDef = TypedDict(
    "GlobalSecondaryIndexUpdateTypeDef",
    {
        "Update": "UpdateGlobalSecondaryIndexActionTypeDef",
        "Create": "CreateGlobalSecondaryIndexActionTypeDef",
        "Delete": "DeleteGlobalSecondaryIndexActionTypeDef",
    },
    total=False,
)

_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef", {"IndexName": str}
)
_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef = TypedDict(
    "_OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef",
    {
        "ProvisionedWriteCapacityUnits": int,
        "ProvisionedWriteCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(
    _RequiredGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
    _OptionalGlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef,
):
    pass


KinesisStreamingDestinationOutputTypeDef = TypedDict(
    "KinesisStreamingDestinationOutputTypeDef",
    {
        "TableName": str,
        "StreamArn": str,
        "DestinationStatus": DestinationStatus,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListBackupsOutputTypeDef = TypedDict(
    "ListBackupsOutputTypeDef",
    {
        "BackupSummaries": List["BackupSummaryTypeDef"],
        "LastEvaluatedBackupArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListContributorInsightsOutputTypeDef = TypedDict(
    "ListContributorInsightsOutputTypeDef",
    {
        "ContributorInsightsSummaries": List["ContributorInsightsSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "ExportSummaries": List["ExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListGlobalTablesOutputTypeDef = TypedDict(
    "ListGlobalTablesOutputTypeDef",
    {
        "GlobalTables": List["GlobalTableTypeDef"],
        "LastEvaluatedGlobalTableName": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTablesOutputTypeDef = TypedDict(
    "ListTablesOutputTypeDef",
    {
        "TableNames": List[str],
        "LastEvaluatedTableName": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsOfResourceOutputTypeDef = TypedDict(
    "ListTagsOfResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

LocalSecondaryIndexTypeDef = TypedDict(
    "LocalSecondaryIndexTypeDef",
    {
        "IndexName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Projection": "ProjectionTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredParameterizedStatementTypeDef = TypedDict(
    "_RequiredParameterizedStatementTypeDef", {"Statement": str}
)
_OptionalParameterizedStatementTypeDef = TypedDict(
    "_OptionalParameterizedStatementTypeDef",
    {
        "Parameters": List[
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
    },
    total=False,
)


class ParameterizedStatementTypeDef(
    _RequiredParameterizedStatementTypeDef, _OptionalParameterizedStatementTypeDef
):
    pass


PointInTimeRecoverySpecificationTypeDef = TypedDict(
    "PointInTimeRecoverySpecificationTypeDef", {"PointInTimeRecoveryEnabled": bool}
)

PutItemOutputTypeDef = TypedDict(
    "PutItemOutputTypeDef",
    {
        "Attributes": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

QueryOutputTypeDef = TypedDict(
    "QueryOutputTypeDef",
    {
        "Items": List[
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
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_RequiredReplicaAutoScalingUpdateTypeDef", {"RegionName": str}
)
_OptionalReplicaAutoScalingUpdateTypeDef = TypedDict(
    "_OptionalReplicaAutoScalingUpdateTypeDef",
    {
        "ReplicaGlobalSecondaryIndexUpdates": List[
            "ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef"
        ],
        "ReplicaProvisionedReadCapacityAutoScalingUpdate": "AutoScalingSettingsUpdateTypeDef",
    },
    total=False,
)


class ReplicaAutoScalingUpdateTypeDef(
    _RequiredReplicaAutoScalingUpdateTypeDef, _OptionalReplicaAutoScalingUpdateTypeDef
):
    pass


_RequiredReplicaSettingsUpdateTypeDef = TypedDict(
    "_RequiredReplicaSettingsUpdateTypeDef", {"RegionName": str}
)
_OptionalReplicaSettingsUpdateTypeDef = TypedDict(
    "_OptionalReplicaSettingsUpdateTypeDef",
    {
        "ReplicaProvisionedReadCapacityUnits": int,
        "ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate": "AutoScalingSettingsUpdateTypeDef",
        "ReplicaGlobalSecondaryIndexSettingsUpdate": List[
            "ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef"
        ],
    },
    total=False,
)


class ReplicaSettingsUpdateTypeDef(
    _RequiredReplicaSettingsUpdateTypeDef, _OptionalReplicaSettingsUpdateTypeDef
):
    pass


ReplicaUpdateTypeDef = TypedDict(
    "ReplicaUpdateTypeDef",
    {"Create": "CreateReplicaActionTypeDef", "Delete": "DeleteReplicaActionTypeDef"},
    total=False,
)

ReplicationGroupUpdateTypeDef = TypedDict(
    "ReplicationGroupUpdateTypeDef",
    {
        "Create": "CreateReplicationGroupMemberActionTypeDef",
        "Update": "UpdateReplicationGroupMemberActionTypeDef",
        "Delete": "DeleteReplicationGroupMemberActionTypeDef",
    },
    total=False,
)

RestoreTableFromBackupOutputTypeDef = TypedDict(
    "RestoreTableFromBackupOutputTypeDef",
    {"TableDescription": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RestoreTableToPointInTimeOutputTypeDef = TypedDict(
    "RestoreTableToPointInTimeOutputTypeDef",
    {"TableDescription": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SSESpecificationTypeDef = TypedDict(
    "SSESpecificationTypeDef",
    {"Enabled": bool, "SSEType": SSEType, "KMSMasterKeyId": str},
    total=False,
)

ScanOutputTypeDef = TypedDict(
    "ScanOutputTypeDef",
    {
        "Items": List[
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
        "Count": int,
        "ScannedCount": int,
        "LastEvaluatedKey": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

TransactGetItemTypeDef = TypedDict("TransactGetItemTypeDef", {"Get": "GetTypeDef"})

TransactGetItemsOutputTypeDef = TypedDict(
    "TransactGetItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "Responses": List["ItemResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

TransactWriteItemTypeDef = TypedDict(
    "TransactWriteItemTypeDef",
    {
        "ConditionCheck": "ConditionCheckTypeDef",
        "Put": "PutTypeDef",
        "Delete": "DeleteTypeDef",
        "Update": "UpdateTypeDef",
    },
    total=False,
)

TransactWriteItemsOutputTypeDef = TypedDict(
    "TransactWriteItemsOutputTypeDef",
    {
        "ConsumedCapacity": List["ConsumedCapacityTypeDef"],
        "ItemCollectionMetrics": Dict[str, List["ItemCollectionMetricsTypeDef"]],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateContinuousBackupsOutputTypeDef = TypedDict(
    "UpdateContinuousBackupsOutputTypeDef",
    {
        "ContinuousBackupsDescription": "ContinuousBackupsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateContributorInsightsOutputTypeDef = TypedDict(
    "UpdateContributorInsightsOutputTypeDef",
    {
        "TableName": str,
        "IndexName": str,
        "ContributorInsightsStatus": ContributorInsightsStatus,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateGlobalTableOutputTypeDef = TypedDict(
    "UpdateGlobalTableOutputTypeDef",
    {
        "GlobalTableDescription": "GlobalTableDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateGlobalTableSettingsOutputTypeDef = TypedDict(
    "UpdateGlobalTableSettingsOutputTypeDef",
    {
        "GlobalTableName": str,
        "ReplicaSettings": List["ReplicaSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateItemOutputTypeDef = TypedDict(
    "UpdateItemOutputTypeDef",
    {
        "Attributes": Dict[
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
        ],
        "ConsumedCapacity": "ConsumedCapacityTypeDef",
        "ItemCollectionMetrics": "ItemCollectionMetricsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateTableOutputTypeDef = TypedDict(
    "UpdateTableOutputTypeDef",
    {"TableDescription": "TableDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateTableReplicaAutoScalingOutputTypeDef = TypedDict(
    "UpdateTableReplicaAutoScalingOutputTypeDef",
    {
        "TableAutoScalingDescription": "TableAutoScalingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

UpdateTimeToLiveOutputTypeDef = TypedDict(
    "UpdateTimeToLiveOutputTypeDef",
    {
        "TimeToLiveSpecification": "TimeToLiveSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
