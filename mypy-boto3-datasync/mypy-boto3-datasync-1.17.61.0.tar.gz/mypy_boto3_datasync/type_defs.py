"""
Main interface for datasync service type definitions.

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
    FilterType,
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
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgentListEntryTypeDef",
    "Ec2ConfigTypeDef",
    "FilterRuleTypeDef",
    "LocationListEntryTypeDef",
    "NfsMountOptionsTypeDef",
    "OnPremConfigTypeDef",
    "OptionsTypeDef",
    "PrivateLinkConfigTypeDef",
    "S3ConfigTypeDef",
    "SmbMountOptionsTypeDef",
    "TagListEntryTypeDef",
    "TaskExecutionListEntryTypeDef",
    "TaskExecutionResultDetailTypeDef",
    "TaskListEntryTypeDef",
    "TaskScheduleTypeDef",
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
    "ListAgentsResponseTypeDef",
    "ListLocationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskExecutionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "LocationFilterTypeDef",
    "PaginatorConfigTypeDef",
    "StartTaskExecutionResponseTypeDef",
    "TaskFilterTypeDef",
)

AgentListEntryTypeDef = TypedDict(
    "AgentListEntryTypeDef", {"AgentArn": str, "Name": str, "Status": AgentStatus}, total=False
)

Ec2ConfigTypeDef = TypedDict("Ec2ConfigTypeDef", {"SubnetArn": str, "SecurityGroupArns": List[str]})

FilterRuleTypeDef = TypedDict(
    "FilterRuleTypeDef", {"FilterType": FilterType, "Value": str}, total=False
)

LocationListEntryTypeDef = TypedDict(
    "LocationListEntryTypeDef", {"LocationArn": str, "LocationUri": str}, total=False
)

NfsMountOptionsTypeDef = TypedDict("NfsMountOptionsTypeDef", {"Version": NfsVersion}, total=False)

OnPremConfigTypeDef = TypedDict("OnPremConfigTypeDef", {"AgentArns": List[str]})

OptionsTypeDef = TypedDict(
    "OptionsTypeDef",
    {
        "VerifyMode": VerifyMode,
        "OverwriteMode": OverwriteMode,
        "Atime": Atime,
        "Mtime": Mtime,
        "Uid": Uid,
        "Gid": Gid,
        "PreserveDeletedFiles": PreserveDeletedFiles,
        "PreserveDevices": PreserveDevices,
        "PosixPermissions": PosixPermissions,
        "BytesPerSecond": int,
        "TaskQueueing": TaskQueueing,
        "LogLevel": LogLevel,
        "TransferMode": TransferMode,
    },
    total=False,
)

PrivateLinkConfigTypeDef = TypedDict(
    "PrivateLinkConfigTypeDef",
    {
        "VpcEndpointId": str,
        "PrivateLinkEndpoint": str,
        "SubnetArns": List[str],
        "SecurityGroupArns": List[str],
    },
    total=False,
)

S3ConfigTypeDef = TypedDict("S3ConfigTypeDef", {"BucketAccessRoleArn": str})

SmbMountOptionsTypeDef = TypedDict("SmbMountOptionsTypeDef", {"Version": SmbVersion}, total=False)

_RequiredTagListEntryTypeDef = TypedDict("_RequiredTagListEntryTypeDef", {"Key": str})
_OptionalTagListEntryTypeDef = TypedDict(
    "_OptionalTagListEntryTypeDef", {"Value": str}, total=False
)


class TagListEntryTypeDef(_RequiredTagListEntryTypeDef, _OptionalTagListEntryTypeDef):
    pass


TaskExecutionListEntryTypeDef = TypedDict(
    "TaskExecutionListEntryTypeDef",
    {"TaskExecutionArn": str, "Status": TaskExecutionStatus},
    total=False,
)

TaskExecutionResultDetailTypeDef = TypedDict(
    "TaskExecutionResultDetailTypeDef",
    {
        "PrepareDuration": int,
        "PrepareStatus": PhaseStatus,
        "TotalDuration": int,
        "TransferDuration": int,
        "TransferStatus": PhaseStatus,
        "VerifyDuration": int,
        "VerifyStatus": PhaseStatus,
        "ErrorCode": str,
        "ErrorDetail": str,
    },
    total=False,
)

TaskListEntryTypeDef = TypedDict(
    "TaskListEntryTypeDef", {"TaskArn": str, "Status": TaskStatus, "Name": str}, total=False
)

TaskScheduleTypeDef = TypedDict("TaskScheduleTypeDef", {"ScheduleExpression": str})

CreateAgentResponseTypeDef = TypedDict("CreateAgentResponseTypeDef", {"AgentArn": str}, total=False)

CreateLocationEfsResponseTypeDef = TypedDict(
    "CreateLocationEfsResponseTypeDef", {"LocationArn": str}, total=False
)

CreateLocationFsxWindowsResponseTypeDef = TypedDict(
    "CreateLocationFsxWindowsResponseTypeDef", {"LocationArn": str}, total=False
)

CreateLocationNfsResponseTypeDef = TypedDict(
    "CreateLocationNfsResponseTypeDef", {"LocationArn": str}, total=False
)

CreateLocationObjectStorageResponseTypeDef = TypedDict(
    "CreateLocationObjectStorageResponseTypeDef", {"LocationArn": str}, total=False
)

CreateLocationS3ResponseTypeDef = TypedDict(
    "CreateLocationS3ResponseTypeDef", {"LocationArn": str}, total=False
)

CreateLocationSmbResponseTypeDef = TypedDict(
    "CreateLocationSmbResponseTypeDef", {"LocationArn": str}, total=False
)

CreateTaskResponseTypeDef = TypedDict("CreateTaskResponseTypeDef", {"TaskArn": str}, total=False)

DescribeAgentResponseTypeDef = TypedDict(
    "DescribeAgentResponseTypeDef",
    {
        "AgentArn": str,
        "Name": str,
        "Status": AgentStatus,
        "LastConnectionTime": datetime,
        "CreationTime": datetime,
        "EndpointType": EndpointType,
        "PrivateLinkConfig": "PrivateLinkConfigTypeDef",
    },
    total=False,
)

DescribeLocationEfsResponseTypeDef = TypedDict(
    "DescribeLocationEfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "Ec2Config": "Ec2ConfigTypeDef",
        "CreationTime": datetime,
    },
    total=False,
)

DescribeLocationFsxWindowsResponseTypeDef = TypedDict(
    "DescribeLocationFsxWindowsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "SecurityGroupArns": List[str],
        "CreationTime": datetime,
        "User": str,
        "Domain": str,
    },
    total=False,
)

DescribeLocationNfsResponseTypeDef = TypedDict(
    "DescribeLocationNfsResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "OnPremConfig": "OnPremConfigTypeDef",
        "MountOptions": "NfsMountOptionsTypeDef",
        "CreationTime": datetime,
    },
    total=False,
)

DescribeLocationObjectStorageResponseTypeDef = TypedDict(
    "DescribeLocationObjectStorageResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AccessKey": str,
        "ServerPort": int,
        "ServerProtocol": ObjectStorageServerProtocol,
        "AgentArns": List[str],
        "CreationTime": datetime,
    },
    total=False,
)

DescribeLocationS3ResponseTypeDef = TypedDict(
    "DescribeLocationS3ResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "S3StorageClass": S3StorageClass,
        "S3Config": "S3ConfigTypeDef",
        "AgentArns": List[str],
        "CreationTime": datetime,
    },
    total=False,
)

DescribeLocationSmbResponseTypeDef = TypedDict(
    "DescribeLocationSmbResponseTypeDef",
    {
        "LocationArn": str,
        "LocationUri": str,
        "AgentArns": List[str],
        "User": str,
        "Domain": str,
        "MountOptions": "SmbMountOptionsTypeDef",
        "CreationTime": datetime,
    },
    total=False,
)

DescribeTaskExecutionResponseTypeDef = TypedDict(
    "DescribeTaskExecutionResponseTypeDef",
    {
        "TaskExecutionArn": str,
        "Status": TaskExecutionStatus,
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Includes": List["FilterRuleTypeDef"],
        "StartTime": datetime,
        "EstimatedFilesToTransfer": int,
        "EstimatedBytesToTransfer": int,
        "FilesTransferred": int,
        "BytesWritten": int,
        "BytesTransferred": int,
        "Result": "TaskExecutionResultDetailTypeDef",
    },
    total=False,
)

DescribeTaskResponseTypeDef = TypedDict(
    "DescribeTaskResponseTypeDef",
    {
        "TaskArn": str,
        "Status": TaskStatus,
        "Name": str,
        "CurrentTaskExecutionArn": str,
        "SourceLocationArn": str,
        "DestinationLocationArn": str,
        "CloudWatchLogGroupArn": str,
        "SourceNetworkInterfaceArns": List[str],
        "DestinationNetworkInterfaceArns": List[str],
        "Options": "OptionsTypeDef",
        "Excludes": List["FilterRuleTypeDef"],
        "Schedule": "TaskScheduleTypeDef",
        "ErrorCode": str,
        "ErrorDetail": str,
        "CreationTime": datetime,
    },
    total=False,
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {"Agents": List["AgentListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListLocationsResponseTypeDef = TypedDict(
    "ListLocationsResponseTypeDef",
    {"Locations": List["LocationListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListTaskExecutionsResponseTypeDef = TypedDict(
    "ListTaskExecutionsResponseTypeDef",
    {"TaskExecutions": List["TaskExecutionListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef",
    {"Tasks": List["TaskListEntryTypeDef"], "NextToken": str},
    total=False,
)

LocationFilterTypeDef = TypedDict(
    "LocationFilterTypeDef", {"Name": LocationFilterName, "Values": List[str], "Operator": Operator}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartTaskExecutionResponseTypeDef = TypedDict(
    "StartTaskExecutionResponseTypeDef", {"TaskExecutionArn": str}, total=False
)

TaskFilterTypeDef = TypedDict(
    "TaskFilterTypeDef", {"Name": TaskFilterName, "Values": List[str], "Operator": Operator}
)
