"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AmiDistributionConfigurationTypeDef

    data: AmiDistributionConfigurationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_imagebuilder.literals import (
    ComponentType,
    EbsVolumeType,
    ImageStatus,
    ImageType,
    PipelineExecutionStartCondition,
    PipelineStatus,
    Platform,
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
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "CancelImageCreationResponseTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVersionTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerRecipeTypeDef",
    "ContainerTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetComponentResponseTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "GetImagePipelineResponseTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetImageRecipeResponseTypeDef",
    "GetImageResponseTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "ImagePackageTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceConfigurationTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePackagesResponseTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "TargetContainerRepositoryTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
)


class AmiDistributionConfigurationTypeDef(TypedDict, total=False):
    name: str
    description: str
    targetAccountIds: List[str]
    amiTags: Dict[str, str]
    kmsKeyId: str
    launchPermission: "LaunchPermissionConfigurationTypeDef"


class AmiTypeDef(TypedDict, total=False):
    region: str
    image: str
    name: str
    description: str
    state: "ImageStateTypeDef"
    accountId: str


class CancelImageCreationResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str


class ComponentConfigurationTypeDef(TypedDict):
    componentArn: str


ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Platform,
        "supportedOsVersions": List[str],
        "type": ComponentType,
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": ComponentType,
        "platform": Platform,
        "supportedOsVersions": List[str],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "platform": Platform,
        "supportedOsVersions": List[str],
        "type": ComponentType,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)


class _RequiredContainerDistributionConfigurationTypeDef(TypedDict):
    targetRepository: "TargetContainerRepositoryTypeDef"


class ContainerDistributionConfigurationTypeDef(
    _RequiredContainerDistributionConfigurationTypeDef, total=False
):
    description: str
    containerTags: List[str]


class ContainerRecipeSummaryTypeDef(TypedDict, total=False):
    arn: str
    containerType: Literal["DOCKER"]
    name: str
    platform: Platform
    owner: str
    parentImage: str
    dateCreated: str
    tags: Dict[str, str]


class ContainerRecipeTypeDef(TypedDict, total=False):
    arn: str
    containerType: Literal["DOCKER"]
    name: str
    description: str
    platform: Platform
    owner: str
    version: str
    components: List["ComponentConfigurationTypeDef"]
    instanceConfiguration: "InstanceConfigurationTypeDef"
    dockerfileTemplateData: str
    kmsKeyId: str
    encrypted: bool
    parentImage: str
    dateCreated: str
    tags: Dict[str, str]
    workingDirectory: str
    targetRepository: "TargetContainerRepositoryTypeDef"


class ContainerTypeDef(TypedDict, total=False):
    region: str
    imageUris: List[str]


class CreateComponentResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str


class CreateContainerRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    containerRecipeArn: str


class CreateDistributionConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str


class CreateImagePipelineResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imagePipelineArn: str


class CreateImageRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imageRecipeArn: str


class CreateImageResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str


class CreateInfrastructureConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str


class DeleteComponentResponseTypeDef(TypedDict, total=False):
    requestId: str
    componentBuildVersionArn: str


class DeleteContainerRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    containerRecipeArn: str


class DeleteDistributionConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    distributionConfigurationArn: str


class DeleteImagePipelineResponseTypeDef(TypedDict, total=False):
    requestId: str
    imagePipelineArn: str


class DeleteImageRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageRecipeArn: str


class DeleteImageResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageBuildVersionArn: str


class DeleteInfrastructureConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    infrastructureConfigurationArn: str


class DistributionConfigurationSummaryTypeDef(TypedDict, total=False):
    arn: str
    name: str
    description: str
    dateCreated: str
    dateUpdated: str
    tags: Dict[str, str]
    regions: List[str]


class _RequiredDistributionConfigurationTypeDef(TypedDict):
    timeoutMinutes: int


class DistributionConfigurationTypeDef(_RequiredDistributionConfigurationTypeDef, total=False):
    arn: str
    name: str
    description: str
    distributions: List["DistributionTypeDef"]
    dateCreated: str
    dateUpdated: str
    tags: Dict[str, str]


