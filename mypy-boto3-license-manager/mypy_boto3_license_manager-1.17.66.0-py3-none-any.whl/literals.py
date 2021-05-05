"""
Type annotations for license-manager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_license_manager/literals.html)

Usage::

    ```python
    from mypy_boto3_license_manager.literals import AllowedOperation

    data: AllowedOperation = "CheckInLicense"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AllowedOperation",
    "CheckoutType",
    "DigitalSignatureMethod",
    "EntitlementDataUnit",
    "EntitlementUnit",
    "GrantStatus",
    "InventoryFilterCondition",
    "LicenseConfigurationStatus",
    "LicenseCountingType",
    "LicenseDeletionStatus",
    "LicenseStatus",
    "ListAssociationsForLicenseConfigurationPaginatorName",
    "ListLicenseConfigurationsPaginatorName",
    "ListLicenseSpecificationsForResourcePaginatorName",
    "ListResourceInventoryPaginatorName",
    "ListUsageForLicenseConfigurationPaginatorName",
    "ReceivedStatus",
    "RenewType",
    "ResourceType",
    "TokenType",
)


AllowedOperation = Literal[
    "CheckInLicense",
    "CheckoutBorrowLicense",
    "CheckoutLicense",
    "CreateGrant",
    "CreateToken",
    "ExtendConsumptionLicense",
    "ListPurchasedLicenses",
]
CheckoutType = Literal["PROVISIONAL"]
DigitalSignatureMethod = Literal["JWT_PS384"]
EntitlementDataUnit = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
EntitlementUnit = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
GrantStatus = Literal[
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "FAILED_WORKFLOW",
    "PENDING_ACCEPT",
    "PENDING_DELETE",
    "PENDING_WORKFLOW",
    "REJECTED",
]
InventoryFilterCondition = Literal["BEGINS_WITH", "CONTAINS", "EQUALS", "NOT_EQUALS"]
LicenseConfigurationStatus = Literal["AVAILABLE", "DISABLED"]
LicenseCountingType = Literal["Core", "Instance", "Socket", "vCPU"]
LicenseDeletionStatus = Literal["DELETED", "PENDING_DELETE"]
LicenseStatus = Literal[
    "AVAILABLE",
    "DEACTIVATED",
    "DELETED",
    "EXPIRED",
    "PENDING_AVAILABLE",
    "PENDING_DELETE",
    "SUSPENDED",
]
ListAssociationsForLicenseConfigurationPaginatorName = Literal[
    "list_associations_for_license_configuration"
]
ListLicenseConfigurationsPaginatorName = Literal["list_license_configurations"]
ListLicenseSpecificationsForResourcePaginatorName = Literal[
    "list_license_specifications_for_resource"
]
ListResourceInventoryPaginatorName = Literal["list_resource_inventory"]
ListUsageForLicenseConfigurationPaginatorName = Literal["list_usage_for_license_configuration"]
ReceivedStatus = Literal[
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "FAILED_WORKFLOW",
    "PENDING_ACCEPT",
    "PENDING_WORKFLOW",
    "REJECTED",
]
RenewType = Literal["Monthly", "None", "Weekly"]
ResourceType = Literal[
    "EC2_AMI", "EC2_HOST", "EC2_INSTANCE", "RDS", "SYSTEMS_MANAGER_MANAGED_INSTANCE"
]
TokenType = Literal["REFRESH_TOKEN"]
