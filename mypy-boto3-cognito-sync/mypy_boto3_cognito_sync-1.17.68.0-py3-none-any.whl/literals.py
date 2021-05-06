"""
Type annotations for cognito-sync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/literals.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.literals import BulkPublishStatus

    data: BulkPublishStatus = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BulkPublishStatus", "Operation", "Platform", "StreamingStatus")


BulkPublishStatus = Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"]
Operation = Literal["remove", "replace"]
Platform = Literal["ADM", "APNS", "APNS_SANDBOX", "GCM"]
StreamingStatus = Literal["DISABLED", "ENABLED"]