class _RequiredDistributionTypeDef(TypedDict):
    region: str


class DistributionTypeDef(_RequiredDistributionTypeDef, total=False):
    amiDistributionConfiguration: "AmiDistributionConfigurationTypeDef"
    containerDistributionConfiguration: "ContainerDistributionConfigurationTypeDef"
    licenseConfigurationArns: List[str]
    launchTemplateConfigurations: List["LaunchTemplateConfigurationTypeDef"]


class EbsInstanceBlockDeviceSpecificationTypeDef(TypedDict, total=False):
    encrypted: bool
    deleteOnTermination: bool
    iops: int
    kmsKeyId: str
    snapshotId: str
    volumeSize: int
    volumeType: EbsVolumeType


class FilterTypeDef(TypedDict, total=False):
    name: str
    values: List[str]


class GetComponentPolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    policy: str


class GetComponentResponseTypeDef(TypedDict, total=False):
    requestId: str
    component: "ComponentTypeDef"


class GetContainerRecipePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    policy: str


class GetContainerRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    containerRecipe: "ContainerRecipeTypeDef"


class GetDistributionConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    distributionConfiguration: "DistributionConfigurationTypeDef"


class GetImagePipelineResponseTypeDef(TypedDict, total=False):
    requestId: str
    imagePipeline: "ImagePipelineTypeDef"


class GetImagePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    policy: str


class GetImageRecipePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    policy: str


class GetImageRecipeResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageRecipe: "ImageRecipeTypeDef"


class GetImageResponseTypeDef(TypedDict, total=False):
    requestId: str
    image: "ImageTypeDef"


class GetInfrastructureConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    infrastructureConfiguration: "InfrastructureConfigurationTypeDef"


class ImagePackageTypeDef(TypedDict, total=False):
    packageName: str
    packageVersion: str


class ImagePipelineTypeDef(TypedDict, total=False):
    arn: str
    name: str
    description: str
    platform: Platform
    enhancedImageMetadataEnabled: bool
    imageRecipeArn: str
    containerRecipeArn: str
    infrastructureConfigurationArn: str
    distributionConfigurationArn: str
    imageTestsConfiguration: "ImageTestsConfigurationTypeDef"
    schedule: "ScheduleTypeDef"
    status: PipelineStatus
    dateCreated: str
    dateUpdated: str
    dateLastRun: str
    dateNextRun: str
    tags: Dict[str, str]


class ImageRecipeSummaryTypeDef(TypedDict, total=False):
    arn: str
    name: str
    platform: Platform
    owner: str
    parentImage: str
    dateCreated: str
    tags: Dict[str, str]


ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": str,
        "type": ImageType,
        "name": str,
        "description": str,
        "platform": Platform,
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
    },
    total=False,
)


class ImageStateTypeDef(TypedDict, total=False):
    status: ImageStatus
    reason: str


ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageType,
        "version": str,
        "platform": Platform,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "owner": str,
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class ImageTestsConfigurationTypeDef(TypedDict, total=False):
    imageTestsEnabled: bool
    timeoutMinutes: int


ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": str,
        "type": ImageType,
        "name": str,
        "version": str,
        "platform": Platform,
        "enhancedImageMetadataEnabled": bool,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "imageRecipe": "ImageRecipeTypeDef",
        "containerRecipe": "ContainerRecipeTypeDef",
        "sourcePipelineName": str,
        "sourcePipelineArn": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageType,
        "version": str,
        "platform": Platform,
        "osVersion": str,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)


class ImportComponentResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str


class InfrastructureConfigurationSummaryTypeDef(TypedDict, total=False):
    arn: str
    name: str
    description: str
    dateCreated: str
    dateUpdated: str
    resourceTags: Dict[str, str]
    tags: Dict[str, str]
    instanceTypes: List[str]
    instanceProfileName: str


