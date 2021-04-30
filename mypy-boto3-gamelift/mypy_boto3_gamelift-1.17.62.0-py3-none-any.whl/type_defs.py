"""
Main interface for gamelift service type definitions.

Usage::

    ```python
    from mypy_boto3_gamelift.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_gamelift.literals import (
    BackfillMode,
    BalancingStrategy,
    BuildStatus,
    CertificateType,
    ComparisonOperatorType,
    EC2InstanceType,
    EventCode,
    FleetAction,
    FleetStatus,
    FleetType,
    FlexMatchMode,
    GameServerClaimStatus,
    GameServerGroupAction,
    GameServerGroupInstanceType,
    GameServerGroupStatus,
    GameServerInstanceStatus,
    GameServerProtectionPolicy,
    GameServerUtilizationStatus,
    GameSessionPlacementState,
    GameSessionStatus,
    GameSessionStatusReason,
    InstanceStatus,
    IpProtocol,
    LocationUpdateStatus,
    MatchmakingConfigurationStatus,
    MetricName,
    OperatingSystem,
    PlayerSessionCreationPolicy,
    PlayerSessionStatus,
    PolicyType,
    PriorityType,
    ProtectionPolicy,
    RoutingStrategyType,
    ScalingAdjustmentType,
    ScalingStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FilterConfigurationTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerInstanceTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LocationAttributesTypeDef",
    "LocationStateTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "PriorityConfigurationTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadata",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "ServerProcessTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
    "ClaimGameServerOutputTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateFleetLocationsOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "CreateGameSessionOutputTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "CreateScriptOutputTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "DeleteFleetLocationsOutputTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DescribeAliasOutputTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetLocationAttributesOutputTypeDef",
    "DescribeFleetLocationCapacityOutputTypeDef",
    "DescribeFleetLocationUtilizationOutputTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "DescribeGameServerInstancesOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "DescribeInstancesOutputTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "DescribeScriptOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    "DesiredPlayerSessionTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopFleetActionsOutputTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "UpdateAliasOutputTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "UpdateGameServerOutputTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "UpdateScriptOutputTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": str,
        "Name": str,
        "AliasArn": str,
        "Description": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {"S": str, "N": float, "SL": List[str], "SDM": Dict[str, float]},
    total=False,
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str},
    total=False,
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": str,
        "BuildArn": str,
        "Name": str,
        "Version": str,
        "Status": BuildStatus,
        "SizeOnDisk": int,
        "OperatingSystem": OperatingSystem,
        "CreationTime": datetime,
    },
    total=False,
)

CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef", {"CertificateType": CertificateType}
)

EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": int,
        "MINIMUM": int,
        "MAXIMUM": int,
        "PENDING": int,
        "ACTIVE": int,
        "IDLE": int,
        "TERMINATING": int,
    },
    total=False,
)

EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": EC2InstanceType,
        "CurrentInstances": int,
        "InstanceLimit": int,
        "Location": str,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": str,
        "ResourceId": str,
        "EventCode": EventCode,
        "Message": str,
        "EventTime": datetime,
        "PreSignedLogUrl": str,
    },
    total=False,
)

FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef", {"AllowedLocations": List[str]}, total=False
)

FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "FleetType": FleetType,
        "InstanceType": EC2InstanceType,
        "Description": str,
        "Name": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": FleetStatus,
        "BuildId": str,
        "BuildArn": str,
        "ScriptId": str,
        "ScriptArn": str,
        "ServerLaunchPath": str,
        "ServerLaunchParameters": str,
        "LogPaths": List[str],
        "NewGameSessionProtectionPolicy": ProtectionPolicy,
        "OperatingSystem": OperatingSystem,
        "ResourceCreationLimitPolicy": "ResourceCreationLimitPolicyTypeDef",
        "MetricGroups": List[str],
        "StoppedActions": List[FleetAction],
        "InstanceRoleArn": str,
        "CertificateConfiguration": "CertificateConfigurationTypeDef",
    },
    total=False,
)

FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceType": EC2InstanceType,
        "InstanceCounts": "EC2InstanceCountsTypeDef",
        "Location": str,
    },
    total=False,
)

FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ActiveServerProcessCount": int,
        "ActiveGameSessionCount": int,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Location": str,
    },
    total=False,
)

GamePropertyTypeDef = TypedDict("GamePropertyTypeDef", {"Key": str, "Value": str})

GameServerGroupTypeDef = TypedDict(
    "GameServerGroupTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "RoleArn": str,
        "InstanceDefinitions": List["InstanceDefinitionTypeDef"],
        "BalancingStrategy": BalancingStrategy,
        "GameServerProtectionPolicy": GameServerProtectionPolicy,
        "AutoScalingGroupArn": str,
        "Status": GameServerGroupStatus,
        "StatusReason": str,
        "SuspendedActions": List[GameServerGroupAction],
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

GameServerInstanceTypeDef = TypedDict(
    "GameServerInstanceTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "InstanceId": str,
        "InstanceStatus": GameServerInstanceStatus,
    },
    total=False,
)

GameServerTypeDef = TypedDict(
    "GameServerTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerGroupArn": str,
        "GameServerId": str,
        "InstanceId": str,
        "ConnectionInfo": str,
        "GameServerData": str,
        "ClaimStatus": GameServerClaimStatus,
        "UtilizationStatus": GameServerUtilizationStatus,
        "RegistrationTime": datetime,
        "LastClaimTime": datetime,
        "LastHealthCheckTime": datetime,
    },
    total=False,
)

GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": str,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "MatchedPlayerSessions": List["MatchedPlayerSessionTypeDef"],
    },
    total=False,
)

GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {"GameSession": "GameSessionTypeDef", "ProtectionPolicy": ProtectionPolicy},
    total=False,
)

GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "Status": GameSessionPlacementState,
        "GameProperties": List["GamePropertyTypeDef"],
        "MaximumPlayerSessionCount": int,
        "GameSessionName": str,
        "GameSessionId": str,
        "GameSessionArn": str,
        "GameSessionRegion": str,
        "PlayerLatencies": List["PlayerLatencyTypeDef"],
        "StartTime": datetime,
        "EndTime": datetime,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlacedPlayerSessions": List["PlacedPlayerSessionTypeDef"],
        "GameSessionData": str,
        "MatchmakerData": str,
    },
    total=False,
)

GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef", {"DestinationArn": str}, total=False
)

GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": str,
        "GameSessionQueueArn": str,
        "TimeoutInSeconds": int,
        "PlayerLatencyPolicies": List["PlayerLatencyPolicyTypeDef"],
        "Destinations": List["GameSessionQueueDestinationTypeDef"],
        "FilterConfiguration": "FilterConfigurationTypeDef",
        "PriorityConfiguration": "PriorityConfigurationTypeDef",
        "CustomEventData": str,
        "NotificationTarget": str,
    },
    total=False,
)

GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": str,
        "Name": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "CurrentPlayerSessionCount": int,
        "MaximumPlayerSessionCount": int,
        "Status": GameSessionStatus,
        "StatusReason": GameSessionStatusReason,
        "GameProperties": List["GamePropertyTypeDef"],
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerSessionCreationPolicy": PlayerSessionCreationPolicy,
        "CreatorId": str,
        "GameSessionData": str,
        "MatchmakerData": str,
        "Location": str,
    },
    total=False,
)

InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
        "IpAddress": str,
        "OperatingSystem": OperatingSystem,
        "Credentials": "InstanceCredentialsTypeDef",
    },
    total=False,
)

InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef", {"UserName": str, "Secret": str}, total=False
)

_RequiredInstanceDefinitionTypeDef = TypedDict(
    "_RequiredInstanceDefinitionTypeDef", {"InstanceType": GameServerGroupInstanceType}
)
_OptionalInstanceDefinitionTypeDef = TypedDict(
    "_OptionalInstanceDefinitionTypeDef", {"WeightedCapacity": str}, total=False
)


class InstanceDefinitionTypeDef(
    _RequiredInstanceDefinitionTypeDef, _OptionalInstanceDefinitionTypeDef
):
    pass


InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InstanceId": str,
        "IpAddress": str,
        "DnsName": str,
        "OperatingSystem": OperatingSystem,
        "Type": EC2InstanceType,
        "Status": InstanceStatus,
        "CreationTime": datetime,
        "Location": str,
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef", {"FromPort": int, "ToPort": int, "IpRange": str, "Protocol": IpProtocol}
)

LocationAttributesTypeDef = TypedDict(
    "LocationAttributesTypeDef",
    {
        "LocationState": "LocationStateTypeDef",
        "StoppedActions": List[FleetAction],
        "UpdateStatus": LocationUpdateStatus,
    },
    total=False,
)

LocationStateTypeDef = TypedDict(
    "LocationStateTypeDef", {"Location": str, "Status": FleetStatus}, total=False
)

MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef", {"PlayerId": str, "PlayerSessionId": str}, total=False
)

MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": str,
        "ConfigurationArn": str,
        "Description": str,
        "GameSessionQueueArns": List[str],
        "RequestTimeoutSeconds": int,
        "AcceptanceTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "RuleSetArn": str,
        "NotificationTarget": str,
        "AdditionalPlayerCount": int,
        "CustomEventData": str,
        "CreationTime": datetime,
        "GameProperties": List["GamePropertyTypeDef"],
        "GameSessionData": str,
        "BackfillMode": BackfillMode,
        "FlexMatchMode": FlexMatchMode,
    },
    total=False,
)

_RequiredMatchmakingRuleSetTypeDef = TypedDict(
    "_RequiredMatchmakingRuleSetTypeDef", {"RuleSetBody": str}
)
_OptionalMatchmakingRuleSetTypeDef = TypedDict(
    "_OptionalMatchmakingRuleSetTypeDef",
    {"RuleSetName": str, "RuleSetArn": str, "CreationTime": datetime},
    total=False,
)


class MatchmakingRuleSetTypeDef(
    _RequiredMatchmakingRuleSetTypeDef, _OptionalMatchmakingRuleSetTypeDef
):
    pass


MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": str,
        "ConfigurationName": str,
        "ConfigurationArn": str,
        "Status": MatchmakingConfigurationStatus,
        "StatusReason": str,
        "StatusMessage": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Players": List["PlayerTypeDef"],
        "GameSessionConnectionInfo": "GameSessionConnectionInfoTypeDef",
        "EstimatedWaitTime": int,
    },
    total=False,
)

PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef", {"PlayerId": str, "PlayerSessionId": str}, total=False
)

PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {"MaximumIndividualPlayerLatencyMilliseconds": int, "PolicyDurationSeconds": int},
    total=False,
)

PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {"PlayerId": str, "RegionIdentifier": str, "LatencyInMilliseconds": float},
    total=False,
)

PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": str,
        "PlayerId": str,
        "GameSessionId": str,
        "FleetId": str,
        "FleetArn": str,
        "CreationTime": datetime,
        "TerminationTime": datetime,
        "Status": PlayerSessionStatus,
        "IpAddress": str,
        "DnsName": str,
        "Port": int,
        "PlayerData": str,
    },
    total=False,
)

PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": str,
        "PlayerAttributes": Dict[str, "AttributeValueTypeDef"],
        "Team": str,
        "LatencyInMs": Dict[str, int],
    },
    total=False,
)

PriorityConfigurationTypeDef = TypedDict(
    "PriorityConfigurationTypeDef",
    {"PriorityOrder": List[PriorityType], "LocationOrder": List[str]},
    total=False,
)

ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {"NewGameSessionsPerCreator": int, "PolicyPeriodInMinutes": int},
    total=False,
)

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

RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {"Type": RoutingStrategyType, "FleetId": str, "Message": str},
    total=False,
)

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": List["ServerProcessTypeDef"],
        "MaxConcurrentGameSessionActivations": int,
        "GameSessionActivationTimeoutSeconds": int,
    },
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {"Bucket": str, "Key": str, "RoleArn": str, "ObjectVersion": str},
    total=False,
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Name": str,
        "Status": ScalingStatusType,
        "ScalingAdjustment": int,
        "ScalingAdjustmentType": ScalingAdjustmentType,
        "ComparisonOperator": ComparisonOperatorType,
        "Threshold": float,
        "EvaluationPeriods": int,
        "MetricName": MetricName,
        "PolicyType": PolicyType,
        "TargetConfiguration": "TargetConfigurationTypeDef",
        "UpdateStatus": LocationUpdateStatus,
        "Location": str,
    },
    total=False,
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": str,
        "ScriptArn": str,
        "Name": str,
        "Version": str,
        "SizeOnDisk": int,
        "CreationTime": datetime,
        "StorageLocation": "S3LocationTypeDef",
    },
    total=False,
)

_RequiredServerProcessTypeDef = TypedDict(
    "_RequiredServerProcessTypeDef", {"LaunchPath": str, "ConcurrentExecutions": int}
)
_OptionalServerProcessTypeDef = TypedDict(
    "_OptionalServerProcessTypeDef", {"Parameters": str}, total=False
)


class ServerProcessTypeDef(_RequiredServerProcessTypeDef, _OptionalServerProcessTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TargetConfigurationTypeDef = TypedDict("TargetConfigurationTypeDef", {"TargetValue": float})

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef", {"TargetValue": float}
)

VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
    },
    total=False,
)

VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef", {"Code": str, "Message": str}, total=False
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "IpV4CidrBlock": str,
        "VpcPeeringConnectionId": str,
        "Status": "VpcPeeringConnectionStatusTypeDef",
        "PeerVpcId": str,
        "GameLiftVpcId": str,
    },
    total=False,
)

ClaimGameServerOutputTypeDef = TypedDict(
    "ClaimGameServerOutputTypeDef",
    {"GameServer": "GameServerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {"Alias": "AliasTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateFleetLocationsOutputTypeDef = TypedDict(
    "CreateFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef",
    {
        "FleetAttributes": "FleetAttributesTypeDef",
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

CreateGameServerGroupOutputTypeDef = TypedDict(
    "CreateGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef",
    {"GameSession": "GameSessionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {"GameSessionQueue": "GameSessionQueueTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {"Configuration": "MatchmakingConfigurationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredCreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "_RequiredCreateMatchmakingRuleSetOutputTypeDef", {"RuleSet": "MatchmakingRuleSetTypeDef"}
)
_OptionalCreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "_OptionalCreateMatchmakingRuleSetOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateMatchmakingRuleSetOutputTypeDef(
    _RequiredCreateMatchmakingRuleSetOutputTypeDef, _OptionalCreateMatchmakingRuleSetOutputTypeDef
):
    pass


CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef",
    {"PlayerSession": "PlayerSessionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef",
    {"PlayerSessions": List["PlayerSessionTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef",
    {"Script": "ScriptTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {
        "VpcPeeringAuthorization": "VpcPeeringAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteFleetLocationsOutputTypeDef = TypedDict(
    "DeleteFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteGameServerGroupOutputTypeDef = TypedDict(
    "DeleteGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef",
    {"Alias": "AliasTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef",
    {"Build": "BuildTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {"EC2InstanceLimits": List["EC2InstanceLimitTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {
        "FleetAttributes": List["FleetAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {
        "FleetCapacity": List["FleetCapacityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {"Events": List["EventTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeFleetLocationAttributesOutputTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List["LocationAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeFleetLocationCapacityOutputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputTypeDef",
    {"FleetCapacity": "FleetCapacityTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeFleetLocationUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputTypeDef",
    {"FleetUtilization": "FleetUtilizationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List["IpPermissionTypeDef"],
        "UpdateStatus": LocationUpdateStatus,
        "Location": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {
        "FleetUtilization": List["FleetUtilizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeGameServerGroupOutputTypeDef = TypedDict(
    "DescribeGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeGameServerInstancesOutputTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputTypeDef",
    {
        "GameServerInstances": List["GameServerInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeGameServerOutputTypeDef = TypedDict(
    "DescribeGameServerOutputTypeDef",
    {"GameServer": "GameServerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {
        "GameSessionDetails": List["GameSessionDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": "GameSessionPlacementTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {
        "GameSessionQueues": List["GameSessionQueueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {
        "Configurations": List["MatchmakingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef",
    {"TicketList": List["MatchmakingTicketTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredDescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "_RequiredDescribeMatchmakingRuleSetsOutputTypeDef",
    {"RuleSets": List["MatchmakingRuleSetTypeDef"]},
)
_OptionalDescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "_OptionalDescribeMatchmakingRuleSetsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeMatchmakingRuleSetsOutputTypeDef(
    _RequiredDescribeMatchmakingRuleSetsOutputTypeDef,
    _OptionalDescribeMatchmakingRuleSetsOutputTypeDef,
):
    pass


DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {"RuntimeConfiguration": "RuntimeConfigurationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef",
    {"Script": "ScriptTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {
        "VpcPeeringAuthorizations": List["VpcPeeringAuthorizationTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef", {"PlayerId": str, "PlayerData": str}, total=False
)

_RequiredGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_RequiredGameServerGroupAutoScalingPolicyTypeDef",
    {"TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef"},
)
_OptionalGameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "_OptionalGameServerGroupAutoScalingPolicyTypeDef",
    {"EstimatedInstanceWarmup": int},
    total=False,
)


class GameServerGroupAutoScalingPolicyTypeDef(
    _RequiredGameServerGroupAutoScalingPolicyTypeDef,
    _OptionalGameServerGroupAutoScalingPolicyTypeDef,
):
    pass


GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef",
    {"PreSignedUrl": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef",
    {"InstanceAccess": "InstanceAccessTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {"LaunchTemplateId": str, "LaunchTemplateName": str, "Version": str},
    total=False,
)

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {"Aliases": List["AliasTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {"Builds": List["BuildTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef",
    {"FleetIds": List[str], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListGameServerGroupsOutputTypeDef = TypedDict(
    "ListGameServerGroupsOutputTypeDef",
    {
        "GameServerGroups": List["GameServerGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListGameServersOutputTypeDef = TypedDict(
    "ListGameServersOutputTypeDef",
    {
        "GameServers": List["GameServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef",
    {"Scripts": List["ScriptTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

LocationConfigurationTypeDef = TypedDict(
    "LocationConfigurationTypeDef", {"Location": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef",
    {"Name": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RegisterGameServerOutputTypeDef = TypedDict(
    "RegisterGameServerOutputTypeDef",
    {"GameServer": "GameServerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ResolveAliasOutputTypeDef = TypedDict(
    "ResolveAliasOutputTypeDef",
    {"FleetId": str, "FleetArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ResumeGameServerGroupOutputTypeDef = TypedDict(
    "ResumeGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

StartFleetActionsOutputTypeDef = TypedDict(
    "StartFleetActionsOutputTypeDef",
    {"FleetId": str, "FleetArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": "GameSessionPlacementTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef",
    {"MatchmakingTicket": "MatchmakingTicketTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef",
    {"MatchmakingTicket": "MatchmakingTicketTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopFleetActionsOutputTypeDef = TypedDict(
    "StopFleetActionsOutputTypeDef",
    {"FleetId": str, "FleetArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {"GameSessionPlacement": "GameSessionPlacementTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SuspendGameServerGroupOutputTypeDef = TypedDict(
    "SuspendGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {"Alias": "AliasTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef",
    {"Build": "BuildTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef",
    {"FleetId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef",
    {"FleetId": str, "FleetArn": str, "Location": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef",
    {"FleetId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGameServerGroupOutputTypeDef = TypedDict(
    "UpdateGameServerGroupOutputTypeDef",
    {"GameServerGroup": "GameServerGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGameServerOutputTypeDef = TypedDict(
    "UpdateGameServerOutputTypeDef",
    {"GameServer": "GameServerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef",
    {"GameSession": "GameSessionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {"GameSessionQueue": "GameSessionQueueTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {"Configuration": "MatchmakingConfigurationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {"RuntimeConfiguration": "RuntimeConfigurationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef",
    {"Script": "ScriptTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef",
    {"Valid": bool, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
