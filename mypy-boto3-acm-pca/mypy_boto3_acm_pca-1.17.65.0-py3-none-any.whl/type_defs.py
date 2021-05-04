"""
Type annotations for acm-pca service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/type_defs.html)

Usage::

    ```python
    from mypy_boto3_acm_pca.type_defs import ASN1SubjectTypeDef

    data: ASN1SubjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_acm_pca.literals import (
    AccessMethodType,
    ActionType,
    AuditReportStatus,
    CertificateAuthorityStatus,
    CertificateAuthorityType,
    ExtendedKeyUsageType,
    FailureReason,
    KeyAlgorithm,
    KeyStorageSecurityStandard,
    SigningAlgorithm,
    ValidityPeriodType,
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
    "ASN1SubjectTypeDef",
    "AccessDescriptionTypeDef",
    "AccessMethodTypeDef",
    "ApiPassthroughTypeDef",
    "CertificateAuthorityConfigurationTypeDef",
    "CertificateAuthorityTypeDef",
    "CreateCertificateAuthorityAuditReportResponseTypeDef",
    "CreateCertificateAuthorityResponseTypeDef",
    "CrlConfigurationTypeDef",
    "CsrExtensionsTypeDef",
    "DescribeCertificateAuthorityAuditReportResponseTypeDef",
    "DescribeCertificateAuthorityResponseTypeDef",
    "EdiPartyNameTypeDef",
    "ExtendedKeyUsageTypeDef",
    "ExtensionsTypeDef",
    "GeneralNameTypeDef",
    "GetCertificateAuthorityCertificateResponseTypeDef",
    "GetCertificateAuthorityCsrResponseTypeDef",
    "GetCertificateResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "IssueCertificateResponseTypeDef",
    "KeyUsageTypeDef",
    "ListCertificateAuthoritiesResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "OtherNameTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PolicyInformationTypeDef",
    "PolicyQualifierInfoTypeDef",
    "QualifierTypeDef",
    "RevocationConfigurationTypeDef",
    "TagTypeDef",
    "ValidityTypeDef",
    "WaiterConfigTypeDef",
)


class ASN1SubjectTypeDef(TypedDict, total=False):
    Country: str
    Organization: str
    OrganizationalUnit: str
    DistinguishedNameQualifier: str
    State: str
    CommonName: str
    SerialNumber: str
    Locality: str
    Title: str
    Surname: str
    GivenName: str
    Initials: str
    Pseudonym: str
    GenerationQualifier: str


class AccessDescriptionTypeDef(TypedDict):
    AccessMethod: "AccessMethodTypeDef"
    AccessLocation: "GeneralNameTypeDef"


class AccessMethodTypeDef(TypedDict, total=False):
    CustomObjectIdentifier: str
    AccessMethodType: AccessMethodType


class ApiPassthroughTypeDef(TypedDict, total=False):
    Extensions: "ExtensionsTypeDef"
    Subject: "ASN1SubjectTypeDef"


class _RequiredCertificateAuthorityConfigurationTypeDef(TypedDict):
    KeyAlgorithm: KeyAlgorithm
    SigningAlgorithm: SigningAlgorithm
    Subject: "ASN1SubjectTypeDef"


class CertificateAuthorityConfigurationTypeDef(
    _RequiredCertificateAuthorityConfigurationTypeDef, total=False
):
    CsrExtensions: "CsrExtensionsTypeDef"


CertificateAuthorityTypeDef = TypedDict(
    "CertificateAuthorityTypeDef",
    {
        "Arn": str,
        "OwnerAccount": str,
        "CreatedAt": datetime,
        "LastStateChangeAt": datetime,
        "Type": CertificateAuthorityType,
        "Serial": str,
        "Status": CertificateAuthorityStatus,
        "NotBefore": datetime,
        "NotAfter": datetime,
        "FailureReason": FailureReason,
        "CertificateAuthorityConfiguration": "CertificateAuthorityConfigurationTypeDef",
        "RevocationConfiguration": "RevocationConfigurationTypeDef",
        "RestorableUntil": datetime,
        "KeyStorageSecurityStandard": KeyStorageSecurityStandard,
    },
    total=False,
)


class CreateCertificateAuthorityAuditReportResponseTypeDef(TypedDict, total=False):
    AuditReportId: str
    S3Key: str


class CreateCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    CertificateAuthorityArn: str


class _RequiredCrlConfigurationTypeDef(TypedDict):
    Enabled: bool


class CrlConfigurationTypeDef(_RequiredCrlConfigurationTypeDef, total=False):
    ExpirationInDays: int
    CustomCname: str
    S3BucketName: str


class CsrExtensionsTypeDef(TypedDict, total=False):
    KeyUsage: "KeyUsageTypeDef"
    SubjectInformationAccess: List["AccessDescriptionTypeDef"]


class DescribeCertificateAuthorityAuditReportResponseTypeDef(TypedDict, total=False):
    AuditReportStatus: AuditReportStatus
    S3BucketName: str
    S3Key: str
    CreatedAt: datetime


class DescribeCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    CertificateAuthority: "CertificateAuthorityTypeDef"


class _RequiredEdiPartyNameTypeDef(TypedDict):
    PartyName: str


class EdiPartyNameTypeDef(_RequiredEdiPartyNameTypeDef, total=False):
    NameAssigner: str


class ExtendedKeyUsageTypeDef(TypedDict, total=False):
    ExtendedKeyUsageType: ExtendedKeyUsageType
    ExtendedKeyUsageObjectIdentifier: str


class ExtensionsTypeDef(TypedDict, total=False):
    CertificatePolicies: List["PolicyInformationTypeDef"]
    ExtendedKeyUsage: List["ExtendedKeyUsageTypeDef"]
    KeyUsage: "KeyUsageTypeDef"
    SubjectAlternativeNames: List["GeneralNameTypeDef"]


class GeneralNameTypeDef(TypedDict, total=False):
    OtherName: "OtherNameTypeDef"
    Rfc822Name: str
    DnsName: str
    DirectoryName: "ASN1SubjectTypeDef"
    EdiPartyName: "EdiPartyNameTypeDef"
    UniformResourceIdentifier: str
    IpAddress: str
    RegisteredId: str


class GetCertificateAuthorityCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: str
    CertificateChain: str


class GetCertificateAuthorityCsrResponseTypeDef(TypedDict, total=False):
    Csr: str


class GetCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: str
    CertificateChain: str


class GetPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class IssueCertificateResponseTypeDef(TypedDict, total=False):
    CertificateArn: str


class KeyUsageTypeDef(TypedDict, total=False):
    DigitalSignature: bool
    NonRepudiation: bool
    KeyEncipherment: bool
    DataEncipherment: bool
    KeyAgreement: bool
    KeyCertSign: bool
    CRLSign: bool
    EncipherOnly: bool
    DecipherOnly: bool


class ListCertificateAuthoritiesResponseTypeDef(TypedDict, total=False):
    CertificateAuthorities: List["CertificateAuthorityTypeDef"]
    NextToken: str


class ListPermissionsResponseTypeDef(TypedDict, total=False):
    Permissions: List["PermissionTypeDef"]
    NextToken: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class OtherNameTypeDef(TypedDict):
    TypeId: str
    Value: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionTypeDef(TypedDict, total=False):
    CertificateAuthorityArn: str
    CreatedAt: datetime
    Principal: str
    SourceAccount: str
    Actions: List[ActionType]
    Policy: str


class _RequiredPolicyInformationTypeDef(TypedDict):
    CertPolicyId: str


class PolicyInformationTypeDef(_RequiredPolicyInformationTypeDef, total=False):
    PolicyQualifiers: List["PolicyQualifierInfoTypeDef"]


class PolicyQualifierInfoTypeDef(TypedDict):
    PolicyQualifierId: Literal["CPS"]
    Qualifier: "QualifierTypeDef"


class QualifierTypeDef(TypedDict):
    CpsUri: str


class RevocationConfigurationTypeDef(TypedDict, total=False):
    CrlConfiguration: "CrlConfigurationTypeDef"


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


ValidityTypeDef = TypedDict("ValidityTypeDef", {"Value": int, "Type": ValidityPeriodType})


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
