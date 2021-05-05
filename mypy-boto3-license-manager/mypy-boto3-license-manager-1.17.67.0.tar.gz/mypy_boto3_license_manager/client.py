"""
Type annotations for license-manager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_license_manager import LicenseManagerClient

    client: LicenseManagerClient = boto3.client("license-manager")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_license_manager.literals import (
    AllowedOperation,
    GrantStatus,
    LicenseConfigurationStatus,
    LicenseCountingType,
    LicenseStatus,
)
from mypy_boto3_license_manager.paginator import (
    ListAssociationsForLicenseConfigurationPaginator,
    ListLicenseConfigurationsPaginator,
    ListLicenseSpecificationsForResourcePaginator,
    ListResourceInventoryPaginator,
    ListUsageForLicenseConfigurationPaginator,
)
from mypy_boto3_license_manager.type_defs import (
    AcceptGrantResponseTypeDef,
    CheckoutBorrowLicenseResponseTypeDef,
    CheckoutLicenseResponseTypeDef,
    ConsumptionConfigurationTypeDef,
    CreateGrantResponseTypeDef,
    CreateGrantVersionResponseTypeDef,
    CreateLicenseConfigurationResponseTypeDef,
    CreateLicenseResponseTypeDef,
    CreateLicenseVersionResponseTypeDef,
    CreateTokenResponseTypeDef,
    DatetimeRangeTypeDef,
    DeleteGrantResponseTypeDef,
    DeleteLicenseResponseTypeDef,
    EntitlementDataTypeDef,
    EntitlementTypeDef,
    ExtendLicenseConsumptionResponseTypeDef,
    FilterTypeDef,
    GetAccessTokenResponseTypeDef,
    GetGrantResponseTypeDef,
    GetLicenseConfigurationResponseTypeDef,
    GetLicenseResponseTypeDef,
    GetLicenseUsageResponseTypeDef,
    GetServiceSettingsResponseTypeDef,
    InventoryFilterTypeDef,
    IssuerTypeDef,
    LicenseSpecificationTypeDef,
    ListAssociationsForLicenseConfigurationResponseTypeDef,
    ListDistributedGrantsResponseTypeDef,
    ListFailuresForLicenseConfigurationOperationsResponseTypeDef,
    ListLicenseConfigurationsResponseTypeDef,
    ListLicenseSpecificationsForResourceResponseTypeDef,
    ListLicensesResponseTypeDef,
    ListLicenseVersionsResponseTypeDef,
    ListReceivedGrantsResponseTypeDef,
    ListReceivedLicensesResponseTypeDef,
    ListResourceInventoryResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTokensResponseTypeDef,
    ListUsageForLicenseConfigurationResponseTypeDef,
    MetadataTypeDef,
    OrganizationConfigurationTypeDef,
    ProductInformationTypeDef,
    RejectGrantResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LicenseManagerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AuthorizationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EntitlementNotAllowedException: Type[BotocoreClientError]
    FailedDependencyException: Type[BotocoreClientError]
    FilterLimitExceededException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    LicenseUsageException: Type[BotocoreClientError]
    NoEntitlementsAllowedException: Type[BotocoreClientError]
    RateLimitExceededException: Type[BotocoreClientError]
    RedirectException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerInternalException: Type[BotocoreClientError]
    UnsupportedDigitalSignatureMethodException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LicenseManagerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_grant(self, GrantArn: str) -> AcceptGrantResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.accept_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#accept-grant)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#can-paginate)
        """

    def check_in_license(
        self, LicenseConsumptionToken: str, Beneficiary: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.check_in_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#check-in-license)
        """

    def checkout_borrow_license(
        self,
        LicenseArn: str,
        Entitlements: List["EntitlementDataTypeDef"],
        DigitalSignatureMethod: Literal["JWT_PS384"],
        ClientToken: str,
        NodeId: str = None,
        CheckoutMetadata: List["MetadataTypeDef"] = None,
    ) -> CheckoutBorrowLicenseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.checkout_borrow_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#checkout-borrow-license)
        """

    def checkout_license(
        self,
        ProductSKU: str,
        CheckoutType: Literal["PROVISIONAL"],
        KeyFingerprint: str,
        Entitlements: List["EntitlementDataTypeDef"],
        ClientToken: str,
        Beneficiary: str = None,
        NodeId: str = None,
    ) -> CheckoutLicenseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.checkout_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#checkout-license)
        """

    def create_grant(
        self,
        ClientToken: str,
        GrantName: str,
        LicenseArn: str,
        Principals: List[str],
        HomeRegion: str,
        AllowedOperations: List[AllowedOperation],
    ) -> CreateGrantResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-grant)
        """

    def create_grant_version(
        self,
        ClientToken: str,
        GrantArn: str,
        GrantName: str = None,
        AllowedOperations: List[AllowedOperation] = None,
        Status: GrantStatus = None,
        SourceVersion: str = None,
    ) -> CreateGrantVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_grant_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-grant-version)
        """

    def create_license(
        self,
        LicenseName: str,
        ProductName: str,
        ProductSKU: str,
        Issuer: IssuerTypeDef,
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        Beneficiary: str,
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None,
    ) -> CreateLicenseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-license)
        """

    def create_license_configuration(
        self,
        Name: str,
        LicenseCountingType: LicenseCountingType,
        Description: str = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        LicenseRules: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        DisassociateWhenNotFound: bool = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None,
    ) -> CreateLicenseConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-license-configuration)
        """

    def create_license_version(
        self,
        LicenseArn: str,
        LicenseName: str,
        ProductName: str,
        Issuer: IssuerTypeDef,
        HomeRegion: str,
        Validity: "DatetimeRangeTypeDef",
        Entitlements: List["EntitlementTypeDef"],
        ConsumptionConfiguration: "ConsumptionConfigurationTypeDef",
        Status: LicenseStatus,
        ClientToken: str,
        LicenseMetadata: List["MetadataTypeDef"] = None,
        SourceVersion: str = None,
    ) -> CreateLicenseVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_license_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-license-version)
        """

    def create_token(
        self,
        LicenseArn: str,
        ClientToken: str,
        RoleArns: List[str] = None,
        ExpirationInDays: int = None,
        TokenProperties: List[str] = None,
    ) -> CreateTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.create_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#create-token)
        """

    def delete_grant(self, GrantArn: str, Version: str) -> DeleteGrantResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.delete_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete-grant)
        """

    def delete_license(self, LicenseArn: str, SourceVersion: str) -> DeleteLicenseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.delete_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete-license)
        """

    def delete_license_configuration(self, LicenseConfigurationArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.delete_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete-license-configuration)
        """

    def delete_token(self, TokenId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.delete_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#delete-token)
        """

    def extend_license_consumption(
        self, LicenseConsumptionToken: str, DryRun: bool = None
    ) -> ExtendLicenseConsumptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.extend_license_consumption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#extend-license-consumption)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#generate-presigned-url)
        """

    def get_access_token(
        self, Token: str, TokenProperties: List[str] = None
    ) -> GetAccessTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_access_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-access-token)
        """

    def get_grant(self, GrantArn: str, Version: str = None) -> GetGrantResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-grant)
        """

    def get_license(self, LicenseArn: str, Version: str = None) -> GetLicenseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-license)
        """

    def get_license_configuration(
        self, LicenseConfigurationArn: str
    ) -> GetLicenseConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-license-configuration)
        """

    def get_license_usage(self, LicenseArn: str) -> GetLicenseUsageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_license_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-license-usage)
        """

    def get_service_settings(self) -> GetServiceSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.get_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#get-service-settings)
        """

    def list_associations_for_license_configuration(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationsForLicenseConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_associations_for_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-associations-for-license-configuration)
        """

    def list_distributed_grants(
        self,
        GrantArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDistributedGrantsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_distributed_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-distributed-grants)
        """

    def list_failures_for_license_configuration_operations(
        self, LicenseConfigurationArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFailuresForLicenseConfigurationOperationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_failures_for_license_configuration_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-failures-for-license-configuration-operations)
        """

    def list_license_configurations(
        self,
        LicenseConfigurationArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListLicenseConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_license_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-license-configurations)
        """

    def list_license_specifications_for_resource(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLicenseSpecificationsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_license_specifications_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-license-specifications-for-resource)
        """

    def list_license_versions(
        self, LicenseArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListLicenseVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_license_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-license-versions)
        """

    def list_licenses(
        self,
        LicenseArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListLicensesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_licenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-licenses)
        """

    def list_received_grants(
        self,
        GrantArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReceivedGrantsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_received_grants)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-received-grants)
        """

    def list_received_licenses(
        self,
        LicenseArns: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListReceivedLicensesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_received_licenses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-received-licenses)
        """

    def list_resource_inventory(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[InventoryFilterTypeDef] = None,
    ) -> ListResourceInventoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_resource_inventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-resource-inventory)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-tags-for-resource)
        """

    def list_tokens(
        self,
        TokenIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTokensResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_tokens)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-tokens)
        """

    def list_usage_for_license_configuration(
        self,
        LicenseConfigurationArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> ListUsageForLicenseConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.list_usage_for_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#list-usage-for-license-configuration)
        """

    def reject_grant(self, GrantArn: str) -> RejectGrantResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.reject_grant)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#reject-grant)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#untag-resource)
        """

    def update_license_configuration(
        self,
        LicenseConfigurationArn: str,
        LicenseConfigurationStatus: LicenseConfigurationStatus = None,
        LicenseRules: List[str] = None,
        LicenseCount: int = None,
        LicenseCountHardLimit: bool = None,
        Name: str = None,
        Description: str = None,
        ProductInformationList: List["ProductInformationTypeDef"] = None,
        DisassociateWhenNotFound: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.update_license_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update-license-configuration)
        """

    def update_license_specifications_for_resource(
        self,
        ResourceArn: str,
        AddLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
        RemoveLicenseSpecifications: List["LicenseSpecificationTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.update_license_specifications_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update-license-specifications-for-resource)
        """

    def update_service_settings(
        self,
        S3BucketArn: str = None,
        SnsTopicArn: str = None,
        OrganizationConfiguration: "OrganizationConfigurationTypeDef" = None,
        EnableCrossAccountsDiscovery: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Client.update_service_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/client.html#update-service-settings)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations_for_license_configuration"]
    ) -> ListAssociationsForLicenseConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Paginator.ListAssociationsForLicenseConfiguration)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listassociationsforlicenseconfigurationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_configurations"]
    ) -> ListLicenseConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listlicenseconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_license_specifications_for_resource"]
    ) -> ListLicenseSpecificationsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Paginator.ListLicenseSpecificationsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listlicensespecificationsforresourcepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_inventory"]
    ) -> ListResourceInventoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Paginator.ListResourceInventory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listresourceinventorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_usage_for_license_configuration"]
    ) -> ListUsageForLicenseConfigurationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/license-manager.html#LicenseManager.Paginator.ListUsageForLicenseConfiguration)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/paginators.html#listusageforlicenseconfigurationpaginator)
        """
