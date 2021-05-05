"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import ActivateGatewayOutputTypeDef

    data: ActivateGatewayOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_storagegateway.literals import (
    ActiveDirectoryStatus,
    AvailabilityMonitorTestStatus,
    CaseSensitivity,
    FileShareType,
    HostEnvironment,
    ObjectACL,
    PoolStatus,
    RetentionLockType,
    SMBSecurityStrategy,
    TapeStorageClass,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivateGatewayOutputTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeOutputTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalOutputTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "DiskTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesOutputTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheOutputTypeDef",
    "ResponseMetadata",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SMBFileShareInfoTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayOutputTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)


class ActivateGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class AddCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class AddTagsToResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: "ResponseMetadata"


class AddUploadBufferOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class AddWorkingStorageOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class AssignTapePoolOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class AssociateFileSystemOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: "ResponseMetadata"


class AttachVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: "ResponseMetadata"


class AutomaticTapeCreationPolicyInfoTypeDef(TypedDict, total=False):
    AutomaticTapeCreationRules: List["AutomaticTapeCreationRuleTypeDef"]
    GatewayARN: str


class _RequiredAutomaticTapeCreationRuleTypeDef(TypedDict):
    TapeBarcodePrefix: str
    PoolId: str
    TapeSizeInBytes: int
    MinimumNumTapes: int


class AutomaticTapeCreationRuleTypeDef(_RequiredAutomaticTapeCreationRuleTypeDef, total=False):
    Worm: bool


class _RequiredBandwidthRateLimitIntervalTypeDef(TypedDict):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]


class BandwidthRateLimitIntervalTypeDef(_RequiredBandwidthRateLimitIntervalTypeDef, total=False):
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int


class CacheAttributesTypeDef(TypedDict, total=False):
    CacheStaleTimeoutInSeconds: int


class CachediSCSIVolumeTypeDef(TypedDict, total=False):
    VolumeARN: str
    VolumeId: str
    VolumeType: str
    VolumeStatus: str
    VolumeAttachmentStatus: str
    VolumeSizeInBytes: int
    VolumeProgress: float
    SourceSnapshotId: str
    VolumeiSCSIAttributes: "VolumeiSCSIAttributesTypeDef"
    CreatedDate: datetime
    VolumeUsedInBytes: int
    KMSKey: str
    TargetName: str


class CancelArchivalOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class CancelRetrievalOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class ChapInfoTypeDef(TypedDict, total=False):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: str


class CreateCachediSCSIVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateNFSFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateSMBFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateSnapshotFromVolumeRecoveryPointOutputTypeDef(TypedDict):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: "ResponseMetadata"


class CreateSnapshotOutputTypeDef(TypedDict):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: "ResponseMetadata"


class CreateStorediSCSIVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateTapePoolOutputTypeDef(TypedDict):
    PoolARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateTapeWithBarcodeOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateTapesOutputTypeDef(TypedDict):
    TapeARNs: List[str]
    ResponseMetadata: "ResponseMetadata"


class DeleteAutomaticTapeCreationPolicyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteChapCredentialsOutputTypeDef(TypedDict):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: "ResponseMetadata"


class DeleteFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteTapeArchiveOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteTapeOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteTapePoolOutputTypeDef(TypedDict):
    PoolARN: str
    ResponseMetadata: "ResponseMetadata"


class DeleteVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: "ResponseMetadata"


class DescribeAvailabilityMonitorTestOutputTypeDef(TypedDict):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatus
    StartTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: "ResponseMetadata"


class DescribeBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    GatewayARN: str
    BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: "ResponseMetadata"


