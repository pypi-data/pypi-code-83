"""
Main interface for acm service type definitions.

Usage::

    ```python
    from mypy_boto3_acm.type_defs import CertificateDetailTypeDef

    data: CertificateDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_acm.literals import (
    CertificateStatus,
    CertificateTransparencyLoggingPreference,
    CertificateType,
    DomainStatus,
    ExtendedKeyUsageName,
    FailureReason,
    KeyAlgorithm,
    KeyUsageName,
    RecordType,
    RenewalEligibility,
    RenewalStatus,
    RevocationReason,
    ValidationMethod,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DomainValidationTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExtendedKeyUsageTypeDef",
    "KeyUsageTypeDef",
    "RenewalSummaryTypeDef",
    "ResourceRecordTypeDef",
    "TagTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "ExportCertificateResponseTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RequestCertificateResponseTypeDef",
    "WaiterConfigTypeDef",
)

CertificateDetailTypeDef = TypedDict(
    "CertificateDetailTypeDef",
    {
        "CertificateArn": str,
        "DomainName": str,
        "SubjectAlternativeNames": List[str],
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "Serial": str,
        "Subject": str,
        "Issuer": str,
        "CreatedAt": datetime,
        "IssuedAt": datetime,
        "ImportedAt": datetime,
        "Status": CertificateStatus,
        "RevokedAt": datetime,
        "RevocationReason": RevocationReason,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "KeyAlgorithm": KeyAlgorithm,
        "SignatureAlgorithm": str,
        "InUseBy": List[str],
        "FailureReason": FailureReason,
        "Type": CertificateType,
        "RenewalSummary": "RenewalSummaryTypeDef",
        "KeyUsages": List["KeyUsageTypeDef"],
        "ExtendedKeyUsages": List["ExtendedKeyUsageTypeDef"],
        "CertificateAuthorityArn": str,
        "RenewalEligibility": RenewalEligibility,
        "Options": "CertificateOptionsTypeDef",
    },
    total=False,
)

CertificateOptionsTypeDef = TypedDict(
    "CertificateOptionsTypeDef",
    {"CertificateTransparencyLoggingPreference": CertificateTransparencyLoggingPreference},
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef", {"CertificateArn": str, "DomainName": str}, total=False
)

_RequiredDomainValidationTypeDef = TypedDict(
    "_RequiredDomainValidationTypeDef", {"DomainName": str}
)
_OptionalDomainValidationTypeDef = TypedDict(
    "_OptionalDomainValidationTypeDef",
    {
        "ValidationEmails": List[str],
        "ValidationDomain": str,
        "ValidationStatus": DomainStatus,
        "ResourceRecord": "ResourceRecordTypeDef",
        "ValidationMethod": ValidationMethod,
    },
    total=False,
)


class DomainValidationTypeDef(_RequiredDomainValidationTypeDef, _OptionalDomainValidationTypeDef):
    pass


ExpiryEventsConfigurationTypeDef = TypedDict(
    "ExpiryEventsConfigurationTypeDef", {"DaysBeforeExpiry": int}, total=False
)

ExtendedKeyUsageTypeDef = TypedDict(
    "ExtendedKeyUsageTypeDef", {"Name": ExtendedKeyUsageName, "OID": str}, total=False
)

KeyUsageTypeDef = TypedDict("KeyUsageTypeDef", {"Name": KeyUsageName}, total=False)

_RequiredRenewalSummaryTypeDef = TypedDict(
    "_RequiredRenewalSummaryTypeDef",
    {
        "RenewalStatus": RenewalStatus,
        "DomainValidationOptions": List["DomainValidationTypeDef"],
        "UpdatedAt": datetime,
    },
)
_OptionalRenewalSummaryTypeDef = TypedDict(
    "_OptionalRenewalSummaryTypeDef", {"RenewalStatusReason": FailureReason}, total=False
)


class RenewalSummaryTypeDef(_RequiredRenewalSummaryTypeDef, _OptionalRenewalSummaryTypeDef):
    pass


ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef", {"Name": str, "Type": RecordType, "Value": str}
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


DescribeCertificateResponseTypeDef = TypedDict(
    "DescribeCertificateResponseTypeDef", {"Certificate": "CertificateDetailTypeDef"}, total=False
)

DomainValidationOptionTypeDef = TypedDict(
    "DomainValidationOptionTypeDef", {"DomainName": str, "ValidationDomain": str}
)

ExportCertificateResponseTypeDef = TypedDict(
    "ExportCertificateResponseTypeDef",
    {"Certificate": str, "CertificateChain": str, "PrivateKey": str},
    total=False,
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef",
    {
        "extendedKeyUsage": List[ExtendedKeyUsageName],
        "keyUsage": List[KeyUsageName],
        "keyTypes": List[KeyAlgorithm],
    },
    total=False,
)

GetAccountConfigurationResponseTypeDef = TypedDict(
    "GetAccountConfigurationResponseTypeDef",
    {"ExpiryEvents": "ExpiryEventsConfigurationTypeDef"},
    total=False,
)

GetCertificateResponseTypeDef = TypedDict(
    "GetCertificateResponseTypeDef", {"Certificate": str, "CertificateChain": str}, total=False
)

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

ListCertificatesResponseTypeDef = TypedDict(
    "ListCertificatesResponseTypeDef",
    {"NextToken": str, "CertificateSummaryList": List["CertificateSummaryTypeDef"]},
    total=False,
)

ListTagsForCertificateResponseTypeDef = TypedDict(
    "ListTagsForCertificateResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RequestCertificateResponseTypeDef = TypedDict(
    "RequestCertificateResponseTypeDef", {"CertificateArn": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
