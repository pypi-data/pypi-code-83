"""
Type annotations for connectparticipant service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/literals.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.literals import ArtifactStatus

    data: ArtifactStatus = "APPROVED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ArtifactStatus",
    "ChatItemType",
    "ConnectionType",
    "ParticipantRole",
    "ScanDirection",
    "SortKey",
)


ArtifactStatus = Literal["APPROVED", "IN_PROGRESS", "REJECTED"]
ChatItemType = Literal[
    "ATTACHMENT",
    "CHAT_ENDED",
    "CONNECTION_ACK",
    "EVENT",
    "MESSAGE",
    "PARTICIPANT_JOINED",
    "PARTICIPANT_LEFT",
    "TRANSFER_FAILED",
    "TRANSFER_SUCCEEDED",
    "TYPING",
]
ConnectionType = Literal["CONNECTION_CREDENTIALS", "WEBSOCKET"]
ParticipantRole = Literal["AGENT", "CUSTOMER", "SYSTEM"]
ScanDirection = Literal["BACKWARD", "FORWARD"]
SortKey = Literal["ASCENDING", "DESCENDING"]
