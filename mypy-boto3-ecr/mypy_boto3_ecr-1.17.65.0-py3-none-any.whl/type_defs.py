"""
Type annotations for ecr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_ecr.literals import (
    EncryptionType,
    FindingSeverity,
    ImageFailureCode,
    ImageTagMutability,
    LayerAvailability,
    LayerFailureCode,
    LifecyclePolicyPreviewStatus,
    ScanStatus,
    TagStatus,
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
    "AttributeTypeDef",
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "BatchGetImageResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeleteRegistryPolicyResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageScanFindingsResponseTypeDef",
    "DescribeImagesFilterTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetDownloadUrlForLayerResponseTypeDef",
    "GetLifecyclePolicyPreviewResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetRegistryPolicyResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsSummaryTypeDef",
    "ImageScanFindingsTypeDef",
    "ImageScanStatusTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "LifecyclePolicyPreviewFilterTypeDef",
    "LifecyclePolicyPreviewResultTypeDef",
    "LifecyclePolicyPreviewSummaryTypeDef",
    "LifecyclePolicyRuleActionTypeDef",
    "ListImagesFilterTypeDef",
    "ListImagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageResponseTypeDef",
    "PutImageScanningConfigurationResponseTypeDef",
    "PutImageTagMutabilityResponseTypeDef",
    "PutLifecyclePolicyResponseTypeDef",
    "PutRegistryPolicyResponseTypeDef",
    "PutReplicationConfigurationResponseTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationDestinationTypeDef",
    "ReplicationRuleTypeDef",
    "RepositoryTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "StartImageScanResponseTypeDef",
    "StartLifecyclePolicyPreviewResponseTypeDef",
    "TagTypeDef",
    "UploadLayerPartResponseTypeDef",
    "WaiterConfigTypeDef",
)


class _RequiredAttributeTypeDef(TypedDict):
    key: str


class AttributeTypeDef(_RequiredAttributeTypeDef, total=False):
    value: str


class AuthorizationDataTypeDef(TypedDict, total=False):
    authorizationToken: str
    expiresAt: datetime
    proxyEndpoint: str


class BatchCheckLayerAvailabilityResponseTypeDef(TypedDict, total=False):
    layers: List["LayerTypeDef"]
    failures: List["LayerFailureTypeDef"]


class BatchDeleteImageResponseTypeDef(TypedDict, total=False):
    imageIds: List["ImageIdentifierTypeDef"]
    failures: List["ImageFailureTypeDef"]


class BatchGetImageResponseTypeDef(TypedDict, total=False):
    images: List["ImageTypeDef"]
    failures: List["ImageFailureTypeDef"]


class CompleteLayerUploadResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str


class CreateRepositoryResponseTypeDef(TypedDict, total=False):
    repository: "RepositoryTypeDef"


class DeleteLifecyclePolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime


class DeleteRegistryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    policyText: str


class DeleteRepositoryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    policyText: str


class DeleteRepositoryResponseTypeDef(TypedDict, total=False):
    repository: "RepositoryTypeDef"


class DescribeImageScanFindingsResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageId: "ImageIdentifierTypeDef"
    imageScanStatus: "ImageScanStatusTypeDef"
    imageScanFindings: "ImageScanFindingsTypeDef"
    nextToken: str


class DescribeImagesFilterTypeDef(TypedDict, total=False):
    tagStatus: TagStatus


class DescribeImagesResponseTypeDef(TypedDict, total=False):
    imageDetails: List["ImageDetailTypeDef"]
    nextToken: str


class DescribeRegistryResponseTypeDef(TypedDict, total=False):
    registryId: str
    replicationConfiguration: "ReplicationConfigurationTypeDef"


class DescribeRepositoriesResponseTypeDef(TypedDict, total=False):
    repositories: List["RepositoryTypeDef"]
    nextToken: str


class _RequiredEncryptionConfigurationTypeDef(TypedDict):
    encryptionType: EncryptionType


class EncryptionConfigurationTypeDef(_RequiredEncryptionConfigurationTypeDef, total=False):
    kmsKey: str


class GetAuthorizationTokenResponseTypeDef(TypedDict, total=False):
    authorizationData: List["AuthorizationDataTypeDef"]


class GetDownloadUrlForLayerResponseTypeDef(TypedDict, total=False):
    downloadUrl: str
    layerDigest: str


class GetLifecyclePolicyPreviewResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatus
    nextToken: str
    previewResults: List["LifecyclePolicyPreviewResultTypeDef"]
    summary: "LifecyclePolicyPreviewSummaryTypeDef"


class GetLifecyclePolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime


class GetRegistryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    policyText: str


class GetRepositoryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    policyText: str


class ImageDetailTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageDigest: str
    imageTags: List[str]
    imageSizeInBytes: int
    imagePushedAt: datetime
    imageScanStatus: "ImageScanStatusTypeDef"
    imageScanFindingsSummary: "ImageScanFindingsSummaryTypeDef"
    imageManifestMediaType: str
    artifactMediaType: str


class ImageFailureTypeDef(TypedDict, total=False):
    imageId: "ImageIdentifierTypeDef"
    failureCode: ImageFailureCode
    failureReason: str


class ImageIdentifierTypeDef(TypedDict, total=False):
    imageDigest: str
    imageTag: str


class ImageScanFindingTypeDef(TypedDict, total=False):
    name: str
    description: str
    uri: str
    severity: FindingSeverity
    attributes: List["AttributeTypeDef"]


class ImageScanFindingsSummaryTypeDef(TypedDict, total=False):
    imageScanCompletedAt: datetime
    vulnerabilitySourceUpdatedAt: datetime
    findingSeverityCounts: Dict[FindingSeverity, int]


class ImageScanFindingsTypeDef(TypedDict, total=False):
    imageScanCompletedAt: datetime
    vulnerabilitySourceUpdatedAt: datetime
    findings: List["ImageScanFindingTypeDef"]
    findingSeverityCounts: Dict[FindingSeverity, int]


class ImageScanStatusTypeDef(TypedDict, total=False):
    status: ScanStatus
    description: str


class ImageScanningConfigurationTypeDef(TypedDict, total=False):
    scanOnPush: bool


class ImageTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageId: "ImageIdentifierTypeDef"
    imageManifest: str
    imageManifestMediaType: str


class InitiateLayerUploadResponseTypeDef(TypedDict, total=False):
    uploadId: str
    partSize: int


class LayerFailureTypeDef(TypedDict, total=False):
    layerDigest: str
    failureCode: LayerFailureCode
    failureReason: str


class LayerTypeDef(TypedDict, total=False):
    layerDigest: str
    layerAvailability: LayerAvailability
    layerSize: int
    mediaType: str


class LifecyclePolicyPreviewFilterTypeDef(TypedDict, total=False):
    tagStatus: TagStatus


class LifecyclePolicyPreviewResultTypeDef(TypedDict, total=False):
    imageTags: List[str]
    imageDigest: str
    imagePushedAt: datetime
    action: "LifecyclePolicyRuleActionTypeDef"
    appliedRulePriority: int


class LifecyclePolicyPreviewSummaryTypeDef(TypedDict, total=False):
    expiringImageTotalCount: int


LifecyclePolicyRuleActionTypeDef = TypedDict(
    "LifecyclePolicyRuleActionTypeDef", {"type": Literal["EXPIRE"]}, total=False
)


class ListImagesFilterTypeDef(TypedDict, total=False):
    tagStatus: TagStatus


class ListImagesResponseTypeDef(TypedDict, total=False):
    imageIds: List["ImageIdentifierTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutImageResponseTypeDef(TypedDict, total=False):
    image: "ImageTypeDef"


class PutImageScanningConfigurationResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageScanningConfiguration: "ImageScanningConfigurationTypeDef"


class PutImageTagMutabilityResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageTagMutability: ImageTagMutability


class PutLifecyclePolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str


class PutRegistryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    policyText: str


class PutReplicationConfigurationResponseTypeDef(TypedDict, total=False):
    replicationConfiguration: "ReplicationConfigurationTypeDef"


class ReplicationConfigurationTypeDef(TypedDict):
    rules: List["ReplicationRuleTypeDef"]


class ReplicationDestinationTypeDef(TypedDict):
    region: str
    registryId: str


class ReplicationRuleTypeDef(TypedDict):
    destinations: List["ReplicationDestinationTypeDef"]


class RepositoryTypeDef(TypedDict, total=False):
    repositoryArn: str
    registryId: str
    repositoryName: str
    repositoryUri: str
    createdAt: datetime
    imageTagMutability: ImageTagMutability
    imageScanningConfiguration: "ImageScanningConfigurationTypeDef"
    encryptionConfiguration: "EncryptionConfigurationTypeDef"


class SetRepositoryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    policyText: str


class StartImageScanResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    imageId: "ImageIdentifierTypeDef"
    imageScanStatus: "ImageScanStatusTypeDef"


class StartLifecyclePolicyPreviewResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatus


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UploadLayerPartResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
