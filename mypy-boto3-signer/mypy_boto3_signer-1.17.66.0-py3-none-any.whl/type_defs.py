"""
Type annotations for signer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionResponseTypeDef

    data: AddProfilePermissionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_signer.literals import (
    EncryptionAlgorithm,
    HashAlgorithm,
    ImageFormat,
    SigningProfileStatus,
    SigningStatus,
    ValidityType,
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
    "AddProfilePermissionResponseTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "GetSigningProfileResponseTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsResponseTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
    "S3DestinationTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SignatureValidityPeriodTypeDef",
    "SignedObjectTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "SigningConfigurationTypeDef",
    "SigningImageFormatTypeDef",
    "SigningJobRevocationRecordTypeDef",
    "SigningJobTypeDef",
    "SigningMaterialTypeDef",
    "SigningPlatformOverridesTypeDef",
    "SigningPlatformTypeDef",
    "SigningProfileRevocationRecordTypeDef",
    "SigningProfileTypeDef",
    "SourceTypeDef",
    "StartSigningJobResponseTypeDef",
    "WaiterConfigTypeDef",
)


class AddProfilePermissionResponseTypeDef(TypedDict, total=False):
    revisionId: str


class DescribeSigningJobResponseTypeDef(TypedDict, total=False):
    jobId: str
    source: "SourceTypeDef"
    signingMaterial: "SigningMaterialTypeDef"
    platformId: str
    platformDisplayName: str
    profileName: str
    profileVersion: str
    overrides: "SigningPlatformOverridesTypeDef"
    signingParameters: Dict[str, str]
    createdAt: datetime
    completedAt: datetime
    signatureExpiresAt: datetime
    requestedBy: str
    status: SigningStatus
    statusReason: str
    revocationRecord: "SigningJobRevocationRecordTypeDef"
    signedObject: "SignedObjectTypeDef"
    jobOwner: str
    jobInvoker: str


class DestinationTypeDef(TypedDict, total=False):
    s3: "S3DestinationTypeDef"


class EncryptionAlgorithmOptionsTypeDef(TypedDict):
    allowedValues: List[EncryptionAlgorithm]
    defaultValue: EncryptionAlgorithm


class GetSigningPlatformResponseTypeDef(TypedDict, total=False):
    platformId: str
    displayName: str
    partner: str
    target: str
    category: Literal["AWSIoT"]
    signingConfiguration: "SigningConfigurationTypeDef"
    signingImageFormat: "SigningImageFormatTypeDef"
    maxSizeInMB: int
    revocationSupported: bool


class GetSigningProfileResponseTypeDef(TypedDict, total=False):
    profileName: str
    profileVersion: str
    profileVersionArn: str
    revocationRecord: "SigningProfileRevocationRecordTypeDef"
    signingMaterial: "SigningMaterialTypeDef"
    platformId: str
    platformDisplayName: str
    signatureValidityPeriod: "SignatureValidityPeriodTypeDef"
    overrides: "SigningPlatformOverridesTypeDef"
    signingParameters: Dict[str, str]
    status: SigningProfileStatus
    statusReason: str
    arn: str
    tags: Dict[str, str]


class HashAlgorithmOptionsTypeDef(TypedDict):
    allowedValues: List[HashAlgorithm]
    defaultValue: HashAlgorithm


class ListProfilePermissionsResponseTypeDef(TypedDict, total=False):
    revisionId: str
    policySizeBytes: int
    permissions: List["PermissionTypeDef"]
    nextToken: str


class ListSigningJobsResponseTypeDef(TypedDict, total=False):
    jobs: List["SigningJobTypeDef"]
    nextToken: str


class ListSigningPlatformsResponseTypeDef(TypedDict, total=False):
    platforms: List["SigningPlatformTypeDef"]
    nextToken: str


class ListSigningProfilesResponseTypeDef(TypedDict, total=False):
    profiles: List["SigningProfileTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionTypeDef(TypedDict, total=False):
    action: str
    principal: str
    statementId: str
    profileVersion: str


class PutSigningProfileResponseTypeDef(TypedDict, total=False):
    arn: str
    profileVersion: str
    profileVersionArn: str


class RemoveProfilePermissionResponseTypeDef(TypedDict, total=False):
    revisionId: str


class S3DestinationTypeDef(TypedDict, total=False):
    bucketName: str
    prefix: str


class S3SignedObjectTypeDef(TypedDict, total=False):
    bucketName: str
    key: str


class S3SourceTypeDef(TypedDict):
    bucketName: str
    key: str
    version: str


SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef", {"value": int, "type": ValidityType}, total=False
)


class SignedObjectTypeDef(TypedDict, total=False):
    s3: "S3SignedObjectTypeDef"


class SigningConfigurationOverridesTypeDef(TypedDict, total=False):
    encryptionAlgorithm: EncryptionAlgorithm
    hashAlgorithm: HashAlgorithm


class SigningConfigurationTypeDef(TypedDict):
    encryptionAlgorithmOptions: "EncryptionAlgorithmOptionsTypeDef"
    hashAlgorithmOptions: "HashAlgorithmOptionsTypeDef"


class SigningImageFormatTypeDef(TypedDict):
    supportedFormats: List[ImageFormat]
    defaultFormat: ImageFormat


class SigningJobRevocationRecordTypeDef(TypedDict, total=False):
    reason: str
    revokedAt: datetime
    revokedBy: str


class SigningJobTypeDef(TypedDict, total=False):
    jobId: str
    source: "SourceTypeDef"
    signedObject: "SignedObjectTypeDef"
    signingMaterial: "SigningMaterialTypeDef"
    createdAt: datetime
    status: SigningStatus
    isRevoked: bool
    profileName: str
    profileVersion: str
    platformId: str
    platformDisplayName: str
    signatureExpiresAt: datetime
    jobOwner: str
    jobInvoker: str


class SigningMaterialTypeDef(TypedDict):
    certificateArn: str


class SigningPlatformOverridesTypeDef(TypedDict, total=False):
    signingConfiguration: "SigningConfigurationOverridesTypeDef"
    signingImageFormat: ImageFormat


class SigningPlatformTypeDef(TypedDict, total=False):
    platformId: str
    displayName: str
    partner: str
    target: str
    category: Literal["AWSIoT"]
    signingConfiguration: "SigningConfigurationTypeDef"
    signingImageFormat: "SigningImageFormatTypeDef"
    maxSizeInMB: int
    revocationSupported: bool


class SigningProfileRevocationRecordTypeDef(TypedDict, total=False):
    revocationEffectiveFrom: datetime
    revokedAt: datetime
    revokedBy: str


class SigningProfileTypeDef(TypedDict, total=False):
    profileName: str
    profileVersion: str
    profileVersionArn: str
    signingMaterial: "SigningMaterialTypeDef"
    signatureValidityPeriod: "SignatureValidityPeriodTypeDef"
    platformId: str
    platformDisplayName: str
    signingParameters: Dict[str, str]
    status: SigningProfileStatus
    arn: str
    tags: Dict[str, str]


class SourceTypeDef(TypedDict, total=False):
    s3: "S3SourceTypeDef"


class StartSigningJobResponseTypeDef(TypedDict, total=False):
    jobId: str
    jobOwner: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
