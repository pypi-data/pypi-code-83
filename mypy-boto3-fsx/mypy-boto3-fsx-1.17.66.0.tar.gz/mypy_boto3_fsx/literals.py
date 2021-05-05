"""
Type annotations for fsx service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/literals.html)

Usage::

    ```python
    from mypy_boto3_fsx.literals import AdministrativeActionType

    data: AdministrativeActionType = "FILE_SYSTEM_ALIAS_ASSOCIATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdministrativeActionType",
    "AliasLifecycle",
    "AutoImportPolicyType",
    "BackupLifecycle",
    "BackupType",
    "DataRepositoryLifecycle",
    "DataRepositoryTaskFilterName",
    "DataRepositoryTaskLifecycle",
    "DataRepositoryTaskType",
    "DescribeBackupsPaginatorName",
    "DescribeFileSystemsPaginatorName",
    "DriveCacheType",
    "FileSystemLifecycle",
    "FileSystemMaintenanceOperation",
    "FileSystemType",
    "FilterName",
    "ListTagsForResourcePaginatorName",
    "LustreDeploymentType",
    "ReportFormat",
    "ReportScope",
    "Status",
    "StorageType",
    "WindowsDeploymentType",
)


AdministrativeActionType = Literal[
    "FILE_SYSTEM_ALIAS_ASSOCIATION",
    "FILE_SYSTEM_ALIAS_DISASSOCIATION",
    "FILE_SYSTEM_UPDATE",
    "STORAGE_OPTIMIZATION",
]
AliasLifecycle = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
AutoImportPolicyType = Literal["NEW", "NEW_CHANGED", "NONE"]
BackupLifecycle = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETED", "FAILED", "PENDING", "TRANSFERRING"
]
BackupType = Literal["AUTOMATIC", "AWS_BACKUP", "USER_INITIATED"]
DataRepositoryLifecycle = Literal["AVAILABLE", "CREATING", "DELETING", "MISCONFIGURED", "UPDATING"]
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
FileSystemMaintenanceOperation = Literal["BACKING_UP", "PATCHING"]
FileSystemType = Literal["LUSTRE", "WINDOWS"]
FilterName = Literal["backup-type", "file-system-id", "file-system-type"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LustreDeploymentType = Literal["PERSISTENT_1", "SCRATCH_1", "SCRATCH_2"]
ReportFormat = Literal["REPORT_CSV_20191124"]
ReportScope = Literal["FAILED_FILES_ONLY"]
Status = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "UPDATED_OPTIMIZING"]
StorageType = Literal["HDD", "SSD"]
WindowsDeploymentType = Literal["MULTI_AZ_1", "SINGLE_AZ_1", "SINGLE_AZ_2"]
