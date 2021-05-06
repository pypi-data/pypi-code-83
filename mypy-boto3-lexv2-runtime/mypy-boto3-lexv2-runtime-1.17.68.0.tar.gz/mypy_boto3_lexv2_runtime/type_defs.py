"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from botocore.response import StreamingBody

from mypy_boto3_lexv2_runtime.literals import (
    ConfirmationState,
    DialogActionType,
    IntentState,
    MessageContentType,
    SentimentType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionTypeDef",
    "GetSessionResponseTypeDef",
    "ImageResponseCardTypeDef",
    "IntentTypeDef",
    "InterpretationTypeDef",
    "MessageTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeTextResponseTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "SentimentResponseTypeDef",
    "SentimentScoreTypeDef",
    "SessionStateTypeDef",
    "SlotTypeDef",
    "ValueTypeDef",
)


class ActiveContextTimeToLiveTypeDef(TypedDict):
    timeToLiveInSeconds: int
    turnsToLive: int


class _RequiredActiveContextTypeDef(TypedDict):
    name: str
    timeToLive: "ActiveContextTimeToLiveTypeDef"


class ActiveContextTypeDef(_RequiredActiveContextTypeDef, total=False):
    contextAttributes: Dict[str, str]


class ButtonTypeDef(TypedDict):
    text: str
    value: str


class ConfidenceScoreTypeDef(TypedDict, total=False):
    score: float


class DeleteSessionResponseTypeDef(TypedDict, total=False):
    botId: str
    botAliasId: str
    localeId: str
    sessionId: str


_RequiredDialogActionTypeDef = TypedDict("_RequiredDialogActionTypeDef", {"type": DialogActionType})
_OptionalDialogActionTypeDef = TypedDict(
    "_OptionalDialogActionTypeDef", {"slotToElicit": str}, total=False
)


class DialogActionTypeDef(_RequiredDialogActionTypeDef, _OptionalDialogActionTypeDef):
    pass


class GetSessionResponseTypeDef(TypedDict, total=False):
    sessionId: str
    messages: List["MessageTypeDef"]
    interpretations: List["InterpretationTypeDef"]
    sessionState: "SessionStateTypeDef"


class _RequiredImageResponseCardTypeDef(TypedDict):
    title: str


class ImageResponseCardTypeDef(_RequiredImageResponseCardTypeDef, total=False):
    subtitle: str
    imageUrl: str
    buttons: List["ButtonTypeDef"]


class _RequiredIntentTypeDef(TypedDict):
    name: str


class IntentTypeDef(_RequiredIntentTypeDef, total=False):
    slots: Dict[str, "SlotTypeDef"]
    state: IntentState
    confirmationState: ConfirmationState


class InterpretationTypeDef(TypedDict, total=False):
    nluConfidence: "ConfidenceScoreTypeDef"
    sentimentResponse: "SentimentResponseTypeDef"
    intent: "IntentTypeDef"


class MessageTypeDef(TypedDict, total=False):
    content: str
    contentType: MessageContentType
    imageResponseCard: "ImageResponseCardTypeDef"


class PutSessionResponseTypeDef(TypedDict, total=False):
    contentType: str
    messages: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    audioStream: StreamingBody


class RecognizeTextResponseTypeDef(TypedDict, total=False):
    messages: List["MessageTypeDef"]
    sessionState: "SessionStateTypeDef"
    interpretations: List["InterpretationTypeDef"]
    requestAttributes: Dict[str, str]
    sessionId: str


class RecognizeUtteranceResponseTypeDef(TypedDict, total=False):
    inputMode: str
    contentType: str
    messages: str
    interpretations: str
    sessionState: str
    requestAttributes: str
    sessionId: str
    inputTranscript: str
    audioStream: StreamingBody


class SentimentResponseTypeDef(TypedDict, total=False):
    sentiment: SentimentType
    sentimentScore: "SentimentScoreTypeDef"


class SentimentScoreTypeDef(TypedDict, total=False):
    positive: float
    negative: float
    neutral: float
    mixed: float


class SessionStateTypeDef(TypedDict, total=False):
    dialogAction: "DialogActionTypeDef"
    intent: "IntentTypeDef"
    activeContexts: List["ActiveContextTypeDef"]
    sessionAttributes: Dict[str, str]
    originatingRequestId: str


class SlotTypeDef(TypedDict, total=False):
    value: "ValueTypeDef"


class _RequiredValueTypeDef(TypedDict):
    interpretedValue: str


class ValueTypeDef(_RequiredValueTypeDef, total=False):
    originalValue: str
    resolvedValues: List[str]
