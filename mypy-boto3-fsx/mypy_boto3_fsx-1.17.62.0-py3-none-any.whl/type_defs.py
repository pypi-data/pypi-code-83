"""
Main interface for fsx service type definitions.

Usage::

    ```python
    from mypy_boto3_fsx.type_defs import ActiveDirectoryBackupAttributesTypeDef

    data: ActiveDirectoryBackupAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_fsx.literals import (
    AdministrativeActionType,
    AliasLifecycle,
    AutoImportPolicyType,
    BackupLifecycle,
    BackupType,
    DataRepositoryLifecycle,
    DataRepositoryTaskFilterName,
    DataRepositoryTaskLifecycle,
    DataRepositoryTaskType,
    DriveCacheType,
    FileSystemLifecycle,
    FileSystemMaintenanceOperation,
    FileSystemType,
    FilterName,
    LustreDeploymentType,
    ReportFormat,
    ReportScope,
    Status,
    StorageType,
    WindowsDeploymentType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CompletionReportTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "TagTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "FileSystemTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
)

ActiveDirectoryBackupAttributesTypeDef = TypedDict(
    "ActiveDirectoryBackupAttributesTypeDef",
    {"DomainName": str, "ActiveDirectoryId": str, "ResourceARN": str},
    total=False,
)

AdministrativeActionFailureDetailsTypeDef = TypedDict(
    "AdministrativeActionFailureDetailsTypeDef", {"Message": str}, total=False
)

AdministrativeActionTypeDef = TypedDict(
    "AdministrativeActionTypeDef",
    {
        "AdministrativeActionType": AdministrativeActionType,
        "ProgressPercent": int,
        "RequestTime": datetime,
        "Status": Status,
        "TargetFileSystemValues": Dict[str, Any],
        "FailureDetails": "AdministrativeActionFailureDetailsTypeDef",
    },
    total=False,
)

AliasTypeDef = TypedDict("AliasTypeDef", {"Name": str, "Lifecycle": AliasLifecycle}, total=False)

BackupFailureDetailsTypeDef = TypedDict(
    "BackupFailureDetailsTypeDef", {"Message": str}, total=False
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycle,
        "Type": BackupType,
        "CreationTime": datetime,
        "FileSystem": Dict[str, Any],
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "FailureDetails": "BackupFailureDetailsTypeDef",
        "ProgressPercent": int,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "DirectoryInformation": "ActiveDirectoryBackupAttributesTypeDef",
        "OwnerId": str,
        "SourceBackupId": str,
        "SourceBackupRegion": str,
    },
    total=False,
)


class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass


_RequiredCompletionReportTypeDef = TypedDict("_RequiredCompletionReportTypeDef", {"Enabled": bool})
_OptionalCompletionReportTypeDef = TypedDict(
    "_OptionalCompletionReportTypeDef",
    {"Path": str, "Format": ReportFormat, "Scope": ReportScope},
    total=False,
)


class CompletionReportTypeDef(_RequiredCompletionReportTypeDef, _OptionalCompletionReportTypeDef):
    pass


DataRepositoryConfigurationTypeDef = TypedDict(
    "DataRepositoryConfigurationTypeDef",
    {
        "Lifecycle": DataRepositoryLifecycle,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "AutoImportPolicy": AutoImportPolicyType,
        "FailureDetails": "DataRepositoryFailureDetailsTypeDef",
    },
    total=False,
)

DataRepositoryFailureDetailsTypeDef = TypedDict(
    "DataRepositoryFailureDetailsTypeDef", {"Message": str}, total=False
)

DataRepositoryTaskFailureDetailsTypeDef = TypedDict(
    "DataRepositoryTaskFailureDetailsTypeDef", {"Message": str}, total=False
)

DataRepositoryTaskStatusTypeDef = TypedDict(
    "DataRepositoryTaskStatusTypeDef",
    {"TotalCount": int, "SucceededCount": int, "FailedCount": int, "LastUpdatedTime": datetime},
    total=False,
)

_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycle,
        "Type": DataRepositoryTaskType,
        "CreationTime": datetime,
        "FileSystemId": str,
    },
)
_OptionalDataRepositoryTaskTypeDef = TypedDict(
    "_OptionalDataRepositoryTaskTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "Paths": List[str],
        "FailureDetails": "DataRepositoryTaskFailureDetailsTypeDef",
        "Status": "DataRepositoryTaskStatusTypeDef",
        "Report": "CompletionReportTypeDef",
    },
    total=False,
)


class DataRepositoryTaskTypeDef(
    _RequiredDataRepositoryTaskTypeDef, _OptionalDataRepositoryTaskTypeDef
):
    pass


DeleteFileSystemLustreResponseTypeDef = TypedDict(
    "DeleteFileSystemLustreResponseTypeDef",
    {"FinalBackupId": str, "FinalBackupTags": List["TagTypeDef"]},
    total=False,
)

DeleteFileSystemWindowsResponseTypeDef = TypedDict(
    "DeleteFileSystemWindowsResponseTypeDef",
    {"FinalBackupId": str, "FinalBackupTags": List["TagTypeDef"]},
    total=False,
)

FileSystemFailureDetailsTypeDef = TypedDict(
    "FileSystemFailureDetailsTypeDef", {"Message": str}, total=False
)

LustreFileSystemConfigurationTypeDef = TypedDict(
    "LustreFileSystemConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DataRepositoryConfiguration": "DataRepositoryConfigurationTypeDef",
        "DeploymentType": LustreDeploymentType,
        "PerUnitStorageThroughput": int,
        "MountName": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheType,
    },
    total=False,
)

SelfManagedActiveDirectoryAttributesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryAttributesTypeDef",
    {
        "DomainName": str,
        "OrganizationalUnitDistinguishedName": str,
        "FileSystemAdministratorsGroup": str,
        "UserName": str,
        "DnsIps": List[str],
    },
    total=False,
)

_RequiredSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_RequiredSelfManagedActiveDirectoryConfigurationTypeDef",
    {"DomainName": str, "UserName": str, "Password": str, "DnsIps": List[str]},
)
_OptionalSelfManagedActiveDirectoryConfigurationTypeDef = TypedDict(
    "_OptionalSelfManagedActiveDirectoryConfigurationTypeDef",
    {"OrganizationalUnitDistinguishedName": str, "FileSystemAdministratorsGroup": str},
    total=False,
)


class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef,
    _OptionalSelfManagedActiveDirectoryConfigurationTypeDef,
):
    pass


SelfManagedActiveDirectoryConfigurationUpdatesTypeDef = TypedDict(
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    {"UserName": str, "Password": str, "DnsIps": List[str]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

WindowsFileSystemConfigurationTypeDef = TypedDict(
    "WindowsFileSystemConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryAttributesTypeDef",
        "DeploymentType": WindowsDeploymentType,
        "RemoteAdministrationEndpoint": str,
        "PreferredSubnetId": str,
        "PreferredFileServerIp": str,
        "ThroughputCapacity": int,
        "MaintenanceOperationsInProgress": List[FileSystemMaintenanceOperation],
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List["AliasTypeDef"],
    },
    total=False,
)

AssociateFileSystemAliasesResponseTypeDef = TypedDict(
    "AssociateFileSystemAliasesResponseTypeDef", {"Aliases": List["AliasTypeDef"]}, total=False
)

CancelDataRepositoryTaskResponseTypeDef = TypedDict(
    "CancelDataRepositoryTaskResponseTypeDef",
    {"Lifecycle": DataRepositoryTaskLifecycle, "TaskId": str},
    total=False,
)

CopyBackupResponseTypeDef = TypedDict(
    "CopyBackupResponseTypeDef", {"Backup": "BackupTypeDef"}, total=False
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef", {"Backup": "BackupTypeDef"}, total=False
)

CreateDataRepositoryTaskResponseTypeDef = TypedDict(
    "CreateDataRepositoryTaskResponseTypeDef",
    {"DataRepositoryTask": "DataRepositoryTaskTypeDef"},
    total=False,
)

CreateFileSystemFromBackupResponseTypeDef = TypedDict(
    "CreateFileSystemFromBackupResponseTypeDef", {"FileSystem": Dict[str, Any]}, total=False
)

CreateFileSystemLustreConfigurationTypeDef = TypedDict(
    "CreateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "ImportPath": str,
        "ExportPath": str,
        "ImportedFileChunkSize": int,
        "DeploymentType": LustreDeploymentType,
        "AutoImportPolicy": AutoImportPolicyType,
        "PerUnitStorageThroughput": int,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "DriveCacheType": DriveCacheType,
    },
    total=False,
)

CreateFileSystemResponseTypeDef = TypedDict(
    "CreateFileSystemResponseTypeDef", {"FileSystem": Dict[str, Any]}, total=False
)

_RequiredCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_RequiredCreateFileSystemWindowsConfigurationTypeDef", {"ThroughputCapacity": int}
)
_OptionalCreateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "_OptionalCreateFileSystemWindowsConfigurationTypeDef",
    {
        "ActiveDirectoryId": str,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationTypeDef",
        "DeploymentType": WindowsDeploymentType,
        "PreferredSubnetId": str,
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "CopyTagsToBackups": bool,
        "Aliases": List[str],
    },
    total=False,
)


class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef,
    _OptionalCreateFileSystemWindowsConfigurationTypeDef,
):
    pass


DataRepositoryTaskFilterTypeDef = TypedDict(
    "DataRepositoryTaskFilterTypeDef",
    {"Name": DataRepositoryTaskFilterName, "Values": List[str]},
    total=False,
)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef", {"BackupId": str, "Lifecycle": BackupLifecycle}, total=False
)

DeleteFileSystemLustreConfigurationTypeDef = TypedDict(
    "DeleteFileSystemLustreConfigurationTypeDef",
    {"SkipFinalBackup": bool, "FinalBackupTags": List["TagTypeDef"]},
    total=False,
)

DeleteFileSystemResponseTypeDef = TypedDict(
    "DeleteFileSystemResponseTypeDef",
    {
        "FileSystemId": str,
        "Lifecycle": FileSystemLifecycle,
        "WindowsResponse": "DeleteFileSystemWindowsResponseTypeDef",
        "LustreResponse": "DeleteFileSystemLustreResponseTypeDef",
    },
    total=False,
)

DeleteFileSystemWindowsConfigurationTypeDef = TypedDict(
    "DeleteFileSystemWindowsConfigurationTypeDef",
    {"SkipFinalBackup": bool, "FinalBackupTags": List["TagTypeDef"]},
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List["BackupTypeDef"], "NextToken": str},
    total=False,
)

DescribeDataRepositoryTasksResponseTypeDef = TypedDict(
    "DescribeDataRepositoryTasksResponseTypeDef",
    {"DataRepositoryTasks": List["DataRepositoryTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeFileSystemAliasesResponseTypeDef = TypedDict(
    "DescribeFileSystemAliasesResponseTypeDef",
    {"Aliases": List["AliasTypeDef"], "NextToken": str},
    total=False,
)

DescribeFileSystemsResponseTypeDef = TypedDict(
    "DescribeFileSystemsResponseTypeDef",
    {"FileSystems": List[Dict[str, Any]], "NextToken": str},
    total=False,
)

FileSystemTypeDef = TypedDict(
    "FileSystemTypeDef",
    {
        "OwnerId": str,
        "CreationTime": datetime,
        "FileSystemId": str,
        "FileSystemType": FileSystemType,
        "Lifecycle": FileSystemLifecycle,
        "FailureDetails": "FileSystemFailureDetailsTypeDef",
        "StorageCapacity": int,
        "StorageType": StorageType,
        "VpcId": str,
        "SubnetIds": List[str],
        "NetworkInterfaceIds": List[str],
        "DNSName": str,
        "KmsKeyId": str,
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "WindowsConfiguration": "WindowsFileSystemConfigurationTypeDef",
        "LustreConfiguration": "LustreFileSystemConfigurationTypeDef",
        "AdministrativeActions": List["AdministrativeActionTypeDef"],
    },
    total=False,
)

DisassociateFileSystemAliasesResponseTypeDef = TypedDict(
    "DisassociateFileSystemAliasesResponseTypeDef", {"Aliases": List["AliasTypeDef"]}, total=False
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": FilterName, "Values": List[str]}, total=False)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateFileSystemLustreConfigurationTypeDef = TypedDict(
    "UpdateFileSystemLustreConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "AutoImportPolicy": AutoImportPolicyType,
    },
    total=False,
)

UpdateFileSystemResponseTypeDef = TypedDict(
    "UpdateFileSystemResponseTypeDef", {"FileSystem": Dict[str, Any]}, total=False
)

UpdateFileSystemWindowsConfigurationTypeDef = TypedDict(
    "UpdateFileSystemWindowsConfigurationTypeDef",
    {
        "WeeklyMaintenanceStartTime": str,
        "DailyAutomaticBackupStartTime": str,
        "AutomaticBackupRetentionDays": int,
        "ThroughputCapacity": int,
        "SelfManagedActiveDirectoryConfiguration": "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    },
    total=False,
)
