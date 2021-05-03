"""
Type annotations for managedblockchain service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/literals.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain.literals import Edition

    data: Edition = "STANDARD"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Edition",
    "Framework",
    "InvitationStatus",
    "MemberStatus",
    "NetworkStatus",
    "NodeStatus",
    "ProposalStatus",
    "StateDBType",
    "ThresholdComparator",
    "VoteValue",
)


Edition = Literal["STANDARD", "STARTER"]
Framework = Literal["ETHEREUM", "HYPERLEDGER_FABRIC"]
InvitationStatus = Literal["ACCEPTED", "ACCEPTING", "EXPIRED", "PENDING", "REJECTED"]
MemberStatus = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING", "UPDATING"]
NetworkStatus = Literal["AVAILABLE", "CREATE_FAILED", "CREATING", "DELETED", "DELETING"]
NodeStatus = Literal[
    "AVAILABLE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "FAILED",
    "UNHEALTHY",
    "UPDATING",
]
ProposalStatus = Literal["ACTION_FAILED", "APPROVED", "EXPIRED", "IN_PROGRESS", "REJECTED"]
StateDBType = Literal["CouchDB", "LevelDB"]
ThresholdComparator = Literal["GREATER_THAN", "GREATER_THAN_OR_EQUAL_TO"]
VoteValue = Literal["NO", "YES"]
