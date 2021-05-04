"""
Type annotations for acm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/type_defs.html)

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
    RenewalEligibility,
    RenewalStatus,
    RevocationReason,
    ValidationMethod,
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
    "CertificateDetailTypeDef",
    "CertificateOptionsTypeDef",
    "CertificateSummaryTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DomainValidationOptionTypeDef",
    "DomainValidationTypeDef",
    "ExpiryEventsConfigurationTypeDef",
    "ExportCertificateResponseTypeDef",
    "ExtendedKeyUsageTypeDef",
    "FiltersTypeDef",
    "GetAccountConfigurationResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "ImportCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListTagsForCertificateResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RenewalSummaryTypeDef",
    "RequestCertificateResponseTypeDef",
    "ResourceRecordTypeDef",
    "TagTypeDef",
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


class CertificateOptionsTypeDef(TypedDict, total=False):
    CertificateTransparencyLoggingPreference: CertificateTransparencyLoggingPreference


class CertificateSummaryTypeDef(TypedDict, total=False):
    CertificateArn: str
    DomainName: str


class DescribeCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: "CertificateDetailTypeDef"


class DomainValidationOptionTypeDef(TypedDict):
    DomainName: str
    ValidationDomain: str


class _RequiredDomainValidationTypeDef(TypedDict):
    DomainName: str


class DomainValidationTypeDef(_RequiredDomainValidationTypeDef, total=False):
    ValidationEmails: List[str]
    ValidationDomain: str
    ValidationStatus: DomainStatus
    ResourceRecord: "ResourceRecordTypeDef"
    ValidationMethod: ValidationMethod


class ExpiryEventsConfigurationTypeDef(TypedDict, total=False):
    DaysBeforeExpiry: int


class ExportCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: str
    CertificateChain: str
    PrivateKey: str


class ExtendedKeyUsageTypeDef(TypedDict, total=False):
    Name: ExtendedKeyUsageName
    OID: str


class FiltersTypeDef(TypedDict, total=False):
    extendedKeyUsage: List[ExtendedKeyUsageName]
    keyUsage: List[KeyUsageName]
    keyTypes: List[KeyAlgorithm]


class GetAccountConfigurationResponseTypeDef(TypedDict, total=False):
    ExpiryEvents: "ExpiryEventsConfigurationTypeDef"


class GetCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: str
    CertificateChain: str


class ImportCertificateResponseTypeDef(TypedDict, total=False):
    CertificateArn: str


class KeyUsageTypeDef(TypedDict, total=False):
    Name: KeyUsageName


class ListCertificatesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    CertificateSummaryList: List["CertificateSummaryTypeDef"]


class ListTagsForCertificateResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredRenewalSummaryTypeDef(TypedDict):
    RenewalStatus: RenewalStatus
    DomainValidationOptions: List["DomainValidationTypeDef"]
    UpdatedAt: datetime


class RenewalSummaryTypeDef(_RequiredRenewalSummaryTypeDef, total=False):
    RenewalStatusReason: FailureReason


class RequestCertificateResponseTypeDef(TypedDict, total=False):
    CertificateArn: str


ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef", {"Name": str, "Type": Literal["CNAME"], "Value": str}
)


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
