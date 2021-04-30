"""
Main interface for codedeploy service type definitions.

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
    "BlueGreenDeploymentConfigurationTypeDef",
    "BlueInstanceTerminationOptionTypeDef",
    "CloudFormationTargetTypeDef",
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
    "GitHubLocationTypeDef",
    "GreenFleetProvisioningOptionTypeDef",
    "InstanceInfoTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTargetTypeDef",
    "LambdaFunctionInfoTypeDef",
    "LambdaTargetTypeDef",
    "LastDeploymentInfoTypeDef",
    "LifecycleEventTypeDef",
    "LoadBalancerInfoTypeDef",
    "MinimumHealthyHostsTypeDef",
    "OnPremisesTagSetTypeDef",
    "RawStringTypeDef",
    "RelatedDeploymentsTypeDef",
    "ResponseMetadata",
    "RevisionInfoTypeDef",
    "RevisionLocationTypeDef",
    "RollbackInfoTypeDef",
    "S3LocationTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "TargetGroupInfoTypeDef",
    "TargetGroupPairInfoTypeDef",
    "TargetInstancesTypeDef",
    "TimeBasedCanaryTypeDef",
    "TimeBasedLinearTypeDef",
    "TrafficRouteTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TriggerConfigTypeDef",
    "BatchGetApplicationRevisionsOutputTypeDef",
    "BatchGetApplicationsOutputTypeDef",
    "BatchGetDeploymentGroupsOutputTypeDef",
    "BatchGetDeploymentInstancesOutputTypeDef",
    "BatchGetDeploymentTargetsOutputTypeDef",
    "BatchGetDeploymentsOutputTypeDef",
    "BatchGetOnPremisesInstancesOutputTypeDef",
    "CreateApplicationOutputTypeDef",
    "CreateDeploymentConfigOutputTypeDef",
    "CreateDeploymentGroupOutputTypeDef",
    "CreateDeploymentOutputTypeDef",
    "DeleteDeploymentGroupOutputTypeDef",
    "DeleteGitHubAccountTokenOutputTypeDef",
    "GetApplicationOutputTypeDef",
    "GetApplicationRevisionOutputTypeDef",
    "GetDeploymentConfigOutputTypeDef",
    "GetDeploymentGroupOutputTypeDef",
    "GetDeploymentInstanceOutputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetDeploymentTargetOutputTypeDef",
    "GetOnPremisesInstanceOutputTypeDef",
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
    "PaginatorConfigTypeDef",
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    "StopDeploymentOutputTypeDef",
    "TimeRangeTypeDef",
    "UpdateDeploymentGroupOutputTypeDef",
    "WaiterConfigTypeDef",
)

AlarmConfigurationTypeDef = TypedDict(
    "AlarmConfigurationTypeDef",
    {"enabled": bool, "ignorePollAlarmFailure": bool, "alarms": List["AlarmTypeDef"]},
    total=False,
)

AlarmTypeDef = TypedDict("AlarmTypeDef", {"name": str}, total=False)

AppSpecContentTypeDef = TypedDict(
    "AppSpecContentTypeDef", {"content": str, "sha256": str}, total=False
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "applicationId": str,
        "applicationName": str,
        "createTime": datetime,
        "linkedToGitHub": bool,
        "gitHubAccountName": str,
        "computePlatform": ComputePlatform,
    },
    total=False,
)

AutoRollbackConfigurationTypeDef = TypedDict(
    "AutoRollbackConfigurationTypeDef",
    {"enabled": bool, "events": List[AutoRollbackEvent]},
    total=False,
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef", {"name": str, "hook": str}, total=False
)

BlueGreenDeploymentConfigurationTypeDef = TypedDict(
    "BlueGreenDeploymentConfigurationTypeDef",
    {
        "terminateBlueInstancesOnDeploymentSuccess": "BlueInstanceTerminationOptionTypeDef",
        "deploymentReadyOption": "DeploymentReadyOptionTypeDef",
        "greenFleetProvisioningOption": "GreenFleetProvisioningOptionTypeDef",
    },
    total=False,
)

BlueInstanceTerminationOptionTypeDef = TypedDict(
    "BlueInstanceTerminationOptionTypeDef",
    {"action": InstanceAction, "terminationWaitTimeInMinutes": int},
    total=False,
)

CloudFormationTargetTypeDef = TypedDict(
    "CloudFormationTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatus,
        "resourceType": str,
        "targetVersionWeight": float,
    },
    total=False,
)

DeploymentConfigInfoTypeDef = TypedDict(
    "DeploymentConfigInfoTypeDef",
    {
        "deploymentConfigId": str,
        "deploymentConfigName": str,
        "minimumHealthyHosts": "MinimumHealthyHostsTypeDef",
        "createTime": datetime,
        "computePlatform": ComputePlatform,
        "trafficRoutingConfig": "TrafficRoutingConfigTypeDef",
    },
    total=False,
)

DeploymentGroupInfoTypeDef = TypedDict(
    "DeploymentGroupInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupId": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "ec2TagFilters": List["EC2TagFilterTypeDef"],
        "onPremisesInstanceTagFilters": List["TagFilterTypeDef"],
        "autoScalingGroups": List["AutoScalingGroupTypeDef"],
        "serviceRoleArn": str,
        "targetRevision": "RevisionLocationTypeDef",
        "triggerConfigurations": List["TriggerConfigTypeDef"],
        "alarmConfiguration": "AlarmConfigurationTypeDef",
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "outdatedInstancesStrategy": OutdatedInstancesStrategy,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "lastSuccessfulDeployment": "LastDeploymentInfoTypeDef",
        "lastAttemptedDeployment": "LastDeploymentInfoTypeDef",
        "ec2TagSet": "EC2TagSetTypeDef",
        "onPremisesTagSet": "OnPremisesTagSetTypeDef",
        "computePlatform": ComputePlatform,
        "ecsServices": List["ECSServiceTypeDef"],
    },
    total=False,
)

DeploymentInfoTypeDef = TypedDict(
    "DeploymentInfoTypeDef",
    {
        "applicationName": str,
        "deploymentGroupName": str,
        "deploymentConfigName": str,
        "deploymentId": str,
        "previousRevision": "RevisionLocationTypeDef",
        "revision": "RevisionLocationTypeDef",
        "status": DeploymentStatus,
        "errorInformation": "ErrorInformationTypeDef",
        "createTime": datetime,
        "startTime": datetime,
        "completeTime": datetime,
        "deploymentOverview": "DeploymentOverviewTypeDef",
        "description": str,
        "creator": DeploymentCreator,
        "ignoreApplicationStopFailures": bool,
        "autoRollbackConfiguration": "AutoRollbackConfigurationTypeDef",
        "updateOutdatedInstancesOnly": bool,
        "rollbackInfo": "RollbackInfoTypeDef",
        "deploymentStyle": "DeploymentStyleTypeDef",
        "targetInstances": "TargetInstancesTypeDef",
        "instanceTerminationWaitTimeStarted": bool,
        "blueGreenDeploymentConfiguration": "BlueGreenDeploymentConfigurationTypeDef",
        "loadBalancerInfo": "LoadBalancerInfoTypeDef",
        "additionalDeploymentStatusInfo": str,
        "fileExistsBehavior": FileExistsBehavior,
        "deploymentStatusMessages": List[str],
        "computePlatform": ComputePlatform,
        "externalId": str,
        "relatedDeployments": "RelatedDeploymentsTypeDef",
    },
    total=False,
)

DeploymentOverviewTypeDef = TypedDict(
    "DeploymentOverviewTypeDef",
    {
        "Pending": int,
        "InProgress": int,
        "Succeeded": int,
        "Failed": int,
        "Skipped": int,
        "Ready": int,
    },
    total=False,
)

DeploymentReadyOptionTypeDef = TypedDict(
    "DeploymentReadyOptionTypeDef",
    {"actionOnTimeout": DeploymentReadyAction, "waitTimeInMinutes": int},
    total=False,
)

DeploymentStyleTypeDef = TypedDict(
    "DeploymentStyleTypeDef",
    {"deploymentType": DeploymentType, "deploymentOption": DeploymentOption},
    total=False,
)

DeploymentTargetTypeDef = TypedDict(
    "DeploymentTargetTypeDef",
    {
        "deploymentTargetType": DeploymentTargetType,
        "instanceTarget": "InstanceTargetTypeDef",
        "lambdaTarget": "LambdaTargetTypeDef",
        "ecsTarget": "ECSTargetTypeDef",
        "cloudFormationTarget": "CloudFormationTargetTypeDef",
    },
    total=False,
)

DiagnosticsTypeDef = TypedDict(
    "DiagnosticsTypeDef",
    {"errorCode": LifecycleErrorCode, "scriptName": str, "message": str, "logTail": str},
    total=False,
)

EC2TagFilterTypeDef = TypedDict(
    "EC2TagFilterTypeDef", {"Key": str, "Value": str, "Type": EC2TagFilterType}, total=False
)

EC2TagSetTypeDef = TypedDict(
    "EC2TagSetTypeDef", {"ec2TagSetList": List[List["EC2TagFilterTypeDef"]]}, total=False
)

ECSServiceTypeDef = TypedDict(
    "ECSServiceTypeDef", {"serviceName": str, "clusterName": str}, total=False
)

ECSTargetTypeDef = TypedDict(
    "ECSTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "status": TargetStatus,
        "taskSetsInfo": List["ECSTaskSetTypeDef"],
    },
    total=False,
)

ECSTaskSetTypeDef = TypedDict(
    "ECSTaskSetTypeDef",
    {
        "identifer": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "status": str,
        "trafficWeight": float,
        "targetGroup": "TargetGroupInfoTypeDef",
        "taskSetLabel": TargetLabel,
    },
    total=False,
)

ELBInfoTypeDef = TypedDict("ELBInfoTypeDef", {"name": str}, total=False)

ErrorInformationTypeDef = TypedDict(
    "ErrorInformationTypeDef", {"code": ErrorCode, "message": str}, total=False
)

GenericRevisionInfoTypeDef = TypedDict(
    "GenericRevisionInfoTypeDef",
    {
        "description": str,
        "deploymentGroups": List[str],
        "firstUsedTime": datetime,
        "lastUsedTime": datetime,
        "registerTime": datetime,
    },
    total=False,
)

GitHubLocationTypeDef = TypedDict(
    "GitHubLocationTypeDef", {"repository": str, "commitId": str}, total=False
)

GreenFleetProvisioningOptionTypeDef = TypedDict(
    "GreenFleetProvisioningOptionTypeDef", {"action": GreenFleetProvisioningAction}, total=False
)

InstanceInfoTypeDef = TypedDict(
    "InstanceInfoTypeDef",
    {
        "instanceName": str,
        "iamSessionArn": str,
        "iamUserArn": str,
        "instanceArn": str,
        "registerTime": datetime,
        "deregisterTime": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "deploymentId": str,
        "instanceId": str,
        "status": InstanceStatus,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceType": InstanceType,
    },
    total=False,
)

InstanceTargetTypeDef = TypedDict(
    "InstanceTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatus,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "instanceLabel": TargetLabel,
    },
    total=False,
)

LambdaFunctionInfoTypeDef = TypedDict(
    "LambdaFunctionInfoTypeDef",
    {
        "functionName": str,
        "functionAlias": str,
        "currentVersion": str,
        "targetVersion": str,
        "targetVersionWeight": float,
    },
    total=False,
)

LambdaTargetTypeDef = TypedDict(
    "LambdaTargetTypeDef",
    {
        "deploymentId": str,
        "targetId": str,
        "targetArn": str,
        "status": TargetStatus,
        "lastUpdatedAt": datetime,
        "lifecycleEvents": List["LifecycleEventTypeDef"],
        "lambdaFunctionInfo": "LambdaFunctionInfoTypeDef",
    },
    total=False,
)

LastDeploymentInfoTypeDef = TypedDict(
    "LastDeploymentInfoTypeDef",
    {"deploymentId": str, "status": DeploymentStatus, "endTime": datetime, "createTime": datetime},
    total=False,
)

LifecycleEventTypeDef = TypedDict(
    "LifecycleEventTypeDef",
    {
        "lifecycleEventName": str,
        "diagnostics": "DiagnosticsTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": LifecycleEventStatus,
    },
    total=False,
)

LoadBalancerInfoTypeDef = TypedDict(
    "LoadBalancerInfoTypeDef",
    {
        "elbInfoList": List["ELBInfoTypeDef"],
        "targetGroupInfoList": List["TargetGroupInfoTypeDef"],
        "targetGroupPairInfoList": List["TargetGroupPairInfoTypeDef"],
    },
    total=False,
)

MinimumHealthyHostsTypeDef = TypedDict(
    "MinimumHealthyHostsTypeDef", {"type": MinimumHealthyHostsType, "value": int}, total=False
)

OnPremisesTagSetTypeDef = TypedDict(
    "OnPremisesTagSetTypeDef", {"onPremisesTagSetList": List[List["TagFilterTypeDef"]]}, total=False
)

RawStringTypeDef = TypedDict("RawStringTypeDef", {"content": str, "sha256": str}, total=False)

RelatedDeploymentsTypeDef = TypedDict(
    "RelatedDeploymentsTypeDef",
    {
        "autoUpdateOutdatedInstancesRootDeploymentId": str,
        "autoUpdateOutdatedInstancesDeploymentIds": List[str],
    },
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

RevisionInfoTypeDef = TypedDict(
    "RevisionInfoTypeDef",
    {
        "revisionLocation": "RevisionLocationTypeDef",
        "genericRevisionInfo": "GenericRevisionInfoTypeDef",
    },
    total=False,
)

RevisionLocationTypeDef = TypedDict(
    "RevisionLocationTypeDef",
    {
        "revisionType": RevisionLocationType,
        "s3Location": "S3LocationTypeDef",
        "gitHubLocation": "GitHubLocationTypeDef",
        "string": "RawStringTypeDef",
        "appSpecContent": "AppSpecContentTypeDef",
    },
    total=False,
)

RollbackInfoTypeDef = TypedDict(
    "RollbackInfoTypeDef",
    {"rollbackDeploymentId": str, "rollbackTriggeringDeploymentId": str, "rollbackMessage": str},
    total=False,
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {"bucket": str, "key": str, "bundleType": BundleType, "version": str, "eTag": str},
    total=False,
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef", {"Key": str, "Value": str, "Type": TagFilterType}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TargetGroupInfoTypeDef = TypedDict("TargetGroupInfoTypeDef", {"name": str}, total=False)

TargetGroupPairInfoTypeDef = TypedDict(
    "TargetGroupPairInfoTypeDef",
    {
        "targetGroups": List["TargetGroupInfoTypeDef"],
        "prodTrafficRoute": "TrafficRouteTypeDef",
        "testTrafficRoute": "TrafficRouteTypeDef",
    },
    total=False,
)

TargetInstancesTypeDef = TypedDict(
    "TargetInstancesTypeDef",
    {
        "tagFilters": List["EC2TagFilterTypeDef"],
        "autoScalingGroups": List[str],
        "ec2TagSet": "EC2TagSetTypeDef",
    },
    total=False,
)

TimeBasedCanaryTypeDef = TypedDict(
    "TimeBasedCanaryTypeDef", {"canaryPercentage": int, "canaryInterval": int}, total=False
)

TimeBasedLinearTypeDef = TypedDict(
    "TimeBasedLinearTypeDef", {"linearPercentage": int, "linearInterval": int}, total=False
)

TrafficRouteTypeDef = TypedDict("TrafficRouteTypeDef", {"listenerArns": List[str]}, total=False)

TrafficRoutingConfigTypeDef = TypedDict(
    "TrafficRoutingConfigTypeDef",
    {
        "type": TrafficRoutingType,
        "timeBasedCanary": "TimeBasedCanaryTypeDef",
        "timeBasedLinear": "TimeBasedLinearTypeDef",
    },
    total=False,
)

TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {"triggerName": str, "triggerTargetArn": str, "triggerEvents": List[TriggerEventType]},
    total=False,
)

BatchGetApplicationRevisionsOutputTypeDef = TypedDict(
    "BatchGetApplicationRevisionsOutputTypeDef",
    {
        "applicationName": str,
        "errorMessage": str,
        "revisions": List["RevisionInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetApplicationsOutputTypeDef = TypedDict(
    "BatchGetApplicationsOutputTypeDef",
    {"applicationsInfo": List["ApplicationInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

BatchGetDeploymentGroupsOutputTypeDef = TypedDict(
    "BatchGetDeploymentGroupsOutputTypeDef",
    {
        "deploymentGroupsInfo": List["DeploymentGroupInfoTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetDeploymentInstancesOutputTypeDef = TypedDict(
    "BatchGetDeploymentInstancesOutputTypeDef",
    {
        "instancesSummary": List["InstanceSummaryTypeDef"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetDeploymentTargetsOutputTypeDef = TypedDict(
    "BatchGetDeploymentTargetsOutputTypeDef",
    {"deploymentTargets": List["DeploymentTargetTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

BatchGetDeploymentsOutputTypeDef = TypedDict(
    "BatchGetDeploymentsOutputTypeDef",
    {"deploymentsInfo": List["DeploymentInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

BatchGetOnPremisesInstancesOutputTypeDef = TypedDict(
    "BatchGetOnPremisesInstancesOutputTypeDef",
    {"instanceInfos": List["InstanceInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateApplicationOutputTypeDef = TypedDict(
    "CreateApplicationOutputTypeDef",
    {"applicationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateDeploymentConfigOutputTypeDef = TypedDict(
    "CreateDeploymentConfigOutputTypeDef",
    {"deploymentConfigId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateDeploymentGroupOutputTypeDef = TypedDict(
    "CreateDeploymentGroupOutputTypeDef",
    {"deploymentGroupId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateDeploymentOutputTypeDef = TypedDict(
    "CreateDeploymentOutputTypeDef",
    {"deploymentId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteDeploymentGroupOutputTypeDef = TypedDict(
    "DeleteDeploymentGroupOutputTypeDef",
    {"hooksNotCleanedUp": List["AutoScalingGroupTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteGitHubAccountTokenOutputTypeDef = TypedDict(
    "DeleteGitHubAccountTokenOutputTypeDef",
    {"tokenName": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {"application": "ApplicationInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetApplicationRevisionOutputTypeDef = TypedDict(
    "GetApplicationRevisionOutputTypeDef",
    {
        "applicationName": str,
        "revision": "RevisionLocationTypeDef",
        "revisionInfo": "GenericRevisionInfoTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetDeploymentConfigOutputTypeDef = TypedDict(
    "GetDeploymentConfigOutputTypeDef",
    {"deploymentConfigInfo": "DeploymentConfigInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDeploymentGroupOutputTypeDef = TypedDict(
    "GetDeploymentGroupOutputTypeDef",
    {"deploymentGroupInfo": "DeploymentGroupInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDeploymentInstanceOutputTypeDef = TypedDict(
    "GetDeploymentInstanceOutputTypeDef",
    {"instanceSummary": "InstanceSummaryTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDeploymentOutputTypeDef = TypedDict(
    "GetDeploymentOutputTypeDef",
    {"deploymentInfo": "DeploymentInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDeploymentTargetOutputTypeDef = TypedDict(
    "GetDeploymentTargetOutputTypeDef",
    {"deploymentTarget": "DeploymentTargetTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetOnPremisesInstanceOutputTypeDef = TypedDict(
    "GetOnPremisesInstanceOutputTypeDef",
    {"instanceInfo": "InstanceInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListApplicationRevisionsOutputTypeDef = TypedDict(
    "ListApplicationRevisionsOutputTypeDef",
    {
        "revisions": List["RevisionLocationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {"applications": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListDeploymentConfigsOutputTypeDef = TypedDict(
    "ListDeploymentConfigsOutputTypeDef",
    {"deploymentConfigsList": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListDeploymentGroupsOutputTypeDef = TypedDict(
    "ListDeploymentGroupsOutputTypeDef",
    {
        "applicationName": str,
        "deploymentGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListDeploymentInstancesOutputTypeDef = TypedDict(
    "ListDeploymentInstancesOutputTypeDef",
    {"instancesList": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListDeploymentTargetsOutputTypeDef = TypedDict(
    "ListDeploymentTargetsOutputTypeDef",
    {"targetIds": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListDeploymentsOutputTypeDef = TypedDict(
    "ListDeploymentsOutputTypeDef",
    {"deployments": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListGitHubAccountTokenNamesOutputTypeDef = TypedDict(
    "ListGitHubAccountTokenNamesOutputTypeDef",
    {"tokenNameList": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListOnPremisesInstancesOutputTypeDef = TypedDict(
    "ListOnPremisesInstancesOutputTypeDef",
    {"instanceNames": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutLifecycleEventHookExecutionStatusOutputTypeDef = TypedDict(
    "PutLifecycleEventHookExecutionStatusOutputTypeDef",
    {"lifecycleEventHookExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopDeploymentOutputTypeDef = TypedDict(
    "StopDeploymentOutputTypeDef",
    {"status": StopStatus, "statusMessage": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

TimeRangeTypeDef = TypedDict("TimeRangeTypeDef", {"start": datetime, "end": datetime}, total=False)

UpdateDeploymentGroupOutputTypeDef = TypedDict(
    "UpdateDeploymentGroupOutputTypeDef",
    {"hooksNotCleanedUp": List["AutoScalingGroupTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
