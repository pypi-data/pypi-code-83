"""
Type annotations for gamelift service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_gamelift import GameLiftClient

    client: GameLiftClient = boto3.client("gamelift")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_gamelift.literals import (
    AcceptanceType,
    BackfillMode,
    BalancingStrategy,
    BuildStatus,
    ComparisonOperatorType,
    EC2InstanceType,
    FleetType,
    FlexMatchMode,
    GameServerGroupDeleteOption,
    GameServerProtectionPolicy,
    GameServerUtilizationStatus,
    MetricName,
    OperatingSystem,
    PlayerSessionCreationPolicy,
    PolicyType,
    ProtectionPolicy,
    RoutingStrategyType,
    ScalingAdjustmentType,
    ScalingStatusType,
    SortOrder,
)
from mypy_boto3_gamelift.paginator import (
    DescribeFleetAttributesPaginator,
    DescribeFleetCapacityPaginator,
    DescribeFleetEventsPaginator,
    DescribeFleetUtilizationPaginator,
    DescribeGameServerInstancesPaginator,
    DescribeGameSessionDetailsPaginator,
    DescribeGameSessionQueuesPaginator,
    DescribeGameSessionsPaginator,
    DescribeInstancesPaginator,
    DescribeMatchmakingConfigurationsPaginator,
    DescribeMatchmakingRuleSetsPaginator,
    DescribePlayerSessionsPaginator,
    DescribeScalingPoliciesPaginator,
    ListAliasesPaginator,
    ListBuildsPaginator,
    ListFleetsPaginator,
    ListGameServerGroupsPaginator,
    ListGameServersPaginator,
    ListScriptsPaginator,
    SearchGameSessionsPaginator,
)
from mypy_boto3_gamelift.type_defs import (
    CertificateConfigurationTypeDef,
    ClaimGameServerOutputTypeDef,
    CreateAliasOutputTypeDef,
    CreateBuildOutputTypeDef,
    CreateFleetLocationsOutputTypeDef,
    CreateFleetOutputTypeDef,
    CreateGameServerGroupOutputTypeDef,
    CreateGameSessionOutputTypeDef,
    CreateGameSessionQueueOutputTypeDef,
    CreateMatchmakingConfigurationOutputTypeDef,
    CreateMatchmakingRuleSetOutputTypeDef,
    CreatePlayerSessionOutputTypeDef,
    CreatePlayerSessionsOutputTypeDef,
    CreateScriptOutputTypeDef,
    CreateVpcPeeringAuthorizationOutputTypeDef,
    DeleteFleetLocationsOutputTypeDef,
    DeleteGameServerGroupOutputTypeDef,
    DescribeAliasOutputTypeDef,
    DescribeBuildOutputTypeDef,
    DescribeEC2InstanceLimitsOutputTypeDef,
    DescribeFleetAttributesOutputTypeDef,
    DescribeFleetCapacityOutputTypeDef,
    DescribeFleetEventsOutputTypeDef,
    DescribeFleetLocationAttributesOutputTypeDef,
    DescribeFleetLocationCapacityOutputTypeDef,
    DescribeFleetLocationUtilizationOutputTypeDef,
    DescribeFleetPortSettingsOutputTypeDef,
    DescribeFleetUtilizationOutputTypeDef,
    DescribeGameServerGroupOutputTypeDef,
    DescribeGameServerInstancesOutputTypeDef,
    DescribeGameServerOutputTypeDef,
    DescribeGameSessionDetailsOutputTypeDef,
    DescribeGameSessionPlacementOutputTypeDef,
    DescribeGameSessionQueuesOutputTypeDef,
    DescribeGameSessionsOutputTypeDef,
    DescribeInstancesOutputTypeDef,
    DescribeMatchmakingConfigurationsOutputTypeDef,
    DescribeMatchmakingOutputTypeDef,
    DescribeMatchmakingRuleSetsOutputTypeDef,
    DescribePlayerSessionsOutputTypeDef,
    DescribeRuntimeConfigurationOutputTypeDef,
    DescribeScalingPoliciesOutputTypeDef,
    DescribeScriptOutputTypeDef,
    DescribeVpcPeeringAuthorizationsOutputTypeDef,
    DescribeVpcPeeringConnectionsOutputTypeDef,
    DesiredPlayerSessionTypeDef,
    FilterConfigurationTypeDef,
    GamePropertyTypeDef,
    GameServerGroupAutoScalingPolicyTypeDef,
    GameSessionQueueDestinationTypeDef,
    GetGameSessionLogUrlOutputTypeDef,
    GetInstanceAccessOutputTypeDef,
    InstanceDefinitionTypeDef,
    IpPermissionTypeDef,
    LaunchTemplateSpecificationTypeDef,
    ListAliasesOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListFleetsOutputTypeDef,
    ListGameServerGroupsOutputTypeDef,
    ListGameServersOutputTypeDef,
    ListScriptsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationConfigurationTypeDef,
    PlayerLatencyPolicyTypeDef,
    PlayerLatencyTypeDef,
    PlayerTypeDef,
    PriorityConfigurationTypeDef,
    PutScalingPolicyOutputTypeDef,
    RegisterGameServerOutputTypeDef,
    RequestUploadCredentialsOutputTypeDef,
    ResolveAliasOutputTypeDef,
    ResourceCreationLimitPolicyTypeDef,
    ResumeGameServerGroupOutputTypeDef,
    RoutingStrategyTypeDef,
    RuntimeConfigurationTypeDef,
    S3LocationTypeDef,
    SearchGameSessionsOutputTypeDef,
    StartFleetActionsOutputTypeDef,
    StartGameSessionPlacementOutputTypeDef,
    StartMatchBackfillOutputTypeDef,
    StartMatchmakingOutputTypeDef,
    StopFleetActionsOutputTypeDef,
    StopGameSessionPlacementOutputTypeDef,
    SuspendGameServerGroupOutputTypeDef,
    TagTypeDef,
    TargetConfigurationTypeDef,
    UpdateAliasOutputTypeDef,
    UpdateBuildOutputTypeDef,
    UpdateFleetAttributesOutputTypeDef,
    UpdateFleetCapacityOutputTypeDef,
    UpdateFleetPortSettingsOutputTypeDef,
    UpdateGameServerGroupOutputTypeDef,
    UpdateGameServerOutputTypeDef,
    UpdateGameSessionOutputTypeDef,
    UpdateGameSessionQueueOutputTypeDef,
    UpdateMatchmakingConfigurationOutputTypeDef,
    UpdateRuntimeConfigurationOutputTypeDef,
    UpdateScriptOutputTypeDef,
    ValidateMatchmakingRuleSetOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GameLiftClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    FleetCapacityExceededException: Type[BotocoreClientError]
    GameSessionFullException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidFleetStatusException: Type[BotocoreClientError]
    InvalidGameSessionStatusException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    OutOfCapacityException: Type[BotocoreClientError]
    TaggingFailedException: Type[BotocoreClientError]
    TerminalRoutingStrategyException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnsupportedRegionException: Type[BotocoreClientError]


class GameLiftClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_match(
        self, TicketId: str, PlayerIds: List[str], AcceptanceType: AcceptanceType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.accept_match)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#accept-match)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#can-paginate)
        """

    def claim_game_server(
        self, GameServerGroupName: str, GameServerId: str = None, GameServerData: str = None
    ) -> ClaimGameServerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.claim_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#claim-game-server)
        """

    def create_alias(
        self,
        Name: str,
        RoutingStrategy: "RoutingStrategyTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAliasOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-alias)
        """

    def create_build(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        OperatingSystem: OperatingSystem = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-build)
        """

    def create_fleet(
        self,
        Name: str,
        EC2InstanceType: EC2InstanceType,
        Description: str = None,
        BuildId: str = None,
        ScriptId: str = None,
        ServerLaunchPath: str = None,
        ServerLaunchParameters: str = None,
        LogPaths: List[str] = None,
        EC2InboundPermissions: List["IpPermissionTypeDef"] = None,
        NewGameSessionProtectionPolicy: ProtectionPolicy = None,
        RuntimeConfiguration: "RuntimeConfigurationTypeDef" = None,
        ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
        MetricGroups: List[str] = None,
        PeerVpcAwsAccountId: str = None,
        PeerVpcId: str = None,
        FleetType: FleetType = None,
        InstanceRoleArn: str = None,
        CertificateConfiguration: "CertificateConfigurationTypeDef" = None,
        Locations: List[LocationConfigurationTypeDef] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateFleetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-fleet)
        """

    def create_fleet_locations(
        self, FleetId: str, Locations: List[LocationConfigurationTypeDef]
    ) -> CreateFleetLocationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_fleet_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-fleet-locations)
        """

    def create_game_server_group(
        self,
        GameServerGroupName: str,
        RoleArn: str,
        MinSize: int,
        MaxSize: int,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef,
        InstanceDefinitions: List["InstanceDefinitionTypeDef"],
        AutoScalingPolicy: GameServerGroupAutoScalingPolicyTypeDef = None,
        BalancingStrategy: BalancingStrategy = None,
        GameServerProtectionPolicy: GameServerProtectionPolicy = None,
        VpcSubnets: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-game-server-group)
        """

    def create_game_session(
        self,
        MaximumPlayerSessionCount: int,
        FleetId: str = None,
        AliasId: str = None,
        Name: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        CreatorId: str = None,
        GameSessionId: str = None,
        IdempotencyToken: str = None,
        GameSessionData: str = None,
        Location: str = None,
    ) -> CreateGameSessionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_game_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-game-session)
        """

    def create_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
        Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
        FilterConfiguration: "FilterConfigurationTypeDef" = None,
        PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
        CustomEventData: str = None,
        NotificationTarget: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateGameSessionQueueOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-game-session-queue)
        """

    def create_matchmaking_configuration(
        self,
        Name: str,
        RequestTimeoutSeconds: int,
        AcceptanceRequired: bool,
        RuleSetName: str,
        Description: str = None,
        GameSessionQueueArns: List[str] = None,
        AcceptanceTimeoutSeconds: int = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionData: str = None,
        BackfillMode: BackfillMode = None,
        FlexMatchMode: FlexMatchMode = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMatchmakingConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-matchmaking-configuration)
        """

    def create_matchmaking_rule_set(
        self, Name: str, RuleSetBody: str, Tags: List["TagTypeDef"] = None
    ) -> CreateMatchmakingRuleSetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-matchmaking-rule-set)
        """

    def create_player_session(
        self, GameSessionId: str, PlayerId: str, PlayerData: str = None
    ) -> CreatePlayerSessionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_player_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-player-session)
        """

    def create_player_sessions(
        self, GameSessionId: str, PlayerIds: List[str], PlayerDataMap: Dict[str, str] = None
    ) -> CreatePlayerSessionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_player_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-player-sessions)
        """

    def create_script(
        self,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        ZipFile: Union[bytes, IO[bytes]] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateScriptOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-script)
        """

    def create_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> CreateVpcPeeringAuthorizationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-vpc-peering-authorization)
        """

    def create_vpc_peering_connection(
        self, FleetId: str, PeerVpcAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#create-vpc-peering-connection)
        """

    def delete_alias(self, AliasId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-alias)
        """

    def delete_build(self, BuildId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-build)
        """

    def delete_fleet(self, FleetId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-fleet)
        """

    def delete_fleet_locations(
        self, FleetId: str, Locations: List[str]
    ) -> DeleteFleetLocationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_fleet_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-fleet-locations)
        """

    def delete_game_server_group(
        self, GameServerGroupName: str, DeleteOption: GameServerGroupDeleteOption = None
    ) -> DeleteGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-game-server-group)
        """

    def delete_game_session_queue(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-game-session-queue)
        """

    def delete_matchmaking_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-matchmaking-configuration)
        """

    def delete_matchmaking_rule_set(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-matchmaking-rule-set)
        """

    def delete_scaling_policy(self, Name: str, FleetId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-scaling-policy)
        """

    def delete_script(self, ScriptId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-script)
        """

    def delete_vpc_peering_authorization(
        self, GameLiftAwsAccountId: str, PeerVpcId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-vpc-peering-authorization)
        """

    def delete_vpc_peering_connection(
        self, FleetId: str, VpcPeeringConnectionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.delete_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#delete-vpc-peering-connection)
        """

    def deregister_game_server(self, GameServerGroupName: str, GameServerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.deregister_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#deregister-game-server)
        """

    def describe_alias(self, AliasId: str) -> DescribeAliasOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-alias)
        """

    def describe_build(self, BuildId: str) -> DescribeBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-build)
        """

    def describe_ec2_instance_limits(
        self, EC2InstanceType: EC2InstanceType = None, Location: str = None
    ) -> DescribeEC2InstanceLimitsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_ec2_instance_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-ec2-instance-limits)
        """

    def describe_fleet_attributes(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetAttributesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-attributes)
        """

    def describe_fleet_capacity(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetCapacityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-capacity)
        """

    def describe_fleet_events(
        self,
        FleetId: str,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeFleetEventsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-events)
        """

    def describe_fleet_location_attributes(
        self, FleetId: str, Locations: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetLocationAttributesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-location-attributes)
        """

    def describe_fleet_location_capacity(
        self, FleetId: str, Location: str
    ) -> DescribeFleetLocationCapacityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-location-capacity)
        """

    def describe_fleet_location_utilization(
        self, FleetId: str, Location: str
    ) -> DescribeFleetLocationUtilizationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_location_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-location-utilization)
        """

    def describe_fleet_port_settings(
        self, FleetId: str, Location: str = None
    ) -> DescribeFleetPortSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_port_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-port-settings)
        """

    def describe_fleet_utilization(
        self, FleetIds: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeFleetUtilizationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_fleet_utilization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-fleet-utilization)
        """

    def describe_game_server(
        self, GameServerGroupName: str, GameServerId: str
    ) -> DescribeGameServerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-server)
        """

    def describe_game_server_group(
        self, GameServerGroupName: str
    ) -> DescribeGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-server-group)
        """

    def describe_game_server_instances(
        self,
        GameServerGroupName: str,
        InstanceIds: List[str] = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeGameServerInstancesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_server_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-server-instances)
        """

    def describe_game_session_details(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeGameSessionDetailsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_session_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-session-details)
        """

    def describe_game_session_placement(
        self, PlacementId: str
    ) -> DescribeGameSessionPlacementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-session-placement)
        """

    def describe_game_session_queues(
        self, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeGameSessionQueuesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_session_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-session-queues)
        """

    def describe_game_sessions(
        self,
        FleetId: str = None,
        GameSessionId: str = None,
        AliasId: str = None,
        Location: str = None,
        StatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeGameSessionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_game_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-game-sessions)
        """

    def describe_instances(
        self,
        FleetId: str,
        InstanceId: str = None,
        Limit: int = None,
        NextToken: str = None,
        Location: str = None,
    ) -> DescribeInstancesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-instances)
        """

    def describe_matchmaking(self, TicketIds: List[str]) -> DescribeMatchmakingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-matchmaking)
        """

    def describe_matchmaking_configurations(
        self,
        Names: List[str] = None,
        RuleSetName: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribeMatchmakingConfigurationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-matchmaking-configurations)
        """

    def describe_matchmaking_rule_sets(
        self, Names: List[str] = None, Limit: int = None, NextToken: str = None
    ) -> DescribeMatchmakingRuleSetsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_matchmaking_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-matchmaking-rule-sets)
        """

    def describe_player_sessions(
        self,
        GameSessionId: str = None,
        PlayerId: str = None,
        PlayerSessionId: str = None,
        PlayerSessionStatusFilter: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> DescribePlayerSessionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_player_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-player-sessions)
        """

    def describe_runtime_configuration(
        self, FleetId: str
    ) -> DescribeRuntimeConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-runtime-configuration)
        """

    def describe_scaling_policies(
        self,
        FleetId: str,
        StatusFilter: ScalingStatusType = None,
        Limit: int = None,
        NextToken: str = None,
        Location: str = None,
    ) -> DescribeScalingPoliciesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_scaling_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-scaling-policies)
        """

    def describe_script(self, ScriptId: str) -> DescribeScriptOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-script)
        """

    def describe_vpc_peering_authorizations(self) -> DescribeVpcPeeringAuthorizationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-vpc-peering-authorizations)
        """

    def describe_vpc_peering_connections(
        self, FleetId: str = None
    ) -> DescribeVpcPeeringConnectionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.describe_vpc_peering_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#describe-vpc-peering-connections)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#generate-presigned-url)
        """

    def get_game_session_log_url(self, GameSessionId: str) -> GetGameSessionLogUrlOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.get_game_session_log_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get-game-session-log-url)
        """

    def get_instance_access(self, FleetId: str, InstanceId: str) -> GetInstanceAccessOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.get_instance_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#get-instance-access)
        """

    def list_aliases(
        self,
        RoutingStrategyType: RoutingStrategyType = None,
        Name: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ListAliasesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-aliases)
        """

    def list_builds(
        self, Status: BuildStatus = None, Limit: int = None, NextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-builds)
        """

    def list_fleets(
        self, BuildId: str = None, ScriptId: str = None, Limit: int = None, NextToken: str = None
    ) -> ListFleetsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-fleets)
        """

    def list_game_server_groups(
        self, Limit: int = None, NextToken: str = None
    ) -> ListGameServerGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_game_server_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-game-server-groups)
        """

    def list_game_servers(
        self,
        GameServerGroupName: str,
        SortOrder: SortOrder = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> ListGameServersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_game_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-game-servers)
        """

    def list_scripts(self, Limit: int = None, NextToken: str = None) -> ListScriptsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_scripts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-scripts)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#list-tags-for-resource)
        """

    def put_scaling_policy(
        self,
        Name: str,
        FleetId: str,
        MetricName: MetricName,
        ScalingAdjustment: int = None,
        ScalingAdjustmentType: ScalingAdjustmentType = None,
        Threshold: float = None,
        ComparisonOperator: ComparisonOperatorType = None,
        EvaluationPeriods: int = None,
        PolicyType: PolicyType = None,
        TargetConfiguration: "TargetConfigurationTypeDef" = None,
    ) -> PutScalingPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.put_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#put-scaling-policy)
        """

    def register_game_server(
        self,
        GameServerGroupName: str,
        GameServerId: str,
        InstanceId: str,
        ConnectionInfo: str = None,
        GameServerData: str = None,
    ) -> RegisterGameServerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.register_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#register-game-server)
        """

    def request_upload_credentials(self, BuildId: str) -> RequestUploadCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.request_upload_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#request-upload-credentials)
        """

    def resolve_alias(self, AliasId: str) -> ResolveAliasOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.resolve_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#resolve-alias)
        """

    def resume_game_server_group(
        self, GameServerGroupName: str, ResumeActions: List[Literal["REPLACE_INSTANCE_TYPES"]]
    ) -> ResumeGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.resume_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#resume-game-server-group)
        """

    def search_game_sessions(
        self,
        FleetId: str = None,
        AliasId: str = None,
        Location: str = None,
        FilterExpression: str = None,
        SortExpression: str = None,
        Limit: int = None,
        NextToken: str = None,
    ) -> SearchGameSessionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.search_game_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#search-game-sessions)
        """

    def start_fleet_actions(
        self, FleetId: str, Actions: List[Literal["AUTO_SCALING"]], Location: str = None
    ) -> StartFleetActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.start_fleet_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start-fleet-actions)
        """

    def start_game_session_placement(
        self,
        PlacementId: str,
        GameSessionQueueName: str,
        MaximumPlayerSessionCount: int,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionName: str = None,
        PlayerLatencies: List["PlayerLatencyTypeDef"] = None,
        DesiredPlayerSessions: List[DesiredPlayerSessionTypeDef] = None,
        GameSessionData: str = None,
    ) -> StartGameSessionPlacementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.start_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start-game-session-placement)
        """

    def start_match_backfill(
        self,
        ConfigurationName: str,
        Players: List["PlayerTypeDef"],
        TicketId: str = None,
        GameSessionArn: str = None,
    ) -> StartMatchBackfillOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.start_match_backfill)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start-match-backfill)
        """

    def start_matchmaking(
        self, ConfigurationName: str, Players: List["PlayerTypeDef"], TicketId: str = None
    ) -> StartMatchmakingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.start_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#start-matchmaking)
        """

    def stop_fleet_actions(
        self, FleetId: str, Actions: List[Literal["AUTO_SCALING"]], Location: str = None
    ) -> StopFleetActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.stop_fleet_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop-fleet-actions)
        """

    def stop_game_session_placement(
        self, PlacementId: str
    ) -> StopGameSessionPlacementOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.stop_game_session_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop-game-session-placement)
        """

    def stop_matchmaking(self, TicketId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.stop_matchmaking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#stop-matchmaking)
        """

    def suspend_game_server_group(
        self, GameServerGroupName: str, SuspendActions: List[Literal["REPLACE_INSTANCE_TYPES"]]
    ) -> SuspendGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.suspend_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#suspend-game-server-group)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#tag-resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#untag-resource)
        """

    def update_alias(
        self,
        AliasId: str,
        Name: str = None,
        Description: str = None,
        RoutingStrategy: "RoutingStrategyTypeDef" = None,
    ) -> UpdateAliasOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-alias)
        """

    def update_build(
        self, BuildId: str, Name: str = None, Version: str = None
    ) -> UpdateBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-build)
        """

    def update_fleet_attributes(
        self,
        FleetId: str,
        Name: str = None,
        Description: str = None,
        NewGameSessionProtectionPolicy: ProtectionPolicy = None,
        ResourceCreationLimitPolicy: "ResourceCreationLimitPolicyTypeDef" = None,
        MetricGroups: List[str] = None,
    ) -> UpdateFleetAttributesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_fleet_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-fleet-attributes)
        """

    def update_fleet_capacity(
        self,
        FleetId: str,
        DesiredInstances: int = None,
        MinSize: int = None,
        MaxSize: int = None,
        Location: str = None,
    ) -> UpdateFleetCapacityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_fleet_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-fleet-capacity)
        """

    def update_fleet_port_settings(
        self,
        FleetId: str,
        InboundPermissionAuthorizations: List["IpPermissionTypeDef"] = None,
        InboundPermissionRevocations: List["IpPermissionTypeDef"] = None,
    ) -> UpdateFleetPortSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_fleet_port_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-fleet-port-settings)
        """

    def update_game_server(
        self,
        GameServerGroupName: str,
        GameServerId: str,
        GameServerData: str = None,
        UtilizationStatus: GameServerUtilizationStatus = None,
        HealthCheck: Literal["HEALTHY"] = None,
    ) -> UpdateGameServerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_game_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-game-server)
        """

    def update_game_server_group(
        self,
        GameServerGroupName: str,
        RoleArn: str = None,
        InstanceDefinitions: List["InstanceDefinitionTypeDef"] = None,
        GameServerProtectionPolicy: GameServerProtectionPolicy = None,
        BalancingStrategy: BalancingStrategy = None,
    ) -> UpdateGameServerGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_game_server_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-game-server-group)
        """

    def update_game_session(
        self,
        GameSessionId: str,
        MaximumPlayerSessionCount: int = None,
        Name: str = None,
        PlayerSessionCreationPolicy: PlayerSessionCreationPolicy = None,
        ProtectionPolicy: ProtectionPolicy = None,
    ) -> UpdateGameSessionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_game_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-game-session)
        """

    def update_game_session_queue(
        self,
        Name: str,
        TimeoutInSeconds: int = None,
        PlayerLatencyPolicies: List["PlayerLatencyPolicyTypeDef"] = None,
        Destinations: List["GameSessionQueueDestinationTypeDef"] = None,
        FilterConfiguration: "FilterConfigurationTypeDef" = None,
        PriorityConfiguration: "PriorityConfigurationTypeDef" = None,
        CustomEventData: str = None,
        NotificationTarget: str = None,
    ) -> UpdateGameSessionQueueOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_game_session_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-game-session-queue)
        """

    def update_matchmaking_configuration(
        self,
        Name: str,
        Description: str = None,
        GameSessionQueueArns: List[str] = None,
        RequestTimeoutSeconds: int = None,
        AcceptanceTimeoutSeconds: int = None,
        AcceptanceRequired: bool = None,
        RuleSetName: str = None,
        NotificationTarget: str = None,
        AdditionalPlayerCount: int = None,
        CustomEventData: str = None,
        GameProperties: List["GamePropertyTypeDef"] = None,
        GameSessionData: str = None,
        BackfillMode: BackfillMode = None,
        FlexMatchMode: FlexMatchMode = None,
    ) -> UpdateMatchmakingConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_matchmaking_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-matchmaking-configuration)
        """

    def update_runtime_configuration(
        self, FleetId: str, RuntimeConfiguration: "RuntimeConfigurationTypeDef"
    ) -> UpdateRuntimeConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-runtime-configuration)
        """

    def update_script(
        self,
        ScriptId: str,
        Name: str = None,
        Version: str = None,
        StorageLocation: "S3LocationTypeDef" = None,
        ZipFile: Union[bytes, IO[bytes]] = None,
    ) -> UpdateScriptOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.update_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#update-script)
        """

    def validate_matchmaking_rule_set(
        self, RuleSetBody: str
    ) -> ValidateMatchmakingRuleSetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Client.validate_matchmaking_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/client.html#validate-matchmaking-rule-set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_attributes"]
    ) -> DescribeFleetAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetAttributes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetattributespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_capacity"]
    ) -> DescribeFleetCapacityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetCapacity)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetcapacitypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_events"]
    ) -> DescribeFleetEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleeteventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fleet_utilization"]
    ) -> DescribeFleetUtilizationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeFleetUtilization)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describefleetutilizationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_server_instances"]
    ) -> DescribeGameServerInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeGameServerInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegameserverinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_details"]
    ) -> DescribeGameSessionDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionDetails)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessiondetailspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_session_queues"]
    ) -> DescribeGameSessionQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessionQueues)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessionqueuespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_game_sessions"]
    ) -> DescribeGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeGameSessions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describegamesessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describeinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_configurations"]
    ) -> DescribeMatchmakingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describematchmakingconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_matchmaking_rule_sets"]
    ) -> DescribeMatchmakingRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeMatchmakingRuleSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describematchmakingrulesetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_player_sessions"]
    ) -> DescribePlayerSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribePlayerSessions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describeplayersessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> DescribeScalingPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.DescribeScalingPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#describescalingpoliciespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listaliasespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListBuilds)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listbuildspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_fleets"]) -> ListFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listfleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_server_groups"]
    ) -> ListGameServerGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListGameServerGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listgameservergroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_game_servers"]
    ) -> ListGameServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListGameServers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listgameserverspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_scripts"]) -> ListScriptsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.ListScripts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#listscriptspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_game_sessions"]
    ) -> SearchGameSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/gamelift.html#GameLift.Paginator.SearchGameSessions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamelift/paginators.html#searchgamesessionspaginator)
        """
