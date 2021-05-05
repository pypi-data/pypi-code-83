"""
Type annotations for imagebuilder service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_imagebuilder import ImagebuilderClient

    client: ImagebuilderClient = boto3.client("imagebuilder")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_imagebuilder.literals import ComponentType, Ownership, PipelineStatus, Platform
from mypy_boto3_imagebuilder.type_defs import (
    CancelImageCreationResponseTypeDef,
    ComponentConfigurationTypeDef,
    CreateComponentResponseTypeDef,
    CreateContainerRecipeResponseTypeDef,
    CreateDistributionConfigurationResponseTypeDef,
    CreateImagePipelineResponseTypeDef,
    CreateImageRecipeResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateInfrastructureConfigurationResponseTypeDef,
    DeleteComponentResponseTypeDef,
    DeleteContainerRecipeResponseTypeDef,
    DeleteDistributionConfigurationResponseTypeDef,
    DeleteImagePipelineResponseTypeDef,
    DeleteImageRecipeResponseTypeDef,
    DeleteImageResponseTypeDef,
    DeleteInfrastructureConfigurationResponseTypeDef,
    DistributionTypeDef,
    FilterTypeDef,
    GetComponentPolicyResponseTypeDef,
    GetComponentResponseTypeDef,
    GetContainerRecipePolicyResponseTypeDef,
    GetContainerRecipeResponseTypeDef,
    GetDistributionConfigurationResponseTypeDef,
    GetImagePipelineResponseTypeDef,
    GetImagePolicyResponseTypeDef,
    GetImageRecipePolicyResponseTypeDef,
    GetImageRecipeResponseTypeDef,
    GetImageResponseTypeDef,
    GetInfrastructureConfigurationResponseTypeDef,
    ImageTestsConfigurationTypeDef,
    ImportComponentResponseTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceConfigurationTypeDef,
    ListComponentBuildVersionsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListContainerRecipesResponseTypeDef,
    ListDistributionConfigurationsResponseTypeDef,
    ListImageBuildVersionsResponseTypeDef,
    ListImagePackagesResponseTypeDef,
    ListImagePipelineImagesResponseTypeDef,
    ListImagePipelinesResponseTypeDef,
    ListImageRecipesResponseTypeDef,
    ListImagesResponseTypeDef,
    ListInfrastructureConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingTypeDef,
    PutComponentPolicyResponseTypeDef,
    PutContainerRecipePolicyResponseTypeDef,
    PutImagePolicyResponseTypeDef,
    PutImageRecipePolicyResponseTypeDef,
    ScheduleTypeDef,
    StartImagePipelineExecutionResponseTypeDef,
    TargetContainerRepositoryTypeDef,
    UpdateDistributionConfigurationResponseTypeDef,
    UpdateImagePipelineResponseTypeDef,
    UpdateInfrastructureConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ImagebuilderClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    CallRateLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidVersionNumberException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceDependencyException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class ImagebuilderClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#can-paginate)
        """

    def cancel_image_creation(
        self, imageBuildVersionArn: str, clientToken: str
    ) -> CancelImageCreationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.cancel_image_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#cancel-image-creation)
        """

    def create_component(
        self,
        name: str,
        semanticVersion: str,
        platform: Platform,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        supportedOsVersions: List[str] = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-component)
        """

    def create_container_recipe(
        self,
        containerType: Literal["DOCKER"],
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        targetRepository: "TargetContainerRepositoryTypeDef",
        clientToken: str,
        description: str = None,
        instanceConfiguration: "InstanceConfigurationTypeDef" = None,
        dockerfileTemplateData: str = None,
        dockerfileTemplateUri: str = None,
        platformOverride: Platform = None,
        imageOsVersionOverride: str = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
        kmsKeyId: str = None,
    ) -> CreateContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-container-recipe)
        """

    def create_distribution_configuration(
        self,
        name: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-distribution-configuration)
        """

    def create_image(
        self,
        infrastructureConfigurationArn: str,
        clientToken: str,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        tags: Dict[str, str] = None,
    ) -> CreateImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-image)
        """

    def create_image_pipeline(
        self,
        name: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatus = None,
        tags: Dict[str, str] = None,
    ) -> CreateImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-image-pipeline)
        """

    def create_image_recipe(
        self,
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        clientToken: str,
        description: str = None,
        blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"] = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
    ) -> CreateImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-image-recipe)
        """

    def create_infrastructure_configuration(
        self,
        name: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None,
        tags: Dict[str, str] = None,
    ) -> CreateInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.create_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create-infrastructure-configuration)
        """

    def delete_component(self, componentBuildVersionArn: str) -> DeleteComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-component)
        """

    def delete_container_recipe(
        self, containerRecipeArn: str
    ) -> DeleteContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-container-recipe)
        """

    def delete_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> DeleteDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-distribution-configuration)
        """

    def delete_image(self, imageBuildVersionArn: str) -> DeleteImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-image)
        """

    def delete_image_pipeline(self, imagePipelineArn: str) -> DeleteImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-image-pipeline)
        """

    def delete_image_recipe(self, imageRecipeArn: str) -> DeleteImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-image-recipe)
        """

    def delete_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> DeleteInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.delete_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete-infrastructure-configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#generate-presigned-url)
        """

    def get_component(self, componentBuildVersionArn: str) -> GetComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-component)
        """

    def get_component_policy(self, componentArn: str) -> GetComponentPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-component-policy)
        """

    def get_container_recipe(self, containerRecipeArn: str) -> GetContainerRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-container-recipe)
        """

    def get_container_recipe_policy(
        self, containerRecipeArn: str
    ) -> GetContainerRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-container-recipe-policy)
        """

    def get_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> GetDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-distribution-configuration)
        """

    def get_image(self, imageBuildVersionArn: str) -> GetImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-image)
        """

    def get_image_pipeline(self, imagePipelineArn: str) -> GetImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-image-pipeline)
        """

    def get_image_policy(self, imageArn: str) -> GetImagePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-image-policy)
        """

    def get_image_recipe(self, imageRecipeArn: str) -> GetImageRecipeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-image-recipe)
        """

    def get_image_recipe_policy(self, imageRecipeArn: str) -> GetImageRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-image-recipe-policy)
        """

    def get_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> GetInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.get_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get-infrastructure-configuration)
        """

    def import_component(
        self,
        name: str,
        semanticVersion: str,
        type: ComponentType,
        format: Literal["SHELL"],
        platform: Platform,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> ImportComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.import_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#import-component)
        """

    def list_component_build_versions(
        self, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentBuildVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_component_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-component-build-versions)
        """

    def list_components(
        self,
        owner: Ownership = None,
        filters: List[FilterTypeDef] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListComponentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-components)
        """

    def list_container_recipes(
        self,
        owner: Ownership = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListContainerRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_container_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-container-recipes)
        """

    def list_distribution_configurations(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListDistributionConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_distribution_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-distribution-configurations)
        """

    def list_image_build_versions(
        self,
        imageVersionArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImageBuildVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-image-build-versions)
        """

    def list_image_packages(
        self, imageBuildVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListImagePackagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-image-packages)
        """

    def list_image_pipeline_images(
        self,
        imagePipelineArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImagePipelineImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipeline_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-image-pipeline-images)
        """

    def list_image_pipelines(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListImagePipelinesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-image-pipelines)
        """

    def list_image_recipes(
        self,
        owner: Ownership = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImageRecipesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-image-recipes)
        """

    def list_images(
        self,
        owner: Ownership = None,
        filters: List[FilterTypeDef] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None,
        includeDeprecated: bool = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-images)
        """

    def list_infrastructure_configurations(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListInfrastructureConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_infrastructure_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-infrastructure-configurations)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list-tags-for-resource)
        """

    def put_component_policy(
        self, componentArn: str, policy: str
    ) -> PutComponentPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.put_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put-component-policy)
        """

    def put_container_recipe_policy(
        self, containerRecipeArn: str, policy: str
    ) -> PutContainerRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.put_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put-container-recipe-policy)
        """

    def put_image_policy(self, imageArn: str, policy: str) -> PutImagePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put-image-policy)
        """

    def put_image_recipe_policy(
        self, imageRecipeArn: str, policy: str
    ) -> PutImageRecipePolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put-image-recipe-policy)
        """

    def start_image_pipeline_execution(
        self, imagePipelineArn: str, clientToken: str
    ) -> StartImagePipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.start_image_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#start-image-pipeline-execution)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#untag-resource)
        """

    def update_distribution_configuration(
        self,
        distributionConfigurationArn: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
    ) -> UpdateDistributionConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.update_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update-distribution-configuration)
        """

    def update_image_pipeline(
        self,
        imagePipelineArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatus = None,
    ) -> UpdateImagePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.update_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update-image-pipeline)
        """

    def update_infrastructure_configuration(
        self,
        infrastructureConfigurationArn: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None,
    ) -> UpdateInfrastructureConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/imagebuilder.html#Imagebuilder.Client.update_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update-infrastructure-configuration)
        """
