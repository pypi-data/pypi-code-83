"""
Type annotations for glacier service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/literals.html)

Usage::

    ```python
    from mypy_boto3_glacier.literals import ActionCode

    data: ActionCode = "ArchiveRetrieval"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionCode",
    "CannedACL",
    "EncryptionType",
    "ExpressionType",
    "FileHeaderInfo",
    "ListJobsPaginatorName",
    "ListMultipartUploadsPaginatorName",
    "ListPartsPaginatorName",
    "ListVaultsPaginatorName",
    "Permission",
    "QuoteFields",
    "StatusCode",
    "StorageClass",
    "TypeType",
    "VaultExistsWaiterName",
    "VaultNotExistsWaiterName",
)


ActionCode = Literal["ArchiveRetrieval", "InventoryRetrieval", "Select"]
CannedACL = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
EncryptionType = Literal["AES256", "aws:kms"]
ExpressionType = Literal["SQL"]
FileHeaderInfo = Literal["IGNORE", "NONE", "USE"]
ListJobsPaginatorName = Literal["list_jobs"]
ListMultipartUploadsPaginatorName = Literal["list_multipart_uploads"]
ListPartsPaginatorName = Literal["list_parts"]
ListVaultsPaginatorName = Literal["list_vaults"]
Permission = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
QuoteFields = Literal["ALWAYS", "ASNEEDED"]
StatusCode = Literal["Failed", "InProgress", "Succeeded"]
StorageClass = Literal["REDUCED_REDUNDANCY", "STANDARD", "STANDARD_IA"]
TypeType = Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]
VaultExistsWaiterName = Literal["vault_exists"]
VaultNotExistsWaiterName = Literal["vault_not_exists"]