class InfrastructureConfigurationTypeDef(TypedDict, total=False):
    arn: str
    name: str
    description: str
    instanceTypes: List[str]
    instanceProfileName: str
    securityGroupIds: List[str]
    subnetId: str
    logging: "LoggingTypeDef"
    keyPair: str
    terminateInstanceOnFailure: bool
    snsTopicArn: str
    dateCreated: str
    dateUpdated: str
    resourceTags: Dict[str, str]
    tags: Dict[str, str]


class InstanceBlockDeviceMappingTypeDef(TypedDict, total=False):
    deviceName: str
    ebs: "EbsInstanceBlockDeviceSpecificationTypeDef"
    virtualName: str
    noDevice: str


class InstanceConfigurationTypeDef(TypedDict, total=False):
    image: str
    blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"]


class LaunchPermissionConfigurationTypeDef(TypedDict, total=False):
    userIds: List[str]
    userGroups: List[str]


class _RequiredLaunchTemplateConfigurationTypeDef(TypedDict):
    launchTemplateId: str


class LaunchTemplateConfigurationTypeDef(_RequiredLaunchTemplateConfigurationTypeDef, total=False):
    accountId: str
    setDefaultVersion: bool


class ListComponentBuildVersionsResponseTypeDef(TypedDict, total=False):
    requestId: str
    componentSummaryList: List["ComponentSummaryTypeDef"]
    nextToken: str


class ListComponentsResponseTypeDef(TypedDict, total=False):
    requestId: str
    componentVersionList: List["ComponentVersionTypeDef"]
    nextToken: str


class ListContainerRecipesResponseTypeDef(TypedDict, total=False):
    requestId: str
    containerRecipeSummaryList: List["ContainerRecipeSummaryTypeDef"]
    nextToken: str


class ListDistributionConfigurationsResponseTypeDef(TypedDict, total=False):
    requestId: str
    distributionConfigurationSummaryList: List["DistributionConfigurationSummaryTypeDef"]
    nextToken: str


class ListImageBuildVersionsResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageSummaryList: List["ImageSummaryTypeDef"]
    nextToken: str


class ListImagePackagesResponseTypeDef(TypedDict, total=False):
    requestId: str
    imagePackageList: List["ImagePackageTypeDef"]
    nextToken: str


class ListImagePipelineImagesResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageSummaryList: List["ImageSummaryTypeDef"]
    nextToken: str


class ListImagePipelinesResponseTypeDef(TypedDict, total=False):
    requestId: str
    imagePipelineList: List["ImagePipelineTypeDef"]
    nextToken: str


class ListImageRecipesResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageRecipeSummaryList: List["ImageRecipeSummaryTypeDef"]
    nextToken: str


class ListImagesResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageVersionList: List["ImageVersionTypeDef"]
    nextToken: str


class ListInfrastructureConfigurationsResponseTypeDef(TypedDict, total=False):
    requestId: str
    infrastructureConfigurationSummaryList: List["InfrastructureConfigurationSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class LoggingTypeDef(TypedDict, total=False):
    s3Logs: "S3LogsTypeDef"


class OutputResourcesTypeDef(TypedDict, total=False):
    amis: List["AmiTypeDef"]
    containers: List["ContainerTypeDef"]


class PutComponentPolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    componentArn: str


class PutContainerRecipePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    containerRecipeArn: str


class PutImagePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageArn: str


class PutImageRecipePolicyResponseTypeDef(TypedDict, total=False):
    requestId: str
    imageRecipeArn: str


class S3LogsTypeDef(TypedDict, total=False):
    s3BucketName: str
    s3KeyPrefix: str


class ScheduleTypeDef(TypedDict, total=False):
    scheduleExpression: str
    timezone: str
    pipelineExecutionStartCondition: PipelineExecutionStartCondition


class StartImagePipelineExecutionResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str


class TargetContainerRepositoryTypeDef(TypedDict):
    service: Literal["ECR"]
    repositoryName: str


class UpdateDistributionConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str


class UpdateImagePipelineResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    imagePipelineArn: str


class UpdateInfrastructureConfigurationResponseTypeDef(TypedDict, total=False):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
