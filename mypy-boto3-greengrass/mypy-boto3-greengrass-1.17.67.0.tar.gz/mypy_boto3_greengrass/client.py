"""
Type annotations for greengrass service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_greengrass import GreengrassClient

    client: GreengrassClient = boto3.client("greengrass")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_greengrass.literals import (
    DeploymentType,
    SoftwareToUpdate,
    UpdateAgentLogLevel,
    UpdateTargetsArchitecture,
    UpdateTargetsOperatingSystem,
)
from mypy_boto3_greengrass.paginator import (
    ListBulkDeploymentDetailedReportsPaginator,
    ListBulkDeploymentsPaginator,
    ListConnectorDefinitionsPaginator,
    ListConnectorDefinitionVersionsPaginator,
    ListCoreDefinitionsPaginator,
    ListCoreDefinitionVersionsPaginator,
    ListDeploymentsPaginator,
    ListDeviceDefinitionsPaginator,
    ListDeviceDefinitionVersionsPaginator,
    ListFunctionDefinitionsPaginator,
    ListFunctionDefinitionVersionsPaginator,
    ListGroupsPaginator,
    ListGroupVersionsPaginator,
    ListLoggerDefinitionsPaginator,
    ListLoggerDefinitionVersionsPaginator,
    ListResourceDefinitionsPaginator,
    ListResourceDefinitionVersionsPaginator,
    ListSubscriptionDefinitionsPaginator,
    ListSubscriptionDefinitionVersionsPaginator,
)
from mypy_boto3_greengrass.type_defs import (
    AssociateRoleToGroupResponseTypeDef,
    AssociateServiceRoleToAccountResponseTypeDef,
    ConnectivityInfoTypeDef,
    ConnectorDefinitionVersionTypeDef,
    ConnectorTypeDef,
    CoreDefinitionVersionTypeDef,
    CoreTypeDef,
    CreateConnectorDefinitionResponseTypeDef,
    CreateConnectorDefinitionVersionResponseTypeDef,
    CreateCoreDefinitionResponseTypeDef,
    CreateCoreDefinitionVersionResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDeviceDefinitionResponseTypeDef,
    CreateDeviceDefinitionVersionResponseTypeDef,
    CreateFunctionDefinitionResponseTypeDef,
    CreateFunctionDefinitionVersionResponseTypeDef,
    CreateGroupCertificateAuthorityResponseTypeDef,
    CreateGroupResponseTypeDef,
    CreateGroupVersionResponseTypeDef,
    CreateLoggerDefinitionResponseTypeDef,
    CreateLoggerDefinitionVersionResponseTypeDef,
    CreateResourceDefinitionResponseTypeDef,
    CreateResourceDefinitionVersionResponseTypeDef,
    CreateSoftwareUpdateJobResponseTypeDef,
    CreateSubscriptionDefinitionResponseTypeDef,
    CreateSubscriptionDefinitionVersionResponseTypeDef,
    DeviceDefinitionVersionTypeDef,
    DeviceTypeDef,
    DisassociateRoleFromGroupResponseTypeDef,
    DisassociateServiceRoleFromAccountResponseTypeDef,
    FunctionDefaultConfigTypeDef,
    FunctionDefinitionVersionTypeDef,
    FunctionTypeDef,
    GetAssociatedRoleResponseTypeDef,
    GetBulkDeploymentStatusResponseTypeDef,
    GetConnectivityInfoResponseTypeDef,
    GetConnectorDefinitionResponseTypeDef,
    GetConnectorDefinitionVersionResponseTypeDef,
    GetCoreDefinitionResponseTypeDef,
    GetCoreDefinitionVersionResponseTypeDef,
    GetDeploymentStatusResponseTypeDef,
    GetDeviceDefinitionResponseTypeDef,
    GetDeviceDefinitionVersionResponseTypeDef,
    GetFunctionDefinitionResponseTypeDef,
    GetFunctionDefinitionVersionResponseTypeDef,
    GetGroupCertificateAuthorityResponseTypeDef,
    GetGroupCertificateConfigurationResponseTypeDef,
    GetGroupResponseTypeDef,
    GetGroupVersionResponseTypeDef,
    GetLoggerDefinitionResponseTypeDef,
    GetLoggerDefinitionVersionResponseTypeDef,
    GetResourceDefinitionResponseTypeDef,
    GetResourceDefinitionVersionResponseTypeDef,
    GetServiceRoleForAccountResponseTypeDef,
    GetSubscriptionDefinitionResponseTypeDef,
    GetSubscriptionDefinitionVersionResponseTypeDef,
    GetThingRuntimeConfigurationResponseTypeDef,
    GroupVersionTypeDef,
    ListBulkDeploymentDetailedReportsResponseTypeDef,
    ListBulkDeploymentsResponseTypeDef,
    ListConnectorDefinitionsResponseTypeDef,
    ListConnectorDefinitionVersionsResponseTypeDef,
    ListCoreDefinitionsResponseTypeDef,
    ListCoreDefinitionVersionsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListDeviceDefinitionsResponseTypeDef,
    ListDeviceDefinitionVersionsResponseTypeDef,
    ListFunctionDefinitionsResponseTypeDef,
    ListFunctionDefinitionVersionsResponseTypeDef,
    ListGroupCertificateAuthoritiesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListGroupVersionsResponseTypeDef,
    ListLoggerDefinitionsResponseTypeDef,
    ListLoggerDefinitionVersionsResponseTypeDef,
    ListResourceDefinitionsResponseTypeDef,
    ListResourceDefinitionVersionsResponseTypeDef,
    ListSubscriptionDefinitionsResponseTypeDef,
    ListSubscriptionDefinitionVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggerDefinitionVersionTypeDef,
    LoggerTypeDef,
    ResetDeploymentsResponseTypeDef,
    ResourceDefinitionVersionTypeDef,
    ResourceTypeDef,
    StartBulkDeploymentResponseTypeDef,
    SubscriptionDefinitionVersionTypeDef,
    SubscriptionTypeDef,
    TelemetryConfigurationUpdateTypeDef,
    UpdateConnectivityInfoResponseTypeDef,
    UpdateGroupCertificateConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GreengrassClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]


class GreengrassClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_role_to_group(
        self, GroupId: str, RoleArn: str
    ) -> AssociateRoleToGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.associate_role_to_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#associate-role-to-group)
        """

    def associate_service_role_to_account(
        self, RoleArn: str
    ) -> AssociateServiceRoleToAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.associate_service_role_to_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#associate-service-role-to-account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#can-paginate)
        """

    def create_connector_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "ConnectorDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateConnectorDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_connector_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-connector-definition)
        """

    def create_connector_definition_version(
        self,
        ConnectorDefinitionId: str,
        AmznClientToken: str = None,
        Connectors: List["ConnectorTypeDef"] = None,
    ) -> CreateConnectorDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_connector_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-connector-definition-version)
        """

    def create_core_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "CoreDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateCoreDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_core_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-core-definition)
        """

    def create_core_definition_version(
        self, CoreDefinitionId: str, AmznClientToken: str = None, Cores: List["CoreTypeDef"] = None
    ) -> CreateCoreDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_core_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-core-definition-version)
        """

    def create_deployment(
        self,
        DeploymentType: DeploymentType,
        GroupId: str,
        AmznClientToken: str = None,
        DeploymentId: str = None,
        GroupVersionId: str = None,
    ) -> CreateDeploymentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-deployment)
        """

    def create_device_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "DeviceDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDeviceDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_device_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-device-definition)
        """

    def create_device_definition_version(
        self,
        DeviceDefinitionId: str,
        AmznClientToken: str = None,
        Devices: List["DeviceTypeDef"] = None,
    ) -> CreateDeviceDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_device_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-device-definition-version)
        """

    def create_function_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "FunctionDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateFunctionDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_function_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-function-definition)
        """

    def create_function_definition_version(
        self,
        FunctionDefinitionId: str,
        AmznClientToken: str = None,
        DefaultConfig: "FunctionDefaultConfigTypeDef" = None,
        Functions: List["FunctionTypeDef"] = None,
    ) -> CreateFunctionDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_function_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-function-definition-version)
        """

    def create_group(
        self,
        Name: str,
        AmznClientToken: str = None,
        InitialVersion: "GroupVersionTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-group)
        """

    def create_group_certificate_authority(
        self, GroupId: str, AmznClientToken: str = None
    ) -> CreateGroupCertificateAuthorityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_group_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-group-certificate-authority)
        """

    def create_group_version(
        self,
        GroupId: str,
        AmznClientToken: str = None,
        ConnectorDefinitionVersionArn: str = None,
        CoreDefinitionVersionArn: str = None,
        DeviceDefinitionVersionArn: str = None,
        FunctionDefinitionVersionArn: str = None,
        LoggerDefinitionVersionArn: str = None,
        ResourceDefinitionVersionArn: str = None,
        SubscriptionDefinitionVersionArn: str = None,
    ) -> CreateGroupVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_group_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-group-version)
        """

    def create_logger_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "LoggerDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateLoggerDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_logger_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-logger-definition)
        """

    def create_logger_definition_version(
        self,
        LoggerDefinitionId: str,
        AmznClientToken: str = None,
        Loggers: List["LoggerTypeDef"] = None,
    ) -> CreateLoggerDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_logger_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-logger-definition-version)
        """

    def create_resource_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "ResourceDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateResourceDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_resource_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-resource-definition)
        """

    def create_resource_definition_version(
        self,
        ResourceDefinitionId: str,
        AmznClientToken: str = None,
        Resources: List["ResourceTypeDef"] = None,
    ) -> CreateResourceDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_resource_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-resource-definition-version)
        """

    def create_software_update_job(
        self,
        S3UrlSignerRole: str,
        SoftwareToUpdate: SoftwareToUpdate,
        UpdateTargets: List[str],
        UpdateTargetsArchitecture: UpdateTargetsArchitecture,
        UpdateTargetsOperatingSystem: UpdateTargetsOperatingSystem,
        AmznClientToken: str = None,
        UpdateAgentLogLevel: UpdateAgentLogLevel = None,
    ) -> CreateSoftwareUpdateJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_software_update_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-software-update-job)
        """

    def create_subscription_definition(
        self,
        AmznClientToken: str = None,
        InitialVersion: "SubscriptionDefinitionVersionTypeDef" = None,
        Name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSubscriptionDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-subscription-definition)
        """

    def create_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        AmznClientToken: str = None,
        Subscriptions: List["SubscriptionTypeDef"] = None,
    ) -> CreateSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.create_subscription_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#create-subscription-definition-version)
        """

    def delete_connector_definition(self, ConnectorDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_connector_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-connector-definition)
        """

    def delete_core_definition(self, CoreDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_core_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-core-definition)
        """

    def delete_device_definition(self, DeviceDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_device_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-device-definition)
        """

    def delete_function_definition(self, FunctionDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_function_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-function-definition)
        """

    def delete_group(self, GroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-group)
        """

    def delete_logger_definition(self, LoggerDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_logger_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-logger-definition)
        """

    def delete_resource_definition(self, ResourceDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_resource_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-resource-definition)
        """

    def delete_subscription_definition(self, SubscriptionDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.delete_subscription_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#delete-subscription-definition)
        """

    def disassociate_role_from_group(
        self, GroupId: str
    ) -> DisassociateRoleFromGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.disassociate_role_from_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#disassociate-role-from-group)
        """

    def disassociate_service_role_from_account(
        self,
    ) -> DisassociateServiceRoleFromAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.disassociate_service_role_from_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#disassociate-service-role-from-account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#generate-presigned-url)
        """

    def get_associated_role(self, GroupId: str) -> GetAssociatedRoleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_associated_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-associated-role)
        """

    def get_bulk_deployment_status(
        self, BulkDeploymentId: str
    ) -> GetBulkDeploymentStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_bulk_deployment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-bulk-deployment-status)
        """

    def get_connectivity_info(self, ThingName: str) -> GetConnectivityInfoResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_connectivity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-connectivity-info)
        """

    def get_connector_definition(
        self, ConnectorDefinitionId: str
    ) -> GetConnectorDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_connector_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-connector-definition)
        """

    def get_connector_definition_version(
        self, ConnectorDefinitionId: str, ConnectorDefinitionVersionId: str, NextToken: str = None
    ) -> GetConnectorDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_connector_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-connector-definition-version)
        """

    def get_core_definition(self, CoreDefinitionId: str) -> GetCoreDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_core_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-core-definition)
        """

    def get_core_definition_version(
        self, CoreDefinitionId: str, CoreDefinitionVersionId: str
    ) -> GetCoreDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_core_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-core-definition-version)
        """

    def get_deployment_status(
        self, DeploymentId: str, GroupId: str
    ) -> GetDeploymentStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_deployment_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-deployment-status)
        """

    def get_device_definition(self, DeviceDefinitionId: str) -> GetDeviceDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_device_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-device-definition)
        """

    def get_device_definition_version(
        self, DeviceDefinitionId: str, DeviceDefinitionVersionId: str, NextToken: str = None
    ) -> GetDeviceDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_device_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-device-definition-version)
        """

    def get_function_definition(
        self, FunctionDefinitionId: str
    ) -> GetFunctionDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_function_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-function-definition)
        """

    def get_function_definition_version(
        self, FunctionDefinitionId: str, FunctionDefinitionVersionId: str, NextToken: str = None
    ) -> GetFunctionDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_function_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-function-definition-version)
        """

    def get_group(self, GroupId: str) -> GetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-group)
        """

    def get_group_certificate_authority(
        self, CertificateAuthorityId: str, GroupId: str
    ) -> GetGroupCertificateAuthorityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_authority)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-group-certificate-authority)
        """

    def get_group_certificate_configuration(
        self, GroupId: str
    ) -> GetGroupCertificateConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_group_certificate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-group-certificate-configuration)
        """

    def get_group_version(
        self, GroupId: str, GroupVersionId: str
    ) -> GetGroupVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_group_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-group-version)
        """

    def get_logger_definition(self, LoggerDefinitionId: str) -> GetLoggerDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_logger_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-logger-definition)
        """

    def get_logger_definition_version(
        self, LoggerDefinitionId: str, LoggerDefinitionVersionId: str, NextToken: str = None
    ) -> GetLoggerDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_logger_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-logger-definition-version)
        """

    def get_resource_definition(
        self, ResourceDefinitionId: str
    ) -> GetResourceDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_resource_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-resource-definition)
        """

    def get_resource_definition_version(
        self, ResourceDefinitionId: str, ResourceDefinitionVersionId: str
    ) -> GetResourceDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_resource_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-resource-definition-version)
        """

    def get_service_role_for_account(self) -> GetServiceRoleForAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_service_role_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-service-role-for-account)
        """

    def get_subscription_definition(
        self, SubscriptionDefinitionId: str
    ) -> GetSubscriptionDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-subscription-definition)
        """

    def get_subscription_definition_version(
        self,
        SubscriptionDefinitionId: str,
        SubscriptionDefinitionVersionId: str,
        NextToken: str = None,
    ) -> GetSubscriptionDefinitionVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_subscription_definition_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-subscription-definition-version)
        """

    def get_thing_runtime_configuration(
        self, ThingName: str
    ) -> GetThingRuntimeConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.get_thing_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#get-thing-runtime-configuration)
        """

    def list_bulk_deployment_detailed_reports(
        self, BulkDeploymentId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentDetailedReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployment_detailed_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-bulk-deployment-detailed-reports)
        """

    def list_bulk_deployments(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListBulkDeploymentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_bulk_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-bulk-deployments)
        """

    def list_connector_definition_versions(
        self, ConnectorDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_connector_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-connector-definition-versions)
        """

    def list_connector_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListConnectorDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_connector_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-connector-definitions)
        """

    def list_core_definition_versions(
        self, CoreDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_core_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-core-definition-versions)
        """

    def list_core_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListCoreDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_core_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-core-definitions)
        """

    def list_deployments(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeploymentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-deployments)
        """

    def list_device_definition_versions(
        self, DeviceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_device_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-device-definition-versions)
        """

    def list_device_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListDeviceDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_device_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-device-definitions)
        """

    def list_function_definition_versions(
        self, FunctionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_function_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-function-definition-versions)
        """

    def list_function_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListFunctionDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_function_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-function-definitions)
        """

    def list_group_certificate_authorities(
        self, GroupId: str
    ) -> ListGroupCertificateAuthoritiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_group_certificate_authorities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-group-certificate-authorities)
        """

    def list_group_versions(
        self, GroupId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_group_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-group-versions)
        """

    def list_groups(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-groups)
        """

    def list_logger_definition_versions(
        self, LoggerDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_logger_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-logger-definition-versions)
        """

    def list_logger_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListLoggerDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_logger_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-logger-definitions)
        """

    def list_resource_definition_versions(
        self, ResourceDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_resource_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-resource-definition-versions)
        """

    def list_resource_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListResourceDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_resource_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-resource-definitions)
        """

    def list_subscription_definition_versions(
        self, SubscriptionDefinitionId: str, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_subscription_definition_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-subscription-definition-versions)
        """

    def list_subscription_definitions(
        self, MaxResults: str = None, NextToken: str = None
    ) -> ListSubscriptionDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_subscription_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-subscription-definitions)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#list-tags-for-resource)
        """

    def reset_deployments(
        self, GroupId: str, AmznClientToken: str = None, Force: bool = None
    ) -> ResetDeploymentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.reset_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#reset-deployments)
        """

    def start_bulk_deployment(
        self,
        ExecutionRoleArn: str,
        InputFileUri: str,
        AmznClientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> StartBulkDeploymentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.start_bulk_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#start-bulk-deployment)
        """

    def stop_bulk_deployment(self, BulkDeploymentId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.stop_bulk_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#stop-bulk-deployment)
        """

    def tag_resource(self, ResourceArn: str, tags: Dict[str, str] = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#untag-resource)
        """

    def update_connectivity_info(
        self, ThingName: str, ConnectivityInfo: List["ConnectivityInfoTypeDef"] = None
    ) -> UpdateConnectivityInfoResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_connectivity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-connectivity-info)
        """

    def update_connector_definition(
        self, ConnectorDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_connector_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-connector-definition)
        """

    def update_core_definition(self, CoreDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_core_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-core-definition)
        """

    def update_device_definition(self, DeviceDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_device_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-device-definition)
        """

    def update_function_definition(
        self, FunctionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_function_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-function-definition)
        """

    def update_group(self, GroupId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-group)
        """

    def update_group_certificate_configuration(
        self, GroupId: str, CertificateExpiryInMilliseconds: str = None
    ) -> UpdateGroupCertificateConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_group_certificate_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-group-certificate-configuration)
        """

    def update_logger_definition(self, LoggerDefinitionId: str, Name: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_logger_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-logger-definition)
        """

    def update_resource_definition(
        self, ResourceDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_resource_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-resource-definition)
        """

    def update_subscription_definition(
        self, SubscriptionDefinitionId: str, Name: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_subscription_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-subscription-definition)
        """

    def update_thing_runtime_configuration(
        self, ThingName: str, TelemetryConfiguration: TelemetryConfigurationUpdateTypeDef = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Client.update_thing_runtime_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/client.html#update-thing-runtime-configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployment_detailed_reports"]
    ) -> ListBulkDeploymentDetailedReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeploymentDetailedReports)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listbulkdeploymentdetailedreportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bulk_deployments"]
    ) -> ListBulkDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListBulkDeployments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listbulkdeploymentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_connector_definition_versions"]
    ) -> ListConnectorDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listconnectordefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_connector_definitions"]
    ) -> ListConnectorDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListConnectorDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listconnectordefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_definition_versions"]
    ) -> ListCoreDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listcoredefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_definitions"]
    ) -> ListCoreDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListCoreDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listcoredefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deployments"]
    ) -> ListDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListDeployments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listdeploymentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_definition_versions"]
    ) -> ListDeviceDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listdevicedefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_definitions"]
    ) -> ListDeviceDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListDeviceDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listdevicedefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_definition_versions"]
    ) -> ListFunctionDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listfunctiondefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_definitions"]
    ) -> ListFunctionDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListFunctionDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listfunctiondefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_group_versions"]
    ) -> ListGroupVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListGroupVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listgroupversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logger_definition_versions"]
    ) -> ListLoggerDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listloggerdefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_logger_definitions"]
    ) -> ListLoggerDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListLoggerDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listloggerdefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_definition_versions"]
    ) -> ListResourceDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listresourcedefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_definitions"]
    ) -> ListResourceDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListResourceDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listresourcedefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_definition_versions"]
    ) -> ListSubscriptionDefinitionVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitionVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listsubscriptiondefinitionversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_definitions"]
    ) -> ListSubscriptionDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/greengrass.html#Greengrass.Paginator.ListSubscriptionDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/paginators.html#listsubscriptiondefinitionspaginator)
        """
