"""
Type annotations for ds service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ds import DirectoryServiceClient

    client: DirectoryServiceClient = boto3.client("ds")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ds.literals import (
    CertificateType,
    DirectoryEdition,
    DirectorySize,
    SelectiveAuth,
    ShareMethod,
    TrustDirection,
    TrustType,
)
from mypy_boto3_ds.paginator import (
    DescribeDirectoriesPaginator,
    DescribeDomainControllersPaginator,
    DescribeSharedDirectoriesPaginator,
    DescribeSnapshotsPaginator,
    DescribeTrustsPaginator,
    ListIpRoutesPaginator,
    ListLogSubscriptionsPaginator,
    ListSchemaExtensionsPaginator,
    ListTagsForResourcePaginator,
)
from mypy_boto3_ds.type_defs import (
    AcceptSharedDirectoryResultTypeDef,
    AttributeTypeDef,
    ClientCertAuthSettingsTypeDef,
    ConnectDirectoryResultTypeDef,
    CreateAliasResultTypeDef,
    CreateComputerResultTypeDef,
    CreateDirectoryResultTypeDef,
    CreateMicrosoftADResultTypeDef,
    CreateSnapshotResultTypeDef,
    CreateTrustResultTypeDef,
    DeleteDirectoryResultTypeDef,
    DeleteSnapshotResultTypeDef,
    DeleteTrustResultTypeDef,
    DescribeCertificateResultTypeDef,
    DescribeConditionalForwardersResultTypeDef,
    DescribeDirectoriesResultTypeDef,
    DescribeDomainControllersResultTypeDef,
    DescribeEventTopicsResultTypeDef,
    DescribeLDAPSSettingsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeSharedDirectoriesResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeTrustsResultTypeDef,
    DirectoryConnectSettingsTypeDef,
    DirectoryVpcSettingsTypeDef,
    GetDirectoryLimitsResultTypeDef,
    GetSnapshotLimitsResultTypeDef,
    IpRouteTypeDef,
    ListCertificatesResultTypeDef,
    ListIpRoutesResultTypeDef,
    ListLogSubscriptionsResultTypeDef,
    ListSchemaExtensionsResultTypeDef,
    ListTagsForResourceResultTypeDef,
    RadiusSettingsTypeDef,
    RegisterCertificateResultTypeDef,
    RejectSharedDirectoryResultTypeDef,
    ShareDirectoryResultTypeDef,
    ShareTargetTypeDef,
    StartSchemaExtensionResultTypeDef,
    TagTypeDef,
    UnshareDirectoryResultTypeDef,
    UnshareTargetTypeDef,
    UpdateTrustResultTypeDef,
    VerifyTrustResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectoryServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AuthenticationFailedException: Type[BotocoreClientError]
    CertificateAlreadyExistsException: Type[BotocoreClientError]
    CertificateDoesNotExistException: Type[BotocoreClientError]
    CertificateInUseException: Type[BotocoreClientError]
    CertificateLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    DirectoryAlreadyInRegionException: Type[BotocoreClientError]
    DirectoryAlreadySharedException: Type[BotocoreClientError]
    DirectoryDoesNotExistException: Type[BotocoreClientError]
    DirectoryLimitExceededException: Type[BotocoreClientError]
    DirectoryNotSharedException: Type[BotocoreClientError]
    DirectoryUnavailableException: Type[BotocoreClientError]
    DomainControllerLimitExceededException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityDoesNotExistException: Type[BotocoreClientError]
    InsufficientPermissionsException: Type[BotocoreClientError]
    InvalidCertificateException: Type[BotocoreClientError]
    InvalidClientAuthStatusException: Type[BotocoreClientError]
    InvalidLDAPSStatusException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidTargetException: Type[BotocoreClientError]
    IpRouteLimitExceededException: Type[BotocoreClientError]
    NoAvailableCertificateException: Type[BotocoreClientError]
    OrganizationsException: Type[BotocoreClientError]
    RegionLimitExceededException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ShareLimitExceededException: Type[BotocoreClientError]
    SnapshotLimitExceededException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UserDoesNotExistException: Type[BotocoreClientError]


class DirectoryServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_shared_directory(self, SharedDirectoryId: str) -> AcceptSharedDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.accept_shared_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#accept-shared-directory)
        """

    def add_ip_routes(
        self,
        DirectoryId: str,
        IpRoutes: List[IpRouteTypeDef],
        UpdateSecurityGroupForDirectoryControllers: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.add_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add-ip-routes)
        """

    def add_region(
        self, DirectoryId: str, RegionName: str, VPCSettings: "DirectoryVpcSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.add_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add-region)
        """

    def add_tags_to_resource(self, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#add-tags-to-resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#can-paginate)
        """

    def cancel_schema_extension(self, DirectoryId: str, SchemaExtensionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.cancel_schema_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#cancel-schema-extension)
        """

    def connect_directory(
        self,
        Name: str,
        Password: str,
        Size: DirectorySize,
        ConnectSettings: DirectoryConnectSettingsTypeDef,
        ShortName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ConnectDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.connect_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#connect-directory)
        """

    def create_alias(self, DirectoryId: str, Alias: str) -> CreateAliasResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-alias)
        """

    def create_computer(
        self,
        DirectoryId: str,
        ComputerName: str,
        Password: str,
        OrganizationalUnitDistinguishedName: str = None,
        ComputerAttributes: List["AttributeTypeDef"] = None,
    ) -> CreateComputerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_computer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-computer)
        """

    def create_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-conditional-forwarder)
        """

    def create_directory(
        self,
        Name: str,
        Password: str,
        Size: DirectorySize,
        ShortName: str = None,
        Description: str = None,
        VpcSettings: "DirectoryVpcSettingsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-directory)
        """

    def create_log_subscription(self, DirectoryId: str, LogGroupName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-log-subscription)
        """

    def create_microsoft_ad(
        self,
        Name: str,
        Password: str,
        VpcSettings: "DirectoryVpcSettingsTypeDef",
        ShortName: str = None,
        Description: str = None,
        Edition: DirectoryEdition = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMicrosoftADResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_microsoft_ad)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-microsoft-ad)
        """

    def create_snapshot(self, DirectoryId: str, Name: str = None) -> CreateSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-snapshot)
        """

    def create_trust(
        self,
        DirectoryId: str,
        RemoteDomainName: str,
        TrustPassword: str,
        TrustDirection: TrustDirection,
        TrustType: TrustType = None,
        ConditionalForwarderIpAddrs: List[str] = None,
        SelectiveAuth: SelectiveAuth = None,
    ) -> CreateTrustResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.create_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#create-trust)
        """

    def delete_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.delete_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete-conditional-forwarder)
        """

    def delete_directory(self, DirectoryId: str) -> DeleteDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.delete_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete-directory)
        """

    def delete_log_subscription(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.delete_log_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete-log-subscription)
        """

    def delete_snapshot(self, SnapshotId: str) -> DeleteSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete-snapshot)
        """

    def delete_trust(
        self, TrustId: str, DeleteAssociatedConditionalForwarder: bool = None
    ) -> DeleteTrustResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.delete_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#delete-trust)
        """

    def deregister_certificate(self, DirectoryId: str, CertificateId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.deregister_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#deregister-certificate)
        """

    def deregister_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.deregister_event_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#deregister-event-topic)
        """

    def describe_certificate(
        self, DirectoryId: str, CertificateId: str
    ) -> DescribeCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-certificate)
        """

    def describe_conditional_forwarders(
        self, DirectoryId: str, RemoteDomainNames: List[str] = None
    ) -> DescribeConditionalForwardersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_conditional_forwarders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-conditional-forwarders)
        """

    def describe_directories(
        self, DirectoryIds: List[str] = None, NextToken: str = None, Limit: int = None
    ) -> DescribeDirectoriesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-directories)
        """

    def describe_domain_controllers(
        self,
        DirectoryId: str,
        DomainControllerIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeDomainControllersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_domain_controllers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-domain-controllers)
        """

    def describe_event_topics(
        self, DirectoryId: str = None, TopicNames: List[str] = None
    ) -> DescribeEventTopicsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_event_topics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-event-topics)
        """

    def describe_ldaps_settings(
        self,
        DirectoryId: str,
        Type: Literal["Client"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeLDAPSSettingsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_ldaps_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-ldaps-settings)
        """

    def describe_regions(
        self, DirectoryId: str, RegionName: str = None, NextToken: str = None
    ) -> DescribeRegionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-regions)
        """

    def describe_shared_directories(
        self,
        OwnerDirectoryId: str,
        SharedDirectoryIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSharedDirectoriesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_shared_directories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-shared-directories)
        """

    def describe_snapshots(
        self,
        DirectoryId: str = None,
        SnapshotIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-snapshots)
        """

    def describe_trusts(
        self,
        DirectoryId: str = None,
        TrustIds: List[str] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeTrustsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.describe_trusts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#describe-trusts)
        """

    def disable_client_authentication(
        self, DirectoryId: str, Type: Literal["SmartCard"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.disable_client_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable-client-authentication)
        """

    def disable_ldaps(self, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.disable_ldaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable-ldaps)
        """

    def disable_radius(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.disable_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable-radius)
        """

    def disable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.disable_sso)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#disable-sso)
        """

    def enable_client_authentication(
        self, DirectoryId: str, Type: Literal["SmartCard"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.enable_client_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable-client-authentication)
        """

    def enable_ldaps(self, DirectoryId: str, Type: Literal["Client"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.enable_ldaps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable-ldaps)
        """

    def enable_radius(
        self, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.enable_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable-radius)
        """

    def enable_sso(
        self, DirectoryId: str, UserName: str = None, Password: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.enable_sso)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#enable-sso)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#generate-presigned-url)
        """

    def get_directory_limits(self) -> GetDirectoryLimitsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.get_directory_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#get-directory-limits)
        """

    def get_snapshot_limits(self, DirectoryId: str) -> GetSnapshotLimitsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.get_snapshot_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#get-snapshot-limits)
        """

    def list_certificates(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListCertificatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.list_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list-certificates)
        """

    def list_ip_routes(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListIpRoutesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.list_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list-ip-routes)
        """

    def list_log_subscriptions(
        self, DirectoryId: str = None, NextToken: str = None, Limit: int = None
    ) -> ListLogSubscriptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.list_log_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list-log-subscriptions)
        """

    def list_schema_extensions(
        self, DirectoryId: str, NextToken: str = None, Limit: int = None
    ) -> ListSchemaExtensionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.list_schema_extensions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list-schema-extensions)
        """

    def list_tags_for_resource(
        self, ResourceId: str, NextToken: str = None, Limit: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#list-tags-for-resource)
        """

    def register_certificate(
        self,
        DirectoryId: str,
        CertificateData: str,
        Type: CertificateType = None,
        ClientCertAuthSettings: "ClientCertAuthSettingsTypeDef" = None,
    ) -> RegisterCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.register_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#register-certificate)
        """

    def register_event_topic(self, DirectoryId: str, TopicName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.register_event_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#register-event-topic)
        """

    def reject_shared_directory(self, SharedDirectoryId: str) -> RejectSharedDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.reject_shared_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#reject-shared-directory)
        """

    def remove_ip_routes(self, DirectoryId: str, CidrIps: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.remove_ip_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove-ip-routes)
        """

    def remove_region(self, DirectoryId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.remove_region)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove-region)
        """

    def remove_tags_from_resource(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#remove-tags-from-resource)
        """

    def reset_user_password(
        self, DirectoryId: str, UserName: str, NewPassword: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.reset_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#reset-user-password)
        """

    def restore_from_snapshot(self, SnapshotId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.restore_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#restore-from-snapshot)
        """

    def share_directory(
        self,
        DirectoryId: str,
        ShareTarget: ShareTargetTypeDef,
        ShareMethod: ShareMethod,
        ShareNotes: str = None,
    ) -> ShareDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.share_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#share-directory)
        """

    def start_schema_extension(
        self,
        DirectoryId: str,
        CreateSnapshotBeforeSchemaExtension: bool,
        LdifContent: str,
        Description: str,
    ) -> StartSchemaExtensionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.start_schema_extension)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#start-schema-extension)
        """

    def unshare_directory(
        self, DirectoryId: str, UnshareTarget: UnshareTargetTypeDef
    ) -> UnshareDirectoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.unshare_directory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#unshare-directory)
        """

    def update_conditional_forwarder(
        self, DirectoryId: str, RemoteDomainName: str, DnsIpAddrs: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.update_conditional_forwarder)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update-conditional-forwarder)
        """

    def update_number_of_domain_controllers(
        self, DirectoryId: str, DesiredNumber: int
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.update_number_of_domain_controllers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update-number-of-domain-controllers)
        """

    def update_radius(
        self, DirectoryId: str, RadiusSettings: "RadiusSettingsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.update_radius)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update-radius)
        """

    def update_trust(
        self, TrustId: str, SelectiveAuth: SelectiveAuth = None
    ) -> UpdateTrustResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.update_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#update-trust)
        """

    def verify_trust(self, TrustId: str) -> VerifyTrustResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Client.verify_trust)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/client.html#verify-trust)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_directories"]
    ) -> DescribeDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.DescribeDirectories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_domain_controllers"]
    ) -> DescribeDomainControllersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.DescribeDomainControllers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describedomaincontrollerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_shared_directories"]
    ) -> DescribeSharedDirectoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.DescribeSharedDirectories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describeshareddirectoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.DescribeSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describesnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_trusts"]) -> DescribeTrustsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.DescribeTrusts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#describetrustspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_routes"]) -> ListIpRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.ListIpRoutes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listiproutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_log_subscriptions"]
    ) -> ListLogSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.ListLogSubscriptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listlogsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_extensions"]
    ) -> ListSchemaExtensionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.ListSchemaExtensions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listschemaextensionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ds.html#DirectoryService.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/paginators.html#listtagsforresourcepaginator)
        """
