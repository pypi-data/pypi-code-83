"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cloudhsmv2.literals import BackupState, ClusterState, HsmState

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackupRetentionPolicyTypeDef",
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "ModifyClusterResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RestoreBackupResponseTypeDef",
    "TagTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef", {"Type": Literal["DAYS"], "Value": str}, total=False
)


class _RequiredBackupTypeDef(TypedDict):
    BackupId: str


class BackupTypeDef(_RequiredBackupTypeDef, total=False):
    BackupState: BackupState
    ClusterId: str
    CreateTimestamp: datetime
    CopyTimestamp: datetime
    NeverExpires: bool
    SourceRegion: str
    SourceBackup: str
    SourceCluster: str
    DeleteTimestamp: datetime
    TagList: List["TagTypeDef"]


class CertificatesTypeDef(TypedDict, total=False):
    ClusterCsr: str
    HsmCertificate: str
    AwsHardwareCertificate: str
    ManufacturerHardwareCertificate: str
    ClusterCertificate: str


class ClusterTypeDef(TypedDict, total=False):
    BackupPolicy: Literal["DEFAULT"]
    BackupRetentionPolicy: "BackupRetentionPolicyTypeDef"
    ClusterId: str
    CreateTimestamp: datetime
    Hsms: List["HsmTypeDef"]
    HsmType: str
    PreCoPassword: str
    SecurityGroup: str
    SourceBackupId: str
    State: ClusterState
    StateMessage: str
    SubnetMapping: Dict[str, str]
    VpcId: str
    Certificates: "CertificatesTypeDef"
    TagList: List["TagTypeDef"]


class CopyBackupToRegionResponseTypeDef(TypedDict, total=False):
    DestinationBackup: "DestinationBackupTypeDef"


class CreateClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class CreateHsmResponseTypeDef(TypedDict, total=False):
    Hsm: "HsmTypeDef"


class DeleteBackupResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class DeleteClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class DeleteHsmResponseTypeDef(TypedDict, total=False):
    HsmId: str


class DescribeBackupsResponseTypeDef(TypedDict, total=False):
    Backups: List["BackupTypeDef"]
    NextToken: str


class DescribeClustersResponseTypeDef(TypedDict, total=False):
    Clusters: List["ClusterTypeDef"]
    NextToken: str


class DestinationBackupTypeDef(TypedDict, total=False):
    CreateTimestamp: datetime
    SourceRegion: str
    SourceBackup: str
    SourceCluster: str


class _RequiredHsmTypeDef(TypedDict):
    HsmId: str


class HsmTypeDef(_RequiredHsmTypeDef, total=False):
    AvailabilityZone: str
    ClusterId: str
    SubnetId: str
    EniId: str
    EniIp: str
    State: HsmState
    StateMessage: str


class InitializeClusterResponseTypeDef(TypedDict, total=False):
    State: ClusterState
    StateMessage: str


class _RequiredListTagsResponseTypeDef(TypedDict):
    TagList: List["TagTypeDef"]


class ListTagsResponseTypeDef(_RequiredListTagsResponseTypeDef, total=False):
    NextToken: str


class ModifyBackupAttributesResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class ModifyClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RestoreBackupResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str
