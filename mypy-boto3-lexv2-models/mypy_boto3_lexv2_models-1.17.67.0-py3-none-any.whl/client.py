"""
Type annotations for lexv2-models service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_models import LexModelsV2Client

    client: LexModelsV2Client = boto3.client("lexv2-models")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lexv2_models.type_defs import (
    BotAliasLocaleSettingsTypeDef,
    BotFilterTypeDef,
    BotLocaleFilterTypeDef,
    BotLocaleSortByTypeDef,
    BotSortByTypeDef,
    BotVersionLocaleDetailsTypeDef,
    BotVersionSortByTypeDef,
    BuildBotLocaleResponseTypeDef,
    BuiltInIntentSortByTypeDef,
    BuiltInSlotTypeSortByTypeDef,
    ConversationLogSettingsTypeDef,
    CreateBotAliasResponseTypeDef,
    CreateBotLocaleResponseTypeDef,
    CreateBotResponseTypeDef,
    CreateBotVersionResponseTypeDef,
    CreateIntentResponseTypeDef,
    CreateSlotResponseTypeDef,
    CreateSlotTypeResponseTypeDef,
    DataPrivacyTypeDef,
    DeleteBotAliasResponseTypeDef,
    DeleteBotLocaleResponseTypeDef,
    DeleteBotResponseTypeDef,
    DeleteBotVersionResponseTypeDef,
    DescribeBotAliasResponseTypeDef,
    DescribeBotLocaleResponseTypeDef,
    DescribeBotResponseTypeDef,
    DescribeBotVersionResponseTypeDef,
    DescribeIntentResponseTypeDef,
    DescribeSlotResponseTypeDef,
    DescribeSlotTypeResponseTypeDef,
    DialogCodeHookSettingsTypeDef,
    FulfillmentCodeHookSettingsTypeDef,
    InputContextTypeDef,
    IntentClosingSettingTypeDef,
    IntentConfirmationSettingTypeDef,
    IntentFilterTypeDef,
    IntentSortByTypeDef,
    KendraConfigurationTypeDef,
    ListBotAliasesResponseTypeDef,
    ListBotLocalesResponseTypeDef,
    ListBotsResponseTypeDef,
    ListBotVersionsResponseTypeDef,
    ListBuiltInIntentsResponseTypeDef,
    ListBuiltInSlotTypesResponseTypeDef,
    ListIntentsResponseTypeDef,
    ListSlotsResponseTypeDef,
    ListSlotTypesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ObfuscationSettingTypeDef,
    OutputContextTypeDef,
    SampleUtteranceTypeDef,
    SentimentAnalysisSettingsTypeDef,
    SlotFilterTypeDef,
    SlotPriorityTypeDef,
    SlotSortByTypeDef,
    SlotTypeFilterTypeDef,
    SlotTypeSortByTypeDef,
    SlotTypeValueTypeDef,
    SlotValueElicitationSettingTypeDef,
    SlotValueSelectionSettingTypeDef,
    UpdateBotAliasResponseTypeDef,
    UpdateBotLocaleResponseTypeDef,
    UpdateBotResponseTypeDef,
    UpdateIntentResponseTypeDef,
    UpdateSlotResponseTypeDef,
    UpdateSlotTypeResponseTypeDef,
    VoiceSettingsTypeDef,
)

__all__ = ("LexModelsV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexModelsV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def build_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> BuildBotLocaleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.build_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#build-bot-locale)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#can-paginate)
        """

    def create_bot(
        self,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
        botTags: Dict[str, str] = None,
        testBotAliasTags: Dict[str, str] = None,
    ) -> CreateBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-bot)
        """

    def create_bot_alias(
        self,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-bot-alias)
        """

    def create_bot_locale(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
    ) -> CreateBotLocaleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-bot-locale)
        """

    def create_bot_version(
        self,
        botId: str,
        botVersionLocaleSpecification: Dict[str, "BotVersionLocaleDetailsTypeDef"],
        description: str = None,
    ) -> CreateBotVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-bot-version)
        """

    def create_intent(
        self,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
    ) -> CreateIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-intent)
        """

    def create_slot(
        self,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
    ) -> CreateSlotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-slot)
        """

    def create_slot_type(
        self,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None,
    ) -> CreateSlotTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.create_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#create-slot-type)
        """

    def delete_bot(
        self, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-bot)
        """

    def delete_bot_alias(
        self, botAliasId: str, botId: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-bot-alias)
        """

    def delete_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> DeleteBotLocaleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-bot-locale)
        """

    def delete_bot_version(
        self, botId: str, botVersion: str, skipResourceInUseCheck: bool = None
    ) -> DeleteBotVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-bot-version)
        """

    def delete_intent(self, intentId: str, botId: str, botVersion: str, localeId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-intent)
        """

    def delete_slot(
        self, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-slot)
        """

    def delete_slot_type(
        self,
        slotTypeId: str,
        botId: str,
        botVersion: str,
        localeId: str,
        skipResourceInUseCheck: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.delete_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#delete-slot-type)
        """

    def describe_bot(self, botId: str) -> DescribeBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-bot)
        """

    def describe_bot_alias(self, botAliasId: str, botId: str) -> DescribeBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-bot-alias)
        """

    def describe_bot_locale(
        self, botId: str, botVersion: str, localeId: str
    ) -> DescribeBotLocaleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-bot-locale)
        """

    def describe_bot_version(
        self, botId: str, botVersion: str
    ) -> DescribeBotVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_bot_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-bot-version)
        """

    def describe_intent(
        self, intentId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-intent)
        """

    def describe_slot(
        self, slotId: str, botId: str, botVersion: str, localeId: str, intentId: str
    ) -> DescribeSlotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-slot)
        """

    def describe_slot_type(
        self, slotTypeId: str, botId: str, botVersion: str, localeId: str
    ) -> DescribeSlotTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.describe_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#describe-slot-type)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#generate-presigned-url)
        """

    def list_bot_aliases(
        self, botId: str, maxResults: int = None, nextToken: str = None
    ) -> ListBotAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-bot-aliases)
        """

    def list_bot_locales(
        self,
        botId: str,
        botVersion: str,
        sortBy: BotLocaleSortByTypeDef = None,
        filters: List[BotLocaleFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotLocalesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_locales)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-bot-locales)
        """

    def list_bot_versions(
        self,
        botId: str,
        sortBy: BotVersionSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_bot_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-bot-versions)
        """

    def list_bots(
        self,
        sortBy: BotSortByTypeDef = None,
        filters: List[BotFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_bots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-bots)
        """

    def list_built_in_intents(
        self,
        localeId: str,
        sortBy: BuiltInIntentSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBuiltInIntentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-built-in-intents)
        """

    def list_built_in_slot_types(
        self,
        localeId: str,
        sortBy: BuiltInSlotTypeSortByTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListBuiltInSlotTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_built_in_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-built-in-slot-types)
        """

    def list_intents(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: IntentSortByTypeDef = None,
        filters: List[IntentFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListIntentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_intents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-intents)
        """

    def list_slot_types(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        sortBy: SlotTypeSortByTypeDef = None,
        filters: List[SlotTypeFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSlotTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_slot_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-slot-types)
        """

    def list_slots(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        sortBy: SlotSortByTypeDef = None,
        filters: List[SlotFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSlotsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_slots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-slots)
        """

    def list_tags_for_resource(self, resourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#list-tags-for-resource)
        """

    def tag_resource(self, resourceARN: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#tag-resource)
        """

    def untag_resource(self, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#untag-resource)
        """

    def update_bot(
        self,
        botId: str,
        botName: str,
        roleArn: str,
        dataPrivacy: "DataPrivacyTypeDef",
        idleSessionTTLInSeconds: int,
        description: str = None,
    ) -> UpdateBotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-bot)
        """

    def update_bot_alias(
        self,
        botAliasId: str,
        botAliasName: str,
        botId: str,
        description: str = None,
        botVersion: str = None,
        botAliasLocaleSettings: Dict[str, "BotAliasLocaleSettingsTypeDef"] = None,
        conversationLogSettings: "ConversationLogSettingsTypeDef" = None,
        sentimentAnalysisSettings: "SentimentAnalysisSettingsTypeDef" = None,
    ) -> UpdateBotAliasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-bot-alias)
        """

    def update_bot_locale(
        self,
        botId: str,
        botVersion: str,
        localeId: str,
        nluIntentConfidenceThreshold: float,
        description: str = None,
        voiceSettings: "VoiceSettingsTypeDef" = None,
    ) -> UpdateBotLocaleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_bot_locale)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-bot-locale)
        """

    def update_intent(
        self,
        intentId: str,
        intentName: str,
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        parentIntentSignature: str = None,
        sampleUtterances: List["SampleUtteranceTypeDef"] = None,
        dialogCodeHook: "DialogCodeHookSettingsTypeDef" = None,
        fulfillmentCodeHook: "FulfillmentCodeHookSettingsTypeDef" = None,
        slotPriorities: List["SlotPriorityTypeDef"] = None,
        intentConfirmationSetting: "IntentConfirmationSettingTypeDef" = None,
        intentClosingSetting: "IntentClosingSettingTypeDef" = None,
        inputContexts: List["InputContextTypeDef"] = None,
        outputContexts: List["OutputContextTypeDef"] = None,
        kendraConfiguration: "KendraConfigurationTypeDef" = None,
    ) -> UpdateIntentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_intent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-intent)
        """

    def update_slot(
        self,
        slotId: str,
        slotName: str,
        slotTypeId: str,
        valueElicitationSetting: "SlotValueElicitationSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        intentId: str,
        description: str = None,
        obfuscationSetting: "ObfuscationSettingTypeDef" = None,
    ) -> UpdateSlotResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-slot)
        """

    def update_slot_type(
        self,
        slotTypeId: str,
        slotTypeName: str,
        valueSelectionSetting: "SlotValueSelectionSettingTypeDef",
        botId: str,
        botVersion: str,
        localeId: str,
        description: str = None,
        slotTypeValues: List["SlotTypeValueTypeDef"] = None,
        parentSlotTypeSignature: str = None,
    ) -> UpdateSlotTypeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lexv2-models.html#LexModelsV2.Client.update_slot_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/client.html#update-slot-type)
        """
