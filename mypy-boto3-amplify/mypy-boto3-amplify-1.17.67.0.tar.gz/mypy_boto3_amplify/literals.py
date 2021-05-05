"""
Type annotations for amplify service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/literals.html)

Usage::

    ```python
    from mypy_boto3_amplify.literals import DomainStatus

    data: DomainStatus = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DomainStatus",
    "JobStatus",
    "JobType",
    "ListAppsPaginatorName",
    "ListBranchesPaginatorName",
    "ListDomainAssociationsPaginatorName",
    "ListJobsPaginatorName",
    "Platform",
    "Stage",
)


DomainStatus = Literal[
    "AVAILABLE",
    "CREATING",
    "FAILED",
    "IN_PROGRESS",
    "PENDING_DEPLOYMENT",
    "PENDING_VERIFICATION",
    "REQUESTING_CERTIFICATE",
    "UPDATING",
]
JobStatus = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "PENDING", "PROVISIONING", "RUNNING", "SUCCEED"
]
JobType = Literal["MANUAL", "RELEASE", "RETRY", "WEB_HOOK"]
ListAppsPaginatorName = Literal["list_apps"]
ListBranchesPaginatorName = Literal["list_branches"]
ListDomainAssociationsPaginatorName = Literal["list_domain_associations"]
ListJobsPaginatorName = Literal["list_jobs"]
Platform = Literal["WEB"]
Stage = Literal["BETA", "DEVELOPMENT", "EXPERIMENTAL", "PRODUCTION", "PULL_REQUEST"]
