"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from botocore.response import StreamingBody

from mypy_boto3_codeartifact.literals import (
    DomainStatus,
    HashAlgorithm,
    PackageFormat,
    PackageVersionErrorCode,
    PackageVersionStatus,
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
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "CreateDomainResultTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteDomainResultTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeDomainResultTypeDef",
    "DescribePackageVersionResultTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "DomainDescriptionTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "LicenseInfoTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListPackageVersionsResultTypeDef",
    "ListPackagesResultTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PackageDependencyTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "UpdateRepositoryResultTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UpstreamRepositoryTypeDef",
)


class _RequiredAssetSummaryTypeDef(TypedDict):
    name: str


class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, total=False):
    size: int
    hashes: Dict[HashAlgorithm, str]


class AssociateExternalConnectionResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class CopyPackageVersionsResultTypeDef(TypedDict, total=False):
    successfulVersions: Dict[str, "SuccessfulPackageVersionInfoTypeDef"]
    failedVersions: Dict[str, "PackageVersionErrorTypeDef"]


class CreateDomainResultTypeDef(TypedDict, total=False):
    domain: "DomainDescriptionTypeDef"


class CreateRepositoryResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class DeleteDomainPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class DeleteDomainResultTypeDef(TypedDict, total=False):
    domain: "DomainDescriptionTypeDef"


class DeletePackageVersionsResultTypeDef(TypedDict, total=False):
    successfulVersions: Dict[str, "SuccessfulPackageVersionInfoTypeDef"]
    failedVersions: Dict[str, "PackageVersionErrorTypeDef"]


class DeleteRepositoryPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class DeleteRepositoryResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class DescribeDomainResultTypeDef(TypedDict, total=False):
    domain: "DomainDescriptionTypeDef"


class DescribePackageVersionResultTypeDef(TypedDict):
    packageVersion: "PackageVersionDescriptionTypeDef"


class DescribeRepositoryResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class DisassociateExternalConnectionResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class DisposePackageVersionsResultTypeDef(TypedDict, total=False):
    successfulVersions: Dict[str, "SuccessfulPackageVersionInfoTypeDef"]
    failedVersions: Dict[str, "PackageVersionErrorTypeDef"]


class DomainDescriptionTypeDef(TypedDict, total=False):
    name: str
    owner: str
    arn: str
    status: DomainStatus
    createdTime: datetime
    encryptionKey: str
    repositoryCount: int
    assetSizeBytes: int
    s3BucketArn: str


class DomainSummaryTypeDef(TypedDict, total=False):
    name: str
    owner: str
    arn: str
    status: DomainStatus
    createdTime: datetime
    encryptionKey: str


class GetAuthorizationTokenResultTypeDef(TypedDict, total=False):
    authorizationToken: str
    expiration: datetime


class GetDomainPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class GetPackageVersionAssetResultTypeDef(TypedDict, total=False):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str


GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormat,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
    },
    total=False,
)


class GetRepositoryEndpointResultTypeDef(TypedDict, total=False):
    repositoryEndpoint: str


class GetRepositoryPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class LicenseInfoTypeDef(TypedDict, total=False):
    name: str
    url: str


class ListDomainsResultTypeDef(TypedDict, total=False):
    domains: List["DomainSummaryTypeDef"]
    nextToken: str


ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormat,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List["AssetSummaryTypeDef"],
    },
    total=False,
)

ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormat,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List["PackageDependencyTypeDef"],
    },
    total=False,
)

ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormat,
        "namespace": str,
        "package": str,
        "versions": List["PackageVersionSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)


class ListPackagesResultTypeDef(TypedDict, total=False):
    packages: List["PackageSummaryTypeDef"]
    nextToken: str


class ListRepositoriesInDomainResultTypeDef(TypedDict, total=False):
    repositories: List["RepositorySummaryTypeDef"]
    nextToken: str


class ListRepositoriesResultTypeDef(TypedDict, total=False):
    repositories: List["RepositorySummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class PackageDependencyTypeDef(TypedDict, total=False):
    namespace: str
    package: str
    dependencyType: str
    versionRequirement: str


PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {"format": PackageFormat, "namespace": str, "package": str},
    total=False,
)

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": PackageFormat,
        "namespace": str,
        "packageName": str,
        "displayName": str,
        "version": str,
        "summary": str,
        "homePage": str,
        "sourceCodeRepository": str,
        "publishedTime": datetime,
        "licenses": List["LicenseInfoTypeDef"],
        "revision": str,
        "status": PackageVersionStatus,
    },
    total=False,
)


class PackageVersionErrorTypeDef(TypedDict, total=False):
    errorCode: PackageVersionErrorCode
    errorMessage: str


class _RequiredPackageVersionSummaryTypeDef(TypedDict):
    version: str
    status: PackageVersionStatus


class PackageVersionSummaryTypeDef(_RequiredPackageVersionSummaryTypeDef, total=False):
    revision: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutDomainPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class PutRepositoryPermissionsPolicyResultTypeDef(TypedDict, total=False):
    policy: "ResourcePolicyTypeDef"


class RepositoryDescriptionTypeDef(TypedDict, total=False):
    name: str
    administratorAccount: str
    domainName: str
    domainOwner: str
    arn: str
    description: str
    upstreams: List["UpstreamRepositoryInfoTypeDef"]
    externalConnections: List["RepositoryExternalConnectionInfoTypeDef"]


class RepositoryExternalConnectionInfoTypeDef(TypedDict, total=False):
    externalConnectionName: str
    packageFormat: PackageFormat
    status: Literal["Available"]


class RepositorySummaryTypeDef(TypedDict, total=False):
    name: str
    administratorAccount: str
    domainName: str
    domainOwner: str
    arn: str
    description: str


class ResourcePolicyTypeDef(TypedDict, total=False):
    resourceArn: str
    revision: str
    document: str


class SuccessfulPackageVersionInfoTypeDef(TypedDict, total=False):
    revision: str
    status: PackageVersionStatus


class TagTypeDef(TypedDict):
    key: str
    value: str


class UpdatePackageVersionsStatusResultTypeDef(TypedDict, total=False):
    successfulVersions: Dict[str, "SuccessfulPackageVersionInfoTypeDef"]
    failedVersions: Dict[str, "PackageVersionErrorTypeDef"]


class UpdateRepositoryResultTypeDef(TypedDict, total=False):
    repository: "RepositoryDescriptionTypeDef"


class UpstreamRepositoryInfoTypeDef(TypedDict, total=False):
    repositoryName: str


class UpstreamRepositoryTypeDef(TypedDict):
    repositoryName: str
