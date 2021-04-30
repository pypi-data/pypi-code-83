"""
Main interface for license-manager service type definitions.

Usage::

    ```python
    from mypy_boto3_license_manager.type_defs import AutomatedDiscoveryInformationTypeDef

    data: AutomatedDiscoveryInformationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_license_manager.literals import (
    AllowedOperation,
    CheckoutType,
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
    TokenType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AutomatedDiscoveryInformationTypeDef",
    "BorrowConfigurationTypeDef",
    "ConsumedLicenseSummaryTypeDef",
    "ConsumptionConfigurationTypeDef",
    "DatetimeRangeTypeDef",
    "EntitlementDataTypeDef",
    "EntitlementTypeDef",
    "EntitlementUsageTypeDef",
    "GrantTypeDef",
    "GrantedLicenseTypeDef",
    "IssuerDetailsTypeDef",
    "LicenseConfigurationAssociationTypeDef",
    "LicenseConfigurationTypeDef",
    "LicenseConfigurationUsageTypeDef",
    "LicenseOperationFailureTypeDef",
    "LicenseSpecificationTypeDef",
    "LicenseTypeDef",
    "LicenseUsageTypeDef",
    "ManagedResourceSummaryTypeDef",
    "MetadataTypeDef",
    "OrganizationConfigurationTypeDef",
    "ProductInformationFilterTypeDef",
    "ProductInformationTypeDef",
    "ProvisionalConfigurationTypeDef",
    "ReceivedMetadataTypeDef",
    "ResourceInventoryTypeDef",
    "TagTypeDef",
    "TokenDataTypeDef",
    "AcceptGrantResponseTypeDef",
    "CheckoutBorrowLicenseResponseTypeDef",
    "CheckoutLicenseResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateGrantVersionResponseTypeDef",
    "CreateLicenseConfigurationResponseTypeDef",
    "CreateLicenseResponseTypeDef",
    "CreateLicenseVersionResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteGrantResponseTypeDef",
    "DeleteLicenseResponseTypeDef",
    "ExtendLicenseConsumptionResponseTypeDef",
    "FilterTypeDef",
    "GetAccessTokenResponseTypeDef",
    "GetGrantResponseTypeDef",
    "GetLicenseConfigurationResponseTypeDef",
    "GetLicenseResponseTypeDef",
    "GetLicenseUsageResponseTypeDef",
    "GetServiceSettingsResponseTypeDef",
    "InventoryFilterTypeDef",
    "IssuerTypeDef",
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
    "PaginatorConfigTypeDef",
    "RejectGrantResponseTypeDef",
)

AutomatedDiscoveryInformationTypeDef = TypedDict(
    "AutomatedDiscoveryInformationTypeDef", {"LastRunTime": datetime}, total=False
)

BorrowConfigurationTypeDef = TypedDict(
    "BorrowConfigurationTypeDef", {"AllowEarlyCheckIn": bool, "MaxTimeToLiveInMinutes": int}
)

ConsumedLicenseSummaryTypeDef = TypedDict(
    "ConsumedLicenseSummaryTypeDef",
    {"ResourceType": ResourceType, "ConsumedLicenses": int},
    total=False,
)

ConsumptionConfigurationTypeDef = TypedDict(
    "ConsumptionConfigurationTypeDef",
    {
        "RenewType": RenewType,
        "ProvisionalConfiguration": "ProvisionalConfigurationTypeDef",
        "BorrowConfiguration": "BorrowConfigurationTypeDef",
    },
    total=False,
)

_RequiredDatetimeRangeTypeDef = TypedDict("_RequiredDatetimeRangeTypeDef", {"Begin": str})
_OptionalDatetimeRangeTypeDef = TypedDict(
    "_OptionalDatetimeRangeTypeDef", {"End": str}, total=False
)


class DatetimeRangeTypeDef(_RequiredDatetimeRangeTypeDef, _OptionalDatetimeRangeTypeDef):
    pass


_RequiredEntitlementDataTypeDef = TypedDict(
    "_RequiredEntitlementDataTypeDef", {"Name": str, "Unit": EntitlementDataUnit}
)
_OptionalEntitlementDataTypeDef = TypedDict(
    "_OptionalEntitlementDataTypeDef", {"Value": str}, total=False
)


class EntitlementDataTypeDef(_RequiredEntitlementDataTypeDef, _OptionalEntitlementDataTypeDef):
    pass


_RequiredEntitlementTypeDef = TypedDict(
    "_RequiredEntitlementTypeDef", {"Name": str, "Unit": EntitlementUnit}
)
_OptionalEntitlementTypeDef = TypedDict(
    "_OptionalEntitlementTypeDef",
    {"Value": str, "MaxCount": int, "Overage": bool, "AllowCheckIn": bool},
    total=False,
)


class EntitlementTypeDef(_RequiredEntitlementTypeDef, _OptionalEntitlementTypeDef):
    pass


_RequiredEntitlementUsageTypeDef = TypedDict(
    "_RequiredEntitlementUsageTypeDef",
    {"Name": str, "ConsumedValue": str, "Unit": EntitlementDataUnit},
)
_OptionalEntitlementUsageTypeDef = TypedDict(
    "_OptionalEntitlementUsageTypeDef", {"MaxCount": str}, total=False
)


class EntitlementUsageTypeDef(_RequiredEntitlementUsageTypeDef, _OptionalEntitlementUsageTypeDef):
    pass


_RequiredGrantTypeDef = TypedDict(
    "_RequiredGrantTypeDef",
    {
        "GrantArn": str,
        "GrantName": str,
        "ParentArn": str,
        "LicenseArn": str,
        "GranteePrincipalArn": str,
        "HomeRegion": str,
        "GrantStatus": GrantStatus,
        "Version": str,
        "GrantedOperations": List[AllowedOperation],
    },
)
_OptionalGrantTypeDef = TypedDict("_OptionalGrantTypeDef", {"StatusReason": str}, total=False)


class GrantTypeDef(_RequiredGrantTypeDef, _OptionalGrantTypeDef):
    pass


GrantedLicenseTypeDef = TypedDict(
    "GrantedLicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": LicenseStatus,
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
        "ReceivedMetadata": "ReceivedMetadataTypeDef",
    },
    total=False,
)

IssuerDetailsTypeDef = TypedDict(
    "IssuerDetailsTypeDef", {"Name": str, "SignKey": str, "KeyFingerprint": str}, total=False
)

LicenseConfigurationAssociationTypeDef = TypedDict(
    "LicenseConfigurationAssociationTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceType,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "AmiAssociationScope": str,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "DisassociateWhenNotFound": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
    },
    total=False,
)

LicenseConfigurationUsageTypeDef = TypedDict(
    "LicenseConfigurationUsageTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceType,
        "ResourceStatus": str,
        "ResourceOwnerId": str,
        "AssociationTime": datetime,
        "ConsumedLicenses": int,
    },
    total=False,
)

LicenseOperationFailureTypeDef = TypedDict(
    "LicenseOperationFailureTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": ResourceType,
        "ErrorMessage": str,
        "FailureTime": datetime,
        "OperationName": str,
        "ResourceOwnerId": str,
        "OperationRequestedBy": str,
        "MetadataList": List["MetadataTypeDef"],
    },
    total=False,
)

_RequiredLicenseSpecificationTypeDef = TypedDict(
    "_RequiredLicenseSpecificationTypeDef", {"LicenseConfigurationArn": str}
)
_OptionalLicenseSpecificationTypeDef = TypedDict(
    "_OptionalLicenseSpecificationTypeDef", {"AmiAssociationScope": str}, total=False
)


class LicenseSpecificationTypeDef(
    _RequiredLicenseSpecificationTypeDef, _OptionalLicenseSpecificationTypeDef
):
    pass


LicenseTypeDef = TypedDict(
    "LicenseTypeDef",
    {
        "LicenseArn": str,
        "LicenseName": str,
        "ProductName": str,
        "ProductSKU": str,
        "Issuer": "IssuerDetailsTypeDef",
        "HomeRegion": str,
        "Status": LicenseStatus,
        "Validity": "DatetimeRangeTypeDef",
        "Beneficiary": str,
        "Entitlements": List["EntitlementTypeDef"],
        "ConsumptionConfiguration": "ConsumptionConfigurationTypeDef",
        "LicenseMetadata": List["MetadataTypeDef"],
        "CreateTime": str,
        "Version": str,
    },
    total=False,
)

LicenseUsageTypeDef = TypedDict(
    "LicenseUsageTypeDef", {"EntitlementUsages": List["EntitlementUsageTypeDef"]}, total=False
)

ManagedResourceSummaryTypeDef = TypedDict(
    "ManagedResourceSummaryTypeDef",
    {"ResourceType": ResourceType, "AssociationCount": int},
    total=False,
)

MetadataTypeDef = TypedDict("MetadataTypeDef", {"Name": str, "Value": str}, total=False)

OrganizationConfigurationTypeDef = TypedDict(
    "OrganizationConfigurationTypeDef", {"EnableIntegration": bool}
)

_RequiredProductInformationFilterTypeDef = TypedDict(
    "_RequiredProductInformationFilterTypeDef",
    {"ProductInformationFilterName": str, "ProductInformationFilterComparator": str},
)
_OptionalProductInformationFilterTypeDef = TypedDict(
    "_OptionalProductInformationFilterTypeDef",
    {"ProductInformationFilterValue": List[str]},
    total=False,
)


class ProductInformationFilterTypeDef(
    _RequiredProductInformationFilterTypeDef, _OptionalProductInformationFilterTypeDef
):
    pass


ProductInformationTypeDef = TypedDict(
    "ProductInformationTypeDef",
    {"ResourceType": str, "ProductInformationFilterList": List["ProductInformationFilterTypeDef"]},
)

ProvisionalConfigurationTypeDef = TypedDict(
    "ProvisionalConfigurationTypeDef", {"MaxTimeToLiveInMinutes": int}
)

ReceivedMetadataTypeDef = TypedDict(
    "ReceivedMetadataTypeDef",
    {"ReceivedStatus": ReceivedStatus, "AllowedOperations": List[AllowedOperation]},
    total=False,
)

ResourceInventoryTypeDef = TypedDict(
    "ResourceInventoryTypeDef",
    {
        "ResourceId": str,
        "ResourceType": ResourceType,
        "ResourceArn": str,
        "Platform": str,
        "PlatformVersion": str,
        "ResourceOwningAccountId": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

TokenDataTypeDef = TypedDict(
    "TokenDataTypeDef",
    {
        "TokenId": str,
        "TokenType": str,
        "LicenseArn": str,
        "ExpirationTime": str,
        "TokenProperties": List[str],
        "RoleArns": List[str],
        "Status": str,
    },
    total=False,
)

AcceptGrantResponseTypeDef = TypedDict(
    "AcceptGrantResponseTypeDef",
    {"GrantArn": str, "Status": GrantStatus, "Version": str},
    total=False,
)

CheckoutBorrowLicenseResponseTypeDef = TypedDict(
    "CheckoutBorrowLicenseResponseTypeDef",
    {
        "LicenseArn": str,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "NodeId": str,
        "SignedToken": str,
        "IssuedAt": str,
        "Expiration": str,
        "CheckoutMetadata": List["MetadataTypeDef"],
    },
    total=False,
)

CheckoutLicenseResponseTypeDef = TypedDict(
    "CheckoutLicenseResponseTypeDef",
    {
        "CheckoutType": CheckoutType,
        "LicenseConsumptionToken": str,
        "EntitlementsAllowed": List["EntitlementDataTypeDef"],
        "SignedToken": str,
        "NodeId": str,
        "IssuedAt": str,
        "Expiration": str,
    },
    total=False,
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef",
    {"GrantArn": str, "Status": GrantStatus, "Version": str},
    total=False,
)

CreateGrantVersionResponseTypeDef = TypedDict(
    "CreateGrantVersionResponseTypeDef",
    {"GrantArn": str, "Status": GrantStatus, "Version": str},
    total=False,
)

CreateLicenseConfigurationResponseTypeDef = TypedDict(
    "CreateLicenseConfigurationResponseTypeDef", {"LicenseConfigurationArn": str}, total=False
)

CreateLicenseResponseTypeDef = TypedDict(
    "CreateLicenseResponseTypeDef",
    {"LicenseArn": str, "Status": LicenseStatus, "Version": str},
    total=False,
)

CreateLicenseVersionResponseTypeDef = TypedDict(
    "CreateLicenseVersionResponseTypeDef",
    {"LicenseArn": str, "Version": str, "Status": LicenseStatus},
    total=False,
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {"TokenId": str, "TokenType": TokenType, "Token": str},
    total=False,
)

DeleteGrantResponseTypeDef = TypedDict(
    "DeleteGrantResponseTypeDef",
    {"GrantArn": str, "Status": GrantStatus, "Version": str},
    total=False,
)

DeleteLicenseResponseTypeDef = TypedDict(
    "DeleteLicenseResponseTypeDef",
    {"Status": LicenseDeletionStatus, "DeletionDate": str},
    total=False,
)

ExtendLicenseConsumptionResponseTypeDef = TypedDict(
    "ExtendLicenseConsumptionResponseTypeDef",
    {"LicenseConsumptionToken": str, "Expiration": str},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

GetAccessTokenResponseTypeDef = TypedDict(
    "GetAccessTokenResponseTypeDef", {"AccessToken": str}, total=False
)

GetGrantResponseTypeDef = TypedDict(
    "GetGrantResponseTypeDef", {"Grant": "GrantTypeDef"}, total=False
)

GetLicenseConfigurationResponseTypeDef = TypedDict(
    "GetLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationId": str,
        "LicenseConfigurationArn": str,
        "Name": str,
        "Description": str,
        "LicenseCountingType": LicenseCountingType,
        "LicenseRules": List[str],
        "LicenseCount": int,
        "LicenseCountHardLimit": bool,
        "ConsumedLicenses": int,
        "Status": str,
        "OwnerAccountId": str,
        "ConsumedLicenseSummaryList": List["ConsumedLicenseSummaryTypeDef"],
        "ManagedResourceSummaryList": List["ManagedResourceSummaryTypeDef"],
        "Tags": List["TagTypeDef"],
        "ProductInformationList": List["ProductInformationTypeDef"],
        "AutomatedDiscoveryInformation": "AutomatedDiscoveryInformationTypeDef",
        "DisassociateWhenNotFound": bool,
    },
    total=False,
)

GetLicenseResponseTypeDef = TypedDict(
    "GetLicenseResponseTypeDef", {"License": "LicenseTypeDef"}, total=False
)

GetLicenseUsageResponseTypeDef = TypedDict(
    "GetLicenseUsageResponseTypeDef", {"LicenseUsage": "LicenseUsageTypeDef"}, total=False
)

GetServiceSettingsResponseTypeDef = TypedDict(
    "GetServiceSettingsResponseTypeDef",
    {
        "S3BucketArn": str,
        "SnsTopicArn": str,
        "OrganizationConfiguration": "OrganizationConfigurationTypeDef",
        "EnableCrossAccountsDiscovery": bool,
        "LicenseManagerResourceShareArn": str,
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef", {"Name": str, "Condition": InventoryFilterCondition}
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef", {"Value": str}, total=False
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


_RequiredIssuerTypeDef = TypedDict("_RequiredIssuerTypeDef", {"Name": str})
_OptionalIssuerTypeDef = TypedDict("_OptionalIssuerTypeDef", {"SignKey": str}, total=False)


class IssuerTypeDef(_RequiredIssuerTypeDef, _OptionalIssuerTypeDef):
    pass


ListAssociationsForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListAssociationsForLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationAssociations": List["LicenseConfigurationAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDistributedGrantsResponseTypeDef = TypedDict(
    "ListDistributedGrantsResponseTypeDef",
    {"Grants": List["GrantTypeDef"], "NextToken": str},
    total=False,
)

ListFailuresForLicenseConfigurationOperationsResponseTypeDef = TypedDict(
    "ListFailuresForLicenseConfigurationOperationsResponseTypeDef",
    {"LicenseOperationFailureList": List["LicenseOperationFailureTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseConfigurationsResponseTypeDef = TypedDict(
    "ListLicenseConfigurationsResponseTypeDef",
    {"LicenseConfigurations": List["LicenseConfigurationTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseSpecificationsForResourceResponseTypeDef = TypedDict(
    "ListLicenseSpecificationsForResourceResponseTypeDef",
    {"LicenseSpecifications": List["LicenseSpecificationTypeDef"], "NextToken": str},
    total=False,
)

ListLicenseVersionsResponseTypeDef = TypedDict(
    "ListLicenseVersionsResponseTypeDef",
    {"Licenses": List["LicenseTypeDef"], "NextToken": str},
    total=False,
)

ListLicensesResponseTypeDef = TypedDict(
    "ListLicensesResponseTypeDef",
    {"Licenses": List["LicenseTypeDef"], "NextToken": str},
    total=False,
)

ListReceivedGrantsResponseTypeDef = TypedDict(
    "ListReceivedGrantsResponseTypeDef",
    {"Grants": List["GrantTypeDef"], "NextToken": str},
    total=False,
)

ListReceivedLicensesResponseTypeDef = TypedDict(
    "ListReceivedLicensesResponseTypeDef",
    {"Licenses": List["GrantedLicenseTypeDef"], "NextToken": str},
    total=False,
)

ListResourceInventoryResponseTypeDef = TypedDict(
    "ListResourceInventoryResponseTypeDef",
    {"ResourceInventoryList": List["ResourceInventoryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListTokensResponseTypeDef = TypedDict(
    "ListTokensResponseTypeDef", {"Tokens": List["TokenDataTypeDef"], "NextToken": str}, total=False
)

ListUsageForLicenseConfigurationResponseTypeDef = TypedDict(
    "ListUsageForLicenseConfigurationResponseTypeDef",
    {"LicenseConfigurationUsageList": List["LicenseConfigurationUsageTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RejectGrantResponseTypeDef = TypedDict(
    "RejectGrantResponseTypeDef",
    {"GrantArn": str, "Status": GrantStatus, "Version": str},
    total=False,
)
