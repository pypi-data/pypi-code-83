"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from botocore.response import StreamingBody

from mypy_boto3_lex_runtime.literals import (
    ConfirmationStatus,
    DialogActionType,
    DialogState,
    FulfillmentState,
    MessageFormatType,
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
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionTypeDef",
    "GenericAttachmentTypeDef",
    "GetSessionResponseTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryTypeDef",
    "PostContentResponseTypeDef",
    "PostTextResponseTypeDef",
    "PredictedIntentTypeDef",
    "PutSessionResponseTypeDef",
    "ResponseCardTypeDef",
    "SentimentResponseTypeDef",
)


class ActiveContextTimeToLiveTypeDef(TypedDict, total=False):
    timeToLiveInSeconds: int
    turnsToLive: int


class ActiveContextTypeDef(TypedDict):
    name: str
    timeToLive: "ActiveContextTimeToLiveTypeDef"
    parameters: Dict[str, str]


class ButtonTypeDef(TypedDict):
    text: str
    value: str


class DeleteSessionResponseTypeDef(TypedDict, total=False):
    botName: str
    botAlias: str
    userId: str
    sessionId: str


_RequiredDialogActionTypeDef = TypedDict("_RequiredDialogActionTypeDef", {"type": DialogActionType})
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef",
    {
        "intentName": str,
        "slots": Dict[str, str],
        "slotToElicit": str,
        "fulfillmentState": FulfillmentState,
        "message": str,
        "messageFormat": MessageFormatType,
    },
    total=False,
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


class GenericAttachmentTypeDef(TypedDict, total=False):
    title: str
    subTitle: str
    attachmentLinkUrl: str
    imageUrl: str
    buttons: List["ButtonTypeDef"]


class GetSessionResponseTypeDef(TypedDict, total=False):
    recentIntentSummaryView: List["IntentSummaryTypeDef"]
    sessionAttributes: Dict[str, str]
    sessionId: str
    dialogAction: "DialogActionTypeDef"
    activeContexts: List["ActiveContextTypeDef"]


class IntentConfidenceTypeDef(TypedDict, total=False):
    score: float


class _RequiredIntentSummaryTypeDef(TypedDict):
    dialogActionType: DialogActionType


class IntentSummaryTypeDef(_RequiredIntentSummaryTypeDef, total=False):
    intentName: str
    checkpointLabel: str
    slots: Dict[str, str]
    confirmationStatus: ConfirmationStatus
    fulfillmentState: FulfillmentState
    slotToElicit: str


class PostContentResponseTypeDef(TypedDict, total=False):
    contentType: str
    intentName: str
    nluIntentConfidence: str
    alternativeIntents: str
    slots: str
    sessionAttributes: str
    sentimentResponse: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatType
    dialogState: DialogState
    slotToElicit: str
    inputTranscript: str
    encodedInputTranscript: str
    audioStream: StreamingBody
    botVersion: str
    sessionId: str
    activeContexts: str


class PostTextResponseTypeDef(TypedDict, total=False):
    intentName: str
    nluIntentConfidence: "IntentConfidenceTypeDef"
    alternativeIntents: List["PredictedIntentTypeDef"]
    slots: Dict[str, str]
    sessionAttributes: Dict[str, str]
    message: str
    sentimentResponse: "SentimentResponseTypeDef"
    messageFormat: MessageFormatType
    dialogState: DialogState
    slotToElicit: str
    responseCard: "ResponseCardTypeDef"
    sessionId: str
    botVersion: str
    activeContexts: List["ActiveContextTypeDef"]


class PredictedIntentTypeDef(TypedDict, total=False):
    intentName: str
    nluIntentConfidence: "IntentConfidenceTypeDef"
    slots: Dict[str, str]


class PutSessionResponseTypeDef(TypedDict, total=False):
    contentType: str
    intentName: str
    slots: str
    sessionAttributes: str
    message: str
    encodedMessage: str
    messageFormat: MessageFormatType
    dialogState: DialogState
    slotToElicit: str
    audioStream: StreamingBody
    sessionId: str
    activeContexts: str


class ResponseCardTypeDef(TypedDict, total=False):
    version: str
    contentType: Literal["application/vnd.amazonaws.card.generic"]
    genericAttachments: List["GenericAttachmentTypeDef"]


class SentimentResponseTypeDef(TypedDict, total=False):
    sentimentLabel: str
    sentimentScore: str
