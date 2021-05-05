"""
Type annotations for fsx service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fsx/type_defs.html)

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
    DriveCacheType,
    FileSystemLifecycle,
    FileSystemMaintenanceOperation,
    FileSystemType,
    FilterName,
    LustreDeploymentType,
    Status,
    StorageType,
    WindowsDeploymentType,
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
    "ActiveDirectoryBackupAttributesTypeDef",
    "AdministrativeActionFailureDetailsTypeDef",
    "AdministrativeActionTypeDef",
    "AliasTypeDef",
    "AssociateFileSystemAliasesResponseTypeDef",
    "BackupFailureDetailsTypeDef",
    "BackupTypeDef",
    "CancelDataRepositoryTaskResponseTypeDef",
    "CompletionReportTypeDef",
    "CopyBackupResponseTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateDataRepositoryTaskResponseTypeDef",
    "CreateFileSystemFromBackupResponseTypeDef",
    "CreateFileSystemLustreConfigurationTypeDef",
    "CreateFileSystemResponseTypeDef",
    "CreateFileSystemWindowsConfigurationTypeDef",
    "DataRepositoryConfigurationTypeDef",
    "DataRepositoryFailureDetailsTypeDef",
    "DataRepositoryTaskFailureDetailsTypeDef",
    "DataRepositoryTaskFilterTypeDef",
    "DataRepositoryTaskStatusTypeDef",
    "DataRepositoryTaskTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteFileSystemLustreConfigurationTypeDef",
    "DeleteFileSystemLustreResponseTypeDef",
    "DeleteFileSystemResponseTypeDef",
    "DeleteFileSystemWindowsConfigurationTypeDef",
    "DeleteFileSystemWindowsResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeDataRepositoryTasksResponseTypeDef",
    "DescribeFileSystemAliasesResponseTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DisassociateFileSystemAliasesResponseTypeDef",
    "FileSystemFailureDetailsTypeDef",
    "FileSystemTypeDef",
    "FilterTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LustreFileSystemConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "SelfManagedActiveDirectoryAttributesTypeDef",
    "SelfManagedActiveDirectoryConfigurationTypeDef",
    "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef",
    "TagTypeDef",
    "UpdateFileSystemLustreConfigurationTypeDef",
    "UpdateFileSystemResponseTypeDef",
    "UpdateFileSystemWindowsConfigurationTypeDef",
    "WindowsFileSystemConfigurationTypeDef",
)


class ActiveDirectoryBackupAttributesTypeDef(TypedDict, total=False):
    DomainName: str
    ActiveDirectoryId: str
    ResourceARN: str


class AdministrativeActionFailureDetailsTypeDef(TypedDict, total=False):
    Message: str


class AdministrativeActionTypeDef(TypedDict, total=False):
    AdministrativeActionType: AdministrativeActionType
    ProgressPercent: int
    RequestTime: datetime
    Status: Status
    TargetFileSystemValues: Dict[str, Any]
    FailureDetails: "AdministrativeActionFailureDetailsTypeDef"


class AliasTypeDef(TypedDict, total=False):
    Name: str
    Lifecycle: AliasLifecycle


class AssociateFileSystemAliasesResponseTypeDef(TypedDict, total=False):
    Aliases: List["AliasTypeDef"]


class BackupFailureDetailsTypeDef(TypedDict, total=False):
    Message: str


_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
        "Lifecycle": BackupLifecycle,
        "Type": BackupType,
        "CreationTime": datetime,
        "FileSystem": "FileSystemTypeDef",
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


class CancelDataRepositoryTaskResponseTypeDef(TypedDict, total=False):
    Lifecycle: DataRepositoryTaskLifecycle
    TaskId: str


class _RequiredCompletionReportTypeDef(TypedDict):
    Enabled: bool


class CompletionReportTypeDef(_RequiredCompletionReportTypeDef, total=False):
    Path: str
    Format: Literal["REPORT_CSV_20191124"]
    Scope: Literal["FAILED_FILES_ONLY"]


class CopyBackupResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class CreateBackupResponseTypeDef(TypedDict, total=False):
    Backup: "BackupTypeDef"


class CreateDataRepositoryTaskResponseTypeDef(TypedDict, total=False):
    DataRepositoryTask: "DataRepositoryTaskTypeDef"


class CreateFileSystemFromBackupResponseTypeDef(TypedDict, total=False):
    FileSystem: "FileSystemTypeDef"


class CreateFileSystemLustreConfigurationTypeDef(TypedDict, total=False):
    WeeklyMaintenanceStartTime: str
    ImportPath: str
    ExportPath: str
    ImportedFileChunkSize: int
    DeploymentType: LustreDeploymentType
    AutoImportPolicy: AutoImportPolicyType
    PerUnitStorageThroughput: int
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    CopyTagsToBackups: bool
    DriveCacheType: DriveCacheType


class CreateFileSystemResponseTypeDef(TypedDict, total=False):
    FileSystem: "FileSystemTypeDef"


class _RequiredCreateFileSystemWindowsConfigurationTypeDef(TypedDict):
    ThroughputCapacity: int


class CreateFileSystemWindowsConfigurationTypeDef(
    _RequiredCreateFileSystemWindowsConfigurationTypeDef, total=False
):
    ActiveDirectoryId: str
    SelfManagedActiveDirectoryConfiguration: "SelfManagedActiveDirectoryConfigurationTypeDef"
    DeploymentType: WindowsDeploymentType
    PreferredSubnetId: str
    WeeklyMaintenanceStartTime: str
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    CopyTagsToBackups: bool
    Aliases: List[str]


class DataRepositoryConfigurationTypeDef(TypedDict, total=False):
    Lifecycle: DataRepositoryLifecycle
    ImportPath: str
    ExportPath: str
    ImportedFileChunkSize: int
    AutoImportPolicy: AutoImportPolicyType
    FailureDetails: "DataRepositoryFailureDetailsTypeDef"


class DataRepositoryFailureDetailsTypeDef(TypedDict, total=False):
    Message: str


class DataRepositoryTaskFailureDetailsTypeDef(TypedDict, total=False):
    Message: str


class DataRepositoryTaskFilterTypeDef(TypedDict, total=False):
    Name: DataRepositoryTaskFilterName
    Values: List[str]


class DataRepositoryTaskStatusTypeDef(TypedDict, total=False):
    TotalCount: int
    SucceededCount: int
    FailedCount: int
    LastUpdatedTime: datetime


_RequiredDataRepositoryTaskTypeDef = TypedDict(
    "_RequiredDataRepositoryTaskTypeDef",
    {
        "TaskId": str,
        "Lifecycle": DataRepositoryTaskLifecycle,
        "Type": Literal["EXPORT_TO_REPOSITORY"],
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


class DeleteBackupResponseTypeDef(TypedDict, total=False):
    BackupId: str
    Lifecycle: BackupLifecycle


class DeleteFileSystemLustreConfigurationTypeDef(TypedDict, total=False):
    SkipFinalBackup: bool
    FinalBackupTags: List["TagTypeDef"]


class DeleteFileSystemLustreResponseTypeDef(TypedDict, total=False):
    FinalBackupId: str
    FinalBackupTags: List["TagTypeDef"]


class DeleteFileSystemResponseTypeDef(TypedDict, total=False):
    FileSystemId: str
    Lifecycle: FileSystemLifecycle
    WindowsResponse: "DeleteFileSystemWindowsResponseTypeDef"
    LustreResponse: "DeleteFileSystemLustreResponseTypeDef"


class DeleteFileSystemWindowsConfigurationTypeDef(TypedDict, total=False):
    SkipFinalBackup: bool
    FinalBackupTags: List["TagTypeDef"]


class DeleteFileSystemWindowsResponseTypeDef(TypedDict, total=False):
    FinalBackupId: str
    FinalBackupTags: List["TagTypeDef"]


class DescribeBackupsResponseTypeDef(TypedDict, total=False):
    Backups: List["BackupTypeDef"]
    NextToken: str


class DescribeDataRepositoryTasksResponseTypeDef(TypedDict, total=False):
    DataRepositoryTasks: List["DataRepositoryTaskTypeDef"]
    NextToken: str


class DescribeFileSystemAliasesResponseTypeDef(TypedDict, total=False):
    Aliases: List["AliasTypeDef"]
    NextToken: str


class DescribeFileSystemsResponseTypeDef(TypedDict, total=False):
    FileSystems: List["FileSystemTypeDef"]
    NextToken: str


class DisassociateFileSystemAliasesResponseTypeDef(TypedDict, total=False):
    Aliases: List["AliasTypeDef"]


class FileSystemFailureDetailsTypeDef(TypedDict, total=False):
    Message: str


class FileSystemTypeDef(TypedDict, total=False):
    OwnerId: str
    CreationTime: datetime
    FileSystemId: str
    FileSystemType: FileSystemType
    Lifecycle: FileSystemLifecycle
    FailureDetails: "FileSystemFailureDetailsTypeDef"
    StorageCapacity: int
    StorageType: StorageType
    VpcId: str
    SubnetIds: List[str]
    NetworkInterfaceIds: List[str]
    DNSName: str
    KmsKeyId: str
    ResourceARN: str
    Tags: List["TagTypeDef"]
    WindowsConfiguration: "WindowsFileSystemConfigurationTypeDef"
    LustreConfiguration: "LustreFileSystemConfigurationTypeDef"
    AdministrativeActions: List[Dict[str, Any]]


class FilterTypeDef(TypedDict, total=False):
    Name: FilterName
    Values: List[str]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class LustreFileSystemConfigurationTypeDef(TypedDict, total=False):
    WeeklyMaintenanceStartTime: str
    DataRepositoryConfiguration: "DataRepositoryConfigurationTypeDef"
    DeploymentType: LustreDeploymentType
    PerUnitStorageThroughput: int
    MountName: str
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    CopyTagsToBackups: bool
    DriveCacheType: DriveCacheType


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class SelfManagedActiveDirectoryAttributesTypeDef(TypedDict, total=False):
    DomainName: str
    OrganizationalUnitDistinguishedName: str
    FileSystemAdministratorsGroup: str
    UserName: str
    DnsIps: List[str]


class _RequiredSelfManagedActiveDirectoryConfigurationTypeDef(TypedDict):
    DomainName: str
    UserName: str
    Password: str
    DnsIps: List[str]


class SelfManagedActiveDirectoryConfigurationTypeDef(
    _RequiredSelfManagedActiveDirectoryConfigurationTypeDef, total=False
):
    OrganizationalUnitDistinguishedName: str
    FileSystemAdministratorsGroup: str


class SelfManagedActiveDirectoryConfigurationUpdatesTypeDef(TypedDict, total=False):
    UserName: str
    Password: str
    DnsIps: List[str]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateFileSystemLustreConfigurationTypeDef(TypedDict, total=False):
    WeeklyMaintenanceStartTime: str
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    AutoImportPolicy: AutoImportPolicyType


class UpdateFileSystemResponseTypeDef(TypedDict, total=False):
    FileSystem: "FileSystemTypeDef"


class UpdateFileSystemWindowsConfigurationTypeDef(TypedDict, total=False):
    WeeklyMaintenanceStartTime: str
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    ThroughputCapacity: int
    SelfManagedActiveDirectoryConfiguration: "SelfManagedActiveDirectoryConfigurationUpdatesTypeDef"


class WindowsFileSystemConfigurationTypeDef(TypedDict, total=False):
    ActiveDirectoryId: str
    SelfManagedActiveDirectoryConfiguration: "SelfManagedActiveDirectoryAttributesTypeDef"
    DeploymentType: WindowsDeploymentType
    RemoteAdministrationEndpoint: str
    PreferredSubnetId: str
    PreferredFileServerIp: str
    ThroughputCapacity: int
    MaintenanceOperationsInProgress: List[FileSystemMaintenanceOperation]
    WeeklyMaintenanceStartTime: str
    DailyAutomaticBackupStartTime: str
    AutomaticBackupRetentionDays: int
    CopyTagsToBackups: bool
    Aliases: List["AliasTypeDef"]
