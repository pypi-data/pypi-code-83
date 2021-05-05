"""
Type annotations for storagegateway service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_storagegateway import StorageGatewayClient

    client: StorageGatewayClient = boto3.client("storagegateway")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_storagegateway.literals import (
    CaseSensitivity,
    ObjectACL,
    RetentionLockType,
    SMBSecurityStrategy,
    TapeStorageClass,
)
from mypy_boto3_storagegateway.paginator import (
    DescribeTapeArchivesPaginator,
    DescribeTapeRecoveryPointsPaginator,
    DescribeTapesPaginator,
    DescribeVTLDevicesPaginator,
    ListFileSharesPaginator,
    ListFileSystemAssociationsPaginator,
    ListGatewaysPaginator,
    ListTagsForResourcePaginator,
    ListTapePoolsPaginator,
    ListTapesPaginator,
    ListVolumesPaginator,
)
from mypy_boto3_storagegateway.type_defs import (
    ActivateGatewayOutputTypeDef,
    AddCacheOutputTypeDef,
    AddTagsToResourceOutputTypeDef,
    AddUploadBufferOutputTypeDef,
    AddWorkingStorageOutputTypeDef,
    AssignTapePoolOutputTypeDef,
    AssociateFileSystemOutputTypeDef,
    AttachVolumeOutputTypeDef,
    AutomaticTapeCreationRuleTypeDef,
    BandwidthRateLimitIntervalTypeDef,
    CacheAttributesTypeDef,
    CancelArchivalOutputTypeDef,
    CancelRetrievalOutputTypeDef,
    CreateCachediSCSIVolumeOutputTypeDef,
    CreateNFSFileShareOutputTypeDef,
    CreateSMBFileShareOutputTypeDef,
    CreateSnapshotFromVolumeRecoveryPointOutputTypeDef,
    CreateSnapshotOutputTypeDef,
    CreateStorediSCSIVolumeOutputTypeDef,
    CreateTapePoolOutputTypeDef,
    CreateTapesOutputTypeDef,
    CreateTapeWithBarcodeOutputTypeDef,
    DeleteAutomaticTapeCreationPolicyOutputTypeDef,
    DeleteBandwidthRateLimitOutputTypeDef,
    DeleteChapCredentialsOutputTypeDef,
    DeleteFileShareOutputTypeDef,
    DeleteGatewayOutputTypeDef,
    DeleteSnapshotScheduleOutputTypeDef,
    DeleteTapeArchiveOutputTypeDef,
    DeleteTapeOutputTypeDef,
    DeleteTapePoolOutputTypeDef,
    DeleteVolumeOutputTypeDef,
    DescribeAvailabilityMonitorTestOutputTypeDef,
    DescribeBandwidthRateLimitOutputTypeDef,
    DescribeBandwidthRateLimitScheduleOutputTypeDef,
    DescribeCachediSCSIVolumesOutputTypeDef,
    DescribeCacheOutputTypeDef,
    DescribeChapCredentialsOutputTypeDef,
    DescribeFileSystemAssociationsOutputTypeDef,
    DescribeGatewayInformationOutputTypeDef,
    DescribeMaintenanceStartTimeOutputTypeDef,
    DescribeNFSFileSharesOutputTypeDef,
    DescribeSMBFileSharesOutputTypeDef,
    DescribeSMBSettingsOutputTypeDef,
    DescribeSnapshotScheduleOutputTypeDef,
    DescribeStorediSCSIVolumesOutputTypeDef,
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeUploadBufferOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    DescribeWorkingStorageOutputTypeDef,
    DetachVolumeOutputTypeDef,
    DisableGatewayOutputTypeDef,
    DisassociateFileSystemOutputTypeDef,
    JoinDomainOutputTypeDef,
    ListAutomaticTapeCreationPoliciesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListFileSystemAssociationsOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListLocalDisksOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapePoolsOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumeInitiatorsOutputTypeDef,
    ListVolumeRecoveryPointsOutputTypeDef,
    ListVolumesOutputTypeDef,
    NFSFileShareDefaultsTypeDef,
    NotifyWhenUploadedOutputTypeDef,
    RefreshCacheOutputTypeDef,
    RemoveTagsFromResourceOutputTypeDef,
    ResetCacheOutputTypeDef,
    RetrieveTapeArchiveOutputTypeDef,
    RetrieveTapeRecoveryPointOutputTypeDef,
    SetLocalConsolePasswordOutputTypeDef,
    SetSMBGuestPasswordOutputTypeDef,
    ShutdownGatewayOutputTypeDef,
    StartAvailabilityMonitorTestOutputTypeDef,
    StartGatewayOutputTypeDef,
    TagTypeDef,
    UpdateAutomaticTapeCreationPolicyOutputTypeDef,
    UpdateBandwidthRateLimitOutputTypeDef,
    UpdateBandwidthRateLimitScheduleOutputTypeDef,
    UpdateChapCredentialsOutputTypeDef,
    UpdateFileSystemAssociationOutputTypeDef,
    UpdateGatewayInformationOutputTypeDef,
    UpdateGatewaySoftwareNowOutputTypeDef,
    UpdateMaintenanceStartTimeOutputTypeDef,
    UpdateNFSFileShareOutputTypeDef,
    UpdateSMBFileShareOutputTypeDef,
    UpdateSMBFileShareVisibilityOutputTypeDef,
    UpdateSMBSecurityStrategyOutputTypeDef,
    UpdateSnapshotScheduleOutputTypeDef,
    UpdateVTLDeviceTypeOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("StorageGatewayClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidGatewayRequestException: Type[BotocoreClientError]
    ServiceUnavailableError: Type[BotocoreClientError]


class StorageGatewayClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def activate_gateway(
        self,
        ActivationKey: str,
        GatewayName: str,
        GatewayTimezone: str,
        GatewayRegion: str,
        GatewayType: str = None,
        TapeDriveType: str = None,
        MediumChangerType: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ActivateGatewayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.activate_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#activate-gateway)
        """

    def add_cache(self, GatewayARN: str, DiskIds: List[str]) -> AddCacheOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.add_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add-cache)
        """

    def add_tags_to_resource(
        self, ResourceARN: str, Tags: List["TagTypeDef"]
    ) -> AddTagsToResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add-tags-to-resource)
        """

    def add_upload_buffer(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddUploadBufferOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.add_upload_buffer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add-upload-buffer)
        """

    def add_working_storage(
        self, GatewayARN: str, DiskIds: List[str]
    ) -> AddWorkingStorageOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.add_working_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#add-working-storage)
        """

    def assign_tape_pool(
        self, TapeARN: str, PoolId: str, BypassGovernanceRetention: bool = None
    ) -> AssignTapePoolOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.assign_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#assign-tape-pool)
        """

    def associate_file_system(
        self,
        UserName: str,
        Password: str,
        ClientToken: str,
        GatewayARN: str,
        LocationARN: str,
        Tags: List["TagTypeDef"] = None,
        AuditDestinationARN: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
    ) -> AssociateFileSystemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.associate_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#associate-file-system)
        """

    def attach_volume(
        self,
        GatewayARN: str,
        VolumeARN: str,
        NetworkInterfaceId: str,
        TargetName: str = None,
        DiskId: str = None,
    ) -> AttachVolumeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#attach-volume)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#can-paginate)
        """

    def cancel_archival(self, GatewayARN: str, TapeARN: str) -> CancelArchivalOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.cancel_archival)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#cancel-archival)
        """

    def cancel_retrieval(self, GatewayARN: str, TapeARN: str) -> CancelRetrievalOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.cancel_retrieval)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#cancel-retrieval)
        """

    def create_cached_iscsi_volume(
        self,
        GatewayARN: str,
        VolumeSizeInBytes: int,
        TargetName: str,
        NetworkInterfaceId: str,
        ClientToken: str,
        SnapshotId: str = None,
        SourceVolumeARN: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCachediSCSIVolumeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_cached_iscsi_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-cached-iscsi-volume)
        """

    def create_nfs_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACL = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> CreateNFSFileShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_nfs_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-nfs-file-share)
        """

    def create_smb_file_share(
        self,
        ClientToken: str,
        GatewayARN: str,
        Role: str,
        LocationARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACL = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AccessBasedEnumeration: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        AuditDestinationARN: str = None,
        Authentication: str = None,
        CaseSensitivity: CaseSensitivity = None,
        Tags: List["TagTypeDef"] = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> CreateSMBFileShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_smb_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-smb-file-share)
        """

    def create_snapshot(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-snapshot)
        """

    def create_snapshot_from_volume_recovery_point(
        self, VolumeARN: str, SnapshotDescription: str, Tags: List["TagTypeDef"] = None
    ) -> CreateSnapshotFromVolumeRecoveryPointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_snapshot_from_volume_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-snapshot-from-volume-recovery-point)
        """

    def create_stored_iscsi_volume(
        self,
        GatewayARN: str,
        DiskId: str,
        PreserveExistingData: bool,
        TargetName: str,
        NetworkInterfaceId: str,
        SnapshotId: str = None,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateStorediSCSIVolumeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_stored_iscsi_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-stored-iscsi-volume)
        """

    def create_tape_pool(
        self,
        PoolName: str,
        StorageClass: TapeStorageClass,
        RetentionLockType: RetentionLockType = None,
        RetentionLockTimeInDays: int = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapePoolOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-tape-pool)
        """

    def create_tape_with_barcode(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        TapeBarcode: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapeWithBarcodeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_tape_with_barcode)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-tape-with-barcode)
        """

    def create_tapes(
        self,
        GatewayARN: str,
        TapeSizeInBytes: int,
        ClientToken: str,
        NumTapesToCreate: int,
        TapeBarcodePrefix: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        PoolId: str = None,
        Worm: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTapesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.create_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#create-tapes)
        """

    def delete_automatic_tape_creation_policy(
        self, GatewayARN: str
    ) -> DeleteAutomaticTapeCreationPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_automatic_tape_creation_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-automatic-tape-creation-policy)
        """

    def delete_bandwidth_rate_limit(
        self, GatewayARN: str, BandwidthType: str
    ) -> DeleteBandwidthRateLimitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-bandwidth-rate-limit)
        """

    def delete_chap_credentials(
        self, TargetARN: str, InitiatorName: str
    ) -> DeleteChapCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-chap-credentials)
        """

    def delete_file_share(
        self, FileShareARN: str, ForceDelete: bool = None
    ) -> DeleteFileShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-file-share)
        """

    def delete_gateway(self, GatewayARN: str) -> DeleteGatewayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-gateway)
        """

    def delete_snapshot_schedule(self, VolumeARN: str) -> DeleteSnapshotScheduleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-snapshot-schedule)
        """

    def delete_tape(
        self, GatewayARN: str, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_tape)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-tape)
        """

    def delete_tape_archive(
        self, TapeARN: str, BypassGovernanceRetention: bool = None
    ) -> DeleteTapeArchiveOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-tape-archive)
        """

    def delete_tape_pool(self, PoolARN: str) -> DeleteTapePoolOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_tape_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-tape-pool)
        """

    def delete_volume(self, VolumeARN: str) -> DeleteVolumeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.delete_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#delete-volume)
        """

    def describe_availability_monitor_test(
        self, GatewayARN: str
    ) -> DescribeAvailabilityMonitorTestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_availability_monitor_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-availability-monitor-test)
        """

    def describe_bandwidth_rate_limit(
        self, GatewayARN: str
    ) -> DescribeBandwidthRateLimitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-bandwidth-rate-limit)
        """

    def describe_bandwidth_rate_limit_schedule(
        self, GatewayARN: str
    ) -> DescribeBandwidthRateLimitScheduleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-bandwidth-rate-limit-schedule)
        """

    def describe_cache(self, GatewayARN: str) -> DescribeCacheOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-cache)
        """

    def describe_cached_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeCachediSCSIVolumesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_cached_iscsi_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-cached-iscsi-volumes)
        """

    def describe_chap_credentials(self, TargetARN: str) -> DescribeChapCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-chap-credentials)
        """

    def describe_file_system_associations(
        self, FileSystemAssociationARNList: List[str]
    ) -> DescribeFileSystemAssociationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_file_system_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-file-system-associations)
        """

    def describe_gateway_information(
        self, GatewayARN: str
    ) -> DescribeGatewayInformationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_gateway_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-gateway-information)
        """

    def describe_maintenance_start_time(
        self, GatewayARN: str
    ) -> DescribeMaintenanceStartTimeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_maintenance_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-maintenance-start-time)
        """

    def describe_nfs_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeNFSFileSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_nfs_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-nfs-file-shares)
        """

    def describe_smb_file_shares(
        self, FileShareARNList: List[str]
    ) -> DescribeSMBFileSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-smb-file-shares)
        """

    def describe_smb_settings(self, GatewayARN: str) -> DescribeSMBSettingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_smb_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-smb-settings)
        """

    def describe_snapshot_schedule(self, VolumeARN: str) -> DescribeSnapshotScheduleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-snapshot-schedule)
        """

    def describe_stored_iscsi_volumes(
        self, VolumeARNs: List[str]
    ) -> DescribeStorediSCSIVolumesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_stored_iscsi_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-stored-iscsi-volumes)
        """

    def describe_tape_archives(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_archives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-tape-archives)
        """

    def describe_tape_recovery_points(
        self, GatewayARN: str, Marker: str = None, Limit: int = None
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_tape_recovery_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-tape-recovery-points)
        """

    def describe_tapes(
        self, GatewayARN: str, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> DescribeTapesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-tapes)
        """

    def describe_upload_buffer(self, GatewayARN: str) -> DescribeUploadBufferOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_upload_buffer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-upload-buffer)
        """

    def describe_vtl_devices(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        Marker: str = None,
        Limit: int = None,
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_vtl_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-vtl-devices)
        """

    def describe_working_storage(self, GatewayARN: str) -> DescribeWorkingStorageOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.describe_working_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#describe-working-storage)
        """

    def detach_volume(self, VolumeARN: str, ForceDetach: bool = None) -> DetachVolumeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#detach-volume)
        """

    def disable_gateway(self, GatewayARN: str) -> DisableGatewayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.disable_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#disable-gateway)
        """

    def disassociate_file_system(
        self, FileSystemAssociationARN: str, ForceDelete: bool = None
    ) -> DisassociateFileSystemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.disassociate_file_system)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#disassociate-file-system)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#generate-presigned-url)
        """

    def join_domain(
        self,
        GatewayARN: str,
        DomainName: str,
        UserName: str,
        Password: str,
        OrganizationalUnit: str = None,
        DomainControllers: List[str] = None,
        TimeoutInSeconds: int = None,
    ) -> JoinDomainOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.join_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#join-domain)
        """

    def list_automatic_tape_creation_policies(
        self, GatewayARN: str = None
    ) -> ListAutomaticTapeCreationPoliciesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_automatic_tape_creation_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-automatic-tape-creation-policies)
        """

    def list_file_shares(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_file_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-file-shares)
        """

    def list_file_system_associations(
        self, GatewayARN: str = None, Limit: int = None, Marker: str = None
    ) -> ListFileSystemAssociationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_file_system_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-file-system-associations)
        """

    def list_gateways(self, Marker: str = None, Limit: int = None) -> ListGatewaysOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-gateways)
        """

    def list_local_disks(self, GatewayARN: str) -> ListLocalDisksOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_local_disks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-local-disks)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, Marker: str = None, Limit: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-tags-for-resource)
        """

    def list_tape_pools(
        self, PoolARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapePoolsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_tape_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-tape-pools)
        """

    def list_tapes(
        self, TapeARNs: List[str] = None, Marker: str = None, Limit: int = None
    ) -> ListTapesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_tapes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-tapes)
        """

    def list_volume_initiators(self, VolumeARN: str) -> ListVolumeInitiatorsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_volume_initiators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-volume-initiators)
        """

    def list_volume_recovery_points(self, GatewayARN: str) -> ListVolumeRecoveryPointsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_volume_recovery_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-volume-recovery-points)
        """

    def list_volumes(
        self, GatewayARN: str = None, Marker: str = None, Limit: int = None
    ) -> ListVolumesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.list_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#list-volumes)
        """

    def notify_when_uploaded(self, FileShareARN: str) -> NotifyWhenUploadedOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.notify_when_uploaded)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#notify-when-uploaded)
        """

    def refresh_cache(
        self, FileShareARN: str, FolderList: List[str] = None, Recursive: bool = None
    ) -> RefreshCacheOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.refresh_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#refresh-cache)
        """

    def remove_tags_from_resource(
        self, ResourceARN: str, TagKeys: List[str]
    ) -> RemoveTagsFromResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#remove-tags-from-resource)
        """

    def reset_cache(self, GatewayARN: str) -> ResetCacheOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.reset_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#reset-cache)
        """

    def retrieve_tape_archive(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeArchiveOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#retrieve-tape-archive)
        """

    def retrieve_tape_recovery_point(
        self, TapeARN: str, GatewayARN: str
    ) -> RetrieveTapeRecoveryPointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.retrieve_tape_recovery_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#retrieve-tape-recovery-point)
        """

    def set_local_console_password(
        self, GatewayARN: str, LocalConsolePassword: str
    ) -> SetLocalConsolePasswordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.set_local_console_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#set-local-console-password)
        """

    def set_smb_guest_password(
        self, GatewayARN: str, Password: str
    ) -> SetSMBGuestPasswordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.set_smb_guest_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#set-smb-guest-password)
        """

    def shutdown_gateway(self, GatewayARN: str) -> ShutdownGatewayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.shutdown_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#shutdown-gateway)
        """

    def start_availability_monitor_test(
        self, GatewayARN: str
    ) -> StartAvailabilityMonitorTestOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.start_availability_monitor_test)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#start-availability-monitor-test)
        """

    def start_gateway(self, GatewayARN: str) -> StartGatewayOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.start_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#start-gateway)
        """

    def update_automatic_tape_creation_policy(
        self, AutomaticTapeCreationRules: List["AutomaticTapeCreationRuleTypeDef"], GatewayARN: str
    ) -> UpdateAutomaticTapeCreationPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_automatic_tape_creation_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-automatic-tape-creation-policy)
        """

    def update_bandwidth_rate_limit(
        self,
        GatewayARN: str,
        AverageUploadRateLimitInBitsPerSec: int = None,
        AverageDownloadRateLimitInBitsPerSec: int = None,
    ) -> UpdateBandwidthRateLimitOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-bandwidth-rate-limit)
        """

    def update_bandwidth_rate_limit_schedule(
        self,
        GatewayARN: str,
        BandwidthRateLimitIntervals: List["BandwidthRateLimitIntervalTypeDef"],
    ) -> UpdateBandwidthRateLimitScheduleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_bandwidth_rate_limit_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-bandwidth-rate-limit-schedule)
        """

    def update_chap_credentials(
        self,
        TargetARN: str,
        SecretToAuthenticateInitiator: str,
        InitiatorName: str,
        SecretToAuthenticateTarget: str = None,
    ) -> UpdateChapCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_chap_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-chap-credentials)
        """

    def update_file_system_association(
        self,
        FileSystemAssociationARN: str,
        UserName: str = None,
        Password: str = None,
        AuditDestinationARN: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
    ) -> UpdateFileSystemAssociationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_file_system_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-file-system-association)
        """

    def update_gateway_information(
        self,
        GatewayARN: str,
        GatewayName: str = None,
        GatewayTimezone: str = None,
        CloudWatchLogGroupARN: str = None,
    ) -> UpdateGatewayInformationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-gateway-information)
        """

    def update_gateway_software_now(self, GatewayARN: str) -> UpdateGatewaySoftwareNowOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_gateway_software_now)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-gateway-software-now)
        """

    def update_maintenance_start_time(
        self,
        GatewayARN: str,
        HourOfDay: int,
        MinuteOfHour: int,
        DayOfWeek: int = None,
        DayOfMonth: int = None,
    ) -> UpdateMaintenanceStartTimeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_maintenance_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-maintenance-start-time)
        """

    def update_nfs_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        NFSFileShareDefaults: "NFSFileShareDefaultsTypeDef" = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACL = None,
        ClientList: List[str] = None,
        Squash: str = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> UpdateNFSFileShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_nfs_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-nfs-file-share)
        """

    def update_smb_file_share(
        self,
        FileShareARN: str,
        KMSEncrypted: bool = None,
        KMSKey: str = None,
        DefaultStorageClass: str = None,
        ObjectACL: ObjectACL = None,
        ReadOnly: bool = None,
        GuessMIMETypeEnabled: bool = None,
        RequesterPays: bool = None,
        SMBACLEnabled: bool = None,
        AccessBasedEnumeration: bool = None,
        AdminUserList: List[str] = None,
        ValidUserList: List[str] = None,
        InvalidUserList: List[str] = None,
        AuditDestinationARN: str = None,
        CaseSensitivity: CaseSensitivity = None,
        FileShareName: str = None,
        CacheAttributes: "CacheAttributesTypeDef" = None,
        NotificationPolicy: str = None,
    ) -> UpdateSMBFileShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-smb-file-share)
        """

    def update_smb_file_share_visibility(
        self, GatewayARN: str, FileSharesVisible: bool
    ) -> UpdateSMBFileShareVisibilityOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_smb_file_share_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-smb-file-share-visibility)
        """

    def update_smb_security_strategy(
        self, GatewayARN: str, SMBSecurityStrategy: SMBSecurityStrategy
    ) -> UpdateSMBSecurityStrategyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_smb_security_strategy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-smb-security-strategy)
        """

    def update_snapshot_schedule(
        self,
        VolumeARN: str,
        StartAt: int,
        RecurrenceInHours: int,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> UpdateSnapshotScheduleOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_snapshot_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-snapshot-schedule)
        """

    def update_vtl_device_type(
        self, VTLDeviceARN: str, DeviceType: str
    ) -> UpdateVTLDeviceTypeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Client.update_vtl_device_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/client.html#update-vtl-device-type)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_archives"]
    ) -> DescribeTapeArchivesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetapearchivespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_tape_recovery_points"]
    ) -> DescribeTapeRecoveryPointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetaperecoverypointspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tapes"]) -> DescribeTapesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describetapespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vtl_devices"]
    ) -> DescribeVTLDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#describevtldevicespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_file_shares"]) -> ListFileSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listfilesharespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_file_system_associations"]
    ) -> ListFileSystemAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileSystemAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listfilesystemassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tape_pools"]) -> ListTapePoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapePools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtapepoolspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tapes"]) -> ListTapesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listtapespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_volumes"]) -> ListVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/paginators.html#listvolumespaginator)
        """