class DescribeCachediSCSIVolumesOutputTypeDef(TypedDict):
    CachediSCSIVolumes: List["CachediSCSIVolumeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeChapCredentialsOutputTypeDef(TypedDict):
    ChapCredentials: List["ChapInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeFileSystemAssociationsOutputTypeDef(TypedDict):
    FileSystemAssociationInfoList: List["FileSystemAssociationInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeGatewayInformationOutputTypeDef(TypedDict):
    GatewayARN: str
    GatewayId: str
    GatewayName: str
    GatewayTimezone: str
    GatewayState: str
    GatewayNetworkInterfaces: List["NetworkInterfaceTypeDef"]
    GatewayType: str
    NextUpdateAvailabilityDate: str
    LastSoftwareUpdate: str
    Ec2InstanceId: str
    Ec2InstanceRegion: str
    Tags: List["TagTypeDef"]
    VPCEndpoint: str
    CloudWatchLogGroupARN: str
    HostEnvironment: HostEnvironment
    EndpointType: str
    SoftwareUpdatesEndDate: str
    DeprecationDate: str
    ResponseMetadata: "ResponseMetadata"


class DescribeMaintenanceStartTimeOutputTypeDef(TypedDict):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    ResponseMetadata: "ResponseMetadata"


class DescribeNFSFileSharesOutputTypeDef(TypedDict):
    NFSFileShareInfoList: List["NFSFileShareInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeSMBFileSharesOutputTypeDef(TypedDict):
    SMBFileShareInfoList: List["SMBFileShareInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeSMBSettingsOutputTypeDef(TypedDict):
    GatewayARN: str
    DomainName: str
    ActiveDirectoryStatus: ActiveDirectoryStatus
    SMBGuestPasswordSet: bool
    SMBSecurityStrategy: SMBSecurityStrategy
    FileSharesVisible: bool
    ResponseMetadata: "ResponseMetadata"


class DescribeSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeStorediSCSIVolumesOutputTypeDef(TypedDict):
    StorediSCSIVolumes: List["StorediSCSIVolumeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeTapeArchivesOutputTypeDef(TypedDict):
    TapeArchives: List["TapeArchiveTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeTapeRecoveryPointsOutputTypeDef(TypedDict):
    GatewayARN: str
    TapeRecoveryPointInfos: List["TapeRecoveryPointInfoTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeTapesOutputTypeDef(TypedDict):
    Tapes: List["TapeTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeUploadBufferOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: "ResponseMetadata"


class DescribeVTLDevicesOutputTypeDef(TypedDict):
    GatewayARN: str
    VTLDevices: List["VTLDeviceTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeWorkingStorageOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: "ResponseMetadata"


class DetachVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: "ResponseMetadata"


class DeviceiSCSIAttributesTypeDef(TypedDict, total=False):
    TargetARN: str
    NetworkInterfaceId: str
    NetworkInterfacePort: int
    ChapEnabled: bool


class DisableGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class DisassociateFileSystemOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: "ResponseMetadata"


class DiskTypeDef(TypedDict, total=False):
    DiskId: str
    DiskPath: str
    DiskNode: str
    DiskStatus: str
    DiskSizeInBytes: int
    DiskAllocationType: str
    DiskAllocationResource: str
    DiskAttributeList: List[str]


class FileShareInfoTypeDef(TypedDict, total=False):
    FileShareType: FileShareType
    FileShareARN: str
    FileShareId: str
    FileShareStatus: str
    GatewayARN: str


class FileSystemAssociationInfoTypeDef(TypedDict, total=False):
    FileSystemAssociationARN: str
    LocationARN: str
    FileSystemAssociationStatus: str
    AuditDestinationARN: str
    GatewayARN: str
    Tags: List["TagTypeDef"]
    CacheAttributes: "CacheAttributesTypeDef"


class FileSystemAssociationSummaryTypeDef(TypedDict, total=False):
    FileSystemAssociationId: str
    FileSystemAssociationARN: str
    FileSystemAssociationStatus: str
    GatewayARN: str


class GatewayInfoTypeDef(TypedDict, total=False):
    GatewayId: str
    GatewayARN: str
    GatewayType: str
    GatewayOperationalState: str
    GatewayName: str
    Ec2InstanceId: str
    Ec2InstanceRegion: str


class JoinDomainOutputTypeDef(TypedDict):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatus
    ResponseMetadata: "ResponseMetadata"


class ListAutomaticTapeCreationPoliciesOutputTypeDef(TypedDict):
    AutomaticTapeCreationPolicyInfos: List["AutomaticTapeCreationPolicyInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListFileSharesOutputTypeDef(TypedDict):
    Marker: str
    NextMarker: str
    FileShareInfoList: List["FileShareInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListFileSystemAssociationsOutputTypeDef(TypedDict):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List["FileSystemAssociationSummaryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListGatewaysOutputTypeDef(TypedDict):
    Gateways: List["GatewayInfoTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListLocalDisksOutputTypeDef(TypedDict):
    GatewayARN: str
    Disks: List["DiskTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    Marker: str
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListTapePoolsOutputTypeDef(TypedDict):
    PoolInfos: List["PoolInfoTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListTapesOutputTypeDef(TypedDict):
    TapeInfos: List["TapeInfoTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListVolumeInitiatorsOutputTypeDef(TypedDict):
    Initiators: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListVolumeRecoveryPointsOutputTypeDef(TypedDict):
    GatewayARN: str
    VolumeRecoveryPointInfos: List["VolumeRecoveryPointInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListVolumesOutputTypeDef(TypedDict):
    GatewayARN: str
    Marker: str
    VolumeInfos: List["VolumeInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class NFSFileShareDefaultsTypeDef(TypedDict, total=False):
    FileMode: str
    DirectoryMode: str
    GroupId: int
    OwnerId: int


class NFSFileShareInfoTypeDef(TypedDict, total=False):
    NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef"
    FileShareARN: str
    FileShareId: str
    FileShareStatus: str
    GatewayARN: str
    KMSEncrypted: bool
    KMSKey: str
    Path: str
    Role: str
    LocationARN: str
    DefaultStorageClass: str
    ObjectACL: ObjectACL
    ClientList: List[str]
    Squash: str
    ReadOnly: bool
    GuessMIMETypeEnabled: bool
    RequesterPays: bool
    Tags: List["TagTypeDef"]
    FileShareName: str
    CacheAttributes: "CacheAttributesTypeDef"
    NotificationPolicy: str


class NetworkInterfaceTypeDef(TypedDict, total=False):
    Ipv4Address: str
    MacAddress: str
    Ipv6Address: str


class NotifyWhenUploadedOutputTypeDef(TypedDict):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PoolInfoTypeDef(TypedDict, total=False):
    PoolARN: str
    PoolName: str
    StorageClass: TapeStorageClass
    RetentionLockType: RetentionLockType
    RetentionLockTimeInDays: int
    PoolStatus: PoolStatus


class RefreshCacheOutputTypeDef(TypedDict):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: "ResponseMetadata"


class RemoveTagsFromResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: "ResponseMetadata"


class ResetCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RetrieveTapeArchiveOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class RetrieveTapeRecoveryPointOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: "ResponseMetadata"


class SMBFileShareInfoTypeDef(TypedDict, total=False):
    FileShareARN: str
    FileShareId: str
    FileShareStatus: str
    GatewayARN: str
    KMSEncrypted: bool
    KMSKey: str
    Path: str
    Role: str
    LocationARN: str
    DefaultStorageClass: str
    ObjectACL: ObjectACL
    ReadOnly: bool
    GuessMIMETypeEnabled: bool
    RequesterPays: bool
    SMBACLEnabled: bool
    AccessBasedEnumeration: bool
    AdminUserList: List[str]
    ValidUserList: List[str]
    InvalidUserList: List[str]
    AuditDestinationARN: str
    Authentication: str
    CaseSensitivity: CaseSensitivity
    Tags: List["TagTypeDef"]
    FileShareName: str
    CacheAttributes: "CacheAttributesTypeDef"
    NotificationPolicy: str


class SetLocalConsolePasswordOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class SetSMBGuestPasswordOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class ShutdownGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class StartAvailabilityMonitorTestOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class StartGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class StorediSCSIVolumeTypeDef(TypedDict, total=False):
    VolumeARN: str
    VolumeId: str
    VolumeType: str
    VolumeStatus: str
    VolumeAttachmentStatus: str
    VolumeSizeInBytes: int
    VolumeProgress: float
    VolumeDiskId: str
    SourceSnapshotId: str
    PreservedExistingData: bool
    VolumeiSCSIAttributes: "VolumeiSCSIAttributesTypeDef"
    CreatedDate: datetime
    VolumeUsedInBytes: int
    KMSKey: str
    TargetName: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TapeArchiveTypeDef(TypedDict, total=False):
    TapeARN: str
    TapeBarcode: str
    TapeCreatedDate: datetime
    TapeSizeInBytes: int
    CompletionTime: datetime
    RetrievedTo: str
    TapeStatus: str
    TapeUsedInBytes: int
    KMSKey: str
    PoolId: str
    Worm: bool
    RetentionStartDate: datetime
    PoolEntryDate: datetime


class TapeInfoTypeDef(TypedDict, total=False):
    TapeARN: str
    TapeBarcode: str
    TapeSizeInBytes: int
    TapeStatus: str
    GatewayARN: str
    PoolId: str
    RetentionStartDate: datetime
    PoolEntryDate: datetime


class TapeRecoveryPointInfoTypeDef(TypedDict, total=False):
    TapeARN: str
    TapeRecoveryPointTime: datetime
    TapeSizeInBytes: int
    TapeStatus: str


class TapeTypeDef(TypedDict, total=False):
    TapeARN: str
    TapeBarcode: str
    TapeCreatedDate: datetime
    TapeSizeInBytes: int
    TapeStatus: str
    VTLDevice: str
    Progress: float
    TapeUsedInBytes: int
    KMSKey: str
    PoolId: str
    Worm: bool
    RetentionStartDate: datetime
    PoolEntryDate: datetime


class UpdateAutomaticTapeCreationPolicyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateChapCredentialsOutputTypeDef(TypedDict):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: "ResponseMetadata"


class UpdateFileSystemAssociationOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateGatewayInformationOutputTypeDef(TypedDict):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: "ResponseMetadata"


class UpdateGatewaySoftwareNowOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateMaintenanceStartTimeOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateNFSFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateSMBFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateSMBFileShareVisibilityOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateSMBSecurityStrategyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: "ResponseMetadata"


class UpdateVTLDeviceTypeOutputTypeDef(TypedDict):
    VTLDeviceARN: str
    ResponseMetadata: "ResponseMetadata"


class VTLDeviceTypeDef(TypedDict, total=False):
    VTLDeviceARN: str
    VTLDeviceType: str
    VTLDeviceVendor: str
    VTLDeviceProductIdentifier: str
    DeviceiSCSIAttributes: "DeviceiSCSIAttributesTypeDef"


class VolumeInfoTypeDef(TypedDict, total=False):
    VolumeARN: str
    VolumeId: str
    GatewayARN: str
    GatewayId: str
    VolumeType: str
    VolumeSizeInBytes: int
    VolumeAttachmentStatus: str


class VolumeRecoveryPointInfoTypeDef(TypedDict, total=False):
    VolumeARN: str
    VolumeSizeInBytes: int
    VolumeUsageInBytes: int
    VolumeRecoveryPointTime: str


class VolumeiSCSIAttributesTypeDef(TypedDict, total=False):
    TargetARN: str
    NetworkInterfaceId: str
    NetworkInterfacePort: int
    LunNumber: int
    ChapEnabled: bool
