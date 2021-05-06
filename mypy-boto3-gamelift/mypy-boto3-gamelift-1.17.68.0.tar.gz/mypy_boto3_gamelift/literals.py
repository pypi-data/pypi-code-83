"""
Type annotations for gamelift service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/literals.html)

Usage::

    ```python
    from mypy_boto3_gamelift.literals import AcceptanceType

    data: AcceptanceType = "ACCEPT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AcceptanceType",
    "BackfillMode",
    "BalancingStrategy",
    "BuildStatus",
    "CertificateType",
    "ComparisonOperatorType",
    "DescribeFleetAttributesPaginatorName",
    "DescribeFleetCapacityPaginatorName",
    "DescribeFleetEventsPaginatorName",
    "DescribeFleetUtilizationPaginatorName",
    "DescribeGameServerInstancesPaginatorName",
    "DescribeGameSessionDetailsPaginatorName",
    "DescribeGameSessionQueuesPaginatorName",
    "DescribeGameSessionsPaginatorName",
    "DescribeInstancesPaginatorName",
    "DescribeMatchmakingConfigurationsPaginatorName",
    "DescribeMatchmakingRuleSetsPaginatorName",
    "DescribePlayerSessionsPaginatorName",
    "DescribeScalingPoliciesPaginatorName",
    "EC2InstanceType",
    "EventCode",
    "FleetAction",
    "FleetStatus",
    "FleetType",
    "FlexMatchMode",
    "GameServerClaimStatus",
    "GameServerGroupAction",
    "GameServerGroupDeleteOption",
    "GameServerGroupInstanceType",
    "GameServerGroupStatus",
    "GameServerHealthCheck",
    "GameServerInstanceStatus",
    "GameServerProtectionPolicy",
    "GameServerUtilizationStatus",
    "GameSessionPlacementState",
    "GameSessionStatus",
    "GameSessionStatusReason",
    "InstanceStatus",
    "IpProtocol",
    "ListAliasesPaginatorName",
    "ListBuildsPaginatorName",
    "ListFleetsPaginatorName",
    "ListGameServerGroupsPaginatorName",
    "ListGameServersPaginatorName",
    "ListScriptsPaginatorName",
    "LocationUpdateStatus",
    "MatchmakingConfigurationStatus",
    "MetricName",
    "OperatingSystem",
    "PlayerSessionCreationPolicy",
    "PlayerSessionStatus",
    "PolicyType",
    "PriorityType",
    "ProtectionPolicy",
    "RoutingStrategyType",
    "ScalingAdjustmentType",
    "ScalingStatusType",
    "SearchGameSessionsPaginatorName",
    "SortOrder",
)


AcceptanceType = Literal["ACCEPT", "REJECT"]
BackfillMode = Literal["AUTOMATIC", "MANUAL"]
BalancingStrategy = Literal["ON_DEMAND_ONLY", "SPOT_ONLY", "SPOT_PREFERRED"]
BuildStatus = Literal["FAILED", "INITIALIZED", "READY"]
CertificateType = Literal["DISABLED", "GENERATED"]
ComparisonOperatorType = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
DescribeFleetAttributesPaginatorName = Literal["describe_fleet_attributes"]
DescribeFleetCapacityPaginatorName = Literal["describe_fleet_capacity"]
DescribeFleetEventsPaginatorName = Literal["describe_fleet_events"]
DescribeFleetUtilizationPaginatorName = Literal["describe_fleet_utilization"]
DescribeGameServerInstancesPaginatorName = Literal["describe_game_server_instances"]
DescribeGameSessionDetailsPaginatorName = Literal["describe_game_session_details"]
DescribeGameSessionQueuesPaginatorName = Literal["describe_game_session_queues"]
DescribeGameSessionsPaginatorName = Literal["describe_game_sessions"]
DescribeInstancesPaginatorName = Literal["describe_instances"]
DescribeMatchmakingConfigurationsPaginatorName = Literal["describe_matchmaking_configurations"]
DescribeMatchmakingRuleSetsPaginatorName = Literal["describe_matchmaking_rule_sets"]
DescribePlayerSessionsPaginatorName = Literal["describe_player_sessions"]
DescribeScalingPoliciesPaginatorName = Literal["describe_scaling_policies"]
EC2InstanceType = Literal[
    "c3.2xlarge",
    "c3.4xlarge",
    "c3.8xlarge",
    "c3.large",
    "c3.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "m3.2xlarge",
    "m3.large",
    "m3.medium",
    "m3.xlarge",
    "m4.10xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "r3.2xlarge",
    "r3.4xlarge",
    "r3.8xlarge",
    "r3.large",
    "r3.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
    "t2.large",
    "t2.medium",
    "t2.micro",
    "t2.small",
]
EventCode = Literal[
    "FLEET_ACTIVATION_FAILED",
    "FLEET_ACTIVATION_FAILED_NO_INSTANCES",
    "FLEET_BINARY_DOWNLOAD_FAILED",
    "FLEET_CREATED",
    "FLEET_CREATION_EXTRACTING_BUILD",
    "FLEET_CREATION_RUNNING_INSTALLER",
    "FLEET_CREATION_VALIDATING_RUNTIME_CONFIG",
    "FLEET_DELETED",
    "FLEET_INITIALIZATION_FAILED",
    "FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED",
    "FLEET_SCALING_EVENT",
    "FLEET_STATE_ACTIVATING",
    "FLEET_STATE_ACTIVE",
    "FLEET_STATE_BUILDING",
    "FLEET_STATE_DOWNLOADING",
    "FLEET_STATE_ERROR",
    "FLEET_STATE_VALIDATING",
    "FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE",
    "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
    "FLEET_VALIDATION_TIMED_OUT",
    "FLEET_VPC_PEERING_DELETED",
    "FLEET_VPC_PEERING_FAILED",
    "FLEET_VPC_PEERING_SUCCEEDED",
    "GAME_SESSION_ACTIVATION_TIMEOUT",
    "GENERIC_EVENT",
    "INSTANCE_INTERRUPTED",
    "SERVER_PROCESS_CRASHED",
    "SERVER_PROCESS_FORCE_TERMINATED",
    "SERVER_PROCESS_INVALID_PATH",
    "SERVER_PROCESS_PROCESS_EXIT_TIMEOUT",
    "SERVER_PROCESS_PROCESS_READY_TIMEOUT",
    "SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT",
    "SERVER_PROCESS_TERMINATED_UNHEALTHY",
]
FleetAction = Literal["AUTO_SCALING"]
FleetStatus = Literal[
    "ACTIVATING",
    "ACTIVE",
    "BUILDING",
    "DELETING",
    "DOWNLOADING",
    "ERROR",
    "NEW",
    "TERMINATED",
    "VALIDATING",
]
FleetType = Literal["ON_DEMAND", "SPOT"]
FlexMatchMode = Literal["STANDALONE", "WITH_QUEUE"]
GameServerClaimStatus = Literal["CLAIMED"]
GameServerGroupAction = Literal["REPLACE_INSTANCE_TYPES"]
GameServerGroupDeleteOption = Literal["FORCE_DELETE", "RETAIN", "SAFE_DELETE"]
GameServerGroupInstanceType = Literal[
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "m4.10xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
]
GameServerGroupStatus = Literal[
    "ACTIVATING", "ACTIVE", "DELETED", "DELETE_SCHEDULED", "DELETING", "ERROR", "NEW"
]
GameServerHealthCheck = Literal["HEALTHY"]
GameServerInstanceStatus = Literal["ACTIVE", "DRAINING", "SPOT_TERMINATING"]
GameServerProtectionPolicy = Literal["FULL_PROTECTION", "NO_PROTECTION"]
GameServerUtilizationStatus = Literal["AVAILABLE", "UTILIZED"]
GameSessionPlacementState = Literal["CANCELLED", "FAILED", "FULFILLED", "PENDING", "TIMED_OUT"]
GameSessionStatus = Literal["ACTIVATING", "ACTIVE", "ERROR", "TERMINATED", "TERMINATING"]
GameSessionStatusReason = Literal["INTERRUPTED"]
InstanceStatus = Literal["ACTIVE", "PENDING", "TERMINATING"]
IpProtocol = Literal["TCP", "UDP"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListBuildsPaginatorName = Literal["list_builds"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListGameServerGroupsPaginatorName = Literal["list_game_server_groups"]
ListGameServersPaginatorName = Literal["list_game_servers"]
ListScriptsPaginatorName = Literal["list_scripts"]
LocationUpdateStatus = Literal["PENDING_UPDATE"]
MatchmakingConfigurationStatus = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PLACING",
    "QUEUED",
    "REQUIRES_ACCEPTANCE",
    "SEARCHING",
    "TIMED_OUT",
]
MetricName = Literal[
    "ActivatingGameSessions",
    "ActiveGameSessions",
    "ActiveInstances",
    "AvailableGameSessions",
    "AvailablePlayerSessions",
    "CurrentPlayerSessions",
    "IdleInstances",
    "PercentAvailableGameSessions",
    "PercentIdleInstances",
    "QueueDepth",
    "WaitTime",
]
OperatingSystem = Literal["AMAZON_LINUX", "AMAZON_LINUX_2", "WINDOWS_2012"]
PlayerSessionCreationPolicy = Literal["ACCEPT_ALL", "DENY_ALL"]
PlayerSessionStatus = Literal["ACTIVE", "COMPLETED", "RESERVED", "TIMEDOUT"]
PolicyType = Literal["RuleBased", "TargetBased"]
PriorityType = Literal["COST", "DESTINATION", "LATENCY", "LOCATION"]
ProtectionPolicy = Literal["FullProtection", "NoProtection"]
RoutingStrategyType = Literal["SIMPLE", "TERMINAL"]
ScalingAdjustmentType = Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
ScalingStatusType = Literal[
    "ACTIVE", "DELETED", "DELETE_REQUESTED", "DELETING", "ERROR", "UPDATE_REQUESTED", "UPDATING"
]
SearchGameSessionsPaginatorName = Literal["search_game_sessions"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
