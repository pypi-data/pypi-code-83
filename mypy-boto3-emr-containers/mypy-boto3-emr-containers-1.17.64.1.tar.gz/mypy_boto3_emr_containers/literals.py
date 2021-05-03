"""
Type annotations for emr-containers service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/literals.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.literals import ContainerProviderType

    data: ContainerProviderType = "EKS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ContainerProviderType",
    "EndpointState",
    "FailureReason",
    "JobRunState",
    "ListJobRunsPaginatorName",
    "ListManagedEndpointsPaginatorName",
    "ListVirtualClustersPaginatorName",
    "PersistentAppUI",
    "VirtualClusterState",
)


ContainerProviderType = Literal["EKS"]
EndpointState = Literal["ACTIVE", "CREATING", "TERMINATED", "TERMINATED_WITH_ERRORS", "TERMINATING"]
FailureReason = Literal["CLUSTER_UNAVAILABLE", "INTERNAL_ERROR", "USER_ERROR", "VALIDATION_ERROR"]
JobRunState = Literal[
    "CANCELLED", "CANCEL_PENDING", "COMPLETED", "FAILED", "PENDING", "RUNNING", "SUBMITTED"
]
ListJobRunsPaginatorName = Literal["list_job_runs"]
ListManagedEndpointsPaginatorName = Literal["list_managed_endpoints"]
ListVirtualClustersPaginatorName = Literal["list_virtual_clusters"]
PersistentAppUI = Literal["DISABLED", "ENABLED"]
VirtualClusterState = Literal["ARRESTED", "RUNNING", "TERMINATED", "TERMINATING"]
