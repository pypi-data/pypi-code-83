"""
Type annotations for ecr-public service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef

    data: AuthorizationDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_ecr_public.literals import (
    ImageFailureCode,
    LayerAvailability,
    LayerFailureCode,
    RegistryAliasStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageTagsResponseTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistriesResponseTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetRegistryCatalogDataResponseTypeDef",
    "GetRepositoryCatalogDataResponseTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageTagDetailTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageResponseTypeDef",
    "PutRegistryCatalogDataResponseTypeDef",
    "PutRepositoryCatalogDataResponseTypeDef",
    "ReferencedImageDetailTypeDef",
    "RegistryAliasTypeDef",
    "RegistryCatalogDataTypeDef",
    "RegistryTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "TagTypeDef",
    "UploadLayerPartResponseTypeDef",
)


class AuthorizationDataTypeDef(TypedDict, total=False):
    authorizationToken: str
    expiresAt: datetime


class BatchCheckLayerAvailabilityResponseTypeDef(TypedDict, total=False):
    layers: List["LayerTypeDef"]
    failures: List["LayerFailureTypeDef"]


class BatchDeleteImageResponseTypeDef(TypedDict, total=False):
    imageIds: List["ImageIdentifierTypeDef"]
    failures: List["ImageFailureTypeDef"]


class CompleteLayerUploadResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str


class CreateRepositoryResponseTypeDef(TypedDict, total=False):
    repository: "RepositoryTypeDef"
    catalogData: "RepositoryCatalogDataTypeDef"


class DeleteRepositoryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    policyText: str


class DeleteRepositoryResponseTypeDef(TypedDict, total=False):
    repository: "RepositoryTypeDef"


class DescribeImageTagsResponseTypeDef(TypedDict, total=False):
    imageTagDetails: List["ImageTagDetailTypeDef"]
    nextToken: str


class DescribeImagesResponseTypeDef(TypedDict, total=False):
    imageDetails: List["ImageDetailTypeDef"]
    nextToken: str


class _RequiredDescribeRegistriesResponseTypeDef(TypedDict):
    registries: List["RegistryTypeDef"]


class DescribeRegistriesResponseTypeDef(_RequiredDescribeRegistriesResponseTypeDef, total=False):
    nextToken: str


class DescribeRepositoriesResponseTypeDef(TypedDict, total=False):
    repositories: List["RepositoryTypeDef"]
    nextToken: str


class GetAuthorizationTokenResponseTypeDef(TypedDict, total=False):
    authorizationData: "AuthorizationDataTypeDef"


class GetRegistryCatalogDataResponseTypeDef(TypedDict):
    registryCatalogData: "RegistryCatalogDataTypeDef"


class GetRepositoryCatalogDataResponseTypeDef(TypedDict, total=False):
    catalogData: "RepositoryCatalogDataTypeDef"


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
    imageManifestMediaType: str
    artifactMediaType: str


class ImageFailureTypeDef(TypedDict, total=False):
    imageId: "ImageIdentifierTypeDef"
    failureCode: ImageFailureCode
    failureReason: str


class ImageIdentifierTypeDef(TypedDict, total=False):
    imageDigest: str
    imageTag: str


class ImageTagDetailTypeDef(TypedDict, total=False):
    imageTag: str
    createdAt: datetime
    imageDetail: "ReferencedImageDetailTypeDef"


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


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutImageResponseTypeDef(TypedDict, total=False):
    image: "ImageTypeDef"


class PutRegistryCatalogDataResponseTypeDef(TypedDict):
    registryCatalogData: "RegistryCatalogDataTypeDef"


class PutRepositoryCatalogDataResponseTypeDef(TypedDict, total=False):
    catalogData: "RepositoryCatalogDataTypeDef"


class ReferencedImageDetailTypeDef(TypedDict, total=False):
    imageDigest: str
    imageSizeInBytes: int
    imagePushedAt: datetime
    imageManifestMediaType: str
    artifactMediaType: str


class RegistryAliasTypeDef(TypedDict):
    name: str
    status: RegistryAliasStatus
    primaryRegistryAlias: bool
    defaultRegistryAlias: bool


class RegistryCatalogDataTypeDef(TypedDict, total=False):
    displayName: str


class RegistryTypeDef(TypedDict):
    registryId: str
    registryArn: str
    registryUri: str
    verified: bool
    aliases: List["RegistryAliasTypeDef"]


class RepositoryCatalogDataInputTypeDef(TypedDict, total=False):
    description: str
    architectures: List[str]
    operatingSystems: List[str]
    logoImageBlob: Union[bytes, IO[bytes]]
    aboutText: str
    usageText: str


class RepositoryCatalogDataTypeDef(TypedDict, total=False):
    description: str
    architectures: List[str]
    operatingSystems: List[str]
    logoUrl: str
    aboutText: str
    usageText: str
    marketplaceCertified: bool


class RepositoryTypeDef(TypedDict, total=False):
    repositoryArn: str
    registryId: str
    repositoryName: str
    repositoryUri: str
    createdAt: datetime


class SetRepositoryPolicyResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    policyText: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UploadLayerPartResponseTypeDef(TypedDict, total=False):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
