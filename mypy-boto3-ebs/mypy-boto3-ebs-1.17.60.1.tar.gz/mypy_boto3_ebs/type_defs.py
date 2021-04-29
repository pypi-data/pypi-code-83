"""
Main interface for ebs service type definitions.

Usage::

    ```python
    from mypy_boto3_ebs.type_defs import BlockTypeDef

    data: BlockTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from botocore.response import StreamingBody

from mypy_boto3_ebs.literals import ChecksumAlgorithm, Status

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "TagTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "StartSnapshotResponseTypeDef",
)

BlockTypeDef = TypedDict("BlockTypeDef", {"BlockIndex": int, "BlockToken": str}, total=False)

ChangedBlockTypeDef = TypedDict(
    "ChangedBlockTypeDef",
    {"BlockIndex": int, "FirstBlockToken": str, "SecondBlockToken": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

CompleteSnapshotResponseTypeDef = TypedDict(
    "CompleteSnapshotResponseTypeDef", {"Status": Status}, total=False
)

GetSnapshotBlockResponseTypeDef = TypedDict(
    "GetSnapshotBlockResponseTypeDef",
    {
        "DataLength": int,
        "BlockData": StreamingBody,
        "Checksum": str,
        "ChecksumAlgorithm": ChecksumAlgorithm,
    },
    total=False,
)

ListChangedBlocksResponseTypeDef = TypedDict(
    "ListChangedBlocksResponseTypeDef",
    {
        "ChangedBlocks": List["ChangedBlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
    },
    total=False,
)

ListSnapshotBlocksResponseTypeDef = TypedDict(
    "ListSnapshotBlocksResponseTypeDef",
    {
        "Blocks": List["BlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
    },
    total=False,
)

PutSnapshotBlockResponseTypeDef = TypedDict(
    "PutSnapshotBlockResponseTypeDef",
    {"Checksum": str, "ChecksumAlgorithm": ChecksumAlgorithm},
    total=False,
)

StartSnapshotResponseTypeDef = TypedDict(
    "StartSnapshotResponseTypeDef",
    {
        "Description": str,
        "SnapshotId": str,
        "OwnerId": str,
        "Status": Status,
        "StartTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "Tags": List["TagTypeDef"],
        "ParentSnapshotId": str,
        "KmsKeyArn": str,
    },
    total=False,
)
