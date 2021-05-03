"""
Type annotations for datasync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datasync.type_defs import AgentListEntryTypeDef

    data: AgentListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_datasync.literals import (
    AgentStatus,
    Atime,
    EndpointType,
    Gid,
    LocationFilterName,
    LogLevel,
    Mtime,
    NfsVersion,
    ObjectStorageServerProtocol,
    Operator,
    OverwriteMode,
    PhaseStatus,
    PosixPermissions,
    PreserveDeletedFiles,
    PreserveDevices,
    S3StorageClass,
    SmbVersion,
    TaskExecutionStatus,
    TaskFilterName,
    TaskQueueing,
    TaskStatus,
    TransferMode,
    Uid,
    VerifyMode,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgentListEntryTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateLocationEfsResponseTypeDef",
    "CreateLocationFsxWindowsResponseTypeDef",
    "CreateLocationNfsResponseTypeDef",
    "CreateLocationObjectStorageResponseTypeDef",
    "CreateLocationS3ResponseTypeDef",
    "CreateLocationSmbResponseTypeDef",
    "CreateTaskResponseTypeDef",
    "DescribeAgentResponseTypeDef",
    "DescribeLocationEfsResponseTypeDef",
    "DescribeLocationFsxWindowsResponseTypeDef",
    "DescribeLocationNfsResponseTypeDef",
    "DescribeLocationObjectStorageResponseTypeDef",
    "DescribeLocationS3ResponseTypeDef",
    "DescribeLocationSmbResponseTypeDef",
    "DescribeTaskExecutionResponseTypeDef",
    "DescribeTaskResponseTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "ListAgentsResponseTypeDef",
    "ListLocationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "LocationListEntryTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateLinkConfigTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "TagListEntryTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskFilterTypeDef",
    "TaskListEntryTypeDef",
    "TaskScheduleTypeDef",
)


class AgentListEntryTypeDef(TypedDict, total=False):
    AgentArn: str
    Name: str
    Status: AgentStatus


class CreateAgentResponseTypeDef(TypedDict, total=False):
    AgentArn: str


class CreateLocationEfsResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateLocationFsxWindowsResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateLocationNfsResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateLocationObjectStorageResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateLocationS3ResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateLocationSmbResponseTypeDef(TypedDict, total=False):
    LocationArn: str


class CreateTaskResponseTypeDef(TypedDict, total=False):
    TaskArn: str


class DescribeAgentResponseTypeDef(TypedDict, total=False):
    AgentArn: str
    Name: str
    Status: AgentStatus
    LastConnectionTime: datetime
    CreationTime: datetime
    EndpointType: EndpointType
    PrivateLinkConfig: "PrivateLinkConfigTypeDef"


class DescribeLocationEfsResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    Ec2Config: "Ec2ConfigTypeDef"
    CreationTime: datetime


class DescribeLocationFsxWindowsResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    SecurityGroupArns: List[str]
    CreationTime: datetime
    User: str
    Domain: str


class DescribeLocationNfsResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    OnPremConfig: "OnPremConfigTypeDef"
    MountOptions: "NfsMountOptionsTypeDef"
    CreationTime: datetime


class DescribeLocationObjectStorageResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    AccessKey: str
    ServerPort: int
    ServerProtocol: ObjectStorageServerProtocol
    AgentArns: List[str]
    CreationTime: datetime


class DescribeLocationS3ResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    S3StorageClass: S3StorageClass
    S3Config: "S3ConfigTypeDef"
    AgentArns: List[str]
    CreationTime: datetime


class DescribeLocationSmbResponseTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str
    AgentArns: List[str]
    User: str
    Domain: str
    MountOptions: "SmbMountOptionsTypeDef"
    CreationTime: datetime


class DescribeTaskExecutionResponseTypeDef(TypedDict, total=False):
    TaskExecutionArn: str
    Status: TaskExecutionStatus
    Options: "OptionsTypeDef"
    Excludes: List["FilterRuleTypeDef"]
    Includes: List["FilterRuleTypeDef"]
    StartTime: datetime
    EstimatedFilesToTransfer: int
    EstimatedBytesToTransfer: int
    FilesTransferred: int
    BytesWritten: int
    BytesTransferred: int
    Result: "TaskExecutionResultDetailTypeDef"


class DescribeTaskResponseTypeDef(TypedDict, total=False):
    TaskArn: str
    Status: TaskStatus
    Name: str
    CurrentTaskExecutionArn: str
    SourceLocationArn: str
    DestinationLocationArn: str
    CloudWatchLogGroupArn: str
    SourceNetworkInterfaceArns: List[str]
    DestinationNetworkInterfaceArns: List[str]
    Options: "OptionsTypeDef"
    Excludes: List["FilterRuleTypeDef"]
    Schedule: "TaskScheduleTypeDef"
    ErrorCode: str
    ErrorDetail: str
    CreationTime: datetime


class Ec2ConfigTypeDef(TypedDict):
    SubnetArn: str
    SecurityGroupArns: List[str]


class FilterRuleTypeDef(TypedDict, total=False):
    FilterType: Literal["SIMPLE_PATTERN"]
    Value: str


class ListAgentsResponseTypeDef(TypedDict, total=False):
    Agents: List["AgentListEntryTypeDef"]
    NextToken: str


class ListLocationsResponseTypeDef(TypedDict, total=False):
    Locations: List["LocationListEntryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagListEntryTypeDef"]
    NextToken: str


class ListTaskExecutionsResponseTypeDef(TypedDict, total=False):
    TaskExecutions: List["TaskExecutionListEntryTypeDef"]
    NextToken: str


class ListTasksResponseTypeDef(TypedDict, total=False):
    Tasks: List["TaskListEntryTypeDef"]
    NextToken: str


class LocationFilterTypeDef(TypedDict):
    Name: LocationFilterName
    Values: List[str]
    Operator: Operator


class LocationListEntryTypeDef(TypedDict, total=False):
    LocationArn: str
    LocationUri: str


class NfsMountOptionsTypeDef(TypedDict, total=False):
    Version: NfsVersion


class OnPremConfigTypeDef(TypedDict):
    AgentArns: List[str]


class OptionsTypeDef(TypedDict, total=False):
    VerifyMode: VerifyMode
    OverwriteMode: OverwriteMode
    Atime: Atime
    Mtime: Mtime
    Uid: Uid
    Gid: Gid
    PreserveDeletedFiles: PreserveDeletedFiles
    PreserveDevices: PreserveDevices
    PosixPermissions: PosixPermissions
    BytesPerSecond: int
    TaskQueueing: TaskQueueing
    LogLevel: LogLevel
    TransferMode: TransferMode


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PrivateLinkConfigTypeDef(TypedDict, total=False):
    VpcEndpointId: str
    PrivateLinkEndpoint: str
    SubnetArns: List[str]
    SecurityGroupArns: List[str]


class S3ConfigTypeDef(TypedDict):
    BucketAccessRoleArn: str


class SmbMountOptionsTypeDef(TypedDict, total=False):
    Version: SmbVersion


class StartTaskExecutionResponseTypeDef(TypedDict, total=False):
    TaskExecutionArn: str


class _RequiredTagListEntryTypeDef(TypedDict):
    Key: str


class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, total=False):
    Value: str


class TaskExecutionListEntryTypeDef(TypedDict, total=False):
    TaskExecutionArn: str
    Status: TaskExecutionStatus


class TaskExecutionResultDetailTypeDef(TypedDict, total=False):
    PrepareDuration: int
    PrepareStatus: PhaseStatus
    TotalDuration: int
    TransferDuration: int
    TransferStatus: PhaseStatus
    VerifyDuration: int
    VerifyStatus: PhaseStatus
    ErrorCode: str
    ErrorDetail: str


class TaskFilterTypeDef(TypedDict):
    Name: TaskFilterName
    Values: List[str]
    Operator: Operator


class TaskListEntryTypeDef(TypedDict, total=False):
    TaskArn: str
    Status: TaskStatus
    Name: str


class TaskScheduleTypeDef(TypedDict):
    ScheduleExpression: str
