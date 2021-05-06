"""
Type annotations for acm-pca service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/literals.html)

Usage::

    ```python
    from mypy_boto3_acm_pca.literals import AccessMethodType

    data: AccessMethodType = "CA_REPOSITORY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessMethodType",
    "ActionType",
    "AuditReportCreatedWaiterName",
    "AuditReportResponseFormat",
    "AuditReportStatus",
    "CertificateAuthorityCSRCreatedWaiterName",
    "CertificateAuthorityStatus",
    "CertificateAuthorityType",
    "CertificateIssuedWaiterName",
    "ExtendedKeyUsageType",
    "FailureReason",
    "KeyAlgorithm",
    "KeyStorageSecurityStandard",
    "ListCertificateAuthoritiesPaginatorName",
    "ListPermissionsPaginatorName",
    "ListTagsPaginatorName",
    "PolicyQualifierId",
    "ResourceOwner",
    "RevocationReason",
    "SigningAlgorithm",
    "ValidityPeriodType",
)


AccessMethodType = Literal["CA_REPOSITORY", "RESOURCE_PKI_MANIFEST", "RESOURCE_PKI_NOTIFY"]
ActionType = Literal["GetCertificate", "IssueCertificate", "ListPermissions"]
AuditReportCreatedWaiterName = Literal["audit_report_created"]
AuditReportResponseFormat = Literal["CSV", "JSON"]
AuditReportStatus = Literal["CREATING", "FAILED", "SUCCESS"]
CertificateAuthorityCSRCreatedWaiterName = Literal["certificate_authority_csr_created"]
CertificateAuthorityStatus = Literal[
    "ACTIVE", "CREATING", "DELETED", "DISABLED", "EXPIRED", "FAILED", "PENDING_CERTIFICATE"
]
CertificateAuthorityType = Literal["ROOT", "SUBORDINATE"]
CertificateIssuedWaiterName = Literal["certificate_issued"]
ExtendedKeyUsageType = Literal[
    "CERTIFICATE_TRANSPARENCY",
    "CLIENT_AUTH",
    "CODE_SIGNING",
    "DOCUMENT_SIGNING",
    "EMAIL_PROTECTION",
    "OCSP_SIGNING",
    "SERVER_AUTH",
    "SMART_CARD_LOGIN",
    "TIME_STAMPING",
]
FailureReason = Literal["OTHER", "REQUEST_TIMED_OUT", "UNSUPPORTED_ALGORITHM"]
KeyAlgorithm = Literal["EC_prime256v1", "EC_secp384r1", "RSA_2048", "RSA_4096"]
KeyStorageSecurityStandard = Literal["FIPS_140_2_LEVEL_2_OR_HIGHER", "FIPS_140_2_LEVEL_3_OR_HIGHER"]
ListCertificateAuthoritiesPaginatorName = Literal["list_certificate_authorities"]
ListPermissionsPaginatorName = Literal["list_permissions"]
ListTagsPaginatorName = Literal["list_tags"]
PolicyQualifierId = Literal["CPS"]
ResourceOwner = Literal["OTHER_ACCOUNTS", "SELF"]
RevocationReason = Literal[
    "AFFILIATION_CHANGED",
    "A_A_COMPROMISE",
    "CERTIFICATE_AUTHORITY_COMPROMISE",
    "CESSATION_OF_OPERATION",
    "KEY_COMPROMISE",
    "PRIVILEGE_WITHDRAWN",
    "SUPERSEDED",
    "UNSPECIFIED",
]
SigningAlgorithm = Literal[
    "SHA256WITHECDSA",
    "SHA256WITHRSA",
    "SHA384WITHECDSA",
    "SHA384WITHRSA",
    "SHA512WITHECDSA",
    "SHA512WITHRSA",
]
ValidityPeriodType = Literal["ABSOLUTE", "DAYS", "END_DATE", "MONTHS", "YEARS"]
