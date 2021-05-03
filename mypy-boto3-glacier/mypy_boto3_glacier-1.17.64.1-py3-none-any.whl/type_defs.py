"""
Type annotations for glacier service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glacier/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glacier.type_defs import ArchiveCreationOutputTypeDef

    data: ArchiveCreationOutputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from botocore.response import StreamingBody

from mypy_boto3_glacier.literals import (
    ActionCode,
    CannedACL,
    EncryptionType,
    FileHeaderInfo,
    Permission,
    QuoteFields,
    StatusCode,
    StorageClass,
    TypeType,
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
    "ArchiveCreationOutputTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CreateVaultOutputTypeDef",
    "DataRetrievalPolicyTypeDef",
    "DataRetrievalRuleTypeDef",
    "DescribeVaultOutputTypeDef",
    "EncryptionTypeDef",
    "GetDataRetrievalPolicyOutputTypeDef",
    "GetJobOutputOutputTypeDef",
    "GetVaultAccessPolicyOutputTypeDef",
    "GetVaultLockOutputTypeDef",
    "GetVaultNotificationsOutputTypeDef",
    "GlacierJobDescriptionTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "InitiateJobOutputTypeDef",
    "InitiateMultipartUploadOutputTypeDef",
    "InitiateVaultLockOutputTypeDef",
    "InputSerializationTypeDef",
    "InventoryRetrievalJobDescriptionTypeDef",
    "InventoryRetrievalJobInputTypeDef",
    "JobParametersTypeDef",
    "ListJobsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListPartsOutputTypeDef",
    "ListProvisionedCapacityOutputTypeDef",
    "ListTagsForVaultOutputTypeDef",
    "ListVaultsOutputTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "PaginatorConfigTypeDef",
    "PartListElementTypeDef",
    "ProvisionedCapacityDescriptionTypeDef",
    "PurchaseProvisionedCapacityOutputTypeDef",
    "ResponseMetadata",
    "S3LocationTypeDef",
    "SelectParametersTypeDef",
    "UploadListElementTypeDef",
    "UploadMultipartPartOutputTypeDef",
    "VaultAccessPolicyTypeDef",
    "VaultLockPolicyTypeDef",
    "VaultNotificationConfigTypeDef",
    "WaiterConfigTypeDef",
)


class ArchiveCreationOutputTypeDef(TypedDict):
    location: str
    checksum: str
    archiveId: str
    ResponseMetadata: "ResponseMetadata"


class CSVInputTypeDef(TypedDict, total=False):
    FileHeaderInfo: FileHeaderInfo
    Comments: str
    QuoteEscapeCharacter: str
    RecordDelimiter: str
    FieldDelimiter: str
    QuoteCharacter: str


class CSVOutputTypeDef(TypedDict):
    QuoteFields: QuoteFields
    QuoteEscapeCharacter: str
    RecordDelimiter: str
    FieldDelimiter: str
    QuoteCharacter: str
    ResponseMetadata: "ResponseMetadata"


class CreateVaultOutputTypeDef(TypedDict):
    location: str
    ResponseMetadata: "ResponseMetadata"


class DataRetrievalPolicyTypeDef(TypedDict, total=False):
    Rules: List["DataRetrievalRuleTypeDef"]


class DataRetrievalRuleTypeDef(TypedDict, total=False):
    Strategy: str
    BytesPerHour: int


class DescribeVaultOutputTypeDef(TypedDict):
    VaultARN: str
    VaultName: str
    CreationDate: str
    LastInventoryDate: str
    NumberOfArchives: int
    SizeInBytes: int
    ResponseMetadata: "ResponseMetadata"


class EncryptionTypeDef(TypedDict, total=False):
    EncryptionType: EncryptionType
    KMSKeyId: str
    KMSContext: str


class GetDataRetrievalPolicyOutputTypeDef(TypedDict):
    Policy: "DataRetrievalPolicyTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetJobOutputOutputTypeDef(TypedDict):
    body: StreamingBody
    checksum: str
    status: int
    contentRange: str
    acceptRanges: str
    contentType: str
    archiveDescription: str
    ResponseMetadata: "ResponseMetadata"


class GetVaultAccessPolicyOutputTypeDef(TypedDict):
    policy: "VaultAccessPolicyTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetVaultLockOutputTypeDef(TypedDict):
    Policy: str
    State: str
    ExpirationDate: str
    CreationDate: str
    ResponseMetadata: "ResponseMetadata"


class GetVaultNotificationsOutputTypeDef(TypedDict):
    vaultNotificationConfig: "VaultNotificationConfigTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GlacierJobDescriptionTypeDef(TypedDict, total=False):
    JobId: str
    JobDescription: str
    Action: ActionCode
    ArchiveId: str
    VaultARN: str
    CreationDate: str
    Completed: bool
    StatusCode: StatusCode
    StatusMessage: str
    ArchiveSizeInBytes: int
    InventorySizeInBytes: int
    SNSTopic: str
    CompletionDate: str
    SHA256TreeHash: str
    ArchiveSHA256TreeHash: str
    RetrievalByteRange: str
    Tier: str
    InventoryRetrievalParameters: "InventoryRetrievalJobDescriptionTypeDef"
    JobOutputPath: str
    SelectParameters: "SelectParametersTypeDef"
    OutputLocation: "OutputLocationTypeDef"


class GrantTypeDef(TypedDict, total=False):
    Grantee: "GranteeTypeDef"
    Permission: Permission


_RequiredGranteeTypeDef = TypedDict("_RequiredGranteeTypeDef", {"Type": TypeType})
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {"DisplayName": str, "URI": str, "ID": str, "EmailAddress": str},
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


class InitiateJobOutputTypeDef(TypedDict):
    location: str
    jobId: str
    jobOutputPath: str
    ResponseMetadata: "ResponseMetadata"


class InitiateMultipartUploadOutputTypeDef(TypedDict):
    location: str
    uploadId: str
    ResponseMetadata: "ResponseMetadata"


class InitiateVaultLockOutputTypeDef(TypedDict):
    lockId: str
    ResponseMetadata: "ResponseMetadata"


class InputSerializationTypeDef(TypedDict, total=False):
    csv: "CSVInputTypeDef"


class InventoryRetrievalJobDescriptionTypeDef(TypedDict, total=False):
    Format: str
    StartDate: str
    EndDate: str
    Limit: str
    Marker: str


class InventoryRetrievalJobInputTypeDef(TypedDict, total=False):
    StartDate: str
    EndDate: str
    Limit: str
    Marker: str


JobParametersTypeDef = TypedDict(
    "JobParametersTypeDef",
    {
        "Format": str,
        "Type": str,
        "ArchiveId": str,
        "Description": str,
        "SNSTopic": str,
        "RetrievalByteRange": str,
        "Tier": str,
        "InventoryRetrievalParameters": "InventoryRetrievalJobInputTypeDef",
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)


class ListJobsOutputTypeDef(TypedDict):
    JobList: List["GlacierJobDescriptionTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListMultipartUploadsOutputTypeDef(TypedDict):
    UploadsList: List["UploadListElementTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListPartsOutputTypeDef(TypedDict):
    MultipartUploadId: str
    VaultARN: str
    ArchiveDescription: str
    PartSizeInBytes: int
    CreationDate: str
    Parts: List["PartListElementTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListProvisionedCapacityOutputTypeDef(TypedDict):
    ProvisionedCapacityList: List["ProvisionedCapacityDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListTagsForVaultOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class ListVaultsOutputTypeDef(TypedDict):
    VaultList: List["DescribeVaultOutputTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class OutputLocationTypeDef(TypedDict, total=False):
    S3: "S3LocationTypeDef"


class OutputSerializationTypeDef(TypedDict, total=False):
    csv: "CSVOutputTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartListElementTypeDef(TypedDict, total=False):
    RangeInBytes: str
    SHA256TreeHash: str


class ProvisionedCapacityDescriptionTypeDef(TypedDict, total=False):
    CapacityId: str
    StartDate: str
    ExpirationDate: str


class PurchaseProvisionedCapacityOutputTypeDef(TypedDict):
    capacityId: str
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3LocationTypeDef(TypedDict, total=False):
    BucketName: str
    Prefix: str
    Encryption: "EncryptionTypeDef"
    CannedACL: CannedACL
    AccessControlList: List["GrantTypeDef"]
    Tagging: Dict[str, str]
    UserMetadata: Dict[str, str]
    StorageClass: StorageClass


class SelectParametersTypeDef(TypedDict, total=False):
    InputSerialization: "InputSerializationTypeDef"
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: "OutputSerializationTypeDef"


class UploadListElementTypeDef(TypedDict, total=False):
    MultipartUploadId: str
    VaultARN: str
    ArchiveDescription: str
    PartSizeInBytes: int
    CreationDate: str


class UploadMultipartPartOutputTypeDef(TypedDict):
    checksum: str
    ResponseMetadata: "ResponseMetadata"


class VaultAccessPolicyTypeDef(TypedDict, total=False):
    Policy: str


class VaultLockPolicyTypeDef(TypedDict, total=False):
    Policy: str


class VaultNotificationConfigTypeDef(TypedDict, total=False):
    SNSTopic: str
    Events: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
