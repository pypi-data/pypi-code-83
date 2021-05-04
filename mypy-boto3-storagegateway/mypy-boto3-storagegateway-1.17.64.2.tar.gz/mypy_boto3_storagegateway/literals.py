"""
Type annotations for storagegateway service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/literals.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.literals import ActiveDirectoryStatus

    data: ActiveDirectoryStatus = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActiveDirectoryStatus",
    "AvailabilityMonitorTestStatus",
    "CaseSensitivity",
    "DescribeTapeArchivesPaginatorName",
    "DescribeTapeRecoveryPointsPaginatorName",
    "DescribeTapesPaginatorName",
    "DescribeVTLDevicesPaginatorName",
    "FileShareType",
    "HostEnvironment",
    "ListFileSharesPaginatorName",
    "ListFileSystemAssociationsPaginatorName",
    "ListGatewaysPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTapePoolsPaginatorName",
    "ListTapesPaginatorName",
    "ListVolumesPaginatorName",
    "ObjectACL",
    "PoolStatus",
    "RetentionLockType",
    "SMBSecurityStrategy",
    "TapeStorageClass",
)


ActiveDirectoryStatus = Literal[
    "ACCESS_DENIED", "DETACHED", "JOINED", "JOINING", "NETWORK_ERROR", "TIMEOUT", "UNKNOWN_ERROR"
]
AvailabilityMonitorTestStatus = Literal["COMPLETE", "FAILED", "PENDING"]
CaseSensitivity = Literal["CaseSensitive", "ClientSpecified"]
DescribeTapeArchivesPaginatorName = Literal["describe_tape_archives"]
DescribeTapeRecoveryPointsPaginatorName = Literal["describe_tape_recovery_points"]
DescribeTapesPaginatorName = Literal["describe_tapes"]
DescribeVTLDevicesPaginatorName = Literal["describe_vtl_devices"]
FileShareType = Literal["NFS", "SMB"]
HostEnvironment = Literal["EC2", "HYPER-V", "KVM", "OTHER", "VMWARE"]
ListFileSharesPaginatorName = Literal["list_file_shares"]
ListFileSystemAssociationsPaginatorName = Literal["list_file_system_associations"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTapePoolsPaginatorName = Literal["list_tape_pools"]
ListTapesPaginatorName = Literal["list_tapes"]
ListVolumesPaginatorName = Literal["list_volumes"]
ObjectACL = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
PoolStatus = Literal["ACTIVE", "DELETED"]
RetentionLockType = Literal["COMPLIANCE", "GOVERNANCE", "NONE"]
SMBSecurityStrategy = Literal["ClientSpecified", "MandatoryEncryption", "MandatorySigning"]
TapeStorageClass = Literal["DEEP_ARCHIVE", "GLACIER"]
