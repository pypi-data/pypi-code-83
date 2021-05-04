"""
Type annotations for cloudhsmv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.literals import BackupPolicy

    data: BackupPolicy = "DEFAULT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BackupPolicy",
    "BackupRetentionType",
    "BackupState",
    "ClusterState",
    "DescribeBackupsPaginatorName",
    "DescribeClustersPaginatorName",
    "HsmState",
    "ListTagsPaginatorName",
)


BackupPolicy = Literal["DEFAULT"]
BackupRetentionType = Literal["DAYS"]
BackupState = Literal["CREATE_IN_PROGRESS", "DELETED", "PENDING_DELETION", "READY"]
ClusterState = Literal[
    "ACTIVE",
    "CREATE_IN_PROGRESS",
    "DEGRADED",
    "DELETED",
    "DELETE_IN_PROGRESS",
    "INITIALIZED",
    "INITIALIZE_IN_PROGRESS",
    "UNINITIALIZED",
    "UPDATE_IN_PROGRESS",
]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
HsmState = Literal["ACTIVE", "CREATE_IN_PROGRESS", "DEGRADED", "DELETED", "DELETE_IN_PROGRESS"]
ListTagsPaginatorName = Literal["list_tags"]
