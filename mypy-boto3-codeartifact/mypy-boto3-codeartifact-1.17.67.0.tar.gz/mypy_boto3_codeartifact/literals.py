"""
Type annotations for codeartifact service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/literals.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.literals import DomainStatus

    data: DomainStatus = "Active"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DomainStatus",
    "ExternalConnectionStatus",
    "HashAlgorithm",
    "ListDomainsPaginatorName",
    "ListPackageVersionAssetsPaginatorName",
    "ListPackageVersionsPaginatorName",
    "ListPackagesPaginatorName",
    "ListRepositoriesInDomainPaginatorName",
    "ListRepositoriesPaginatorName",
    "PackageFormat",
    "PackageVersionErrorCode",
    "PackageVersionSortType",
    "PackageVersionStatus",
)


DomainStatus = Literal["Active", "Deleted"]
ExternalConnectionStatus = Literal["Available"]
HashAlgorithm = Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
ListDomainsPaginatorName = Literal["list_domains"]
ListPackageVersionAssetsPaginatorName = Literal["list_package_version_assets"]
ListPackageVersionsPaginatorName = Literal["list_package_versions"]
ListPackagesPaginatorName = Literal["list_packages"]
ListRepositoriesInDomainPaginatorName = Literal["list_repositories_in_domain"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
PackageFormat = Literal["maven", "npm", "nuget", "pypi"]
PackageVersionErrorCode = Literal[
    "ALREADY_EXISTS",
    "MISMATCHED_REVISION",
    "MISMATCHED_STATUS",
    "NOT_ALLOWED",
    "NOT_FOUND",
    "SKIPPED",
]
PackageVersionSortType = Literal["PUBLISHED_TIME"]
PackageVersionStatus = Literal[
    "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
]
