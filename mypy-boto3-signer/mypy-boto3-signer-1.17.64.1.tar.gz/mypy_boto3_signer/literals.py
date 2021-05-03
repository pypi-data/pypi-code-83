"""
Type annotations for signer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/literals.html)

Usage::

    ```python
    from mypy_boto3_signer.literals import Category

    data: Category = "AWSIoT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Category",
    "EncryptionAlgorithm",
    "HashAlgorithm",
    "ImageFormat",
    "ListSigningJobsPaginatorName",
    "ListSigningPlatformsPaginatorName",
    "ListSigningProfilesPaginatorName",
    "SigningProfileStatus",
    "SigningStatus",
    "SuccessfulSigningJobWaiterName",
    "ValidityType",
)


Category = Literal["AWSIoT"]
EncryptionAlgorithm = Literal["ECDSA", "RSA"]
HashAlgorithm = Literal["SHA1", "SHA256"]
ImageFormat = Literal["JSON", "JSONDetached", "JSONEmbedded"]
ListSigningJobsPaginatorName = Literal["list_signing_jobs"]
ListSigningPlatformsPaginatorName = Literal["list_signing_platforms"]
ListSigningProfilesPaginatorName = Literal["list_signing_profiles"]
SigningProfileStatus = Literal["Active", "Canceled", "Revoked"]
SigningStatus = Literal["Failed", "InProgress", "Succeeded"]
SuccessfulSigningJobWaiterName = Literal["successful_signing_job"]
ValidityType = Literal["DAYS", "MONTHS", "YEARS"]
