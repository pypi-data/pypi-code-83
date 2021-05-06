"""
Type annotations for datasync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datasync/literals.html)

Usage::

    ```python
    from mypy_boto3_datasync.literals import AgentStatus

    data: AgentStatus = "OFFLINE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AgentStatus",
    "Atime",
    "EndpointType",
    "FilterType",
    "Gid",
    "ListAgentsPaginatorName",
    "ListLocationsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTaskExecutionsPaginatorName",
    "ListTasksPaginatorName",
    "LocationFilterName",
    "LogLevel",
    "Mtime",
    "NfsVersion",
    "ObjectStorageServerProtocol",
    "Operator",
    "OverwriteMode",
    "PhaseStatus",
    "PosixPermissions",
    "PreserveDeletedFiles",
    "PreserveDevices",
    "S3StorageClass",
    "SmbVersion",
    "TaskExecutionStatus",
    "TaskFilterName",
    "TaskQueueing",
    "TaskStatus",
    "TransferMode",
    "Uid",
    "VerifyMode",
)


AgentStatus = Literal["OFFLINE", "ONLINE"]
Atime = Literal["BEST_EFFORT", "NONE"]
EndpointType = Literal["FIPS", "PRIVATE_LINK", "PUBLIC"]
FilterType = Literal["SIMPLE_PATTERN"]
Gid = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
ListAgentsPaginatorName = Literal["list_agents"]
ListLocationsPaginatorName = Literal["list_locations"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTaskExecutionsPaginatorName = Literal["list_task_executions"]
ListTasksPaginatorName = Literal["list_tasks"]
LocationFilterName = Literal["CreationTime", "LocationType", "LocationUri"]
LogLevel = Literal["BASIC", "OFF", "TRANSFER"]
Mtime = Literal["NONE", "PRESERVE"]
NfsVersion = Literal["AUTOMATIC", "NFS3", "NFS4_0", "NFS4_1"]
ObjectStorageServerProtocol = Literal["HTTP", "HTTPS"]
Operator = Literal[
    "BeginsWith",
    "Contains",
    "Equals",
    "GreaterThan",
    "GreaterThanOrEqual",
    "In",
    "LessThan",
    "LessThanOrEqual",
    "NotContains",
    "NotEquals",
]
OverwriteMode = Literal["ALWAYS", "NEVER"]
PhaseStatus = Literal["ERROR", "PENDING", "SUCCESS"]
PosixPermissions = Literal["NONE", "PRESERVE"]
PreserveDeletedFiles = Literal["PRESERVE", "REMOVE"]
PreserveDevices = Literal["NONE", "PRESERVE"]
S3StorageClass = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "STANDARD",
    "STANDARD_IA",
]
SmbVersion = Literal["AUTOMATIC", "SMB2", "SMB3"]
TaskExecutionStatus = Literal[
    "ERROR", "LAUNCHING", "PREPARING", "QUEUED", "SUCCESS", "TRANSFERRING", "VERIFYING"
]
TaskFilterName = Literal["CreationTime", "LocationId"]
TaskQueueing = Literal["DISABLED", "ENABLED"]
TaskStatus = Literal["AVAILABLE", "CREATING", "QUEUED", "RUNNING", "UNAVAILABLE"]
TransferMode = Literal["ALL", "CHANGED"]
Uid = Literal["BOTH", "INT_VALUE", "NAME", "NONE"]
VerifyMode = Literal["NONE", "ONLY_FILES_TRANSFERRED", "POINT_IN_TIME_CONSISTENT"]
