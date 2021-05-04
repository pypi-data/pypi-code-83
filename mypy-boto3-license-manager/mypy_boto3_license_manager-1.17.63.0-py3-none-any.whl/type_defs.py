"""
Type annotations for license-manager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AcceptGrantResponseTypeDef

    data: AcceptGrantResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_license_manager.literals import (
    AllowedOperation,
    EntitlementDataUnit,
    EntitlementUnit,
    GrantStatus,
    InventoryFilterCondition,
    LicenseCountingType,
    LicenseDeletionStatus,
    LicenseStatus,
    ReceivedStatus,
    RenewType,
    ResourceType,
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
    "AcceptGrantResponseTypeDef",
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DatetimeRangeTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseResponseTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerDetailsTypeDef",
    "IssuerTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    "ListDistributedGrantsResponseTypeDef",
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    "ListLicenseConfigurationsResponseTypeDef",
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    "ListLicenseVersionsResponseTypeDef",
    "ListLicensesResponseTypeDef",
    "ListReceivedGrantsResponseTypeDef",
    "ListReceivedLicensesResponseTypeDef",
    "ListResourceInventoryResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTokensResponseTypeDef",
    "ListUsageForLicenseConfigurationResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "RejectGrantResponseTypeDef",
    "ResourceInventoryTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
)


class AcceptGrantResponseTypeDef(TypedDict, total=False):
    GrantArn: str
    Status: GrantStatus
    Version: str


class AutomatedDiscoveryInformationTypeDef(TypedDict, total=False):
    LastRunTime: datetime


class BorrowConfigurationTypeDef(TypedDict):
    AllowEarlyCheckIn: bool
    MaxTimeToLiveInMinutes: int


class CheckoutBorrowLicenseResponseTypeDef(TypedDict, total=False):
    LicenseArn: str
    LicenseConsumptionToken: str
    EntitlementsAllowed: List["EntitlementDataTypeDef"]
    NodeId: str
    SignedToken: str
    IssuedAt: str
    Expiration: str
    CheckoutMetadata: List["MetadataTypeDef"]


class CheckoutLicenseResponseTypeDef(TypedDict, total=False):
    CheckoutType: Literal["PROVISIONAL"]
    LicenseConsumptionToken: str
    EntitlementsAllowed: List["EntitlementDataTypeDef"]
    SignedToken: str
    NodeId: str
    IssuedAt: str
    Expiration: str


class ConsumedLicenseSummaryTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    ConsumedLicenses: int


class ConsumptionConfigurationTypeDef(TypedDict, total=False):
    RenewType: RenewType
    ProvisionalConfiguration: "ProvisionalConfigurationTypeDef"
    BorrowConfiguration: "BorrowConfigurationTypeDef"


class CreateGrantResponseTypeDef(TypedDict, total=False):
    GrantArn: str
    Status: GrantStatus
    Version: str


class CreateGrantVersionResponseTypeDef(TypedDict, total=False):
    GrantArn: str
    Status: GrantStatus
    Version: str


class CreateLicenseConfigurationResponseTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class CreateLicenseResponseTypeDef(TypedDict, total=False):
    LicenseArn: str
    Status: LicenseStatus
    Version: str


class CreateLicenseVersionResponseTypeDef(TypedDict, total=False):
    LicenseArn: str
    Version: str
    Status: LicenseStatus


class CreateTokenResponseTypeDef(TypedDict, total=False):
    TokenId: str
    TokenType: Literal["REFRESH_TOKEN"]
    Token: str


class _RequiredDatetimeRangeTypeDef(TypedDict):
    Begin: str


class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, total=False):
    End: str


class DeleteGrantResponseTypeDef(TypedDict, total=False):
    GrantArn: str
    Status: GrantStatus
    Version: str


class DeleteLicenseResponseTypeDef(TypedDict, total=False):
    Status: LicenseDeletionStatus
    DeletionDate: str


class _RequiredEntitlementDataTypeDef(TypedDict):
    Name: str
    Unit: EntitlementDataUnit


class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, total=False):
    Value: str


class _RequiredEntitlementTypeDef(TypedDict):
    Name: str
    Unit: EntitlementUnit


class EntitlementTypeDef(_RequiredEntitlementTypeDef, total=False):
    Value: str
    MaxCount: int
    Overage: bool
    AllowCheckIn: bool


class _RequiredEntitlementUsageTypeDef(TypedDict):
    Name: str
    ConsumedValue: str
    Unit: EntitlementDataUnit


class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, total=False):
    MaxCount: str


class ExtendLicenseConsumptionResponseTypeDef(TypedDict, total=False):
    LicenseConsumptionToken: str
    Expiration: str


class FilterTypeDef(TypedDict, total=False):
    Name: str
    Values: List[str]


class GetAccessTokenResponseTypeDef(TypedDict, total=False):
    AccessToken: str


class GetGrantResponseTypeDef(TypedDict, total=False):
    Grant: "GrantTypeDef"


class GetLicenseConfigurationResponseTypeDef(TypedDict, total=False):
    LicenseConfigurationId: str
    LicenseConfigurationArn: str
    Name: str
    Description: str
    LicenseCountingType: LicenseCountingType
    LicenseRules: List[str]
    LicenseCount: int
    LicenseCountHardLimit: bool
    ConsumedLicenses: int
    Status: str
    OwnerAccountId: str
    ConsumedLicenseSummaryList: List["ConsumedLicenseSummaryTypeDef"]
    ManagedResourceSummaryList: List["ManagedResourceSummaryTypeDef"]
    Tags: List["TagTypeDef"]
    ProductInformationList: List["ProductInformationTypeDef"]
    AutomatedDiscoveryInformation: "AutomatedDiscoveryInformationTypeDef"
    DisassociateWhenNotFound: bool


class GetLicenseResponseTypeDef(TypedDict, total=False):
    License: "LicenseTypeDef"


class GetLicenseUsageResponseTypeDef(TypedDict, total=False):
    LicenseUsage: "LicenseUsageTypeDef"


class GetServiceSettingsResponseTypeDef(TypedDict, total=False):
    S3BucketArn: str
    SnsTopicArn: str
    OrganizationConfiguration: "OrganizationConfigurationTypeDef"
    EnableCrossAccountsDiscovery: bool
    LicenseManagerResourceShareArn: str


class _RequiredGrantTypeDef(TypedDict):
    GrantArn: str
    GrantName: str
    ParentArn: str
    LicenseArn: str
    GranteePrincipalArn: str
    HomeRegion: str
    GrantStatus: GrantStatus
    Version: str
    GrantedOperations: List[AllowedOperation]


class GrantTypeDef(_RequiredGrantTypeDef, total=False):
    StatusReason: str


class GrantedLicenseTypeDef(TypedDict, total=False):
    LicenseArn: str
    LicenseName: str
    ProductName: str
    ProductSKU: str
    Issuer: "IssuerDetailsTypeDef"
    HomeRegion: str
    Status: LicenseStatus
    Validity: "DatetimeRangeTypeDef"
    Beneficiary: str
    Entitlements: List["EntitlementTypeDef"]
    ConsumptionConfiguration: "ConsumptionConfigurationTypeDef"
    LicenseMetadata: List["MetadataTypeDef"]
    CreateTime: str
    Version: str
    ReceivedMetadata: "ReceivedMetadataTypeDef"


class _RequiredInventoryFilterTypeDef(TypedDict):
    Name: str
    Condition: InventoryFilterCondition


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, total=False):
    Value: str


class IssuerDetailsTypeDef(TypedDict, total=False):
    Name: str
    SignKey: str
    KeyFingerprint: str


class _RequiredIssuerTypeDef(TypedDict):
    Name: str


class IssuerTypeDef(_RequiredIssuerTypeDef, total=False):
    SignKey: str


class LicenseConfigurationAssociationTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceType: ResourceType
    ResourceOwnerId: str
    AssociationTime: datetime
    AmiAssociationScope: str


class LicenseConfigurationTypeDef(TypedDict, total=False):
    LicenseConfigurationId: str
    LicenseConfigurationArn: str
    Name: str
    Description: str
    LicenseCountingType: LicenseCountingType
    LicenseRules: List[str]
    LicenseCount: int
    LicenseCountHardLimit: bool
    DisassociateWhenNotFound: bool
    ConsumedLicenses: int
    Status: str
    OwnerAccountId: str
    ConsumedLicenseSummaryList: List["ConsumedLicenseSummaryTypeDef"]
    ManagedResourceSummaryList: List["ManagedResourceSummaryTypeDef"]
    ProductInformationList: List["ProductInformationTypeDef"]
    AutomatedDiscoveryInformation: "AutomatedDiscoveryInformationTypeDef"


class LicenseConfigurationUsageTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceType: ResourceType
    ResourceStatus: str
    ResourceOwnerId: str
    AssociationTime: datetime
    ConsumedLicenses: int


class LicenseOperationFailureTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceType: ResourceType
    ErrorMessage: str
    FailureTime: datetime
    OperationName: str
    ResourceOwnerId: str
    OperationRequestedBy: str
    MetadataList: List["MetadataTypeDef"]


class _RequiredLicenseSpecificationTypeDef(TypedDict):
    LicenseConfigurationArn: str


class LicenseSpecificationTypeDef(_RequiredLicenseSpecificationTypeDef, total=False):
    AmiAssociationScope: str


class LicenseTypeDef(TypedDict, total=False):
    LicenseArn: str
    LicenseName: str
    ProductName: str
    ProductSKU: str
    Issuer: "IssuerDetailsTypeDef"
    HomeRegion: str
    Status: LicenseStatus
    Validity: "DatetimeRangeTypeDef"
    Beneficiary: str
    Entitlements: List["EntitlementTypeDef"]
    ConsumptionConfiguration: "ConsumptionConfigurationTypeDef"
    LicenseMetadata: List["MetadataTypeDef"]
    CreateTime: str
    Version: str


class LicenseUsageTypeDef(TypedDict, total=False):
    EntitlementUsages: List["EntitlementUsageTypeDef"]


class ListAssociationsForLicenseConfigurationResponseTypeDef(TypedDict, total=False):
    LicenseConfigurationAssociations: List["LicenseConfigurationAssociationTypeDef"]
    NextToken: str


class ListDistributedGrantsResponseTypeDef(TypedDict, total=False):
    Grants: List["GrantTypeDef"]
    NextToken: str


class ListFailuresForLicenseConfigurationOperationsResponseTypeDef(TypedDict, total=False):
    LicenseOperationFailureList: List["LicenseOperationFailureTypeDef"]
    NextToken: str


class ListLicenseConfigurationsResponseTypeDef(TypedDict, total=False):
    LicenseConfigurations: List["LicenseConfigurationTypeDef"]
    NextToken: str


class ListLicenseSpecificationsForResourceResponseTypeDef(TypedDict, total=False):
    LicenseSpecifications: List["LicenseSpecificationTypeDef"]
    NextToken: str


class ListLicenseVersionsResponseTypeDef(TypedDict, total=False):
    Licenses: List["LicenseTypeDef"]
    NextToken: str


class ListLicensesResponseTypeDef(TypedDict, total=False):
    Licenses: List["LicenseTypeDef"]
    NextToken: str


class ListReceivedGrantsResponseTypeDef(TypedDict, total=False):
    Grants: List["GrantTypeDef"]
    NextToken: str


class ListReceivedLicensesResponseTypeDef(TypedDict, total=False):
    Licenses: List["GrantedLicenseTypeDef"]
    NextToken: str


class ListResourceInventoryResponseTypeDef(TypedDict, total=False):
    ResourceInventoryList: List["ResourceInventoryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListTokensResponseTypeDef(TypedDict, total=False):
    Tokens: List["TokenDataTypeDef"]
    NextToken: str


class ListUsageForLicenseConfigurationResponseTypeDef(TypedDict, total=False):
    LicenseConfigurationUsageList: List["LicenseConfigurationUsageTypeDef"]
    NextToken: str


class ManagedResourceSummaryTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    AssociationCount: int


class MetadataTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class OrganizationConfigurationTypeDef(TypedDict):
    EnableIntegration: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredProductInformationFilterTypeDef(TypedDict):
    ProductInformationFilterName: str
    ProductInformationFilterComparator: str


class ProductInformationFilterTypeDef(_RequiredProductInformationFilterTypeDef, total=False):
    ProductInformationFilterValue: List[str]


class ProductInformationTypeDef(TypedDict):
    ResourceType: str
    ProductInformationFilterList: List["ProductInformationFilterTypeDef"]


class ProvisionalConfigurationTypeDef(TypedDict):
    MaxTimeToLiveInMinutes: int


class ReceivedMetadataTypeDef(TypedDict, total=False):
    ReceivedStatus: ReceivedStatus
    AllowedOperations: List[AllowedOperation]


class RejectGrantResponseTypeDef(TypedDict, total=False):
    GrantArn: str
    Status: GrantStatus
    Version: str


class ResourceInventoryTypeDef(TypedDict, total=False):
    ResourceId: str
    ResourceType: ResourceType
    ResourceArn: str
    Platform: str
    PlatformVersion: str
    ResourceOwningAccountId: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TokenDataTypeDef(TypedDict, total=False):
    TokenId: str
    TokenType: str
    LicenseArn: str
    ExpirationTime: str
    TokenProperties: List[str]
    RoleArns: List[str]
    Status: str
