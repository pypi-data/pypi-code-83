"""
Main interface for fsx service literal definitions.

Usage::

    ```python
    from mypy_boto3_fsx.literals import AliasLifecycle

    data: AliasLifecycle = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AliasLifecycle",
    "AutoImportPolicyType",
    "BackupLifecycle",
    "BackupType",
    "DataRepositoryTaskFilterName",
    "DataRepositoryTaskLifecycle",
    "DataRepositoryTaskType",
    "DescribeBackupsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DriveCacheType",
    "FileSystemLifecycle",
    "FileSystemType",
    "FilterName",
    "ListTagsForResourcePaginatorName",
    "LustreDeploymentType",
    "ReportFormat",
    "ReportScope",
    "StorageType",
    "WindowsDeploymentType",
)


AliasLifecycle = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyType = Literal["NEW", "NEW_CHANGED", "NONE"]
BackupLifecycle = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETED", "FAILED", "PENDING", "TRANSFERRING"
]
BackupType = Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"]
DataRepositoryTaskFilterName = Literal["file-system-id", "task-lifecycle"]
DataRepositoryTaskLifecycle = Literal[
    "CANCELED", "CANCELING", "EXECUTING", "FAILED", "PENDING", "SUCCEEDED"
]
DataRepositoryTaskType = Literal["EXPORT_TO_REPOSITORY"]
DescribeBackupsPaginatorName = Literal["describe_backups"]
DescribeFileSystemsPaginatorName = Literal["describe_file_systems"]
DriveCacheType = Literal["NONE", "READ"]
FileSystemLifecycle = Literal[
    "AVAILABLE", "CREATING", "DELETING", "FAILED", "MISCONFIGURED", "UPDATING"
]
FileSystemType = Literal["LUSTRE", "WINDOWS"]
FilterName = Literal["backup-type", "file-system-id", "file-system-type"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LustreDeploymentType = Literal["PERSISTENT_1", "SCRATCH_1", "SCRATCH_2"]
ReportFormat = Literal["REPORT_CSV_20191124"]
ReportScope = Literal["FAILED_FILES_ONLY"]
StorageType = Literal["HDD", "SSD"]
WindowsDeploymentType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
