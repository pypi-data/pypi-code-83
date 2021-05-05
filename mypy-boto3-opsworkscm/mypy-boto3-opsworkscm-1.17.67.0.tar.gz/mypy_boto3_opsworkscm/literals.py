"""
Type annotations for opsworkscm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/literals.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.literals import BackupStatus

    data: BackupStatus = "DELETING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BackupStatus",
    "BackupType",
    "DescribeBackupsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeServersPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MaintenanceStatus",
    "NodeAssociatedWaiterName",
    "NodeAssociationStatus",
    "ServerStatus",
)


BackupStatus = Literal["DELETING", "FAILED", "IN_PROGRESS", "OK"]
BackupType = Literal["AUTOMATED", "MANUAL"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeServersPaginatorName = Literal["describe_servers"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MaintenanceStatus = Literal["FAILED", "SUCCESS"]
NodeAssociatedWaiterName = Literal["node_associated"]
NodeAssociationStatus = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ServerStatus = Literal[
    "BACKING_UP",
    "CONNECTION_LOST",
    "CREATING",
    "DELETING",
    "FAILED",
    "HEALTHY",
    "MODIFYING",
    "RESTORING",
    "RUNNING",
    "SETUP",
    "TERMINATED",
    "UNDER_MAINTENANCE",
    "UNHEALTHY",
]
