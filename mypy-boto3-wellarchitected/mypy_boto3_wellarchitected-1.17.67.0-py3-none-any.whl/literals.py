"""
Type annotations for wellarchitected service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/literals.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.literals import DifferenceStatus

    data: DifferenceStatus = "DELETED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DifferenceStatus",
    "LensStatus",
    "NotificationType",
    "PermissionType",
    "Risk",
    "ShareInvitationAction",
    "ShareStatus",
    "WorkloadEnvironment",
    "WorkloadImprovementStatus",
)


DifferenceStatus = Literal["DELETED", "NEW", "UPDATED"]
LensStatus = Literal["CURRENT", "DEPRECATED", "NOT_CURRENT"]
NotificationType = Literal["LENS_VERSION_DEPRECATED", "LENS_VERSION_UPGRADED"]
PermissionType = Literal["CONTRIBUTOR", "READONLY"]
Risk = Literal["HIGH", "MEDIUM", "NONE", "NOT_APPLICABLE", "UNANSWERED"]
ShareInvitationAction = Literal["ACCEPT", "REJECT"]
ShareStatus = Literal["ACCEPTED", "EXPIRED", "PENDING", "REJECTED", "REVOKED"]
WorkloadEnvironment = Literal["PREPRODUCTION", "PRODUCTION"]
WorkloadImprovementStatus = Literal[
    "COMPLETE", "IN_PROGRESS", "NOT_APPLICABLE", "NOT_STARTED", "RISK_ACKNOWLEDGED"
]
