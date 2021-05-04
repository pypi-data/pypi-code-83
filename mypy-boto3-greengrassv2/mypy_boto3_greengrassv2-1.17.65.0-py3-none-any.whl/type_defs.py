"""
Type annotations for greengrassv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import CancelDeploymentResponseTypeDef

    data: CancelDeploymentResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_greengrassv2.literals import (
    CloudComponentState,
    ComponentDependencyType,
    CoreDeviceStatus,
    DeploymentComponentUpdatePolicyAction,
    DeploymentFailureHandlingPolicy,
    DeploymentStatus,
    EffectiveDeploymentExecutionStatus,
    InstalledComponentLifecycleState,
    IoTJobExecutionFailureType,
    LambdaEventSourceType,
    LambdaFilesystemPermission,
    LambdaInputPayloadEncodingType,
    LambdaIsolationMode,
    RecipeOutputFormat,
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
    "CancelDeploymentResponseTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "CoreDeviceTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentResponseTypeDef",
    "EffectiveDeploymentTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetDeploymentResponseTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortConfigTypeDef",
    "IoTJobAbortCriteriaTypeDef",
    "IoTJobExecutionsRolloutConfigTypeDef",
    "IoTJobExponentialRolloutRateTypeDef",
    "IoTJobRateIncreaseCriteriaTypeDef",
    "IoTJobTimeoutConfigTypeDef",
    "LambdaContainerParamsTypeDef",
    "LambdaDeviceMountTypeDef",
    "LambdaEventSourceTypeDef",
    "LambdaExecutionParametersTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "LambdaLinuxProcessParamsTypeDef",
    "LambdaVolumeMountTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
    "ResolvedComponentVersionTypeDef",
)


class CancelDeploymentResponseTypeDef(TypedDict, total=False):
    message: str


class CloudComponentStatusTypeDef(TypedDict, total=False):
    componentState: CloudComponentState
    message: str
    errors: Dict[str, str]


class ComponentCandidateTypeDef(TypedDict, total=False):
    componentName: str
    componentVersion: str
    versionRequirements: Dict[str, str]


class ComponentConfigurationUpdateTypeDef(TypedDict, total=False):
    merge: str
    reset: List[str]


class ComponentDependencyRequirementTypeDef(TypedDict, total=False):
    versionRequirement: str
    dependencyType: ComponentDependencyType


class ComponentDeploymentSpecificationTypeDef(TypedDict, total=False):
    componentVersion: str
    configurationUpdate: "ComponentConfigurationUpdateTypeDef"
    runWith: "ComponentRunWithTypeDef"


class ComponentLatestVersionTypeDef(TypedDict, total=False):
    arn: str
    componentVersion: str
    creationTimestamp: datetime
    description: str
    publisher: str
    platforms: List["ComponentPlatformTypeDef"]


class ComponentPlatformTypeDef(TypedDict, total=False):
    name: str
    attributes: Dict[str, str]


class ComponentRunWithTypeDef(TypedDict, total=False):
    posixUser: str


class ComponentTypeDef(TypedDict, total=False):
    arn: str
    componentName: str
    latestVersion: "ComponentLatestVersionTypeDef"


class ComponentVersionListItemTypeDef(TypedDict, total=False):
    componentName: str
    componentVersion: str
    arn: str


class CoreDeviceTypeDef(TypedDict, total=False):
    coreDeviceThingName: str
    status: CoreDeviceStatus
    lastStatusUpdateTimestamp: datetime


class _RequiredCreateComponentVersionResponseTypeDef(TypedDict):
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: "CloudComponentStatusTypeDef"


class CreateComponentVersionResponseTypeDef(
    _RequiredCreateComponentVersionResponseTypeDef, total=False
):
    arn: str


class CreateDeploymentResponseTypeDef(TypedDict, total=False):
    deploymentId: str
    iotJobId: str
    iotJobArn: str


class DeploymentComponentUpdatePolicyTypeDef(TypedDict, total=False):
    timeoutInSeconds: int
    action: DeploymentComponentUpdatePolicyAction


class DeploymentConfigurationValidationPolicyTypeDef(TypedDict, total=False):
    timeoutInSeconds: int


class DeploymentIoTJobConfigurationTypeDef(TypedDict, total=False):
    jobExecutionsRolloutConfig: "IoTJobExecutionsRolloutConfigTypeDef"
    abortConfig: "IoTJobAbortConfigTypeDef"
    timeoutConfig: "IoTJobTimeoutConfigTypeDef"


class DeploymentPoliciesTypeDef(TypedDict, total=False):
    failureHandlingPolicy: DeploymentFailureHandlingPolicy
    componentUpdatePolicy: "DeploymentComponentUpdatePolicyTypeDef"
    configurationValidationPolicy: "DeploymentConfigurationValidationPolicyTypeDef"


class DeploymentTypeDef(TypedDict, total=False):
    targetArn: str
    revisionId: str
    deploymentId: str
    deploymentName: str
    creationTimestamp: datetime
    deploymentStatus: DeploymentStatus
    isLatestForTarget: bool


class DescribeComponentResponseTypeDef(TypedDict, total=False):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    publisher: str
    description: str
    status: "CloudComponentStatusTypeDef"
    platforms: List["ComponentPlatformTypeDef"]
    tags: Dict[str, str]


class _RequiredEffectiveDeploymentTypeDef(TypedDict):
    deploymentId: str
    deploymentName: str
    targetArn: str
    coreDeviceExecutionStatus: EffectiveDeploymentExecutionStatus
    creationTimestamp: datetime
    modifiedTimestamp: datetime


class EffectiveDeploymentTypeDef(_RequiredEffectiveDeploymentTypeDef, total=False):
    iotJobId: str
    iotJobArn: str
    description: str
    reason: str


class _RequiredGetComponentResponseTypeDef(TypedDict):
    recipeOutputFormat: RecipeOutputFormat
    recipe: Union[bytes, IO[bytes]]


class GetComponentResponseTypeDef(_RequiredGetComponentResponseTypeDef, total=False):
    tags: Dict[str, str]


class GetComponentVersionArtifactResponseTypeDef(TypedDict):
    preSignedUrl: str


class GetCoreDeviceResponseTypeDef(TypedDict, total=False):
    coreDeviceThingName: str
    coreVersion: str
    platform: str
    architecture: str
    status: CoreDeviceStatus
    lastStatusUpdateTimestamp: datetime
    tags: Dict[str, str]


class GetDeploymentResponseTypeDef(TypedDict, total=False):
    targetArn: str
    revisionId: str
    deploymentId: str
    deploymentName: str
    deploymentStatus: DeploymentStatus
    iotJobId: str
    iotJobArn: str
    components: Dict[str, "ComponentDeploymentSpecificationTypeDef"]
    deploymentPolicies: "DeploymentPoliciesTypeDef"
    iotJobConfiguration: "DeploymentIoTJobConfigurationTypeDef"
    creationTimestamp: datetime
    isLatestForTarget: bool
    tags: Dict[str, str]


class InstalledComponentTypeDef(TypedDict, total=False):
    componentName: str
    componentVersion: str
    lifecycleState: InstalledComponentLifecycleState
    lifecycleStateDetails: str
    isRoot: bool


class IoTJobAbortConfigTypeDef(TypedDict):
    criteriaList: List["IoTJobAbortCriteriaTypeDef"]


class IoTJobAbortCriteriaTypeDef(TypedDict):
    failureType: IoTJobExecutionFailureType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class IoTJobExecutionsRolloutConfigTypeDef(TypedDict, total=False):
    exponentialRate: "IoTJobExponentialRolloutRateTypeDef"
    maximumPerMinute: int


class IoTJobExponentialRolloutRateTypeDef(TypedDict):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: "IoTJobRateIncreaseCriteriaTypeDef"


class IoTJobRateIncreaseCriteriaTypeDef(TypedDict, total=False):
    numberOfNotifiedThings: int
    numberOfSucceededThings: int


class IoTJobTimeoutConfigTypeDef(TypedDict, total=False):
    inProgressTimeoutInMinutes: int


class LambdaContainerParamsTypeDef(TypedDict, total=False):
    memorySizeInKB: int
    mountROSysfs: bool
    volumes: List["LambdaVolumeMountTypeDef"]
    devices: List["LambdaDeviceMountTypeDef"]


class _RequiredLambdaDeviceMountTypeDef(TypedDict):
    path: str


class LambdaDeviceMountTypeDef(_RequiredLambdaDeviceMountTypeDef, total=False):
    permission: LambdaFilesystemPermission
    addGroupOwner: bool


LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef", {"topic": str, "type": LambdaEventSourceType}
)


class LambdaExecutionParametersTypeDef(TypedDict, total=False):
    eventSources: List["LambdaEventSourceTypeDef"]
    maxQueueSize: int
    maxInstancesCount: int
    maxIdleTimeInSeconds: int
    timeoutInSeconds: int
    statusTimeoutInSeconds: int
    pinned: bool
    inputPayloadEncodingType: LambdaInputPayloadEncodingType
    execArgs: List[str]
    environmentVariables: Dict[str, str]
    linuxProcessParams: "LambdaLinuxProcessParamsTypeDef"


class _RequiredLambdaFunctionRecipeSourceTypeDef(TypedDict):
    lambdaArn: str


class LambdaFunctionRecipeSourceTypeDef(_RequiredLambdaFunctionRecipeSourceTypeDef, total=False):
    componentName: str
    componentVersion: str
    componentPlatforms: List["ComponentPlatformTypeDef"]
    componentDependencies: Dict[str, "ComponentDependencyRequirementTypeDef"]
    componentLambdaParameters: "LambdaExecutionParametersTypeDef"


class LambdaLinuxProcessParamsTypeDef(TypedDict, total=False):
    isolationMode: LambdaIsolationMode
    containerParams: "LambdaContainerParamsTypeDef"


class _RequiredLambdaVolumeMountTypeDef(TypedDict):
    sourcePath: str
    destinationPath: str


class LambdaVolumeMountTypeDef(_RequiredLambdaVolumeMountTypeDef, total=False):
    permission: LambdaFilesystemPermission
    addGroupOwner: bool


class ListComponentVersionsResponseTypeDef(TypedDict, total=False):
    componentVersions: List["ComponentVersionListItemTypeDef"]
    nextToken: str


class ListComponentsResponseTypeDef(TypedDict, total=False):
    components: List["ComponentTypeDef"]
    nextToken: str


class ListCoreDevicesResponseTypeDef(TypedDict, total=False):
    coreDevices: List["CoreDeviceTypeDef"]
    nextToken: str


class ListDeploymentsResponseTypeDef(TypedDict, total=False):
    deployments: List["DeploymentTypeDef"]
    nextToken: str


class ListEffectiveDeploymentsResponseTypeDef(TypedDict, total=False):
    effectiveDeployments: List["EffectiveDeploymentTypeDef"]
    nextToken: str


class ListInstalledComponentsResponseTypeDef(TypedDict, total=False):
    installedComponents: List["InstalledComponentTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResolveComponentCandidatesResponseTypeDef(TypedDict, total=False):
    resolvedComponentVersions: List["ResolvedComponentVersionTypeDef"]


class ResolvedComponentVersionTypeDef(TypedDict, total=False):
    arn: str
    componentName: str
    componentVersion: str
    recipe: Union[bytes, IO[bytes]]
