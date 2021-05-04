"""
Type annotations for codedeploy service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.type_defs import AlarmConfigurationTypeDef

    data: AlarmConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_codedeploy.literals import (
    AutoRollbackEvent,
    BundleType,
    ComputePlatform,
    DeploymentCreator,
    DeploymentOption,
    DeploymentReadyAction,
    DeploymentStatus,
    DeploymentTargetType,
    DeploymentType,
    EC2TagFilterType,
    ErrorCode,
    FileExistsBehavior,
    GreenFleetProvisioningAction,
    InstanceAction,
    InstanceStatus,
    InstanceType,
    LifecycleErrorCode,
    LifecycleEventStatus,
    MinimumHealthyHostsType,
    OutdatedInstancesStrategy,
    RevisionLocationType,
    StopStatus,
    TagFilterType,
    TargetLabel,
    TargetStatus,
    TrafficRoutingType,
    TriggerEventType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmConfigurationTypeDef",
    "AlarmTypeDef",
    "AppSpecContentTypeDef",
    "ApplicationInfoTypeDef",
    "AutoRollbackConfigurationTypeDef",
    "AutoScalingGroupTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "DeploymentConfigInfoTypeDef",
    "DeploymentGroupInfoTypeDef",
    "DeploymentInfoTypeDef",
    "DeploymentOverviewTypeDef",
    "DeploymentReadyOptionTypeDef",
    "DeploymentStyleTypeDef",
    "DeploymentTargetTypeDef",
    "DiagnosticsTypeDef",
    "EC2TagFilterTypeDef",
    "EC2TagSetTypeDef",
    "ECSServiceTypeDef",
    "ECSTargetTypeDef",
    "ECSTaskSetTypeDef",
    "ELBInfoTypeDef",
    "ErrorInformationTypeDef",
    "GenericRevisionInfoTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "ListApplicationRevisionsOutputTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListDeploymentConfigsOutputTypeDef",
    "ListDeploymentGroupsOutputTypeDef",
    "ListDeploymentInstancesOutputTypeDef",
    "ListDeploymentTargetsOutputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListGitHubAccountTokenNamesOutputTypeDef",
    "ListOnPremisesInstancesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "RawStringTypeDef",
    "RelatedDeploymentsTypeDef",
    "ResponseMetadata",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "StopDeploymentOutputTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TimeRangeTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)


class AlarmConfigurationTypeDef(TypedDict, total=False):
    enabled: bool
    ignorePollAlarmFailure: bool
    alarms: List["AlarmTypeDef"]


class AlarmTypeDef(TypedDict, total=False):
    name: str


class AppSpecContentTypeDef(TypedDict, total=False):
    content: str
    sha256: str


class ApplicationInfoTypeDef(TypedDict, total=False):
    applicationId: str
    applicationName: str
    createTime: datetime
    linkedToGitHub: bool
    gitHubAccountName: str
    computePlatform: ComputePlatform


class AutoRollbackConfigurationTypeDef(TypedDict, total=False):
    enabled: bool
    events: List[AutoRollbackEvent]


class AutoScalingGroupTypeDef(TypedDict, total=False):
    name: str
    hook: str


class BatchGetApplicationRevisionsOutputTypeDef(TypedDict):
    applicationName: str
    errorMessage: str
    revisions: List["RevisionInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetApplicationsOutputTypeDef(TypedDict):
    applicationsInfo: List["ApplicationInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetDeploymentGroupsOutputTypeDef(TypedDict):
    deploymentGroupsInfo: List["DeploymentGroupInfoTypeDef"]
    errorMessage: str
    ResponseMetadata: "ResponseMetadata"


class BatchGetDeploymentInstancesOutputTypeDef(TypedDict):
    instancesSummary: List["InstanceSummaryTypeDef"]
    errorMessage: str
    ResponseMetadata: "ResponseMetadata"


class BatchGetDeploymentTargetsOutputTypeDef(TypedDict):
    deploymentTargets: List["DeploymentTargetTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetDeploymentsOutputTypeDef(TypedDict):
    deploymentsInfo: List["DeploymentInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetOnPremisesInstancesOutputTypeDef(TypedDict):
    instanceInfos: List["InstanceInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BlueGreenDeploymentConfigurationTypeDef(TypedDict, total=False):
    terminateBlueInstancesOnDeploymentSuccess: "BlueInstanceTerminationOptionTypeDef"
    deploymentReadyOption: "DeploymentReadyOptionTypeDef"
    greenFleetProvisioningOption: "GreenFleetProvisioningOptionTypeDef"


class BlueInstanceTerminationOptionTypeDef(TypedDict, total=False):
    action: InstanceAction
    terminationWaitTimeInMinutes: int


class CloudFormationTargetTypeDef(TypedDict, total=False):
    deploymentId: str
    targetId: str
    lastUpdatedAt: datetime
    lifecycleEvents: List["LifecycleEventTypeDef"]
    status: TargetStatus
    resourceType: str
    targetVersionWeight: float


class CreateApplicationOutputTypeDef(TypedDict):
    applicationId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDeploymentConfigOutputTypeDef(TypedDict):
    deploymentConfigId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDeploymentGroupOutputTypeDef(TypedDict):
    deploymentGroupId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDeploymentOutputTypeDef(TypedDict):
    deploymentId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteDeploymentGroupOutputTypeDef(TypedDict):
    hooksNotCleanedUp: List["AutoScalingGroupTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DeleteGitHubAccountTokenOutputTypeDef(TypedDict):
    tokenName: str
    ResponseMetadata: "ResponseMetadata"


class DeploymentConfigInfoTypeDef(TypedDict, total=False):
    deploymentConfigId: str
    deploymentConfigName: str
    minimumHealthyHosts: "MinimumHealthyHostsTypeDef"
    createTime: datetime
    computePlatform: ComputePlatform
    trafficRoutingConfig: "TrafficRoutingConfigTypeDef"


class DeploymentGroupInfoTypeDef(TypedDict, total=False):
    applicationName: str
    deploymentGroupId: str
    deploymentGroupName: str
    deploymentConfigName: str
    ec2TagFilters: List["EC2TagFilterTypeDef"]
    onPremisesInstanceTagFilters: List["TagFilterTypeDef"]
    autoScalingGroups: List["AutoScalingGroupTypeDef"]
    serviceRoleArn: str
    targetRevision: "RevisionLocationTypeDef"
    triggerConfigurations: List["TriggerConfigTypeDef"]
    alarmConfiguration: "AlarmConfigurationTypeDef"
    autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef"
    deploymentStyle: "DeploymentStyleTypeDef"
    outdatedInstancesStrategy: OutdatedInstancesStrategy
    blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef"
    loadBalancerInfo: "LoadBalancerInfoTypeDef"
    lastSuccessfulDeployment: "LastDeploymentInfoTypeDef"
    lastAttemptedDeployment: "LastDeploymentInfoTypeDef"
    ec2TagSet: "EC2TagSetTypeDef"
    onPremisesTagSet: "OnPremisesTagSetTypeDef"
    computePlatform: ComputePlatform
    ecsServices: List["ECSServiceTypeDef"]


class DeploymentInfoTypeDef(TypedDict, total=False):
    applicationName: str
    deploymentGroupName: str
    deploymentConfigName: str
    deploymentId: str
    previousRevision: "RevisionLocationTypeDef"
    revision: "RevisionLocationTypeDef"
    status: DeploymentStatus
    errorInformation: "ErrorInformationTypeDef"
    createTime: datetime
    startTime: datetime
    completeTime: datetime
    deploymentOverview: "DeploymentOverviewTypeDef"
    description: str
    creator: DeploymentCreator
    ignoreApplicationStopFailures: bool
    autoRollbackConfiguration: "AutoRollbackConfigurationTypeDef"
    updateOutdatedInstancesOnly: bool
    rollbackInfo: "RollbackInfoTypeDef"
    deploymentStyle: "DeploymentStyleTypeDef"
    targetInstances: "TargetInstancesTypeDef"
    instanceTerminationWaitTimeStarted: bool
    blueGreenDeploymentConfiguration: "BlueGreenDeploymentConfigurationTypeDef"
    loadBalancerInfo: "LoadBalancerInfoTypeDef"
    additionalDeploymentStatusInfo: str
    fileExistsBehavior: FileExistsBehavior
    deploymentStatusMessages: List[str]
    computePlatform: ComputePlatform
    externalId: str
    relatedDeployments: "RelatedDeploymentsTypeDef"


class DeploymentOverviewTypeDef(TypedDict, total=False):
    Pending: int
    InProgress: int
    Succeeded: int
    Failed: int
    Skipped: int
    Ready: int


class DeploymentReadyOptionTypeDef(TypedDict, total=False):
    actionOnTimeout: DeploymentReadyAction
    waitTimeInMinutes: int


class DeploymentStyleTypeDef(TypedDict, total=False):
    deploymentType: DeploymentType
    deploymentOption: DeploymentOption


class DeploymentTargetTypeDef(TypedDict, total=False):
    deploymentTargetType: DeploymentTargetType
    instanceTarget: "InstanceTargetTypeDef"
    lambdaTarget: "LambdaTargetTypeDef"
    ecsTarget: "ECSTargetTypeDef"
    cloudFormationTarget: "CloudFormationTargetTypeDef"


class DiagnosticsTypeDef(TypedDict, total=False):
    errorCode: LifecycleErrorCode
    scriptName: str
    message: str
    logTail: str


EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef", {"Key": str, "Value": str, "Type": EC2TagFilterType}, total=False
)


class EC2TagSetTypeDef(TypedDict, total=False):
    ec2TagSetList: List[List["EC2TagFilterTypeDef"]]


class ECSServiceTypeDef(TypedDict, total=False):
    serviceName: str
    clusterName: str


class ECSTargetTypeDef(TypedDict, total=False):
    deploymentId: str
    targetId: str
    targetArn: str
    lastUpdatedAt: datetime
    lifecycleEvents: List["LifecycleEventTypeDef"]
    status: TargetStatus
    taskSetsInfo: List["ECSTaskSetTypeDef"]


class ECSTaskSetTypeDef(TypedDict, total=False):
    identifer: str
    desiredCount: int
    pendingCount: int
    runningCount: int
    status: str
    trafficWeight: float
    targetGroup: "TargetGroupInfoTypeDef"
    taskSetLabel: TargetLabel


class ELBInfoTypeDef(TypedDict, total=False):
    name: str


class ErrorInformationTypeDef(TypedDict, total=False):
    code: ErrorCode
    message: str


class GenericRevisionInfoTypeDef(TypedDict, total=False):
    description: str
    deploymentGroups: List[str]
    firstUsedTime: datetime
    lastUsedTime: datetime
    registerTime: datetime


class GetApplicationOutputTypeDef(TypedDict):
    application: "ApplicationInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetApplicationRevisionOutputTypeDef(TypedDict):
    applicationName: str
    revision: "RevisionLocationTypeDef"
    revisionInfo: "GenericRevisionInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDeploymentConfigOutputTypeDef(TypedDict):
    deploymentConfigInfo: "DeploymentConfigInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDeploymentGroupOutputTypeDef(TypedDict):
    deploymentGroupInfo: "DeploymentGroupInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDeploymentInstanceOutputTypeDef(TypedDict):
    instanceSummary: "InstanceSummaryTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDeploymentOutputTypeDef(TypedDict):
    deploymentInfo: "DeploymentInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDeploymentTargetOutputTypeDef(TypedDict):
    deploymentTarget: "DeploymentTargetTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetOnPremisesInstanceOutputTypeDef(TypedDict):
    instanceInfo: "InstanceInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GitHubLocationTypeDef(TypedDict, total=False):
    repository: str
    commitId: str


class GreenFleetProvisioningOptionTypeDef(TypedDict, total=False):
    action: GreenFleetProvisioningAction


class InstanceInfoTypeDef(TypedDict, total=False):
    instanceName: str
    iamSessionArn: str
    iamUserArn: str
    instanceArn: str
    registerTime: datetime
    deregisterTime: datetime
    tags: List["TagTypeDef"]


class InstanceSummaryTypeDef(TypedDict, total=False):
    deploymentId: str
    instanceId: str
    status: InstanceStatus
    lastUpdatedAt: datetime
    lifecycleEvents: List["LifecycleEventTypeDef"]
    instanceType: InstanceType


class InstanceTargetTypeDef(TypedDict, total=False):
    deploymentId: str
    targetId: str
    targetArn: str
    status: TargetStatus
    lastUpdatedAt: datetime
    lifecycleEvents: List["LifecycleEventTypeDef"]
    instanceLabel: TargetLabel


class LambdaFunctionInfoTypeDef(TypedDict, total=False):
    functionName: str
    functionAlias: str
    currentVersion: str
    targetVersion: str
    targetVersionWeight: float


class LambdaTargetTypeDef(TypedDict, total=False):
    deploymentId: str
    targetId: str
    targetArn: str
    status: TargetStatus
    lastUpdatedAt: datetime
    lifecycleEvents: List["LifecycleEventTypeDef"]
    lambdaFunctionInfo: "LambdaFunctionInfoTypeDef"


class LastDeploymentInfoTypeDef(TypedDict, total=False):
    deploymentId: str
    status: DeploymentStatus
    endTime: datetime
    createTime: datetime


class LifecycleEventTypeDef(TypedDict, total=False):
    lifecycleEventName: str
    diagnostics: "DiagnosticsTypeDef"
    startTime: datetime
    endTime: datetime
    status: LifecycleEventStatus


class ListApplicationRevisionsOutputTypeDef(TypedDict):
    revisions: List["RevisionLocationTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListApplicationsOutputTypeDef(TypedDict):
    applications: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDeploymentConfigsOutputTypeDef(TypedDict):
    deploymentConfigsList: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDeploymentGroupsOutputTypeDef(TypedDict):
    applicationName: str
    deploymentGroups: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDeploymentInstancesOutputTypeDef(TypedDict):
    instancesList: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDeploymentTargetsOutputTypeDef(TypedDict):
    targetIds: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDeploymentsOutputTypeDef(TypedDict):
    deployments: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListGitHubAccountTokenNamesOutputTypeDef(TypedDict):
    tokenNameList: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListOnPremisesInstancesOutputTypeDef(TypedDict):
    instanceNames: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class LoadBalancerInfoTypeDef(TypedDict, total=False):
    elbInfoList: List["ELBInfoTypeDef"]
    targetGroupInfoList: List["TargetGroupInfoTypeDef"]
    targetGroupPairInfoList: List["TargetGroupPairInfoTypeDef"]


MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef", {"type": MinimumHealthyHostsType, "value": int}, total=False
)


class OnPremisesTagSetTypeDef(TypedDict, total=False):
    onPremisesTagSetList: List[List["TagFilterTypeDef"]]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutLifecycleEventHookExecutionStatusOutputTypeDef(TypedDict):
    lifecycleEventHookExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class RawStringTypeDef(TypedDict, total=False):
    content: str
    sha256: str


class RelatedDeploymentsTypeDef(TypedDict, total=False):
    autoUpdateOutdatedInstancesRootDeploymentId: str
    autoUpdateOutdatedInstancesDeploymentIds: List[str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RevisionInfoTypeDef(TypedDict, total=False):
    revisionLocation: "RevisionLocationTypeDef"
    genericRevisionInfo: "GenericRevisionInfoTypeDef"


class RevisionLocationTypeDef(TypedDict, total=False):
    revisionType: RevisionLocationType
    s3Location: "S3LocationTypeDef"
    gitHubLocation: "GitHubLocationTypeDef"
    string: "RawStringTypeDef"
    appSpecContent: "AppSpecContentTypeDef"


class RollbackInfoTypeDef(TypedDict, total=False):
    rollbackDeploymentId: str
    rollbackTriggeringDeploymentId: str
    rollbackMessage: str


class S3LocationTypeDef(TypedDict, total=False):
    bucket: str
    key: str
    bundleType: BundleType
    version: str
    eTag: str


class StopDeploymentOutputTypeDef(TypedDict):
    status: StopStatus
    statusMessage: str
    ResponseMetadata: "ResponseMetadata"


TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef", {"Key": str, "Value": str, "Type": TagFilterType}, total=False
)


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TargetGroupInfoTypeDef(TypedDict, total=False):
    name: str


class TargetGroupPairInfoTypeDef(TypedDict, total=False):
    targetGroups: List["TargetGroupInfoTypeDef"]
    prodTrafficRoute: "TrafficRouteTypeDef"
    testTrafficRoute: "TrafficRouteTypeDef"


class TargetInstancesTypeDef(TypedDict, total=False):
    tagFilters: List["EC2TagFilterTypeDef"]
    autoScalingGroups: List[str]
    ec2TagSet: "EC2TagSetTypeDef"


class TimeBasedCanaryTypeDef(TypedDict, total=False):
    canaryPercentage: int
    canaryInterval: int


class TimeBasedLinearTypeDef(TypedDict, total=False):
    linearPercentage: int
    linearInterval: int


class TimeRangeTypeDef(TypedDict, total=False):
    start: datetime
    end: datetime


class TrafficRouteTypeDef(TypedDict, total=False):
    listenerArns: List[str]


TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": TrafficRoutingType,
        "timeBasedCanary": "TimeBasedCanaryTypeDef",
        "timeBasedLinear": "TimeBasedLinearTypeDef",
    },
    total=False,
)


class TriggerConfigTypeDef(TypedDict, total=False):
    triggerName: str
    triggerTargetArn: str
    triggerEvents: List[TriggerEventType]


class UpdateDeploymentGroupOutputTypeDef(TypedDict):
    hooksNotCleanedUp: List["AutoScalingGroupTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
