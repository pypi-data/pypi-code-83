"""
Main interface for codeartifact service type definitions.

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
    ExternalConnectionStatus,
    HashAlgorithm,
    PackageFormat,
    PackageVersionErrorCode,
    PackageVersionStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssetSummaryTypeDef",
    "DomainDescriptionTypeDef",
    "DomainSummaryTypeDef",
    "LicenseInfoTypeDef",
    "PackageDependencyTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionSummaryTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagTypeDef",
    "UpstreamRepositoryInfoTypeDef",
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
    "GetAuthorizationTokenResultTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListPackageVersionsResultTypeDef",
    "ListPackagesResultTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "UpdateRepositoryResultTypeDef",
    "UpstreamRepositoryTypeDef",
)

_RequiredAssetSummaryTypeDef = TypedDict("_RequiredAssetSummaryTypeDef", {"name": str})
_OptionalAssetSummaryTypeDef = TypedDict(
    "_OptionalAssetSummaryTypeDef", {"size": int, "hashes": Dict[HashAlgorithm, str]}, total=False
)


class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, _OptionalAssetSummaryTypeDef):
    pass


DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatus,
        "createdTime": datetime,
        "encryptionKey": str,
        "repositoryCount": int,
        "assetSizeBytes": int,
        "s3BucketArn": str,
    },
    total=False,
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatus,
        "createdTime": datetime,
        "encryptionKey": str,
    },
    total=False,
)

LicenseInfoTypeDef = TypedDict("LicenseInfoTypeDef", {"name": str, "url": str}, total=False)

PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {"namespace": str, "package": str, "dependencyType": str, "versionRequirement": str},
    total=False,
)

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

PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {"errorCode": PackageVersionErrorCode, "errorMessage": str},
    total=False,
)

_RequiredPackageVersionSummaryTypeDef = TypedDict(
    "_RequiredPackageVersionSummaryTypeDef", {"version": str, "status": PackageVersionStatus}
)
_OptionalPackageVersionSummaryTypeDef = TypedDict(
    "_OptionalPackageVersionSummaryTypeDef", {"revision": str}, total=False
)


class PackageVersionSummaryTypeDef(
    _RequiredPackageVersionSummaryTypeDef, _OptionalPackageVersionSummaryTypeDef
):
    pass


RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryInfoTypeDef"],
        "externalConnections": List["RepositoryExternalConnectionInfoTypeDef"],
    },
    total=False,
)

RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": str,
        "packageFormat": PackageFormat,
        "status": ExternalConnectionStatus,
    },
    total=False,
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef", {"resourceArn": str, "revision": str, "document": str}, total=False
)

SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {"revision": str, "status": PackageVersionStatus},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef", {"repositoryName": str}, total=False
)

AssociateExternalConnectionResultTypeDef = TypedDict(
    "AssociateExternalConnectionResultTypeDef",
    {"repository": "RepositoryDescriptionTypeDef"},
    total=False,
)

CopyPackageVersionsResultTypeDef = TypedDict(
    "CopyPackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
    },
    total=False,
)

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef", {"domain": "DomainDescriptionTypeDef"}, total=False
)

CreateRepositoryResultTypeDef = TypedDict(
    "CreateRepositoryResultTypeDef", {"repository": "RepositoryDescriptionTypeDef"}, total=False
)

DeleteDomainPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultTypeDef", {"policy": "ResourcePolicyTypeDef"}, total=False
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef", {"domain": "DomainDescriptionTypeDef"}, total=False
)

DeletePackageVersionsResultTypeDef = TypedDict(
    "DeletePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
    },
    total=False,
)

DeleteRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    {"policy": "ResourcePolicyTypeDef"},
    total=False,
)

DeleteRepositoryResultTypeDef = TypedDict(
    "DeleteRepositoryResultTypeDef", {"repository": "RepositoryDescriptionTypeDef"}, total=False
)

DescribeDomainResultTypeDef = TypedDict(
    "DescribeDomainResultTypeDef", {"domain": "DomainDescriptionTypeDef"}, total=False
)

DescribePackageVersionResultTypeDef = TypedDict(
    "DescribePackageVersionResultTypeDef", {"packageVersion": "PackageVersionDescriptionTypeDef"}
)

DescribeRepositoryResultTypeDef = TypedDict(
    "DescribeRepositoryResultTypeDef", {"repository": "RepositoryDescriptionTypeDef"}, total=False
)

DisassociateExternalConnectionResultTypeDef = TypedDict(
    "DisassociateExternalConnectionResultTypeDef",
    {"repository": "RepositoryDescriptionTypeDef"},
    total=False,
)

DisposePackageVersionsResultTypeDef = TypedDict(
    "DisposePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
    },
    total=False,
)

GetAuthorizationTokenResultTypeDef = TypedDict(
    "GetAuthorizationTokenResultTypeDef",
    {"authorizationToken": str, "expiration": datetime},
    total=False,
)

GetDomainPermissionsPolicyResultTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultTypeDef", {"policy": "ResourcePolicyTypeDef"}, total=False
)

GetPackageVersionAssetResultTypeDef = TypedDict(
    "GetPackageVersionAssetResultTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
    },
    total=False,
)

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

GetRepositoryEndpointResultTypeDef = TypedDict(
    "GetRepositoryEndpointResultTypeDef", {"repositoryEndpoint": str}, total=False
)

GetRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultTypeDef", {"policy": "ResourcePolicyTypeDef"}, total=False
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {"domains": List["DomainSummaryTypeDef"], "nextToken": str},
    total=False,
)

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

ListPackagesResultTypeDef = TypedDict(
    "ListPackagesResultTypeDef",
    {"packages": List["PackageSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListRepositoriesInDomainResultTypeDef = TypedDict(
    "ListRepositoriesInDomainResultTypeDef",
    {"repositories": List["RepositorySummaryTypeDef"], "nextToken": str},
    total=False,
)

ListRepositoriesResultTypeDef = TypedDict(
    "ListRepositoriesResultTypeDef",
    {"repositories": List["RepositorySummaryTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutDomainPermissionsPolicyResultTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultTypeDef", {"policy": "ResourcePolicyTypeDef"}, total=False
)

PutRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultTypeDef", {"policy": "ResourcePolicyTypeDef"}, total=False
)

UpdatePackageVersionsStatusResultTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
    },
    total=False,
)

UpdateRepositoryResultTypeDef = TypedDict(
    "UpdateRepositoryResultTypeDef", {"repository": "RepositoryDescriptionTypeDef"}, total=False
)

UpstreamRepositoryTypeDef = TypedDict("UpstreamRepositoryTypeDef", {"repositoryName": str})
