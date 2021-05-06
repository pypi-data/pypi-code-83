"""
Type annotations for cloud9 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/literals.html)

Usage::

    ```python
    from mypy_boto3_cloud9.literals import ConnectionType

    data: ConnectionType = "CONNECT_SSH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ConnectionType",
    "DescribeEnvironmentMembershipsPaginatorName",
    "EnvironmentLifecycleStatus",
    "EnvironmentStatus",
    "EnvironmentType",
    "ListEnvironmentsPaginatorName",
    "ManagedCredentialsStatus",
    "MemberPermissions",
    "Permissions",
)


ConnectionType = Literal["CONNECT_SSH", "CONNECT_SSM"]
DescribeEnvironmentMembershipsPaginatorName = Literal["describe_environment_memberships"]
EnvironmentLifecycleStatus = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
]
EnvironmentStatus = Literal[
    "connecting", "creating", "deleting", "error", "ready", "stopped", "stopping"
]
EnvironmentType = Literal["ec2", "ssh"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ManagedCredentialsStatus = Literal[
    "DISABLED_BY_COLLABORATOR",
    "DISABLED_BY_DEFAULT",
    "DISABLED_BY_OWNER",
    "ENABLED_BY_OWNER",
    "ENABLED_ON_CREATE",
    "FAILED_REMOVAL_BY_COLLABORATOR",
    "FAILED_REMOVAL_BY_OWNER",
    "PENDING_REMOVAL_BY_COLLABORATOR",
    "PENDING_REMOVAL_BY_OWNER",
    "PENDING_START_REMOVAL_BY_COLLABORATOR",
    "PENDING_START_REMOVAL_BY_OWNER",
]
MemberPermissions = Literal["read-only", "read-write"]
Permissions = Literal["owner", "read-only", "read-write"]
