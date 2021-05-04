"""
Type annotations for connectparticipant service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_connectparticipant.literals import ArtifactStatus, ChatItemType, ParticipantRole

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "WebsocketTypeDef",
)


class AttachmentItemTypeDef(TypedDict, total=False):
    ContentType: str
    AttachmentId: str
    AttachmentName: str
    Status: ArtifactStatus


class ConnectionCredentialsTypeDef(TypedDict, total=False):
    ConnectionToken: str
    Expiry: str


class CreateParticipantConnectionResponseTypeDef(TypedDict, total=False):
    Websocket: "WebsocketTypeDef"
    ConnectionCredentials: "ConnectionCredentialsTypeDef"


class GetAttachmentResponseTypeDef(TypedDict, total=False):
    Url: str
    UrlExpiry: str


class GetTranscriptResponseTypeDef(TypedDict, total=False):
    InitialContactId: str
    Transcript: List["ItemTypeDef"]
    NextToken: str


ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": str,
        "Content": str,
        "ContentType": str,
        "Id": str,
        "Type": ChatItemType,
        "ParticipantId": str,
        "DisplayName": str,
        "ParticipantRole": ParticipantRole,
        "Attachments": List["AttachmentItemTypeDef"],
    },
    total=False,
)


class SendEventResponseTypeDef(TypedDict, total=False):
    Id: str
    AbsoluteTime: str


class SendMessageResponseTypeDef(TypedDict, total=False):
    Id: str
    AbsoluteTime: str


class StartAttachmentUploadResponseTypeDef(TypedDict, total=False):
    AttachmentId: str
    UploadMetadata: "UploadMetadataTypeDef"


class StartPositionTypeDef(TypedDict, total=False):
    Id: str
    AbsoluteTime: str
    MostRecent: int


class UploadMetadataTypeDef(TypedDict, total=False):
    Url: str
    UrlExpiry: str
    HeadersToInclude: Dict[str, str]


class WebsocketTypeDef(TypedDict, total=False):
    Url: str
    ConnectionExpiry: str
