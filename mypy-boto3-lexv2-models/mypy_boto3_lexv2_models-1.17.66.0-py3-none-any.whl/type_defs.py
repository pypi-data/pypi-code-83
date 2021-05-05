"""
Type annotations for lexv2-models service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.type_defs import AudioLogDestinationTypeDef

    data: AudioLogDestinationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_lexv2_models.literals import (
    BotAliasStatus,
    BotFilterOperator,
    BotLocaleFilterOperator,
    BotLocaleStatus,
    BotStatus,
    IntentFilterOperator,
    IntentSortAttribute,
    ObfuscationSettingType,
    SlotConstraint,
    SlotFilterOperator,
    SlotSortAttribute,
    SlotTypeFilterOperator,
    SlotTypeSortAttribute,
    SlotValueResolutionStrategy,
    SortOrder,
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
    "AudioLogDestinationTypeDef",
    "AudioLogSettingTypeDef",
    "BotAliasHistoryEventTypeDef",
    "BotAliasLocaleSettingsTypeDef",
    "BotAliasSummaryTypeDef",
    "BotFilterTypeDef",
    "BotLocaleFilterTypeDef",
    "BotLocaleHistoryEventTypeDef",
    "BotLocaleSortByTypeDef",
    "BotLocaleSummaryTypeDef",
    "BotSortByTypeDef",
    "BotSummaryTypeDef",
    "BotVersionLocaleDetailsTypeDef",
    "BotVersionSortByTypeDef",
    "BotVersionSummaryTypeDef",
    "BuildBotLocaleResponseTypeDef",
    "BuiltInIntentSortByTypeDef",
    "BuiltInIntentSummaryTypeDef",
    "BuiltInSlotTypeSortByTypeDef",
    "BuiltInSlotTypeSummaryTypeDef",
    "ButtonTypeDef",
    "CloudWatchLogGroupLogDestinationTypeDef",
    "CodeHookSpecificationTypeDef",
    "ConversationLogSettingsTypeDef",
    "CreateBotAliasResponseTypeDef",
    "CreateBotLocaleResponseTypeDef",
    "CreateBotResponseTypeDef",
    "CreateBotVersionResponseTypeDef",
    "CreateIntentResponseTypeDef",
    "CreateSlotResponseTypeDef",
    "CreateSlotTypeResponseTypeDef",
    "CustomPayloadTypeDef",
    "DataPrivacyTypeDef",
    "DeleteBotAliasResponseTypeDef",
    "DeleteBotLocaleResponseTypeDef",
    "DeleteBotResponseTypeDef",
    "DeleteBotVersionResponseTypeDef",
    "DescribeBotAliasResponseTypeDef",
    "DescribeBotLocaleResponseTypeDef",
    "DescribeBotResponseTypeDef",
    "DescribeBotVersionResponseTypeDef",
    "DescribeIntentResponseTypeDef",
    "DescribeSlotResponseTypeDef",
    "DescribeSlotTypeResponseTypeDef",
    "DialogCodeHookSettingsTypeDef",
    "FulfillmentCodeHookSettingsTypeDef",
    "ImageResponseCardTypeDef",
    "InputContextTypeDef",
    "IntentClosingSettingTypeDef",
    "IntentConfirmationSettingTypeDef",
    "IntentFilterTypeDef",
    "IntentSortByTypeDef",
    "IntentSummaryTypeDef",
    "KendraConfigurationTypeDef",
    "LambdaCodeHookTypeDef",
    "ListBotAliasesResponseTypeDef",
    "ListBotLocalesResponseTypeDef",
    "ListBotVersionsResponseTypeDef",
    "ListBotsResponseTypeDef",
    "ListBuiltInIntentsResponseTypeDef",
    "ListBuiltInSlotTypesResponseTypeDef",
    "ListIntentsResponseTypeDef",
    "ListSlotTypesResponseTypeDef",
    "ListSlotsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageGroupTypeDef",
    "MessageTypeDef",
    "ObfuscationSettingTypeDef",
    "OutputContextTypeDef",
    "PlainTextMessageTypeDef",
    "PromptSpecificationTypeDef",
    "ResponseSpecificationTypeDef",
    "S3BucketLogDestinationTypeDef",
    "SSMLMessageTypeDef",
    "SampleUtteranceTypeDef",
    "SampleValueTypeDef",
    "SentimentAnalysisSettingsTypeDef",
    "SlotDefaultValueSpecificationTypeDef",
    "SlotDefaultValueTypeDef",
    "SlotFilterTypeDef",
    "SlotPriorityTypeDef",
    "SlotSortByTypeDef",
    "SlotSummaryTypeDef",
    "SlotTypeFilterTypeDef",
    "SlotTypeSortByTypeDef",
    "SlotTypeSummaryTypeDef",
    "SlotTypeValueTypeDef",
    "SlotValueElicitationSettingTypeDef",
    "SlotValueRegexFilterTypeDef",
    "SlotValueSelectionSettingTypeDef",
    "StillWaitingResponseSpecificationTypeDef",
    "TextLogDestinationTypeDef",
    "TextLogSettingTypeDef",
    "UpdateBotAliasResponseTypeDef",
    "UpdateBotLocaleResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateIntentResponseTypeDef",
    "UpdateSlotResponseTypeDef",
    "UpdateSlotTypeResponseTypeDef",
    "VoiceSettingsTypeDef",
    "WaitAndContinueSpecificationTypeDef",
)


class AudioLogDestinationTypeDef(TypedDict):
    s3Bucket: "S3BucketLogDestinationTypeDef"


class AudioLogSettingTypeDef(TypedDict):
    enabled: bool
    destination: "AudioLogDestinationTypeDef"


class BotAliasHistoryEventTypeDef(TypedDict, total=False):
    botVersion: str
    startDate: datetime
    endDate: datetime


class _RequiredBotAliasLocaleSettingsTypeDef(TypedDict):
    enabled: bool


class BotAliasLocaleSettingsTypeDef(_RequiredBotAliasLocaleSettingsTypeDef, total=False):
    codeHookSpecification: "CodeHookSpecificationTypeDef"


class BotAliasSummaryTypeDef(TypedDict, total=False):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasStatus: BotAliasStatus
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


BotFilterTypeDef = TypedDict(
    "BotFilterTypeDef",
    {"name": Literal["BotName"], "values": List[str], "operator": BotFilterOperator},
)

BotLocaleFilterTypeDef = TypedDict(
    "BotLocaleFilterTypeDef",
    {"name": Literal["BotLocaleName"], "values": List[str], "operator": BotLocaleFilterOperator},
)


class BotLocaleHistoryEventTypeDef(TypedDict):
    event: str
    eventDate: datetime


class BotLocaleSortByTypeDef(TypedDict):
    attribute: Literal["BotLocaleName"]
    order: SortOrder


class BotLocaleSummaryTypeDef(TypedDict, total=False):
    localeId: str
    localeName: str
    description: str
    botLocaleStatus: BotLocaleStatus
    lastUpdatedDateTime: datetime
    lastBuildSubmittedDateTime: datetime


class BotSortByTypeDef(TypedDict):
    attribute: Literal["BotName"]
    order: SortOrder


class BotSummaryTypeDef(TypedDict, total=False):
    botId: str
    botName: str
    description: str
    botStatus: BotStatus
    latestBotVersion: str
    lastUpdatedDateTime: datetime


class BotVersionLocaleDetailsTypeDef(TypedDict):
    sourceBotVersion: str


class BotVersionSortByTypeDef(TypedDict):
    attribute: Literal["BotVersion"]
    order: SortOrder


class BotVersionSummaryTypeDef(TypedDict, total=False):
    botName: str
    botVersion: str
    description: str
    botStatus: BotStatus
    creationDateTime: datetime


class BuildBotLocaleResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatus
    lastBuildSubmittedDateTime: datetime


class BuiltInIntentSortByTypeDef(TypedDict):
    attribute: Literal["IntentSignature"]
    order: SortOrder


class BuiltInIntentSummaryTypeDef(TypedDict, total=False):
    intentSignature: str
    description: str


class BuiltInSlotTypeSortByTypeDef(TypedDict):
    attribute: Literal["SlotTypeSignature"]
    order: SortOrder


class BuiltInSlotTypeSummaryTypeDef(TypedDict, total=False):
    slotTypeSignature: str
    description: str


class ButtonTypeDef(TypedDict):
    text: str
    value: str


class CloudWatchLogGroupLogDestinationTypeDef(TypedDict):
    cloudWatchLogGroupArn: str
    logPrefix: str


class CodeHookSpecificationTypeDef(TypedDict):
    lambdaCodeHook: "LambdaCodeHookTypeDef"


class ConversationLogSettingsTypeDef(TypedDict, total=False):
    textLogSettings: List["TextLogSettingTypeDef"]
    audioLogSettings: List["AudioLogSettingTypeDef"]


class CreateBotAliasResponseTypeDef(TypedDict, total=False):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"]
    conversationLogSettings: "ConversationLogSettingsTypeDef"
    sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef"
    botAliasStatus: BotAliasStatus
    botId: str
    creationDateTime: datetime
    tags: Dict[str, str]


class CreateBotLocaleResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeName: str
    localeId: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: "VoiceSettingsTypeDef"
    botLocaleStatus: BotLocaleStatus
    creationDateTime: datetime


class CreateBotResponseTypeDef(TypedDict, total=False):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: "DataPrivacyTypeDef"
    idleSessionTTLInSeconds: int
    botStatus: BotStatus
    creationDateTime: datetime
    botTags: Dict[str, str]
    testBotAliasTags: Dict[str, str]


class CreateBotVersionResponseTypeDef(TypedDict, total=False):
    botId: str
    description: str
    botVersion: str
    botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"]
    botStatus: BotStatus
    creationDateTime: datetime


class CreateIntentResponseTypeDef(TypedDict, total=False):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List["SampleUtteranceTypeDef"]
    dialogCodeHook: "DialogCodeHookSettingsTypeDef"
    fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef"
    intentConfirmationSetting: "IntentConfirmationSettingTypeDef"
    intentClosingSetting: "IntentClosingSettingTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]
    kendraConfiguration: "KendraConfigurationTypeDef"
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime


class CreateSlotResponseTypeDef(TypedDict, total=False):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: "SlotValueElicitationSettingTypeDef"
    obfuscationSetting: "ObfuscationSettingTypeDef"
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime


class CreateSlotTypeResponseTypeDef(TypedDict, total=False):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List["SlotTypeValueTypeDef"]
    valueSelectionSetting: "SlotValueSelectionSettingTypeDef"
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime


class CustomPayloadTypeDef(TypedDict):
    value: str


class DataPrivacyTypeDef(TypedDict):
    childDirected: bool


class DeleteBotAliasResponseTypeDef(TypedDict, total=False):
    botAliasId: str
    botId: str
    botAliasStatus: BotAliasStatus


class DeleteBotLocaleResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    botLocaleStatus: BotLocaleStatus


class DeleteBotResponseTypeDef(TypedDict, total=False):
    botId: str
    botStatus: BotStatus


class DeleteBotVersionResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    botStatus: BotStatus


class DescribeBotAliasResponseTypeDef(TypedDict, total=False):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"]
    conversationLogSettings: "ConversationLogSettingsTypeDef"
    sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef"
    botAliasHistoryEvents: List["BotAliasHistoryEventTypeDef"]
    botAliasStatus: BotAliasStatus
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DescribeBotLocaleResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: "VoiceSettingsTypeDef"
    intentsCount: int
    slotTypesCount: int
    botLocaleStatus: BotLocaleStatus
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    lastBuildSubmittedDateTime: datetime
    botLocaleHistoryEvents: List["BotLocaleHistoryEventTypeDef"]


class DescribeBotResponseTypeDef(TypedDict, total=False):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: "DataPrivacyTypeDef"
    idleSessionTTLInSeconds: int
    botStatus: BotStatus
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DescribeBotVersionResponseTypeDef(TypedDict, total=False):
    botId: str
    botName: str
    botVersion: str
    description: str
    roleArn: str
    dataPrivacy: "DataPrivacyTypeDef"
    idleSessionTTLInSeconds: int
    botStatus: BotStatus
    failureReasons: List[str]
    creationDateTime: datetime


class DescribeIntentResponseTypeDef(TypedDict, total=False):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List["SampleUtteranceTypeDef"]
    dialogCodeHook: "DialogCodeHookSettingsTypeDef"
    fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef"
    slotPriorities: List["SlotPriorityTypeDef"]
    intentConfirmationSetting: "IntentConfirmationSettingTypeDef"
    intentClosingSetting: "IntentClosingSettingTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]
    kendraConfiguration: "KendraConfigurationTypeDef"
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DescribeSlotResponseTypeDef(TypedDict, total=False):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: "SlotValueElicitationSettingTypeDef"
    obfuscationSetting: "ObfuscationSettingTypeDef"
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DescribeSlotTypeResponseTypeDef(TypedDict, total=False):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List["SlotTypeValueTypeDef"]
    valueSelectionSetting: "SlotValueSelectionSettingTypeDef"
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DialogCodeHookSettingsTypeDef(TypedDict):
    enabled: bool


class FulfillmentCodeHookSettingsTypeDef(TypedDict):
    enabled: bool


class _RequiredImageResponseCardTypeDef(TypedDict):
    title: str


class ImageResponseCardTypeDef(_RequiredImageResponseCardTypeDef, total=False):
    subtitle: str
    imageUrl: str
    buttons: List["ButtonTypeDef"]


class InputContextTypeDef(TypedDict):
    name: str


class IntentClosingSettingTypeDef(TypedDict):
    closingResponse: "ResponseSpecificationTypeDef"


class IntentConfirmationSettingTypeDef(TypedDict):
    promptSpecification: "PromptSpecificationTypeDef"
    declinationResponse: "ResponseSpecificationTypeDef"


IntentFilterTypeDef = TypedDict(
    "IntentFilterTypeDef",
    {"name": Literal["IntentName"], "values": List[str], "operator": IntentFilterOperator},
)


class IntentSortByTypeDef(TypedDict):
    attribute: IntentSortAttribute
    order: SortOrder


class IntentSummaryTypeDef(TypedDict, total=False):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]
    lastUpdatedDateTime: datetime


class _RequiredKendraConfigurationTypeDef(TypedDict):
    kendraIndex: str


class KendraConfigurationTypeDef(_RequiredKendraConfigurationTypeDef, total=False):
    queryFilterStringEnabled: bool
    queryFilterString: str


class LambdaCodeHookTypeDef(TypedDict):
    lambdaARN: str
    codeHookInterfaceVersion: str


class ListBotAliasesResponseTypeDef(TypedDict, total=False):
    botAliasSummaries: List["BotAliasSummaryTypeDef"]
    nextToken: str
    botId: str


class ListBotLocalesResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    nextToken: str
    botLocaleSummaries: List["BotLocaleSummaryTypeDef"]


class ListBotVersionsResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersionSummaries: List["BotVersionSummaryTypeDef"]
    nextToken: str


class ListBotsResponseTypeDef(TypedDict, total=False):
    botSummaries: List["BotSummaryTypeDef"]
    nextToken: str


class ListBuiltInIntentsResponseTypeDef(TypedDict, total=False):
    builtInIntentSummaries: List["BuiltInIntentSummaryTypeDef"]
    nextToken: str
    localeId: str


class ListBuiltInSlotTypesResponseTypeDef(TypedDict, total=False):
    builtInSlotTypeSummaries: List["BuiltInSlotTypeSummaryTypeDef"]
    nextToken: str
    localeId: str


class ListIntentsResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    intentSummaries: List["IntentSummaryTypeDef"]
    nextToken: str


class ListSlotTypesResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    slotTypeSummaries: List["SlotTypeSummaryTypeDef"]
    nextToken: str


class ListSlotsResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    slotSummaries: List["SlotSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredMessageGroupTypeDef(TypedDict):
    message: "MessageTypeDef"


class MessageGroupTypeDef(_RequiredMessageGroupTypeDef, total=False):
    variations: List["MessageTypeDef"]


class MessageTypeDef(TypedDict, total=False):
    plainTextMessage: "PlainTextMessageTypeDef"
    customPayload: "CustomPayloadTypeDef"
    ssmlMessage: "SSMLMessageTypeDef"
    imageResponseCard: "ImageResponseCardTypeDef"


class ObfuscationSettingTypeDef(TypedDict):
    obfuscationSettingType: ObfuscationSettingType


class OutputContextTypeDef(TypedDict):
    name: str
    timeToLiveInSeconds: int
    turnsToLive: int


class PlainTextMessageTypeDef(TypedDict):
    value: str


class _RequiredPromptSpecificationTypeDef(TypedDict):
    messageGroups: List["MessageGroupTypeDef"]
    maxRetries: int


class PromptSpecificationTypeDef(_RequiredPromptSpecificationTypeDef, total=False):
    allowInterrupt: bool


class _RequiredResponseSpecificationTypeDef(TypedDict):
    messageGroups: List["MessageGroupTypeDef"]


class ResponseSpecificationTypeDef(_RequiredResponseSpecificationTypeDef, total=False):
    allowInterrupt: bool


class _RequiredS3BucketLogDestinationTypeDef(TypedDict):
    s3BucketArn: str
    logPrefix: str


class S3BucketLogDestinationTypeDef(_RequiredS3BucketLogDestinationTypeDef, total=False):
    kmsKeyArn: str


class SSMLMessageTypeDef(TypedDict):
    value: str


class SampleUtteranceTypeDef(TypedDict):
    utterance: str


class SampleValueTypeDef(TypedDict):
    value: str


class SentimentAnalysisSettingsTypeDef(TypedDict):
    detectSentiment: bool


class SlotDefaultValueSpecificationTypeDef(TypedDict):
    defaultValueList: List["SlotDefaultValueTypeDef"]


class SlotDefaultValueTypeDef(TypedDict):
    defaultValue: str


SlotFilterTypeDef = TypedDict(
    "SlotFilterTypeDef",
    {"name": Literal["SlotName"], "values": List[str], "operator": SlotFilterOperator},
)


class SlotPriorityTypeDef(TypedDict):
    priority: int
    slotId: str


class SlotSortByTypeDef(TypedDict):
    attribute: SlotSortAttribute
    order: SortOrder


class SlotSummaryTypeDef(TypedDict, total=False):
    slotId: str
    slotName: str
    description: str
    slotConstraint: SlotConstraint
    slotTypeId: str
    valueElicitationPromptSpecification: "PromptSpecificationTypeDef"
    lastUpdatedDateTime: datetime


SlotTypeFilterTypeDef = TypedDict(
    "SlotTypeFilterTypeDef",
    {"name": Literal["SlotTypeName"], "values": List[str], "operator": SlotTypeFilterOperator},
)


class SlotTypeSortByTypeDef(TypedDict):
    attribute: SlotTypeSortAttribute
    order: SortOrder


class SlotTypeSummaryTypeDef(TypedDict, total=False):
    slotTypeId: str
    slotTypeName: str
    description: str
    parentSlotTypeSignature: str
    lastUpdatedDateTime: datetime


class SlotTypeValueTypeDef(TypedDict, total=False):
    sampleValue: "SampleValueTypeDef"
    synonyms: List["SampleValueTypeDef"]


class _RequiredSlotValueElicitationSettingTypeDef(TypedDict):
    slotConstraint: SlotConstraint


class SlotValueElicitationSettingTypeDef(_RequiredSlotValueElicitationSettingTypeDef, total=False):
    defaultValueSpecification: "SlotDefaultValueSpecificationTypeDef"
    promptSpecification: "PromptSpecificationTypeDef"
    sampleUtterances: List["SampleUtteranceTypeDef"]
    waitAndContinueSpecification: "WaitAndContinueSpecificationTypeDef"


class SlotValueRegexFilterTypeDef(TypedDict):
    pattern: str


class _RequiredSlotValueSelectionSettingTypeDef(TypedDict):
    resolutionStrategy: SlotValueResolutionStrategy


class SlotValueSelectionSettingTypeDef(_RequiredSlotValueSelectionSettingTypeDef, total=False):
    regexFilter: "SlotValueRegexFilterTypeDef"


class _RequiredStillWaitingResponseSpecificationTypeDef(TypedDict):
    messageGroups: List["MessageGroupTypeDef"]
    frequencyInSeconds: int
    timeoutInSeconds: int


class StillWaitingResponseSpecificationTypeDef(
    _RequiredStillWaitingResponseSpecificationTypeDef, total=False
):
    allowInterrupt: bool


class TextLogDestinationTypeDef(TypedDict):
    cloudWatch: "CloudWatchLogGroupLogDestinationTypeDef"


class TextLogSettingTypeDef(TypedDict):
    enabled: bool
    destination: "TextLogDestinationTypeDef"


class UpdateBotAliasResponseTypeDef(TypedDict, total=False):
    botAliasId: str
    botAliasName: str
    description: str
    botVersion: str
    botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"]
    conversationLogSettings: "ConversationLogSettingsTypeDef"
    sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef"
    botAliasStatus: BotAliasStatus
    botId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class UpdateBotLocaleResponseTypeDef(TypedDict, total=False):
    botId: str
    botVersion: str
    localeId: str
    localeName: str
    description: str
    nluIntentConfidenceThreshold: float
    voiceSettings: "VoiceSettingsTypeDef"
    botLocaleStatus: BotLocaleStatus
    failureReasons: List[str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class UpdateBotResponseTypeDef(TypedDict, total=False):
    botId: str
    botName: str
    description: str
    roleArn: str
    dataPrivacy: "DataPrivacyTypeDef"
    idleSessionTTLInSeconds: int
    botStatus: BotStatus
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class UpdateIntentResponseTypeDef(TypedDict, total=False):
    intentId: str
    intentName: str
    description: str
    parentIntentSignature: str
    sampleUtterances: List["SampleUtteranceTypeDef"]
    dialogCodeHook: "DialogCodeHookSettingsTypeDef"
    fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef"
    slotPriorities: List["SlotPriorityTypeDef"]
    intentConfirmationSetting: "IntentConfirmationSettingTypeDef"
    intentClosingSetting: "IntentClosingSettingTypeDef"
    inputContexts: List["InputContextTypeDef"]
    outputContexts: List["OutputContextTypeDef"]
    kendraConfiguration: "KendraConfigurationTypeDef"
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class UpdateSlotResponseTypeDef(TypedDict, total=False):
    slotId: str
    slotName: str
    description: str
    slotTypeId: str
    valueElicitationSetting: "SlotValueElicitationSettingTypeDef"
    obfuscationSetting: "ObfuscationSettingTypeDef"
    botId: str
    botVersion: str
    localeId: str
    intentId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class UpdateSlotTypeResponseTypeDef(TypedDict, total=False):
    slotTypeId: str
    slotTypeName: str
    description: str
    slotTypeValues: List["SlotTypeValueTypeDef"]
    valueSelectionSetting: "SlotValueSelectionSettingTypeDef"
    parentSlotTypeSignature: str
    botId: str
    botVersion: str
    localeId: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class VoiceSettingsTypeDef(TypedDict):
    voiceId: str


class _RequiredWaitAndContinueSpecificationTypeDef(TypedDict):
    waitingResponse: "ResponseSpecificationTypeDef"
    continueResponse: "ResponseSpecificationTypeDef"


class WaitAndContinueSpecificationTypeDef(
    _RequiredWaitAndContinueSpecificationTypeDef, total=False
):
    stillWaitingResponse: "StillWaitingResponseSpecificationTypeDef"
