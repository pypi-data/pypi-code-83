"""
Type annotations for ebs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ebs/type_defs.html)

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

from mypy_boto3_ebs.literals import Status

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "StartSnapshotResponseTypeDef",
    "TagTypeDef",
)


class BlockTypeDef(TypedDict, total=False):
    BlockIndex: int
    BlockToken: str


class ChangedBlockTypeDef(TypedDict, total=False):
    BlockIndex: int
    FirstBlockToken: str
    SecondBlockToken: str


class CompleteSnapshotResponseTypeDef(TypedDict, total=False):
    Status: Status


class GetSnapshotBlockResponseTypeDef(TypedDict, total=False):
    DataLength: int
    BlockData: StreamingBody
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]


class ListChangedBlocksResponseTypeDef(TypedDict, total=False):
    ChangedBlocks: List["ChangedBlockTypeDef"]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    NextToken: str


class ListSnapshotBlocksResponseTypeDef(TypedDict, total=False):
    Blocks: List["BlockTypeDef"]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    NextToken: str


class PutSnapshotBlockResponseTypeDef(TypedDict, total=False):
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]


class StartSnapshotResponseTypeDef(TypedDict, total=False):
    Description: str
    SnapshotId: str
    OwnerId: str
    Status: Status
    StartTime: datetime
    VolumeSize: int
    BlockSize: int
    Tags: List["TagTypeDef"]
    ParentSnapshotId: str
    KmsKeyArn: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str
