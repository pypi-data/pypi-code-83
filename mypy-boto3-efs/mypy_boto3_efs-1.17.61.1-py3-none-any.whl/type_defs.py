"""
Type annotations for efs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_efs.type_defs import AccessPointDescriptionTypeDef

    data: AccessPointDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_efs.literals import (
    LifeCycleState,
    PerformanceMode,
    Status,
    ThroughputMode,
    TransitionToIARules,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPointDescriptionTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "BackupPolicyTypeDef",
    "CreationInfoTypeDef",
    "DescribeAccessPointsResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "FileSystemDescriptionTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MountTargetDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "PosixUserTypeDef",
    "RootDirectoryTypeDef",
    "TagTypeDef",
)


class AccessPointDescriptionTypeDef(TypedDict, total=False):
    ClientToken: str
    Name: str
    Tags: List["TagTypeDef"]
    AccessPointId: str
    AccessPointArn: str
    FileSystemId: str
    PosixUser: "PosixUserTypeDef"
    RootDirectory: "RootDirectoryTypeDef"
    OwnerId: str
    LifeCycleState: LifeCycleState


class BackupPolicyDescriptionTypeDef(TypedDict, total=False):
    BackupPolicy: "BackupPolicyTypeDef"


class BackupPolicyTypeDef(TypedDict):
    Status: Status


class CreationInfoTypeDef(TypedDict):
    OwnerUid: int
    OwnerGid: int
    Permissions: str


class DescribeAccessPointsResponseTypeDef(TypedDict, total=False):
    AccessPoints: List["AccessPointDescriptionTypeDef"]
    NextToken: str


class DescribeFileSystemsResponseTypeDef(TypedDict, total=False):
    Marker: str
    FileSystems: List["FileSystemDescriptionTypeDef"]
    NextMarker: str


class DescribeMountTargetSecurityGroupsResponseTypeDef(TypedDict):
    SecurityGroups: List[str]


class DescribeMountTargetsResponseTypeDef(TypedDict, total=False):
    Marker: str
    MountTargets: List["MountTargetDescriptionTypeDef"]
    NextMarker: str


class _RequiredDescribeTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class DescribeTagsResponseTypeDef(_RequiredDescribeTagsResponseTypeDef, total=False):
    Marker: str
    NextMarker: str


class _RequiredFileSystemDescriptionTypeDef(TypedDict):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    CreationTime: datetime
    LifeCycleState: LifeCycleState
    NumberOfMountTargets: int
    SizeInBytes: "FileSystemSizeTypeDef"
    PerformanceMode: PerformanceMode
    Tags: List["TagTypeDef"]


class FileSystemDescriptionTypeDef(_RequiredFileSystemDescriptionTypeDef, total=False):
    FileSystemArn: str
    Name: str
    Encrypted: bool
    KmsKeyId: str
    ThroughputMode: ThroughputMode
    ProvisionedThroughputInMibps: float
    AvailabilityZoneName: str
    AvailabilityZoneId: str


class FileSystemPolicyDescriptionTypeDef(TypedDict, total=False):
    FileSystemId: str
    Policy: str


class _RequiredFileSystemSizeTypeDef(TypedDict):
    Value: int


class FileSystemSizeTypeDef(_RequiredFileSystemSizeTypeDef, total=False):
    Timestamp: datetime
    ValueInIA: int
    ValueInStandard: int


class LifecycleConfigurationDescriptionTypeDef(TypedDict, total=False):
    LifecyclePolicies: List["LifecyclePolicyTypeDef"]


class LifecyclePolicyTypeDef(TypedDict, total=False):
    TransitionToIA: TransitionToIARules


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class _RequiredMountTargetDescriptionTypeDef(TypedDict):
    MountTargetId: str
    FileSystemId: str
    SubnetId: str
    LifeCycleState: LifeCycleState


class MountTargetDescriptionTypeDef(_RequiredMountTargetDescriptionTypeDef, total=False):
    OwnerId: str
    IpAddress: str
    NetworkInterfaceId: str
    AvailabilityZoneId: str
    AvailabilityZoneName: str
    VpcId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPosixUserTypeDef(TypedDict):
    Uid: int
    Gid: int


class PosixUserTypeDef(_RequiredPosixUserTypeDef, total=False):
    SecondaryGids: List[int]


class RootDirectoryTypeDef(TypedDict, total=False):
    Path: str
    CreationInfo: "CreationInfoTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str
