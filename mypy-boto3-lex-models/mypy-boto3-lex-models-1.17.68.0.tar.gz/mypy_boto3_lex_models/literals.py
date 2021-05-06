"""
Type annotations for lex-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lex_models.literals import ChannelStatus

    data: ChannelStatus = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChannelStatus",
    "ChannelType",
    "ContentType",
    "Destination",
    "ExportStatus",
    "ExportType",
    "FulfillmentActivityType",
    "GetBotAliasesPaginatorName",
    "GetBotChannelAssociationsPaginatorName",
    "GetBotVersionsPaginatorName",
    "GetBotsPaginatorName",
    "GetBuiltinIntentsPaginatorName",
    "GetBuiltinSlotTypesPaginatorName",
    "GetIntentVersionsPaginatorName",
    "GetIntentsPaginatorName",
    "GetSlotTypeVersionsPaginatorName",
    "GetSlotTypesPaginatorName",
    "ImportStatus",
    "Locale",
    "LogType",
    "MergeStrategy",
    "ObfuscationSetting",
    "ProcessBehavior",
    "ResourceType",
    "SlotConstraint",
    "SlotValueSelectionStrategy",
    "Status",
    "StatusType",
)


ChannelStatus = Literal["CREATED", "FAILED", "IN_PROGRESS"]
ChannelType = Literal["Facebook", "Kik", "Slack", "Twilio-Sms"]
ContentType = Literal["CustomPayload", "PlainText", "SSML"]
Destination = Literal["CLOUDWATCH_LOGS", "S3"]
ExportStatus = Literal["FAILED", "IN_PROGRESS", "READY"]
ExportType = Literal["ALEXA_SKILLS_KIT", "LEX"]
FulfillmentActivityType = Literal["CodeHook", "ReturnIntent"]
GetBotAliasesPaginatorName = Literal["get_bot_aliases"]
GetBotChannelAssociationsPaginatorName = Literal["get_bot_channel_associations"]
GetBotVersionsPaginatorName = Literal["get_bot_versions"]
GetBotsPaginatorName = Literal["get_bots"]
GetBuiltinIntentsPaginatorName = Literal["get_builtin_intents"]
GetBuiltinSlotTypesPaginatorName = Literal["get_builtin_slot_types"]
GetIntentVersionsPaginatorName = Literal["get_intent_versions"]
GetIntentsPaginatorName = Literal["get_intents"]
GetSlotTypeVersionsPaginatorName = Literal["get_slot_type_versions"]
GetSlotTypesPaginatorName = Literal["get_slot_types"]
ImportStatus = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
Locale = Literal[
    "de-DE",
    "en-AU",
    "en-GB",
    "en-US",
    "es-419",
    "es-ES",
    "es-US",
    "fr-CA",
    "fr-FR",
    "it-IT",
    "ja-JP",
]
LogType = Literal["AUDIO", "TEXT"]
MergeStrategy = Literal["FAIL_ON_CONFLICT", "OVERWRITE_LATEST"]
ObfuscationSetting = Literal["DEFAULT_OBFUSCATION", "NONE"]
ProcessBehavior = Literal["BUILD", "SAVE"]
ResourceType = Literal["BOT", "INTENT", "SLOT_TYPE"]
SlotConstraint = Literal["Optional", "Required"]
SlotValueSelectionStrategy = Literal["ORIGINAL_VALUE", "TOP_RESOLUTION"]
Status = Literal["BUILDING", "FAILED", "NOT_BUILT", "READY", "READY_BASIC_TESTING"]
StatusType = Literal["Detected", "Missed"]
