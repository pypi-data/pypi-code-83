"""
Type annotations for ecr service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr/literals.html)

Usage::

    ```python
    from mypy_boto3_ecr.literals import DescribeImageScanFindingsPaginatorName

    data: DescribeImageScanFindingsPaginatorName = "describe_image_scan_findings"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeImageScanFindingsPaginatorName",
    "DescribeImagesPaginatorName",
    "DescribeRepositoriesPaginatorName",
    "EncryptionType",
    "FindingSeverity",
    "GetLifecyclePolicyPreviewPaginatorName",
    "ImageActionType",
    "ImageFailureCode",
    "ImageScanCompleteWaiterName",
    "ImageTagMutability",
    "LayerAvailability",
    "LayerFailureCode",
    "LifecyclePolicyPreviewCompleteWaiterName",
    "LifecyclePolicyPreviewStatus",
    "ListImagesPaginatorName",
    "ScanStatus",
    "TagStatus",
)


DescribeImageScanFindingsPaginatorName = Literal["describe_image_scan_findings"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribeRepositoriesPaginatorName = Literal["describe_repositories"]
EncryptionType = Literal["AES256", "KMS"]
FindingSeverity = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNDEFINED"]
GetLifecyclePolicyPreviewPaginatorName = Literal["get_lifecycle_policy_preview"]
ImageActionType = Literal["EXPIRE"]
ImageFailureCode = Literal[
    "ImageNotFound",
    "ImageReferencedByManifestList",
    "ImageTagDoesNotMatchDigest",
    "InvalidImageDigest",
    "InvalidImageTag",
    "KmsError",
    "MissingDigestAndTag",
]
ImageScanCompleteWaiterName = Literal["image_scan_complete"]
ImageTagMutability = Literal["IMMUTABLE", "MUTABLE"]
LayerAvailability = Literal["AVAILABLE", "UNAVAILABLE"]
LayerFailureCode = Literal["InvalidLayerDigest", "MissingLayerDigest"]
LifecyclePolicyPreviewCompleteWaiterName = Literal["lifecycle_policy_preview_complete"]
LifecyclePolicyPreviewStatus = Literal["COMPLETE", "EXPIRED", "FAILED", "IN_PROGRESS"]
ListImagesPaginatorName = Literal["list_images"]
ScanStatus = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
TagStatus = Literal["ANY", "TAGGED", "UNTAGGED"]
