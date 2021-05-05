"""
Type annotations for lex-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_models.type_defs import BotAliasMetadataTypeDef

    data: BotAliasMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_lex_models.literals import (
    ChannelStatus,
    ChannelType,
    ContentType,
    Destination,
    ExportStatus,
    ExportType,
    FulfillmentActivityType,
    ImportStatus,
    Locale,
    LogType,
    MergeStrategy,
    ObfuscationSetting,
    ResourceType,
    SlotConstraint,
    SlotValueSelectionStrategy,
    Status,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BotAliasMetadataTypeDef",
    "BotChannelAssociationTypeDef",
    "BotMetadataTypeDef",
    "BuiltinIntentMetadataTypeDef",
    "BuiltinIntentSlotTypeDef",
    "BuiltinSlotTypeMetadataTypeDef",
    "CodeHookTypeDef",
    "ConversationLogsRequestTypeDef",
    "ConversationLogsResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateIntentVersionResponseTypeDef",
    "CreateSlotTypeVersionResponseTypeDef",
    "EnumerationValueTypeDef",
    "FollowUpPromptTypeDef",
    "FulfillmentActivityTypeDef",
    "GetBotAliasResponseTypeDef",
    "GetBotAliasesResponseTypeDef",
    "GetBotChannelAssociationResponseTypeDef",
    "GetBotChannelAssociationsResponseTypeDef",
    "GetBotResponseTypeDef",
    "GetBotVersionsResponseTypeDef",
    "GetBotsResponseTypeDef",
    "GetBuiltinIntentResponseTypeDef",
    "GetBuiltinIntentsResponseTypeDef",
    "GetBuiltinSlotTypesResponseTypeDef",
    "GetExportResponseTypeDef",
    "GetImportResponseTypeDef",
    "GetIntentResponseTypeDef",
    "GetIntentVersionsResponseTypeDef",
    "GetIntentsResponseTypeDef",
    "GetSlotTypeResponseTypeDef",
    "GetSlotTypeVersionsResponseTypeDef",
    "GetSlotTypesResponseTypeDef",
    "GetUtterancesViewResponseTypeDef",
    "InputContextTypeDef",
    "IntentMetadataTypeDef",
    "IntentTypeDef",
    "KendraConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogSettingsRequestTypeDef",
    "LogSettingsResponseTypeDef",
    "MessageTypeDef",
    "OutputContextTypeDef",
    "PaginatorConfigTypeDef",
    "PromptTypeDef",
    "PutBotAliasResponseTypeDef",
    "PutBotResponseTypeDef",
    "PutIntentResponseTypeDef",
    "PutSlotTypeResponseTypeDef",
    "SlotDefaultValueSpecTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotTypeConfigurationTypeDef",
    "SlotTypeDef",
    "SlotTypeMetadataTypeDef",
    "SlotTypeRegexConfigurationTypeDef",
    "StartImportResponseTypeDef",
    "StatementTypeDef",
    "TagTypeDef",
    "UtteranceDataTypeDef",
    "UtteranceListTypeDef",
)


class BotAliasMetadataTypeDef(TypedDict, total=False):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: "ConversationLogsResponseTypeDef"


BotChannelAssociationTypeDef = TypedDict(
    "BotChannelAssociationTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatus,
        "failureReason": str,
    },
    total=False,
)


class BotMetadataTypeDef(TypedDict, total=False):
    name: str
    description: str
    status: Status
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str


class BuiltinIntentMetadataTypeDef(TypedDict, total=False):
    signature: str
    supportedLocales: List[Locale]


class BuiltinIntentSlotTypeDef(TypedDict, total=False):
    name: str


class BuiltinSlotTypeMetadataTypeDef(TypedDict, total=False):
    signature: str
    supportedLocales: List[Locale]


class CodeHookTypeDef(TypedDict):
    uri: str
    messageVersion: str


class ConversationLogsRequestTypeDef(TypedDict):
    logSettings: List["LogSettingsRequestTypeDef"]
    iamRoleArn: str


class ConversationLogsResponseTypeDef(TypedDict, total=False):
    logSettings: List["LogSettingsResponseTypeDef"]
    iamRoleArn: str


class CreateBotVersionResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    intents: List["IntentTypeDef"]
    clarificationPrompt: "PromptTypeDef"
    abortStatement: "StatementTypeDef"
    status: Status
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: Locale
    childDirected: bool
    enableModelImprovements: bool
    detectSentiment: bool


class CreateIntentVersionResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    slots: List["SlotTypeDef"]
    sampleUtterances: List[str]
    confirmationPrompt: "PromptTypeDef"
    rejectionStatement: "StatementTypeDef"
    followUpPrompt: "FollowUpPromptTypeDef"
    conclusionStatement: "StatementTypeDef"
    dialogCodeHook: "CodeHookTypeDef"
    fulfillmentActivity: "FulfillmentActivityTypeDef"
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: "KendraConfigurationTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]


class CreateSlotTypeVersionResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    enumerationValues: List["EnumerationValueTypeDef"]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategy
    parentSlotTypeSignature: str
    slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"]


class _RequiredEnumerationValueTypeDef(TypedDict):
    value: str


class EnumerationValueTypeDef(_RequiredEnumerationValueTypeDef, total=False):
    synonyms: List[str]


class FollowUpPromptTypeDef(TypedDict):
    prompt: "PromptTypeDef"
    rejectionStatement: "StatementTypeDef"


_RequiredFulfillmentActivityTypeDef = TypedDict(
    "_RequiredFulfillmentActivityTypeDef", {"type": FulfillmentActivityType}
)
_OptionalFulfillmentActivityTypeDef = TypedDict(
    "_OptionalFulfillmentActivityTypeDef", {"codeHook": "CodeHookTypeDef"}, total=False
)


class FulfillmentActivityTypeDef(
    _RequiredFulfillmentActivityTypeDef, _OptionalFulfillmentActivityTypeDef
):
    pass


class GetBotAliasResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: "ConversationLogsResponseTypeDef"


class GetBotAliasesResponseTypeDef(TypedDict, total=False):
    BotAliases: List["BotAliasMetadataTypeDef"]
    nextToken: str


GetBotChannelAssociationResponseTypeDef = TypedDict(
    "GetBotChannelAssociationResponseTypeDef",
    {
        "name": str,
        "description": str,
        "botAlias": str,
        "botName": str,
        "createdDate": datetime,
        "type": ChannelType,
        "botConfiguration": Dict[str, str],
        "status": ChannelStatus,
        "failureReason": str,
    },
    total=False,
)


class GetBotChannelAssociationsResponseTypeDef(TypedDict, total=False):
    botChannelAssociations: List["BotChannelAssociationTypeDef"]
    nextToken: str


class GetBotResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    intents: List["IntentTypeDef"]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: "PromptTypeDef"
    abortStatement: "StatementTypeDef"
    status: Status
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: Locale
    childDirected: bool
    detectSentiment: bool


class GetBotVersionsResponseTypeDef(TypedDict, total=False):
    bots: List["BotMetadataTypeDef"]
    nextToken: str


class GetBotsResponseTypeDef(TypedDict, total=False):
    bots: List["BotMetadataTypeDef"]
    nextToken: str


class GetBuiltinIntentResponseTypeDef(TypedDict, total=False):
    signature: str
    supportedLocales: List[Locale]
    slots: List["BuiltinIntentSlotTypeDef"]


class GetBuiltinIntentsResponseTypeDef(TypedDict, total=False):
    intents: List["BuiltinIntentMetadataTypeDef"]
    nextToken: str


class GetBuiltinSlotTypesResponseTypeDef(TypedDict, total=False):
    slotTypes: List["BuiltinSlotTypeMetadataTypeDef"]
    nextToken: str


class GetExportResponseTypeDef(TypedDict, total=False):
    name: str
    version: str
    resourceType: ResourceType
    exportType: ExportType
    exportStatus: ExportStatus
    failureReason: str
    url: str


class GetImportResponseTypeDef(TypedDict, total=False):
    name: str
    resourceType: ResourceType
    mergeStrategy: MergeStrategy
    importId: str
    importStatus: ImportStatus
    failureReason: List[str]
    createdDate: datetime


class GetIntentResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    slots: List["SlotTypeDef"]
    sampleUtterances: List[str]
    confirmationPrompt: "PromptTypeDef"
    rejectionStatement: "StatementTypeDef"
    followUpPrompt: "FollowUpPromptTypeDef"
    conclusionStatement: "StatementTypeDef"
    dialogCodeHook: "CodeHookTypeDef"
    fulfillmentActivity: "FulfillmentActivityTypeDef"
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    kendraConfiguration: "KendraConfigurationTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]


class GetIntentVersionsResponseTypeDef(TypedDict, total=False):
    intents: List["IntentMetadataTypeDef"]
    nextToken: str


class GetIntentsResponseTypeDef(TypedDict, total=False):
    intents: List["IntentMetadataTypeDef"]
    nextToken: str


class GetSlotTypeResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    enumerationValues: List["EnumerationValueTypeDef"]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategy
    parentSlotTypeSignature: str
    slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"]


class GetSlotTypeVersionsResponseTypeDef(TypedDict, total=False):
    slotTypes: List["SlotTypeMetadataTypeDef"]
    nextToken: str


class GetSlotTypesResponseTypeDef(TypedDict, total=False):
    slotTypes: List["SlotTypeMetadataTypeDef"]
    nextToken: str


class GetUtterancesViewResponseTypeDef(TypedDict, total=False):
    botName: str
    utterances: List["UtteranceListTypeDef"]


class InputContextTypeDef(TypedDict):
    name: str


class IntentMetadataTypeDef(TypedDict, total=False):
    name: str
    description: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str


class IntentTypeDef(TypedDict):
    intentName: str
    intentVersion: str


class _RequiredKendraConfigurationTypeDef(TypedDict):
    kendraIndex: str
    role: str


class KendraConfigurationTypeDef(_RequiredKendraConfigurationTypeDef, total=False):
    queryFilterString: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class _RequiredLogSettingsRequestTypeDef(TypedDict):
    logType: LogType
    destination: Destination
    resourceArn: str


class LogSettingsRequestTypeDef(_RequiredLogSettingsRequestTypeDef, total=False):
    kmsKeyArn: str


class LogSettingsResponseTypeDef(TypedDict, total=False):
    logType: LogType
    destination: Destination
    kmsKeyArn: str
    resourceArn: str
    resourcePrefix: str


class _RequiredMessageTypeDef(TypedDict):
    contentType: ContentType
    content: str


class MessageTypeDef(_RequiredMessageTypeDef, total=False):
    groupNumber: int


class OutputContextTypeDef(TypedDict):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPromptTypeDef(TypedDict):
    messages: List["MessageTypeDef"]
    maxAttempts: int


class PromptTypeDef(_RequiredPromptTypeDef, total=False):
    responseCard: str


class PutBotAliasResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    botVersion: str
    botName: str
    lastUpdatedDate: datetime
    createdDate: datetime
    checksum: str
    conversationLogs: "ConversationLogsResponseTypeDef"
    tags: List["TagTypeDef"]


class PutBotResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    intents: List["IntentTypeDef"]
    enableModelImprovements: bool
    nluIntentConfidenceThreshold: float
    clarificationPrompt: "PromptTypeDef"
    abortStatement: "StatementTypeDef"
    status: Status
    failureReason: str
    lastUpdatedDate: datetime
    createdDate: datetime
    idleSessionTTLInSeconds: int
    voiceId: str
    checksum: str
    version: str
    locale: Locale
    childDirected: bool
    createVersion: bool
    detectSentiment: bool
    tags: List["TagTypeDef"]


class PutIntentResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    slots: List["SlotTypeDef"]
    sampleUtterances: List[str]
    confirmationPrompt: "PromptTypeDef"
    rejectionStatement: "StatementTypeDef"
    followUpPrompt: "FollowUpPromptTypeDef"
    conclusionStatement: "StatementTypeDef"
    dialogCodeHook: "CodeHookTypeDef"
    fulfillmentActivity: "FulfillmentActivityTypeDef"
    parentIntentSignature: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    createVersion: bool
    kendraConfiguration: "KendraConfigurationTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]


class PutSlotTypeResponseTypeDef(TypedDict, total=False):
    name: str
    description: str
    enumerationValues: List["EnumerationValueTypeDef"]
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str
    checksum: str
    valueSelectionStrategy: SlotValueSelectionStrategy
    createVersion: bool
    parentSlotTypeSignature: str
    slotTypeConfigurations: List["SlotTypeConfigurationTypeDef"]


class SlotDefaultValueSpecTypeDef(TypedDict):
    defaultValueList: List["SlotDefaultValueTypeDef"]


class SlotDefaultValueTypeDef(TypedDict):
    defaultValue: str


class SlotTypeConfigurationTypeDef(TypedDict, total=False):
    regexConfiguration: "SlotTypeRegexConfigurationTypeDef"


class _RequiredSlotTypeDef(TypedDict):
    name: str
    slotConstraint: SlotConstraint


class SlotTypeDef(_RequiredSlotTypeDef, total=False):
    description: str
    slotType: str
    slotTypeVersion: str
    valueElicitationPrompt: "PromptTypeDef"
    priority: int
    sampleUtterances: List[str]
    responseCard: str
    obfuscationSetting: ObfuscationSetting
    defaultValueSpec: "SlotDefaultValueSpecTypeDef"


class SlotTypeMetadataTypeDef(TypedDict, total=False):
    name: str
    description: str
    lastUpdatedDate: datetime
    createdDate: datetime
    version: str


class SlotTypeRegexConfigurationTypeDef(TypedDict):
    pattern: str


class StartImportResponseTypeDef(TypedDict, total=False):
    name: str
    resourceType: ResourceType
    mergeStrategy: MergeStrategy
    importId: str
    importStatus: ImportStatus
    tags: List["TagTypeDef"]
    createdDate: datetime


class _RequiredStatementTypeDef(TypedDict):
    messages: List["MessageTypeDef"]


class StatementTypeDef(_RequiredStatementTypeDef, total=False):
    responseCard: str


class TagTypeDef(TypedDict):
    key: str
    value: str


class UtteranceDataTypeDef(TypedDict, total=False):
    utteranceString: str
    count: int
    distinctUsers: int
    firstUtteredDate: datetime
    lastUtteredDate: datetime


class UtteranceListTypeDef(TypedDict, total=False):
    botVersion: str
    utterances: List["UtteranceDataTypeDef"]
