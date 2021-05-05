"""
Type annotations for appconfig service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appconfig import AppConfigClient

    client: AppConfigClient = boto3.client("appconfig")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_appconfig.literals import GrowthType, ReplicateTo
from mypy_boto3_appconfig.type_defs import (
    ApplicationsTypeDef,
    ApplicationTypeDef,
    ConfigurationProfilesTypeDef,
    ConfigurationProfileTypeDef,
    ConfigurationTypeDef,
    DeploymentStrategiesTypeDef,
    DeploymentStrategyTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    EnvironmentsTypeDef,
    EnvironmentTypeDef,
    HostedConfigurationVersionsTypeDef,
    HostedConfigurationVersionTypeDef,
    MonitorTypeDef,
    ResourceTagsTypeDef,
    ValidatorTypeDef,
)

__all__ = ("AppConfigClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]


class AppConfigClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#can-paginate)
        """

    def create_application(
        self, Name: str, Description: str = None, Tags: Dict[str, str] = None
    ) -> "ApplicationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create-application)
        """

    def create_configuration_profile(
        self,
        ApplicationId: str,
        Name: str,
        LocationUri: str,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None,
        Tags: Dict[str, str] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.create_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create-configuration-profile)
        """

    def create_deployment_strategy(
        self,
        Name: str,
        DeploymentDurationInMinutes: int,
        GrowthFactor: float,
        ReplicateTo: ReplicateTo,
        Description: str = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthType: GrowthType = None,
        Tags: Dict[str, str] = None,
    ) -> "DeploymentStrategyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.create_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create-deployment-strategy)
        """

    def create_environment(
        self,
        ApplicationId: str,
        Name: str,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None,
        Tags: Dict[str, str] = None,
    ) -> "EnvironmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create-environment)
        """

    def create_hosted_configuration_version(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Content: Union[bytes, IO[bytes]],
        ContentType: str,
        Description: str = None,
        LatestVersionNumber: int = None,
    ) -> HostedConfigurationVersionTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.create_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#create-hosted-configuration-version)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete-application)
        """

    def delete_configuration_profile(self, ApplicationId: str, ConfigurationProfileId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.delete_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete-configuration-profile)
        """

    def delete_deployment_strategy(self, DeploymentStrategyId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.delete_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete-deployment-strategy)
        """

    def delete_environment(self, ApplicationId: str, EnvironmentId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete-environment)
        """

    def delete_hosted_configuration_version(
        self, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.delete_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#delete-hosted-configuration-version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#generate-presigned-url)
        """

    def get_application(self, ApplicationId: str) -> "ApplicationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-application)
        """

    def get_configuration(
        self,
        Application: str,
        Environment: str,
        Configuration: str,
        ClientId: str,
        ClientConfigurationVersion: str = None,
    ) -> ConfigurationTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-configuration)
        """

    def get_configuration_profile(
        self, ApplicationId: str, ConfigurationProfileId: str
    ) -> ConfigurationProfileTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-configuration-profile)
        """

    def get_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-deployment)
        """

    def get_deployment_strategy(self, DeploymentStrategyId: str) -> "DeploymentStrategyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-deployment-strategy)
        """

    def get_environment(self, ApplicationId: str, EnvironmentId: str) -> "EnvironmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-environment)
        """

    def get_hosted_configuration_version(
        self, ApplicationId: str, ConfigurationProfileId: str, VersionNumber: int
    ) -> HostedConfigurationVersionTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.get_hosted_configuration_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#get-hosted-configuration-version)
        """

    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ApplicationsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-applications)
        """

    def list_configuration_profiles(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ConfigurationProfilesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_configuration_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-configuration-profiles)
        """

    def list_deployment_strategies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentStrategiesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_deployment_strategies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-deployment-strategies)
        """

    def list_deployments(
        self, ApplicationId: str, EnvironmentId: str, MaxResults: int = None, NextToken: str = None
    ) -> DeploymentsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-deployments)
        """

    def list_environments(
        self, ApplicationId: str, MaxResults: int = None, NextToken: str = None
    ) -> EnvironmentsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-environments)
        """

    def list_hosted_configuration_versions(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> HostedConfigurationVersionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_hosted_configuration_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-hosted-configuration-versions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ResourceTagsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#list-tags-for-resource)
        """

    def start_deployment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        DeploymentStrategyId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> DeploymentTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.start_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#start-deployment)
        """

    def stop_deployment(
        self, ApplicationId: str, EnvironmentId: str, DeploymentNumber: int
    ) -> DeploymentTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.stop_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#stop-deployment)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#untag-resource)
        """

    def update_application(
        self, ApplicationId: str, Name: str = None, Description: str = None
    ) -> "ApplicationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update-application)
        """

    def update_configuration_profile(
        self,
        ApplicationId: str,
        ConfigurationProfileId: str,
        Name: str = None,
        Description: str = None,
        RetrievalRoleArn: str = None,
        Validators: List["ValidatorTypeDef"] = None,
    ) -> ConfigurationProfileTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.update_configuration_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update-configuration-profile)
        """

    def update_deployment_strategy(
        self,
        DeploymentStrategyId: str,
        Description: str = None,
        DeploymentDurationInMinutes: int = None,
        FinalBakeTimeInMinutes: int = None,
        GrowthFactor: float = None,
        GrowthType: GrowthType = None,
    ) -> "DeploymentStrategyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.update_deployment_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update-deployment-strategy)
        """

    def update_environment(
        self,
        ApplicationId: str,
        EnvironmentId: str,
        Name: str = None,
        Description: str = None,
        Monitors: List["MonitorTypeDef"] = None,
    ) -> "EnvironmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#update-environment)
        """

    def validate_configuration(
        self, ApplicationId: str, ConfigurationProfileId: str, ConfigurationVersion: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/appconfig.html#AppConfig.Client.validate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/client.html#validate-configuration)
        """
