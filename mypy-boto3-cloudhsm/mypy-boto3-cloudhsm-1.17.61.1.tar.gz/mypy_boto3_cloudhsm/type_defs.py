"""
Type annotations for cloudhsm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsm.type_defs import AddTagsToResourceResponseTypeDef

    data: AddTagsToResourceResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_cloudhsm.literals import CloudHsmObjectState, HsmStatus

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsToResourceResponseTypeDef",
    "CreateHapgResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "CreateLunaClientResponseTypeDef",
    "DeleteHapgResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteLunaClientResponseTypeDef",
    "DescribeHapgResponseTypeDef",
    "DescribeHsmResponseTypeDef",
    "DescribeLunaClientResponseTypeDef",
    "GetConfigResponseTypeDef",
    "ListAvailableZonesResponseTypeDef",
    "ListHapgsResponseTypeDef",
    "ListHsmsResponseTypeDef",
    "ListLunaClientsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyHapgResponseTypeDef",
    "ModifyHsmResponseTypeDef",
    "ModifyLunaClientResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveTagsFromResourceResponseTypeDef",
    "TagTypeDef",
)


class AddTagsToResourceResponseTypeDef(TypedDict):
    Status: str


class CreateHapgResponseTypeDef(TypedDict, total=False):
    HapgArn: str


class CreateHsmResponseTypeDef(TypedDict, total=False):
    HsmArn: str


class CreateLunaClientResponseTypeDef(TypedDict, total=False):
    ClientArn: str


class DeleteHapgResponseTypeDef(TypedDict):
    Status: str


class DeleteHsmResponseTypeDef(TypedDict):
    Status: str


class DeleteLunaClientResponseTypeDef(TypedDict):
    Status: str


class DescribeHapgResponseTypeDef(TypedDict, total=False):
    HapgArn: str
    HapgSerial: str
    HsmsLastActionFailed: List[str]
    HsmsPendingDeletion: List[str]
    HsmsPendingRegistration: List[str]
    Label: str
    LastModifiedTimestamp: str
    PartitionSerialList: List[str]
    State: CloudHsmObjectState


class DescribeHsmResponseTypeDef(TypedDict, total=False):
    HsmArn: str
    Status: HsmStatus
    StatusDetails: str
    AvailabilityZone: str
    EniId: str
    EniIp: str
    SubscriptionType: Literal["PRODUCTION"]
    SubscriptionStartDate: str
    SubscriptionEndDate: str
    VpcId: str
    SubnetId: str
    IamRoleArn: str
    SerialNumber: str
    VendorName: str
    HsmType: str
    SoftwareVersion: str
    SshPublicKey: str
    SshKeyLastUpdated: str
    ServerCertUri: str
    ServerCertLastUpdated: str
    Partitions: List[str]


class DescribeLunaClientResponseTypeDef(TypedDict, total=False):
    ClientArn: str
    Certificate: str
    CertificateFingerprint: str
    LastModifiedTimestamp: str
    Label: str


class GetConfigResponseTypeDef(TypedDict, total=False):
    ConfigType: str
    ConfigFile: str
    ConfigCred: str


class ListAvailableZonesResponseTypeDef(TypedDict, total=False):
    AZList: List[str]


class _RequiredListHapgsResponseTypeDef(TypedDict):
    HapgList: List[str]


class ListHapgsResponseTypeDef(_RequiredListHapgsResponseTypeDef, total=False):
    NextToken: str


class ListHsmsResponseTypeDef(TypedDict, total=False):
    HsmList: List[str]
    NextToken: str


class _RequiredListLunaClientsResponseTypeDef(TypedDict):
    ClientList: List[str]


class ListLunaClientsResponseTypeDef(_RequiredListLunaClientsResponseTypeDef, total=False):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict):
    TagList: List["TagTypeDef"]


class ModifyHapgResponseTypeDef(TypedDict, total=False):
    HapgArn: str


class ModifyHsmResponseTypeDef(TypedDict, total=False):
    HsmArn: str


class ModifyLunaClientResponseTypeDef(TypedDict, total=False):
    ClientArn: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RemoveTagsFromResourceResponseTypeDef(TypedDict):
    Status: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str
