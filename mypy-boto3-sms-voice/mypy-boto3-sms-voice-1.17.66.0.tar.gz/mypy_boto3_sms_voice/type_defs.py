"""
Type annotations for sms-voice service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms_voice/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_sms_voice.literals import EventType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "PlainTextMessageTypeTypeDef",
    "SSMLMessageTypeTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "SnsDestinationTypeDef",
    "VoiceMessageContentTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef", {"Text": str}, total=False
)


class CloudWatchLogsDestinationTypeDef(TypedDict, total=False):
    IamRoleArn: str
    LogGroupArn: str


class EventDestinationDefinitionTypeDef(TypedDict, total=False):
    CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef"
    Enabled: bool
    KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef"
    MatchingEventTypes: List[EventType]
    SnsDestination: "SnsDestinationTypeDef"


class EventDestinationTypeDef(TypedDict, total=False):
    CloudWatchLogsDestination: "CloudWatchLogsDestinationTypeDef"
    Enabled: bool
    KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef"
    MatchingEventTypes: List[EventType]
    Name: str
    SnsDestination: "SnsDestinationTypeDef"


class GetConfigurationSetEventDestinationsResponseTypeDef(TypedDict, total=False):
    EventDestinations: List["EventDestinationTypeDef"]


class KinesisFirehoseDestinationTypeDef(TypedDict, total=False):
    DeliveryStreamArn: str
    IamRoleArn: str


class ListConfigurationSetsResponseTypeDef(TypedDict, total=False):
    ConfigurationSets: List[str]
    NextToken: str


PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef", {"LanguageCode": str, "Text": str, "VoiceId": str}, total=False
)


class SendVoiceMessageResponseTypeDef(TypedDict, total=False):
    MessageId: str


class SnsDestinationTypeDef(TypedDict, total=False):
    TopicArn: str


class VoiceMessageContentTypeDef(TypedDict, total=False):
    CallInstructionsMessage: "CallInstructionsMessageTypeTypeDef"
    PlainTextMessage: "PlainTextMessageTypeTypeDef"
    SSMLMessage: "SSMLMessageTypeTypeDef"
