"""
Type annotations for acm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/literals.html)

Usage::

    ```python
    from mypy_boto3_acm.literals import CertificateStatus

    data: CertificateStatus = "EXPIRED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CertificateStatus",
    "CertificateTransparencyLoggingPreference",
    "CertificateType",
    "CertificateValidatedWaiterName",
    "DomainStatus",
    "ExtendedKeyUsageName",
    "FailureReason",
    "KeyAlgorithm",
    "KeyUsageName",
    "ListCertificatesPaginatorName",
    "RecordType",
    "RenewalEligibility",
    "RenewalStatus",
    "RevocationReason",
    "ValidationMethod",
)


CertificateStatus = Literal[
    "EXPIRED",
    "FAILED",
    "INACTIVE",
    "ISSUED",
    "PENDING_VALIDATION",
    "REVOKED",
    "VALIDATION_TIMED_OUT",
]
CertificateTransparencyLoggingPreference = Literal["DISABLED", "ENABLED"]
CertificateType = Literal["AMAZON_ISSUED", "IMPORTED", "PRIVATE"]
CertificateValidatedWaiterName = Literal["certificate_validated"]
DomainStatus = Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
ExtendedKeyUsageName = Literal[
    "ANY",
    "CODE_SIGNING",
    "CUSTOM",
    "EMAIL_PROTECTION",
    "IPSEC_END_SYSTEM",
    "IPSEC_TUNNEL",
    "IPSEC_USER",
    "NONE",
    "OCSP_SIGNING",
    "TIME_STAMPING",
    "TLS_WEB_CLIENT_AUTHENTICATION",
    "TLS_WEB_SERVER_AUTHENTICATION",
]
FailureReason = Literal[
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "CAA_ERROR",
    "DOMAIN_NOT_ALLOWED",
    "DOMAIN_VALIDATION_DENIED",
    "INVALID_PUBLIC_DOMAIN",
    "NO_AVAILABLE_CONTACTS",
    "OTHER",
    "PCA_ACCESS_DENIED",
    "PCA_INVALID_ARGS",
    "PCA_INVALID_ARN",
    "PCA_INVALID_DURATION",
    "PCA_INVALID_STATE",
    "PCA_LIMIT_EXCEEDED",
    "PCA_NAME_CONSTRAINTS_VALIDATION",
    "PCA_REQUEST_FAILED",
    "PCA_RESOURCE_NOT_FOUND",
    "SLR_NOT_FOUND",
]
KeyAlgorithm = Literal[
    "EC_prime256v1", "EC_secp384r1", "EC_secp521r1", "RSA_1024", "RSA_2048", "RSA_4096"
]
KeyUsageName = Literal[
    "ANY",
    "CERTIFICATE_SIGNING",
    "CRL_SIGNING",
    "CUSTOM",
    "DATA_ENCIPHERMENT",
    "DECIPHER_ONLY",
    "DIGITAL_SIGNATURE",
    "ENCIPHER_ONLY",
    "KEY_AGREEMENT",
    "KEY_ENCIPHERMENT",
    "NON_REPUDIATION",
]
ListCertificatesPaginatorName = Literal["list_certificates"]
RecordType = Literal["CNAME"]
RenewalEligibility = Literal["ELIGIBLE", "INELIGIBLE"]
RenewalStatus = Literal["FAILED", "PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS"]
RevocationReason = Literal[
    "AFFILIATION_CHANGED",
    "A_A_COMPROMISE",
    "CA_COMPROMISE",
    "CERTIFICATE_HOLD",
    "CESSATION_OF_OPERATION",
    "KEY_COMPROMISE",
    "PRIVILEGE_WITHDRAWN",
    "REMOVE_FROM_CRL",
    "SUPERCEDED",
    "UNSPECIFIED",
]
ValidationMethod = Literal["DNS", "EMAIL"]
