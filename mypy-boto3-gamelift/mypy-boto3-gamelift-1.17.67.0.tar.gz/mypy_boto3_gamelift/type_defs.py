"""
Type annotations for gamelift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/type_defs.html)

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
    FleetStatus,
    FleetType,
    FlexMatchMode,
    GameServerGroupInstanceType,
    GameServerGroupStatus,
    GameServerInstanceStatus,
    GameServerProtectionPolicy,
    GameServerUtilizationStatus,
    GameSessionPlacementState,
    GameSessionStatus,
    InstanceStatus,
    IpProtocol,
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
    from typing import Literal
else:
    from typing_extensions import Literal
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
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FilterConfigurationTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerInstanceTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationAttributesTypeDef",
    "LocationConfigurationTypeDef",
    "LocationStateTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PaginatorConfigTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "PriorityConfigurationTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadata",
    "ResumeGameServerGroupOutputTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "ServerProcessTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopFleetActionsOutputTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
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
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
)


class AliasTypeDef(TypedDict, total=False):
    AliasId: str
    Name: str
    AliasArn: str
    Description: str
    RoutingStrategy: "RoutingStrategyTypeDef"
    CreationTime: datetime
    LastUpdatedTime: datetime


class AttributeValueTypeDef(TypedDict, total=False):
    S: str
    N: float
    SL: List[str]
    SDM: Dict[str, float]


class AwsCredentialsTypeDef(TypedDict, total=False):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str


class BuildTypeDef(TypedDict, total=False):
    BuildId: str
    BuildArn: str
    Name: str
    Version: str
    Status: BuildStatus
    SizeOnDisk: int
    OperatingSystem: OperatingSystem
    CreationTime: datetime


class CertificateConfigurationTypeDef(TypedDict):
    CertificateType: CertificateType


class ClaimGameServerOutputTypeDef(TypedDict):
    GameServer: "GameServerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateAliasOutputTypeDef(TypedDict):
    Alias: "AliasTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateBuildOutputTypeDef(TypedDict):
    Build: "BuildTypeDef"
    UploadCredentials: "AwsCredentialsTypeDef"
    StorageLocation: "S3LocationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateFleetLocationsOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    LocationStates: List["LocationStateTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateFleetOutputTypeDef(TypedDict):
    FleetAttributes: "FleetAttributesTypeDef"
    LocationStates: List["LocationStateTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateGameSessionOutputTypeDef(TypedDict):
    GameSession: "GameSessionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateGameSessionQueueOutputTypeDef(TypedDict):
    GameSessionQueue: "GameSessionQueueTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateMatchmakingConfigurationOutputTypeDef(TypedDict):
    Configuration: "MatchmakingConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateMatchmakingRuleSetOutputTypeDef(TypedDict):
    RuleSet: "MatchmakingRuleSetTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreatePlayerSessionOutputTypeDef(TypedDict):
    PlayerSession: "PlayerSessionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreatePlayerSessionsOutputTypeDef(TypedDict):
    PlayerSessions: List["PlayerSessionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateScriptOutputTypeDef(TypedDict):
    Script: "ScriptTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateVpcPeeringAuthorizationOutputTypeDef(TypedDict):
    VpcPeeringAuthorization: "VpcPeeringAuthorizationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteFleetLocationsOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    LocationStates: List["LocationStateTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DeleteGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeAliasOutputTypeDef(TypedDict):
    Alias: "AliasTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeBuildOutputTypeDef(TypedDict):
    Build: "BuildTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeEC2InstanceLimitsOutputTypeDef(TypedDict):
    EC2InstanceLimits: List["EC2InstanceLimitTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetAttributesOutputTypeDef(TypedDict):
    FleetAttributes: List["FleetAttributesTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetCapacityOutputTypeDef(TypedDict):
    FleetCapacity: List["FleetCapacityTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetEventsOutputTypeDef(TypedDict):
    Events: List["EventTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetLocationAttributesOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    LocationAttributes: List["LocationAttributesTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetLocationCapacityOutputTypeDef(TypedDict):
    FleetCapacity: "FleetCapacityTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetLocationUtilizationOutputTypeDef(TypedDict):
    FleetUtilization: "FleetUtilizationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetPortSettingsOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    InboundPermissions: List["IpPermissionTypeDef"]
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str
    ResponseMetadata: "ResponseMetadata"


class DescribeFleetUtilizationOutputTypeDef(TypedDict):
    FleetUtilization: List["FleetUtilizationTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGameServerInstancesOutputTypeDef(TypedDict):
    GameServerInstances: List["GameServerInstanceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeGameServerOutputTypeDef(TypedDict):
    GameServer: "GameServerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGameSessionDetailsOutputTypeDef(TypedDict):
    GameSessionDetails: List["GameSessionDetailTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeGameSessionPlacementOutputTypeDef(TypedDict):
    GameSessionPlacement: "GameSessionPlacementTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGameSessionQueuesOutputTypeDef(TypedDict):
    GameSessionQueues: List["GameSessionQueueTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeGameSessionsOutputTypeDef(TypedDict):
    GameSessions: List["GameSessionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeInstancesOutputTypeDef(TypedDict):
    Instances: List["InstanceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeMatchmakingConfigurationsOutputTypeDef(TypedDict):
    Configurations: List["MatchmakingConfigurationTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeMatchmakingOutputTypeDef(TypedDict):
    TicketList: List["MatchmakingTicketTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeMatchmakingRuleSetsOutputTypeDef(TypedDict):
    RuleSets: List["MatchmakingRuleSetTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribePlayerSessionsOutputTypeDef(TypedDict):
    PlayerSessions: List["PlayerSessionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeRuntimeConfigurationOutputTypeDef(TypedDict):
    RuntimeConfiguration: "RuntimeConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeScalingPoliciesOutputTypeDef(TypedDict):
    ScalingPolicies: List["ScalingPolicyTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeScriptOutputTypeDef(TypedDict):
    Script: "ScriptTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeVpcPeeringAuthorizationsOutputTypeDef(TypedDict):
    VpcPeeringAuthorizations: List["VpcPeeringAuthorizationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeVpcPeeringConnectionsOutputTypeDef(TypedDict):
    VpcPeeringConnections: List["VpcPeeringConnectionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DesiredPlayerSessionTypeDef(TypedDict, total=False):
    PlayerId: str
    PlayerData: str


class EC2InstanceCountsTypeDef(TypedDict, total=False):
    DESIRED: int
    MINIMUM: int
    MAXIMUM: int
    PENDING: int
    ACTIVE: int
    IDLE: int
    TERMINATING: int


class EC2InstanceLimitTypeDef(TypedDict, total=False):
    EC2InstanceType: EC2InstanceType
    CurrentInstances: int
    InstanceLimit: int
    Location: str


class EventTypeDef(TypedDict, total=False):
    EventId: str
    ResourceId: str
    EventCode: EventCode
    Message: str
    EventTime: datetime
    PreSignedLogUrl: str


class FilterConfigurationTypeDef(TypedDict, total=False):
    AllowedLocations: List[str]


class FleetAttributesTypeDef(TypedDict, total=False):
    FleetId: str
    FleetArn: str
    FleetType: FleetType
    InstanceType: EC2InstanceType
    Description: str
    Name: str
    CreationTime: datetime
    TerminationTime: datetime
    Status: FleetStatus
    BuildId: str
    BuildArn: str
    ScriptId: str
    ScriptArn: str
    ServerLaunchPath: str
    ServerLaunchParameters: str
    LogPaths: List[str]
    NewGameSessionProtectionPolicy: ProtectionPolicy
    OperatingSystem: OperatingSystem
    ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef"
    MetricGroups: List[str]
    StoppedActions: List[Literal["AUTO_SCALING"]]
    InstanceRoleArn: str
    CertificateConfiguration: "CertificateConfigurationTypeDef"


class FleetCapacityTypeDef(TypedDict, total=False):
    FleetId: str
    FleetArn: str
    InstanceType: EC2InstanceType
    InstanceCounts: "EC2InstanceCountsTypeDef"
    Location: str


class FleetUtilizationTypeDef(TypedDict, total=False):
    FleetId: str
    FleetArn: str
    ActiveServerProcessCount: int
    ActiveGameSessionCount: int
    CurrentPlayerSessionCount: int
    MaximumPlayerSessionCount: int
    Location: str


class GamePropertyTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredGameServerGroupAutoScalingPolicyTypeDef(TypedDict):
    TargetTrackingConfiguration: "TargetTrackingConfigurationTypeDef"


class GameServerGroupAutoScalingPolicyTypeDef(
    _RequiredGameServerGroupAutoScalingPolicyTypeDef, total=False
):
    EstimatedInstanceWarmup: int


class GameServerGroupTypeDef(TypedDict, total=False):
    GameServerGroupName: str
    GameServerGroupArn: str
    RoleArn: str
    InstanceDefinitions: List["InstanceDefinitionTypeDef"]
    BalancingStrategy: BalancingStrategy
    GameServerProtectionPolicy: GameServerProtectionPolicy
    AutoScalingGroupArn: str
    Status: GameServerGroupStatus
    StatusReason: str
    SuspendedActions: List[Literal["REPLACE_INSTANCE_TYPES"]]
    CreationTime: datetime
    LastUpdatedTime: datetime


class GameServerInstanceTypeDef(TypedDict, total=False):
    GameServerGroupName: str
    GameServerGroupArn: str
    InstanceId: str
    InstanceStatus: GameServerInstanceStatus


class GameServerTypeDef(TypedDict, total=False):
    GameServerGroupName: str
    GameServerGroupArn: str
    GameServerId: str
    InstanceId: str
    ConnectionInfo: str
    GameServerData: str
    ClaimStatus: Literal["CLAIMED"]
    UtilizationStatus: GameServerUtilizationStatus
    RegistrationTime: datetime
    LastClaimTime: datetime
    LastHealthCheckTime: datetime


class GameSessionConnectionInfoTypeDef(TypedDict, total=False):
    GameSessionArn: str
    IpAddress: str
    DnsName: str
    Port: int
    MatchedPlayerSessions: List["MatchedPlayerSessionTypeDef"]


class GameSessionDetailTypeDef(TypedDict, total=False):
    GameSession: "GameSessionTypeDef"
    ProtectionPolicy: ProtectionPolicy


class GameSessionPlacementTypeDef(TypedDict, total=False):
    PlacementId: str
    GameSessionQueueName: str
    Status: GameSessionPlacementState
    GameProperties: List["GamePropertyTypeDef"]
    MaximumPlayerSessionCount: int
    GameSessionName: str
    GameSessionId: str
    GameSessionArn: str
    GameSessionRegion: str
    PlayerLatencies: List["PlayerLatencyTypeDef"]
    StartTime: datetime
    EndTime: datetime
    IpAddress: str
    DnsName: str
    Port: int
    PlacedPlayerSessions: List["PlacedPlayerSessionTypeDef"]
    GameSessionData: str
    MatchmakerData: str


class GameSessionQueueDestinationTypeDef(TypedDict, total=False):
    DestinationArn: str


class GameSessionQueueTypeDef(TypedDict, total=False):
    Name: str
    GameSessionQueueArn: str
    TimeoutInSeconds: int
    PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"]
    Destinations: List["GameSessionQueueDestinationTypeDef"]
    FilterConfiguration: "FilterConfigurationTypeDef"
    PriorityConfiguration: "PriorityConfigurationTypeDef"
    CustomEventData: str
    NotificationTarget: str


class GameSessionTypeDef(TypedDict, total=False):
    GameSessionId: str
    Name: str
    FleetId: str
    FleetArn: str
    CreationTime: datetime
    TerminationTime: datetime
    CurrentPlayerSessionCount: int
    MaximumPlayerSessionCount: int
    Status: GameSessionStatus
    StatusReason: Literal["INTERRUPTED"]
    GameProperties: List["GamePropertyTypeDef"]
    IpAddress: str
    DnsName: str
    Port: int
    PlayerSessionCreationPolicy: PlayerSessionCreationPolicy
    CreatorId: str
    GameSessionData: str
    MatchmakerData: str
    Location: str


class GetGameSessionLogUrlOutputTypeDef(TypedDict):
    PreSignedUrl: str
    ResponseMetadata: "ResponseMetadata"


class GetInstanceAccessOutputTypeDef(TypedDict):
    InstanceAccess: "InstanceAccessTypeDef"
    ResponseMetadata: "ResponseMetadata"


class InstanceAccessTypeDef(TypedDict, total=False):
    FleetId: str
    InstanceId: str
    IpAddress: str
    OperatingSystem: OperatingSystem
    Credentials: "InstanceCredentialsTypeDef"


class InstanceCredentialsTypeDef(TypedDict, total=False):
    UserName: str
    Secret: str


class _RequiredInstanceDefinitionTypeDef(TypedDict):
    InstanceType: GameServerGroupInstanceType


class InstanceDefinitionTypeDef(_RequiredInstanceDefinitionTypeDef, total=False):
    WeightedCapacity: str


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


class LaunchTemplateSpecificationTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    Version: str


class ListAliasesOutputTypeDef(TypedDict):
    Aliases: List["AliasTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBuildsOutputTypeDef(TypedDict):
    Builds: List["BuildTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListFleetsOutputTypeDef(TypedDict):
    FleetIds: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListGameServerGroupsOutputTypeDef(TypedDict):
    GameServerGroups: List["GameServerGroupTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListGameServersOutputTypeDef(TypedDict):
    GameServers: List["GameServerTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListScriptsOutputTypeDef(TypedDict):
    Scripts: List["ScriptTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class LocationAttributesTypeDef(TypedDict, total=False):
    LocationState: "LocationStateTypeDef"
    StoppedActions: List[Literal["AUTO_SCALING"]]
    UpdateStatus: Literal["PENDING_UPDATE"]


class LocationConfigurationTypeDef(TypedDict, total=False):
    Location: str


class LocationStateTypeDef(TypedDict, total=False):
    Location: str
    Status: FleetStatus


class MatchedPlayerSessionTypeDef(TypedDict, total=False):
    PlayerId: str
    PlayerSessionId: str


class MatchmakingConfigurationTypeDef(TypedDict, total=False):
    Name: str
    ConfigurationArn: str
    Description: str
    GameSessionQueueArns: List[str]
    RequestTimeoutSeconds: int
    AcceptanceTimeoutSeconds: int
    AcceptanceRequired: bool
    RuleSetName: str
    RuleSetArn: str
    NotificationTarget: str
    AdditionalPlayerCount: int
    CustomEventData: str
    CreationTime: datetime
    GameProperties: List["GamePropertyTypeDef"]
    GameSessionData: str
    BackfillMode: BackfillMode
    FlexMatchMode: FlexMatchMode


class _RequiredMatchmakingRuleSetTypeDef(TypedDict):
    RuleSetBody: str


class MatchmakingRuleSetTypeDef(_RequiredMatchmakingRuleSetTypeDef, total=False):
    RuleSetName: str
    RuleSetArn: str
    CreationTime: datetime


class MatchmakingTicketTypeDef(TypedDict, total=False):
    TicketId: str
    ConfigurationName: str
    ConfigurationArn: str
    Status: MatchmakingConfigurationStatus
    StatusReason: str
    StatusMessage: str
    StartTime: datetime
    EndTime: datetime
    Players: List["PlayerTypeDef"]
    GameSessionConnectionInfo: "GameSessionConnectionInfoTypeDef"
    EstimatedWaitTime: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlacedPlayerSessionTypeDef(TypedDict, total=False):
    PlayerId: str
    PlayerSessionId: str


class PlayerLatencyPolicyTypeDef(TypedDict, total=False):
    MaximumIndividualPlayerLatencyMilliseconds: int
    PolicyDurationSeconds: int


class PlayerLatencyTypeDef(TypedDict, total=False):
    PlayerId: str
    RegionIdentifier: str
    LatencyInMilliseconds: float


class PlayerSessionTypeDef(TypedDict, total=False):
    PlayerSessionId: str
    PlayerId: str
    GameSessionId: str
    FleetId: str
    FleetArn: str
    CreationTime: datetime
    TerminationTime: datetime
    Status: PlayerSessionStatus
    IpAddress: str
    DnsName: str
    Port: int
    PlayerData: str


class PlayerTypeDef(TypedDict, total=False):
    PlayerId: str
    PlayerAttributes: Dict[str, "AttributeValueTypeDef"]
    Team: str
    LatencyInMs: Dict[str, int]


class PriorityConfigurationTypeDef(TypedDict, total=False):
    PriorityOrder: List[PriorityType]
    LocationOrder: List[str]


class PutScalingPolicyOutputTypeDef(TypedDict):
    Name: str
    ResponseMetadata: "ResponseMetadata"


class RegisterGameServerOutputTypeDef(TypedDict):
    GameServer: "GameServerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class RequestUploadCredentialsOutputTypeDef(TypedDict):
    UploadCredentials: "AwsCredentialsTypeDef"
    StorageLocation: "S3LocationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ResolveAliasOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    ResponseMetadata: "ResponseMetadata"


class ResourceCreationLimitPolicyTypeDef(TypedDict, total=False):
    NewGameSessionsPerCreator: int
    PolicyPeriodInMinutes: int


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class ResumeGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {"Type": RoutingStrategyType, "FleetId": str, "Message": str},
    total=False,
)


class RuntimeConfigurationTypeDef(TypedDict, total=False):
    ServerProcesses: List["ServerProcessTypeDef"]
    MaxConcurrentGameSessionActivations: int
    GameSessionActivationTimeoutSeconds: int


class S3LocationTypeDef(TypedDict, total=False):
    Bucket: str
    Key: str
    RoleArn: str
    ObjectVersion: str


class ScalingPolicyTypeDef(TypedDict, total=False):
    FleetId: str
    FleetArn: str
    Name: str
    Status: ScalingStatusType
    ScalingAdjustment: int
    ScalingAdjustmentType: ScalingAdjustmentType
    ComparisonOperator: ComparisonOperatorType
    Threshold: float
    EvaluationPeriods: int
    MetricName: MetricName
    PolicyType: PolicyType
    TargetConfiguration: "TargetConfigurationTypeDef"
    UpdateStatus: Literal["PENDING_UPDATE"]
    Location: str


class ScriptTypeDef(TypedDict, total=False):
    ScriptId: str
    ScriptArn: str
    Name: str
    Version: str
    SizeOnDisk: int
    CreationTime: datetime
    StorageLocation: "S3LocationTypeDef"


class SearchGameSessionsOutputTypeDef(TypedDict):
    GameSessions: List["GameSessionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredServerProcessTypeDef(TypedDict):
    LaunchPath: str
    ConcurrentExecutions: int


class ServerProcessTypeDef(_RequiredServerProcessTypeDef, total=False):
    Parameters: str


class StartFleetActionsOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    ResponseMetadata: "ResponseMetadata"


class StartGameSessionPlacementOutputTypeDef(TypedDict):
    GameSessionPlacement: "GameSessionPlacementTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StartMatchBackfillOutputTypeDef(TypedDict):
    MatchmakingTicket: "MatchmakingTicketTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StartMatchmakingOutputTypeDef(TypedDict):
    MatchmakingTicket: "MatchmakingTicketTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StopFleetActionsOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    ResponseMetadata: "ResponseMetadata"


class StopGameSessionPlacementOutputTypeDef(TypedDict):
    GameSessionPlacement: "GameSessionPlacementTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SuspendGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TargetConfigurationTypeDef(TypedDict):
    TargetValue: float


class TargetTrackingConfigurationTypeDef(TypedDict):
    TargetValue: float


class UpdateAliasOutputTypeDef(TypedDict):
    Alias: "AliasTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateBuildOutputTypeDef(TypedDict):
    Build: "BuildTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateFleetAttributesOutputTypeDef(TypedDict):
    FleetId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateFleetCapacityOutputTypeDef(TypedDict):
    FleetId: str
    FleetArn: str
    Location: str
    ResponseMetadata: "ResponseMetadata"


class UpdateFleetPortSettingsOutputTypeDef(TypedDict):
    FleetId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateGameServerGroupOutputTypeDef(TypedDict):
    GameServerGroup: "GameServerGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateGameServerOutputTypeDef(TypedDict):
    GameServer: "GameServerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateGameSessionOutputTypeDef(TypedDict):
    GameSession: "GameSessionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateGameSessionQueueOutputTypeDef(TypedDict):
    GameSessionQueue: "GameSessionQueueTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateMatchmakingConfigurationOutputTypeDef(TypedDict):
    Configuration: "MatchmakingConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateRuntimeConfigurationOutputTypeDef(TypedDict):
    RuntimeConfiguration: "RuntimeConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateScriptOutputTypeDef(TypedDict):
    Script: "ScriptTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ValidateMatchmakingRuleSetOutputTypeDef(TypedDict):
    Valid: bool
    ResponseMetadata: "ResponseMetadata"


class VpcPeeringAuthorizationTypeDef(TypedDict, total=False):
    GameLiftAwsAccountId: str
    PeerVpcAwsAccountId: str
    PeerVpcId: str
    CreationTime: datetime
    ExpirationTime: datetime


class VpcPeeringConnectionStatusTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class VpcPeeringConnectionTypeDef(TypedDict, total=False):
    FleetId: str
    FleetArn: str
    IpV4CidrBlock: str
    VpcPeeringConnectionId: str
    Status: "VpcPeeringConnectionStatusTypeDef"
    PeerVpcId: str
    GameLiftVpcId: str
