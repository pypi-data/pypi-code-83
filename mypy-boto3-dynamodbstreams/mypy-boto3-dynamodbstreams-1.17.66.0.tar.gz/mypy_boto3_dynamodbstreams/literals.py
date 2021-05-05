"""
Type annotations for dynamodbstreams service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/literals.html)

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.literals import KeyType

    data: KeyType = "HASH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KeyType", "OperationType", "ShardIteratorType", "StreamStatus", "StreamViewType")


KeyType = Literal["HASH", "RANGE"]
OperationType = Literal["INSERT", "MODIFY", "REMOVE"]
ShardIteratorType = Literal["AFTER_SEQUENCE_NUMBER", "AT_SEQUENCE_NUMBER", "LATEST", "TRIM_HORIZON"]
StreamStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
StreamViewType = Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
