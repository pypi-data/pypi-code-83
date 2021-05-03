"""
Type annotations for qldb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/literals.html)

Usage::

    ```python
    from mypy_boto3_qldb.literals import ErrorCause

    data: ErrorCause = "IAM_PERMISSION_REVOKED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ErrorCause",
    "ExportStatus",
    "LedgerState",
    "PermissionsMode",
    "S3ObjectEncryptionType",
    "StreamStatus",
)


ErrorCause = Literal["IAM_PERMISSION_REVOKED", "KINESIS_STREAM_NOT_FOUND"]
ExportStatus = Literal["CANCELLED", "COMPLETED", "IN_PROGRESS"]
LedgerState = Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]
PermissionsMode = Literal["ALLOW_ALL"]
S3ObjectEncryptionType = Literal["NO_ENCRYPTION", "SSE_KMS", "SSE_S3"]
StreamStatus = Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "IMPAIRED"]
