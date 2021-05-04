"""
Type annotations for opsworkscm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_opsworkscm.literals import (
    BackupStatus,
    BackupType,
    MaintenanceStatus,
    NodeAssociationStatus,
    ServerStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAttributeTypeDef",
    "AssociateNodeResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceResponseTypeDef",
    "TagTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)


class AccountAttributeTypeDef(TypedDict, total=False):
    Name: str
    Maximum: int
    Used: int


class AssociateNodeResponseTypeDef(TypedDict, total=False):
    NodeAssociationStatusToken: str


class BackupTypeDef(TypedDict, total=False):
    BackupArn: str
    BackupId: str
    BackupType: BackupType
    CreatedAt: datetime
    Description: str
    Engine: str
    EngineModel: str
    EngineVersion: str
    InstanceProfileArn: str
    InstanceType: str
    KeyPair: str
    PreferredBackupWindow: str
    PreferredMaintenanceWindow: str
    S3DataSize: int
    S3DataUrl: str
    S3LogUrl: str
    SecurityGroupIds: List[str]
    ServerName: str
    ServiceRoleArn: str
    Status: BackupStatus
    StatusDescription: str
    SubnetIds: List[str]
    ToolsVersion: str
    UserArn: str


class CreateBackupResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class CreateServerResponseTypeDef(TypedDict, total=False):
    Server: "ServerTypeDef"


class DescribeAccountAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AccountAttributeTypeDef"]


class DescribeBackupsResponseTypeDef(TypedDict, total=False):
    Backups: List["BackupTypeDef"]
    NextToken: str


class DescribeEventsResponseTypeDef(TypedDict, total=False):
    ServerEvents: List["ServerEventTypeDef"]
    NextToken: str


class DescribeNodeAssociationStatusResponseTypeDef(TypedDict, total=False):
    NodeAssociationStatus: NodeAssociationStatus
    EngineAttributes: List["EngineAttributeTypeDef"]


class DescribeServersResponseTypeDef(TypedDict, total=False):
    Servers: List["ServerTypeDef"]
    NextToken: str


class DisassociateNodeResponseTypeDef(TypedDict, total=False):
    NodeAssociationStatusToken: str


class EngineAttributeTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class ExportServerEngineAttributeResponseTypeDef(TypedDict, total=False):
    EngineAttribute: "EngineAttributeTypeDef"
    ServerName: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ServerEventTypeDef(TypedDict, total=False):
    CreatedAt: datetime
    ServerName: str
    Message: str
    LogUrl: str


class ServerTypeDef(TypedDict, total=False):
    AssociatePublicIpAddress: bool
    BackupRetentionCount: int
    ServerName: str
    CreatedAt: datetime
    CloudFormationStackArn: str
    CustomDomain: str
    DisableAutomatedBackup: bool
    Endpoint: str
    Engine: str
    EngineModel: str
    EngineAttributes: List["EngineAttributeTypeDef"]
    EngineVersion: str
    InstanceProfileArn: str
    InstanceType: str
    KeyPair: str
    MaintenanceStatus: MaintenanceStatus
    PreferredMaintenanceWindow: str
    PreferredBackupWindow: str
    SecurityGroupIds: List[str]
    ServiceRoleArn: str
    Status: ServerStatus
    StatusReason: str
    SubnetIds: List[str]
    ServerArn: str


class StartMaintenanceResponseTypeDef(TypedDict, total=False):
    Server: "ServerTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateServerEngineAttributesResponseTypeDef(TypedDict, total=False):
    Server: "ServerTypeDef"


class UpdateServerResponseTypeDef(TypedDict, total=False):
    Server: "ServerTypeDef"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
