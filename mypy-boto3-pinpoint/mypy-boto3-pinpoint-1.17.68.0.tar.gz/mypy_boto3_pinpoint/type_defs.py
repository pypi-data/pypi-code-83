"""
Type annotations for pinpoint service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint.type_defs import ADMChannelRequestTypeDef

    data: ADMChannelRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_pinpoint.literals import (
    Action,
    AttributeType,
    CampaignStatus,
    ChannelType,
    DeliveryStatus,
    DimensionType,
    Duration,
    FilterType,
    Format,
    Frequency,
    Include,
    JobStatus,
    MessageType,
    Mode,
    Operator,
    RecencyType,
    SegmentType,
    SourceType,
    State,
    TemplateType,
    TypeType,
    __EndpointTypesElement,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ADMChannelRequestTypeDef",
    "ADMChannelResponseTypeDef",
    "ADMMessageTypeDef",
    "APNSChannelRequestTypeDef",
    "APNSChannelResponseTypeDef",
    "APNSMessageTypeDef",
    "APNSPushNotificationTemplateTypeDef",
    "APNSSandboxChannelRequestTypeDef",
    "APNSSandboxChannelResponseTypeDef",
    "APNSVoipChannelRequestTypeDef",
    "APNSVoipChannelResponseTypeDef",
    "APNSVoipSandboxChannelRequestTypeDef",
    "APNSVoipSandboxChannelResponseTypeDef",
    "ActivitiesResponseTypeDef",
    "ActivityResponseTypeDef",
    "ActivityTypeDef",
    "AddressConfigurationTypeDef",
    "AndroidPushNotificationTemplateTypeDef",
    "ApplicationDateRangeKpiResponseTypeDef",
    "ApplicationResponseTypeDef",
    "ApplicationSettingsResourceTypeDef",
    "ApplicationsResponseTypeDef",
    "AttributeDimensionTypeDef",
    "AttributesResourceTypeDef",
    "BaiduChannelRequestTypeDef",
    "BaiduChannelResponseTypeDef",
    "BaiduMessageTypeDef",
    "BaseKpiResultTypeDef",
    "CampaignCustomMessageTypeDef",
    "CampaignDateRangeKpiResponseTypeDef",
    "CampaignEmailMessageTypeDef",
    "CampaignEventFilterTypeDef",
    "CampaignHookTypeDef",
    "CampaignLimitsTypeDef",
    "CampaignResponseTypeDef",
    "CampaignSmsMessageTypeDef",
    "CampaignStateTypeDef",
    "CampaignsResponseTypeDef",
    "ChannelResponseTypeDef",
    "ChannelsResponseTypeDef",
    "ConditionTypeDef",
    "ConditionalSplitActivityTypeDef",
    "CreateAppResponseTypeDef",
    "CreateApplicationRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateEmailTemplateResponseTypeDef",
    "CreateExportJobResponseTypeDef",
    "CreateImportJobResponseTypeDef",
    "CreateJourneyResponseTypeDef",
    "CreatePushTemplateResponseTypeDef",
    "CreateRecommenderConfigurationResponseTypeDef",
    "CreateRecommenderConfigurationTypeDef",
    "CreateSegmentResponseTypeDef",
    "CreateSmsTemplateResponseTypeDef",
    "CreateTemplateMessageBodyTypeDef",
    "CreateVoiceTemplateResponseTypeDef",
    "CustomDeliveryConfigurationTypeDef",
    "CustomMessageActivityTypeDef",
    "DefaultMessageTypeDef",
    "DefaultPushNotificationMessageTypeDef",
    "DefaultPushNotificationTemplateTypeDef",
    "DeleteAdmChannelResponseTypeDef",
    "DeleteApnsChannelResponseTypeDef",
    "DeleteApnsSandboxChannelResponseTypeDef",
    "DeleteApnsVoipChannelResponseTypeDef",
    "DeleteApnsVoipSandboxChannelResponseTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteBaiduChannelResponseTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteEmailChannelResponseTypeDef",
    "DeleteEmailTemplateResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventStreamResponseTypeDef",
    "DeleteGcmChannelResponseTypeDef",
    "DeleteJourneyResponseTypeDef",
    "DeletePushTemplateResponseTypeDef",
    "DeleteRecommenderConfigurationResponseTypeDef",
    "DeleteSegmentResponseTypeDef",
    "DeleteSmsChannelResponseTypeDef",
    "DeleteSmsTemplateResponseTypeDef",
    "DeleteUserEndpointsResponseTypeDef",
    "DeleteVoiceChannelResponseTypeDef",
    "DeleteVoiceTemplateResponseTypeDef",
    "DirectMessageConfigurationTypeDef",
    "EmailChannelRequestTypeDef",
    "EmailChannelResponseTypeDef",
    "EmailMessageActivityTypeDef",
    "EmailMessageTypeDef",
    "EmailTemplateRequestTypeDef",
    "EmailTemplateResponseTypeDef",
    "EndpointBatchItemTypeDef",
    "EndpointBatchRequestTypeDef",
    "EndpointDemographicTypeDef",
    "EndpointItemResponseTypeDef",
    "EndpointLocationTypeDef",
    "EndpointMessageResultTypeDef",
    "EndpointRequestTypeDef",
    "EndpointResponseTypeDef",
    "EndpointSendConfigurationTypeDef",
    "EndpointUserTypeDef",
    "EndpointsResponseTypeDef",
    "EventConditionTypeDef",
    "EventDimensionsTypeDef",
    "EventFilterTypeDef",
    "EventItemResponseTypeDef",
    "EventStartConditionTypeDef",
    "EventStreamTypeDef",
    "EventTypeDef",
    "EventsBatchTypeDef",
    "EventsRequestTypeDef",
    "EventsResponseTypeDef",
    "ExportJobRequestTypeDef",
    "ExportJobResourceTypeDef",
    "ExportJobResponseTypeDef",
    "ExportJobsResponseTypeDef",
    "GCMChannelRequestTypeDef",
    "GCMChannelResponseTypeDef",
    "GCMMessageTypeDef",
    "GPSCoordinatesTypeDef",
    "GPSPointDimensionTypeDef",
    "GetAdmChannelResponseTypeDef",
    "GetApnsChannelResponseTypeDef",
    "GetApnsSandboxChannelResponseTypeDef",
    "GetApnsVoipChannelResponseTypeDef",
    "GetApnsVoipSandboxChannelResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetApplicationDateRangeKpiResponseTypeDef",
    "GetApplicationSettingsResponseTypeDef",
    "GetAppsResponseTypeDef",
    "GetBaiduChannelResponseTypeDef",
    "GetCampaignActivitiesResponseTypeDef",
    "GetCampaignDateRangeKpiResponseTypeDef",
    "GetCampaignResponseTypeDef",
    "GetCampaignVersionResponseTypeDef",
    "GetCampaignVersionsResponseTypeDef",
    "GetCampaignsResponseTypeDef",
    "GetChannelsResponseTypeDef",
    "GetEmailChannelResponseTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetEndpointResponseTypeDef",
    "GetEventStreamResponseTypeDef",
    "GetExportJobResponseTypeDef",
    "GetExportJobsResponseTypeDef",
    "GetGcmChannelResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "GetImportJobsResponseTypeDef",
    "GetJourneyDateRangeKpiResponseTypeDef",
    "GetJourneyExecutionActivityMetricsResponseTypeDef",
    "GetJourneyExecutionMetricsResponseTypeDef",
    "GetJourneyResponseTypeDef",
    "GetPushTemplateResponseTypeDef",
    "GetRecommenderConfigurationResponseTypeDef",
    "GetRecommenderConfigurationsResponseTypeDef",
    "GetSegmentExportJobsResponseTypeDef",
    "GetSegmentImportJobsResponseTypeDef",
    "GetSegmentResponseTypeDef",
    "GetSegmentVersionResponseTypeDef",
    "GetSegmentVersionsResponseTypeDef",
    "GetSegmentsResponseTypeDef",
    "GetSmsChannelResponseTypeDef",
    "GetSmsTemplateResponseTypeDef",
    "GetUserEndpointsResponseTypeDef",
    "GetVoiceChannelResponseTypeDef",
    "GetVoiceTemplateResponseTypeDef",
    "HoldoutActivityTypeDef",
    "ImportJobRequestTypeDef",
    "ImportJobResourceTypeDef",
    "ImportJobResponseTypeDef",
    "ImportJobsResponseTypeDef",
    "ItemResponseTypeDef",
    "JourneyCustomMessageTypeDef",
    "JourneyDateRangeKpiResponseTypeDef",
    "JourneyEmailMessageTypeDef",
    "JourneyExecutionActivityMetricsResponseTypeDef",
    "JourneyExecutionMetricsResponseTypeDef",
    "JourneyLimitsTypeDef",
    "JourneyPushMessageTypeDef",
    "JourneyResponseTypeDef",
    "JourneySMSMessageTypeDef",
    "JourneyScheduleTypeDef",
    "JourneyStateRequestTypeDef",
    "JourneysResponseTypeDef",
    "ListJourneysResponseTypeDef",
    "ListRecommenderConfigurationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateVersionsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "MessageBodyTypeDef",
    "MessageConfigurationTypeDef",
    "MessageRequestTypeDef",
    "MessageResponseTypeDef",
    "MessageResultTypeDef",
    "MessageTypeDef",
    "MetricDimensionTypeDef",
    "MultiConditionalBranchTypeDef",
    "MultiConditionalSplitActivityTypeDef",
    "NumberValidateRequestTypeDef",
    "NumberValidateResponseTypeDef",
    "PhoneNumberValidateResponseTypeDef",
    "PublicEndpointTypeDef",
    "PushMessageActivityTypeDef",
    "PushNotificationTemplateRequestTypeDef",
    "PushNotificationTemplateResponseTypeDef",
    "PutEventStreamResponseTypeDef",
    "PutEventsResponseTypeDef",
    "QuietTimeTypeDef",
    "RandomSplitActivityTypeDef",
    "RandomSplitEntryTypeDef",
    "RawEmailTypeDef",
    "RecencyDimensionTypeDef",
    "RecommenderConfigurationResponseTypeDef",
    "RemoveAttributesResponseTypeDef",
    "ResultRowTypeDef",
    "ResultRowValueTypeDef",
    "SMSChannelRequestTypeDef",
    "SMSChannelResponseTypeDef",
    "SMSMessageActivityTypeDef",
    "SMSMessageTypeDef",
    "SMSTemplateRequestTypeDef",
    "SMSTemplateResponseTypeDef",
    "ScheduleTypeDef",
    "SegmentBehaviorsTypeDef",
    "SegmentConditionTypeDef",
    "SegmentDemographicsTypeDef",
    "SegmentDimensionsTypeDef",
    "SegmentGroupListTypeDef",
    "SegmentGroupTypeDef",
    "SegmentImportResourceTypeDef",
    "SegmentLocationTypeDef",
    "SegmentReferenceTypeDef",
    "SegmentResponseTypeDef",
    "SegmentsResponseTypeDef",
    "SendMessagesResponseTypeDef",
    "SendUsersMessageRequestTypeDef",
    "SendUsersMessageResponseTypeDef",
    "SendUsersMessagesResponseTypeDef",
    "SessionTypeDef",
    "SetDimensionTypeDef",
    "SimpleConditionTypeDef",
    "SimpleEmailPartTypeDef",
    "SimpleEmailTypeDef",
    "StartConditionTypeDef",
    "TagsModelTypeDef",
    "TemplateActiveVersionRequestTypeDef",
    "TemplateConfigurationTypeDef",
    "TemplateResponseTypeDef",
    "TemplateTypeDef",
    "TemplateVersionResponseTypeDef",
    "TemplateVersionsResponseTypeDef",
    "TemplatesResponseTypeDef",
    "TreatmentResourceTypeDef",
    "UpdateAdmChannelResponseTypeDef",
    "UpdateApnsChannelResponseTypeDef",
    "UpdateApnsSandboxChannelResponseTypeDef",
    "UpdateApnsVoipChannelResponseTypeDef",
    "UpdateApnsVoipSandboxChannelResponseTypeDef",
    "UpdateApplicationSettingsResponseTypeDef",
    "UpdateAttributesRequestTypeDef",
    "UpdateBaiduChannelResponseTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateEmailChannelResponseTypeDef",
    "UpdateEmailTemplateResponseTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateEndpointsBatchResponseTypeDef",
    "UpdateGcmChannelResponseTypeDef",
    "UpdateJourneyResponseTypeDef",
    "UpdateJourneyStateResponseTypeDef",
    "UpdatePushTemplateResponseTypeDef",
    "UpdateRecommenderConfigurationResponseTypeDef",
    "UpdateRecommenderConfigurationTypeDef",
    "UpdateSegmentResponseTypeDef",
    "UpdateSmsChannelResponseTypeDef",
    "UpdateSmsTemplateResponseTypeDef",
    "UpdateTemplateActiveVersionResponseTypeDef",
    "UpdateVoiceChannelResponseTypeDef",
    "UpdateVoiceTemplateResponseTypeDef",
    "VoiceChannelRequestTypeDef",
    "VoiceChannelResponseTypeDef",
    "VoiceMessageTypeDef",
    "VoiceTemplateRequestTypeDef",
    "VoiceTemplateResponseTypeDef",
    "WaitActivityTypeDef",
    "WaitTimeTypeDef",
    "WriteApplicationSettingsRequestTypeDef",
    "WriteCampaignRequestTypeDef",
    "WriteEventStreamTypeDef",
    "WriteJourneyRequestTypeDef",
    "WriteSegmentRequestTypeDef",
    "WriteTreatmentResourceTypeDef",
)


class _RequiredADMChannelRequestTypeDef(TypedDict):
    ClientId: str
    ClientSecret: str


class ADMChannelRequestTypeDef(_RequiredADMChannelRequestTypeDef, total=False):
    Enabled: bool


class _RequiredADMChannelResponseTypeDef(TypedDict):
    Platform: str


class ADMChannelResponseTypeDef(_RequiredADMChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class ADMMessageTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    ConsolidationKey: str
    Data: Dict[str, str]
    ExpiresAfter: str
    IconReference: str
    ImageIconUrl: str
    ImageUrl: str
    MD5: str
    RawContent: str
    SilentPush: bool
    SmallImageIconUrl: str
    Sound: str
    Substitutions: Dict[str, List[str]]
    Title: str
    Url: str


class APNSChannelRequestTypeDef(TypedDict, total=False):
    BundleId: str
    Certificate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    PrivateKey: str
    TeamId: str
    TokenKey: str
    TokenKeyId: str


class _RequiredAPNSChannelResponseTypeDef(TypedDict):
    Platform: str


class APNSChannelResponseTypeDef(_RequiredAPNSChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    HasCredential: bool
    HasTokenKey: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class APNSMessageTypeDef(TypedDict, total=False):
    APNSPushType: str
    Action: Action
    Badge: int
    Body: str
    Category: str
    CollapseId: str
    Data: Dict[str, str]
    MediaUrl: str
    PreferredAuthenticationMethod: str
    Priority: str
    RawContent: str
    SilentPush: bool
    Sound: str
    Substitutions: Dict[str, List[str]]
    ThreadId: str
    TimeToLive: int
    Title: str
    Url: str


class APNSPushNotificationTemplateTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    MediaUrl: str
    RawContent: str
    Sound: str
    Title: str
    Url: str


class APNSSandboxChannelRequestTypeDef(TypedDict, total=False):
    BundleId: str
    Certificate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    PrivateKey: str
    TeamId: str
    TokenKey: str
    TokenKeyId: str


class _RequiredAPNSSandboxChannelResponseTypeDef(TypedDict):
    Platform: str


class APNSSandboxChannelResponseTypeDef(_RequiredAPNSSandboxChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    HasCredential: bool
    HasTokenKey: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class APNSVoipChannelRequestTypeDef(TypedDict, total=False):
    BundleId: str
    Certificate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    PrivateKey: str
    TeamId: str
    TokenKey: str
    TokenKeyId: str


class _RequiredAPNSVoipChannelResponseTypeDef(TypedDict):
    Platform: str


class APNSVoipChannelResponseTypeDef(_RequiredAPNSVoipChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    HasCredential: bool
    HasTokenKey: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class APNSVoipSandboxChannelRequestTypeDef(TypedDict, total=False):
    BundleId: str
    Certificate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    PrivateKey: str
    TeamId: str
    TokenKey: str
    TokenKeyId: str


class _RequiredAPNSVoipSandboxChannelResponseTypeDef(TypedDict):
    Platform: str


class APNSVoipSandboxChannelResponseTypeDef(
    _RequiredAPNSVoipSandboxChannelResponseTypeDef, total=False
):
    ApplicationId: str
    CreationDate: str
    DefaultAuthenticationMethod: str
    Enabled: bool
    HasCredential: bool
    HasTokenKey: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class _RequiredActivitiesResponseTypeDef(TypedDict):
    Item: List["ActivityResponseTypeDef"]


class ActivitiesResponseTypeDef(_RequiredActivitiesResponseTypeDef, total=False):
    NextToken: str


class _RequiredActivityResponseTypeDef(TypedDict):
    ApplicationId: str
    CampaignId: str
    Id: str


class ActivityResponseTypeDef(_RequiredActivityResponseTypeDef, total=False):
    End: str
    Result: str
    ScheduledStart: str
    Start: str
    State: str
    SuccessfulEndpointCount: int
    TimezonesCompletedCount: int
    TimezonesTotalCount: int
    TotalEndpointCount: int
    TreatmentId: str


class ActivityTypeDef(TypedDict, total=False):
    CUSTOM: "CustomMessageActivityTypeDef"
    ConditionalSplit: "ConditionalSplitActivityTypeDef"
    Description: str
    EMAIL: "EmailMessageActivityTypeDef"
    Holdout: "HoldoutActivityTypeDef"
    MultiCondition: "MultiConditionalSplitActivityTypeDef"
    PUSH: "PushMessageActivityTypeDef"
    RandomSplit: "RandomSplitActivityTypeDef"
    SMS: "SMSMessageActivityTypeDef"
    Wait: "WaitActivityTypeDef"


class AddressConfigurationTypeDef(TypedDict, total=False):
    BodyOverride: str
    ChannelType: ChannelType
    Context: Dict[str, str]
    RawContent: str
    Substitutions: Dict[str, List[str]]
    TitleOverride: str


class AndroidPushNotificationTemplateTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    ImageIconUrl: str
    ImageUrl: str
    RawContent: str
    SmallImageIconUrl: str
    Sound: str
    Title: str
    Url: str


class _RequiredApplicationDateRangeKpiResponseTypeDef(TypedDict):
    ApplicationId: str
    EndTime: datetime
    KpiName: str
    KpiResult: "BaseKpiResultTypeDef"
    StartTime: datetime


class ApplicationDateRangeKpiResponseTypeDef(
    _RequiredApplicationDateRangeKpiResponseTypeDef, total=False
):
    NextToken: str


class _RequiredApplicationResponseTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str


class ApplicationResponseTypeDef(_RequiredApplicationResponseTypeDef, total=False):
    tags: Dict[str, str]


class _RequiredApplicationSettingsResourceTypeDef(TypedDict):
    ApplicationId: str


class ApplicationSettingsResourceTypeDef(_RequiredApplicationSettingsResourceTypeDef, total=False):
    CampaignHook: "CampaignHookTypeDef"
    LastModifiedDate: str
    Limits: "CampaignLimitsTypeDef"
    QuietTime: "QuietTimeTypeDef"


class ApplicationsResponseTypeDef(TypedDict, total=False):
    Item: List["ApplicationResponseTypeDef"]
    NextToken: str


class _RequiredAttributeDimensionTypeDef(TypedDict):
    Values: List[str]


class AttributeDimensionTypeDef(_RequiredAttributeDimensionTypeDef, total=False):
    AttributeType: AttributeType


class _RequiredAttributesResourceTypeDef(TypedDict):
    ApplicationId: str
    AttributeType: str


class AttributesResourceTypeDef(_RequiredAttributesResourceTypeDef, total=False):
    Attributes: List[str]


class _RequiredBaiduChannelRequestTypeDef(TypedDict):
    ApiKey: str
    SecretKey: str


class BaiduChannelRequestTypeDef(_RequiredBaiduChannelRequestTypeDef, total=False):
    Enabled: bool


class _RequiredBaiduChannelResponseTypeDef(TypedDict):
    Credential: str
    Platform: str


class BaiduChannelResponseTypeDef(_RequiredBaiduChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class BaiduMessageTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    Data: Dict[str, str]
    IconReference: str
    ImageIconUrl: str
    ImageUrl: str
    RawContent: str
    SilentPush: bool
    SmallImageIconUrl: str
    Sound: str
    Substitutions: Dict[str, List[str]]
    TimeToLive: int
    Title: str
    Url: str


class BaseKpiResultTypeDef(TypedDict):
    Rows: List["ResultRowTypeDef"]


class CampaignCustomMessageTypeDef(TypedDict, total=False):
    Data: str


class _RequiredCampaignDateRangeKpiResponseTypeDef(TypedDict):
    ApplicationId: str
    CampaignId: str
    EndTime: datetime
    KpiName: str
    KpiResult: "BaseKpiResultTypeDef"
    StartTime: datetime


class CampaignDateRangeKpiResponseTypeDef(
    _RequiredCampaignDateRangeKpiResponseTypeDef, total=False
):
    NextToken: str


class CampaignEmailMessageTypeDef(TypedDict, total=False):
    Body: str
    FromAddress: str
    HtmlBody: str
    Title: str


class CampaignEventFilterTypeDef(TypedDict):
    Dimensions: "EventDimensionsTypeDef"
    FilterType: FilterType


class CampaignHookTypeDef(TypedDict, total=False):
    LambdaFunctionName: str
    Mode: Mode
    WebUrl: str


class CampaignLimitsTypeDef(TypedDict, total=False):
    Daily: int
    MaximumDuration: int
    MessagesPerSecond: int
    Total: int


class _RequiredCampaignResponseTypeDef(TypedDict):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    LastModifiedDate: str
    SegmentId: str
    SegmentVersion: int


class CampaignResponseTypeDef(_RequiredCampaignResponseTypeDef, total=False):
    AdditionalTreatments: List["TreatmentResourceTypeDef"]
    CustomDeliveryConfiguration: "CustomDeliveryConfigurationTypeDef"
    DefaultState: "CampaignStateTypeDef"
    Description: str
    HoldoutPercent: int
    Hook: "CampaignHookTypeDef"
    IsPaused: bool
    Limits: "CampaignLimitsTypeDef"
    MessageConfiguration: "MessageConfigurationTypeDef"
    Name: str
    Schedule: "ScheduleTypeDef"
    State: "CampaignStateTypeDef"
    tags: Dict[str, str]
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TreatmentDescription: str
    TreatmentName: str
    Version: int


class CampaignSmsMessageTypeDef(TypedDict, total=False):
    Body: str
    MessageType: MessageType
    OriginationNumber: str
    SenderId: str
    EntityId: str
    TemplateId: str


class CampaignStateTypeDef(TypedDict, total=False):
    CampaignStatus: CampaignStatus


class _RequiredCampaignsResponseTypeDef(TypedDict):
    Item: List["CampaignResponseTypeDef"]


class CampaignsResponseTypeDef(_RequiredCampaignsResponseTypeDef, total=False):
    NextToken: str


class ChannelResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class ChannelsResponseTypeDef(TypedDict):
    Channels: Dict[str, "ChannelResponseTypeDef"]


class ConditionTypeDef(TypedDict, total=False):
    Conditions: List["SimpleConditionTypeDef"]
    Operator: Operator


class ConditionalSplitActivityTypeDef(TypedDict, total=False):
    Condition: "ConditionTypeDef"
    EvaluationWaitTime: "WaitTimeTypeDef"
    FalseActivity: str
    TrueActivity: str


class CreateAppResponseTypeDef(TypedDict):
    ApplicationResponse: "ApplicationResponseTypeDef"


class _RequiredCreateApplicationRequestTypeDef(TypedDict):
    Name: str


class CreateApplicationRequestTypeDef(_RequiredCreateApplicationRequestTypeDef, total=False):
    tags: Dict[str, str]


class CreateCampaignResponseTypeDef(TypedDict):
    CampaignResponse: "CampaignResponseTypeDef"


class CreateEmailTemplateResponseTypeDef(TypedDict):
    CreateTemplateMessageBody: "CreateTemplateMessageBodyTypeDef"


class CreateExportJobResponseTypeDef(TypedDict):
    ExportJobResponse: "ExportJobResponseTypeDef"


class CreateImportJobResponseTypeDef(TypedDict):
    ImportJobResponse: "ImportJobResponseTypeDef"


class CreateJourneyResponseTypeDef(TypedDict):
    JourneyResponse: "JourneyResponseTypeDef"


class CreatePushTemplateResponseTypeDef(TypedDict):
    CreateTemplateMessageBody: "CreateTemplateMessageBodyTypeDef"


class CreateRecommenderConfigurationResponseTypeDef(TypedDict):
    RecommenderConfigurationResponse: "RecommenderConfigurationResponseTypeDef"


class _RequiredCreateRecommenderConfigurationTypeDef(TypedDict):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str


class CreateRecommenderConfigurationTypeDef(
    _RequiredCreateRecommenderConfigurationTypeDef, total=False
):
    Attributes: Dict[str, str]
    Description: str
    Name: str
    RecommendationProviderIdType: str
    RecommendationTransformerUri: str
    RecommendationsDisplayName: str
    RecommendationsPerMessage: int


class CreateSegmentResponseTypeDef(TypedDict):
    SegmentResponse: "SegmentResponseTypeDef"


class CreateSmsTemplateResponseTypeDef(TypedDict):
    CreateTemplateMessageBody: "CreateTemplateMessageBodyTypeDef"


class CreateTemplateMessageBodyTypeDef(TypedDict, total=False):
    Arn: str
    Message: str
    RequestID: str


class CreateVoiceTemplateResponseTypeDef(TypedDict):
    CreateTemplateMessageBody: "CreateTemplateMessageBodyTypeDef"


class _RequiredCustomDeliveryConfigurationTypeDef(TypedDict):
    DeliveryUri: str


class CustomDeliveryConfigurationTypeDef(_RequiredCustomDeliveryConfigurationTypeDef, total=False):
    EndpointTypes: List[__EndpointTypesElement]


class CustomMessageActivityTypeDef(TypedDict, total=False):
    DeliveryUri: str
    EndpointTypes: List[__EndpointTypesElement]
    MessageConfig: "JourneyCustomMessageTypeDef"
    NextActivity: str
    TemplateName: str
    TemplateVersion: str


class DefaultMessageTypeDef(TypedDict, total=False):
    Body: str
    Substitutions: Dict[str, List[str]]


class DefaultPushNotificationMessageTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    Data: Dict[str, str]
    SilentPush: bool
    Substitutions: Dict[str, List[str]]
    Title: str
    Url: str


class DefaultPushNotificationTemplateTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    Sound: str
    Title: str
    Url: str


class DeleteAdmChannelResponseTypeDef(TypedDict):
    ADMChannelResponse: "ADMChannelResponseTypeDef"


class DeleteApnsChannelResponseTypeDef(TypedDict):
    APNSChannelResponse: "APNSChannelResponseTypeDef"


class DeleteApnsSandboxChannelResponseTypeDef(TypedDict):
    APNSSandboxChannelResponse: "APNSSandboxChannelResponseTypeDef"


class DeleteApnsVoipChannelResponseTypeDef(TypedDict):
    APNSVoipChannelResponse: "APNSVoipChannelResponseTypeDef"


class DeleteApnsVoipSandboxChannelResponseTypeDef(TypedDict):
    APNSVoipSandboxChannelResponse: "APNSVoipSandboxChannelResponseTypeDef"


class DeleteAppResponseTypeDef(TypedDict):
    ApplicationResponse: "ApplicationResponseTypeDef"


class DeleteBaiduChannelResponseTypeDef(TypedDict):
    BaiduChannelResponse: "BaiduChannelResponseTypeDef"


class DeleteCampaignResponseTypeDef(TypedDict):
    CampaignResponse: "CampaignResponseTypeDef"


class DeleteEmailChannelResponseTypeDef(TypedDict):
    EmailChannelResponse: "EmailChannelResponseTypeDef"


class DeleteEmailTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class DeleteEndpointResponseTypeDef(TypedDict):
    EndpointResponse: "EndpointResponseTypeDef"


class DeleteEventStreamResponseTypeDef(TypedDict):
    EventStream: "EventStreamTypeDef"


class DeleteGcmChannelResponseTypeDef(TypedDict):
    GCMChannelResponse: "GCMChannelResponseTypeDef"


class DeleteJourneyResponseTypeDef(TypedDict):
    JourneyResponse: "JourneyResponseTypeDef"


class DeletePushTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class DeleteRecommenderConfigurationResponseTypeDef(TypedDict):
    RecommenderConfigurationResponse: "RecommenderConfigurationResponseTypeDef"


class DeleteSegmentResponseTypeDef(TypedDict):
    SegmentResponse: "SegmentResponseTypeDef"


class DeleteSmsChannelResponseTypeDef(TypedDict):
    SMSChannelResponse: "SMSChannelResponseTypeDef"


class DeleteSmsTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class DeleteUserEndpointsResponseTypeDef(TypedDict):
    EndpointsResponse: "EndpointsResponseTypeDef"


class DeleteVoiceChannelResponseTypeDef(TypedDict):
    VoiceChannelResponse: "VoiceChannelResponseTypeDef"


class DeleteVoiceTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class DirectMessageConfigurationTypeDef(TypedDict, total=False):
    ADMMessage: "ADMMessageTypeDef"
    APNSMessage: "APNSMessageTypeDef"
    BaiduMessage: "BaiduMessageTypeDef"
    DefaultMessage: "DefaultMessageTypeDef"
    DefaultPushNotificationMessage: "DefaultPushNotificationMessageTypeDef"
    EmailMessage: "EmailMessageTypeDef"
    GCMMessage: "GCMMessageTypeDef"
    SMSMessage: "SMSMessageTypeDef"
    VoiceMessage: "VoiceMessageTypeDef"


class _RequiredEmailChannelRequestTypeDef(TypedDict):
    FromAddress: str
    Identity: str


class EmailChannelRequestTypeDef(_RequiredEmailChannelRequestTypeDef, total=False):
    ConfigurationSet: str
    Enabled: bool
    RoleArn: str


class _RequiredEmailChannelResponseTypeDef(TypedDict):
    Platform: str


class EmailChannelResponseTypeDef(_RequiredEmailChannelResponseTypeDef, total=False):
    ApplicationId: str
    ConfigurationSet: str
    CreationDate: str
    Enabled: bool
    FromAddress: str
    HasCredential: bool
    Id: str
    Identity: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    MessagesPerSecond: int
    RoleArn: str
    Version: int


class EmailMessageActivityTypeDef(TypedDict, total=False):
    MessageConfig: "JourneyEmailMessageTypeDef"
    NextActivity: str
    TemplateName: str
    TemplateVersion: str


class EmailMessageTypeDef(TypedDict, total=False):
    Body: str
    FeedbackForwardingAddress: str
    FromAddress: str
    RawEmail: "RawEmailTypeDef"
    ReplyToAddresses: List[str]
    SimpleEmail: "SimpleEmailTypeDef"
    Substitutions: Dict[str, List[str]]


class EmailTemplateRequestTypeDef(TypedDict, total=False):
    DefaultSubstitutions: str
    HtmlPart: str
    RecommenderId: str
    Subject: str
    tags: Dict[str, str]
    TemplateDescription: str
    TextPart: str


class _RequiredEmailTemplateResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateType


class EmailTemplateResponseTypeDef(_RequiredEmailTemplateResponseTypeDef, total=False):
    Arn: str
    DefaultSubstitutions: str
    HtmlPart: str
    RecommenderId: str
    Subject: str
    tags: Dict[str, str]
    TemplateDescription: str
    TextPart: str
    Version: str


class EndpointBatchItemTypeDef(TypedDict, total=False):
    Address: str
    Attributes: Dict[str, List[str]]
    ChannelType: ChannelType
    Demographic: "EndpointDemographicTypeDef"
    EffectiveDate: str
    EndpointStatus: str
    Id: str
    Location: "EndpointLocationTypeDef"
    Metrics: Dict[str, float]
    OptOut: str
    RequestId: str
    User: "EndpointUserTypeDef"


class EndpointBatchRequestTypeDef(TypedDict):
    Item: List["EndpointBatchItemTypeDef"]


class EndpointDemographicTypeDef(TypedDict, total=False):
    AppVersion: str
    Locale: str
    Make: str
    Model: str
    ModelVersion: str
    Platform: str
    PlatformVersion: str
    Timezone: str


class EndpointItemResponseTypeDef(TypedDict, total=False):
    Message: str
    StatusCode: int


class EndpointLocationTypeDef(TypedDict, total=False):
    City: str
    Country: str
    Latitude: float
    Longitude: float
    PostalCode: str
    Region: str


class _RequiredEndpointMessageResultTypeDef(TypedDict):
    DeliveryStatus: DeliveryStatus
    StatusCode: int


class EndpointMessageResultTypeDef(_RequiredEndpointMessageResultTypeDef, total=False):
    Address: str
    MessageId: str
    StatusMessage: str
    UpdatedToken: str


class EndpointRequestTypeDef(TypedDict, total=False):
    Address: str
    Attributes: Dict[str, List[str]]
    ChannelType: ChannelType
    Demographic: "EndpointDemographicTypeDef"
    EffectiveDate: str
    EndpointStatus: str
    Location: "EndpointLocationTypeDef"
    Metrics: Dict[str, float]
    OptOut: str
    RequestId: str
    User: "EndpointUserTypeDef"


class EndpointResponseTypeDef(TypedDict, total=False):
    Address: str
    ApplicationId: str
    Attributes: Dict[str, List[str]]
    ChannelType: ChannelType
    CohortId: str
    CreationDate: str
    Demographic: "EndpointDemographicTypeDef"
    EffectiveDate: str
    EndpointStatus: str
    Id: str
    Location: "EndpointLocationTypeDef"
    Metrics: Dict[str, float]
    OptOut: str
    RequestId: str
    User: "EndpointUserTypeDef"


class EndpointSendConfigurationTypeDef(TypedDict, total=False):
    BodyOverride: str
    Context: Dict[str, str]
    RawContent: str
    Substitutions: Dict[str, List[str]]
    TitleOverride: str


class EndpointUserTypeDef(TypedDict, total=False):
    UserAttributes: Dict[str, List[str]]
    UserId: str


class EndpointsResponseTypeDef(TypedDict):
    Item: List["EndpointResponseTypeDef"]


class EventConditionTypeDef(TypedDict, total=False):
    Dimensions: "EventDimensionsTypeDef"
    MessageActivity: str


class EventDimensionsTypeDef(TypedDict, total=False):
    Attributes: Dict[str, "AttributeDimensionTypeDef"]
    EventType: "SetDimensionTypeDef"
    Metrics: Dict[str, "MetricDimensionTypeDef"]


class EventFilterTypeDef(TypedDict):
    Dimensions: "EventDimensionsTypeDef"
    FilterType: FilterType


class EventItemResponseTypeDef(TypedDict, total=False):
    Message: str
    StatusCode: int


class EventStartConditionTypeDef(TypedDict, total=False):
    EventFilter: "EventFilterTypeDef"
    SegmentId: str


class _RequiredEventStreamTypeDef(TypedDict):
    ApplicationId: str
    DestinationStreamArn: str
    RoleArn: str


class EventStreamTypeDef(_RequiredEventStreamTypeDef, total=False):
    ExternalId: str
    LastModifiedDate: str
    LastUpdatedBy: str


class _RequiredEventTypeDef(TypedDict):
    EventType: str
    Timestamp: str


class EventTypeDef(_RequiredEventTypeDef, total=False):
    AppPackageName: str
    AppTitle: str
    AppVersionCode: str
    Attributes: Dict[str, str]
    ClientSdkVersion: str
    Metrics: Dict[str, float]
    SdkName: str
    Session: "SessionTypeDef"


class EventsBatchTypeDef(TypedDict):
    Endpoint: "PublicEndpointTypeDef"
    Events: Dict[str, "EventTypeDef"]


class EventsRequestTypeDef(TypedDict):
    BatchItem: Dict[str, "EventsBatchTypeDef"]


class EventsResponseTypeDef(TypedDict, total=False):
    Results: Dict[str, "ItemResponseTypeDef"]


class _RequiredExportJobRequestTypeDef(TypedDict):
    RoleArn: str
    S3UrlPrefix: str


class ExportJobRequestTypeDef(_RequiredExportJobRequestTypeDef, total=False):
    SegmentId: str
    SegmentVersion: int


class _RequiredExportJobResourceTypeDef(TypedDict):
    RoleArn: str
    S3UrlPrefix: str


class ExportJobResourceTypeDef(_RequiredExportJobResourceTypeDef, total=False):
    SegmentId: str
    SegmentVersion: int


_RequiredExportJobResponseTypeDef = TypedDict(
    "_RequiredExportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ExportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatus,
        "Type": str,
    },
)
_OptionalExportJobResponseTypeDef = TypedDict(
    "_OptionalExportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)


class ExportJobResponseTypeDef(
    _RequiredExportJobResponseTypeDef, _OptionalExportJobResponseTypeDef
):
    pass


class _RequiredExportJobsResponseTypeDef(TypedDict):
    Item: List["ExportJobResponseTypeDef"]


class ExportJobsResponseTypeDef(_RequiredExportJobsResponseTypeDef, total=False):
    NextToken: str


class _RequiredGCMChannelRequestTypeDef(TypedDict):
    ApiKey: str


class GCMChannelRequestTypeDef(_RequiredGCMChannelRequestTypeDef, total=False):
    Enabled: bool


class _RequiredGCMChannelResponseTypeDef(TypedDict):
    Credential: str
    Platform: str


class GCMChannelResponseTypeDef(_RequiredGCMChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class GCMMessageTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    CollapseKey: str
    Data: Dict[str, str]
    IconReference: str
    ImageIconUrl: str
    ImageUrl: str
    Priority: str
    RawContent: str
    RestrictedPackageName: str
    SilentPush: bool
    SmallImageIconUrl: str
    Sound: str
    Substitutions: Dict[str, List[str]]
    TimeToLive: int
    Title: str
    Url: str


class GPSCoordinatesTypeDef(TypedDict):
    Latitude: float
    Longitude: float


class _RequiredGPSPointDimensionTypeDef(TypedDict):
    Coordinates: "GPSCoordinatesTypeDef"


class GPSPointDimensionTypeDef(_RequiredGPSPointDimensionTypeDef, total=False):
    RangeInKilometers: float


class GetAdmChannelResponseTypeDef(TypedDict):
    ADMChannelResponse: "ADMChannelResponseTypeDef"


class GetApnsChannelResponseTypeDef(TypedDict):
    APNSChannelResponse: "APNSChannelResponseTypeDef"


class GetApnsSandboxChannelResponseTypeDef(TypedDict):
    APNSSandboxChannelResponse: "APNSSandboxChannelResponseTypeDef"


class GetApnsVoipChannelResponseTypeDef(TypedDict):
    APNSVoipChannelResponse: "APNSVoipChannelResponseTypeDef"


class GetApnsVoipSandboxChannelResponseTypeDef(TypedDict):
    APNSVoipSandboxChannelResponse: "APNSVoipSandboxChannelResponseTypeDef"


class GetAppResponseTypeDef(TypedDict):
    ApplicationResponse: "ApplicationResponseTypeDef"


class GetApplicationDateRangeKpiResponseTypeDef(TypedDict):
    ApplicationDateRangeKpiResponse: "ApplicationDateRangeKpiResponseTypeDef"


class GetApplicationSettingsResponseTypeDef(TypedDict):
    ApplicationSettingsResource: "ApplicationSettingsResourceTypeDef"


class GetAppsResponseTypeDef(TypedDict):
    ApplicationsResponse: "ApplicationsResponseTypeDef"


class GetBaiduChannelResponseTypeDef(TypedDict):
    BaiduChannelResponse: "BaiduChannelResponseTypeDef"


class GetCampaignActivitiesResponseTypeDef(TypedDict):
    ActivitiesResponse: "ActivitiesResponseTypeDef"


class GetCampaignDateRangeKpiResponseTypeDef(TypedDict):
    CampaignDateRangeKpiResponse: "CampaignDateRangeKpiResponseTypeDef"


class GetCampaignResponseTypeDef(TypedDict):
    CampaignResponse: "CampaignResponseTypeDef"


class GetCampaignVersionResponseTypeDef(TypedDict):
    CampaignResponse: "CampaignResponseTypeDef"


class GetCampaignVersionsResponseTypeDef(TypedDict):
    CampaignsResponse: "CampaignsResponseTypeDef"


class GetCampaignsResponseTypeDef(TypedDict):
    CampaignsResponse: "CampaignsResponseTypeDef"


class GetChannelsResponseTypeDef(TypedDict):
    ChannelsResponse: "ChannelsResponseTypeDef"


class GetEmailChannelResponseTypeDef(TypedDict):
    EmailChannelResponse: "EmailChannelResponseTypeDef"


class GetEmailTemplateResponseTypeDef(TypedDict):
    EmailTemplateResponse: "EmailTemplateResponseTypeDef"


class GetEndpointResponseTypeDef(TypedDict):
    EndpointResponse: "EndpointResponseTypeDef"


class GetEventStreamResponseTypeDef(TypedDict):
    EventStream: "EventStreamTypeDef"


class GetExportJobResponseTypeDef(TypedDict):
    ExportJobResponse: "ExportJobResponseTypeDef"


class GetExportJobsResponseTypeDef(TypedDict):
    ExportJobsResponse: "ExportJobsResponseTypeDef"


class GetGcmChannelResponseTypeDef(TypedDict):
    GCMChannelResponse: "GCMChannelResponseTypeDef"


class GetImportJobResponseTypeDef(TypedDict):
    ImportJobResponse: "ImportJobResponseTypeDef"


class GetImportJobsResponseTypeDef(TypedDict):
    ImportJobsResponse: "ImportJobsResponseTypeDef"


class GetJourneyDateRangeKpiResponseTypeDef(TypedDict):
    JourneyDateRangeKpiResponse: "JourneyDateRangeKpiResponseTypeDef"


class GetJourneyExecutionActivityMetricsResponseTypeDef(TypedDict):
    JourneyExecutionActivityMetricsResponse: "JourneyExecutionActivityMetricsResponseTypeDef"


class GetJourneyExecutionMetricsResponseTypeDef(TypedDict):
    JourneyExecutionMetricsResponse: "JourneyExecutionMetricsResponseTypeDef"


class GetJourneyResponseTypeDef(TypedDict):
    JourneyResponse: "JourneyResponseTypeDef"


class GetPushTemplateResponseTypeDef(TypedDict):
    PushNotificationTemplateResponse: "PushNotificationTemplateResponseTypeDef"


class GetRecommenderConfigurationResponseTypeDef(TypedDict):
    RecommenderConfigurationResponse: "RecommenderConfigurationResponseTypeDef"


class GetRecommenderConfigurationsResponseTypeDef(TypedDict):
    ListRecommenderConfigurationsResponse: "ListRecommenderConfigurationsResponseTypeDef"


class GetSegmentExportJobsResponseTypeDef(TypedDict):
    ExportJobsResponse: "ExportJobsResponseTypeDef"


class GetSegmentImportJobsResponseTypeDef(TypedDict):
    ImportJobsResponse: "ImportJobsResponseTypeDef"


class GetSegmentResponseTypeDef(TypedDict):
    SegmentResponse: "SegmentResponseTypeDef"


class GetSegmentVersionResponseTypeDef(TypedDict):
    SegmentResponse: "SegmentResponseTypeDef"


class GetSegmentVersionsResponseTypeDef(TypedDict):
    SegmentsResponse: "SegmentsResponseTypeDef"


class GetSegmentsResponseTypeDef(TypedDict):
    SegmentsResponse: "SegmentsResponseTypeDef"


class GetSmsChannelResponseTypeDef(TypedDict):
    SMSChannelResponse: "SMSChannelResponseTypeDef"


class GetSmsTemplateResponseTypeDef(TypedDict):
    SMSTemplateResponse: "SMSTemplateResponseTypeDef"


class GetUserEndpointsResponseTypeDef(TypedDict):
    EndpointsResponse: "EndpointsResponseTypeDef"


class GetVoiceChannelResponseTypeDef(TypedDict):
    VoiceChannelResponse: "VoiceChannelResponseTypeDef"


class GetVoiceTemplateResponseTypeDef(TypedDict):
    VoiceTemplateResponse: "VoiceTemplateResponseTypeDef"


class _RequiredHoldoutActivityTypeDef(TypedDict):
    Percentage: int


class HoldoutActivityTypeDef(_RequiredHoldoutActivityTypeDef, total=False):
    NextActivity: str


class _RequiredImportJobRequestTypeDef(TypedDict):
    Format: Format
    RoleArn: str
    S3Url: str


class ImportJobRequestTypeDef(_RequiredImportJobRequestTypeDef, total=False):
    DefineSegment: bool
    ExternalId: str
    RegisterEndpoints: bool
    SegmentId: str
    SegmentName: str


class _RequiredImportJobResourceTypeDef(TypedDict):
    Format: Format
    RoleArn: str
    S3Url: str


class ImportJobResourceTypeDef(_RequiredImportJobResourceTypeDef, total=False):
    DefineSegment: bool
    ExternalId: str
    RegisterEndpoints: bool
    SegmentId: str
    SegmentName: str


_RequiredImportJobResponseTypeDef = TypedDict(
    "_RequiredImportJobResponseTypeDef",
    {
        "ApplicationId": str,
        "CreationDate": str,
        "Definition": "ImportJobResourceTypeDef",
        "Id": str,
        "JobStatus": JobStatus,
        "Type": str,
    },
)
_OptionalImportJobResponseTypeDef = TypedDict(
    "_OptionalImportJobResponseTypeDef",
    {
        "CompletedPieces": int,
        "CompletionDate": str,
        "FailedPieces": int,
        "Failures": List[str],
        "TotalFailures": int,
        "TotalPieces": int,
        "TotalProcessed": int,
    },
    total=False,
)


class ImportJobResponseTypeDef(
    _RequiredImportJobResponseTypeDef, _OptionalImportJobResponseTypeDef
):
    pass


class _RequiredImportJobsResponseTypeDef(TypedDict):
    Item: List["ImportJobResponseTypeDef"]


class ImportJobsResponseTypeDef(_RequiredImportJobsResponseTypeDef, total=False):
    NextToken: str


class ItemResponseTypeDef(TypedDict, total=False):
    EndpointItemResponse: "EndpointItemResponseTypeDef"
    EventsItemResponse: Dict[str, "EventItemResponseTypeDef"]


class JourneyCustomMessageTypeDef(TypedDict, total=False):
    Data: str


class _RequiredJourneyDateRangeKpiResponseTypeDef(TypedDict):
    ApplicationId: str
    EndTime: datetime
    JourneyId: str
    KpiName: str
    KpiResult: "BaseKpiResultTypeDef"
    StartTime: datetime


class JourneyDateRangeKpiResponseTypeDef(_RequiredJourneyDateRangeKpiResponseTypeDef, total=False):
    NextToken: str


class JourneyEmailMessageTypeDef(TypedDict, total=False):
    FromAddress: str


class JourneyExecutionActivityMetricsResponseTypeDef(TypedDict):
    ActivityType: str
    ApplicationId: str
    JourneyActivityId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class JourneyExecutionMetricsResponseTypeDef(TypedDict):
    ApplicationId: str
    JourneyId: str
    LastEvaluatedTime: str
    Metrics: Dict[str, str]


class JourneyLimitsTypeDef(TypedDict, total=False):
    DailyCap: int
    EndpointReentryCap: int
    MessagesPerSecond: int
    EndpointReentryInterval: str


class JourneyPushMessageTypeDef(TypedDict, total=False):
    TimeToLive: str


class _RequiredJourneyResponseTypeDef(TypedDict):
    ApplicationId: str
    Id: str
    Name: str


class JourneyResponseTypeDef(_RequiredJourneyResponseTypeDef, total=False):
    Activities: Dict[str, "ActivityTypeDef"]
    CreationDate: str
    LastModifiedDate: str
    Limits: "JourneyLimitsTypeDef"
    LocalTime: bool
    QuietTime: "QuietTimeTypeDef"
    RefreshFrequency: str
    Schedule: "JourneyScheduleTypeDef"
    StartActivity: str
    StartCondition: "StartConditionTypeDef"
    State: State
    tags: Dict[str, str]
    WaitForQuietTime: bool
    RefreshOnSegmentUpdate: bool


class JourneySMSMessageTypeDef(TypedDict, total=False):
    MessageType: MessageType
    OriginationNumber: str
    SenderId: str
    EntityId: str
    TemplateId: str


class JourneyScheduleTypeDef(TypedDict, total=False):
    EndTime: datetime
    StartTime: datetime
    Timezone: str


class JourneyStateRequestTypeDef(TypedDict, total=False):
    State: State


class _RequiredJourneysResponseTypeDef(TypedDict):
    Item: List["JourneyResponseTypeDef"]


class JourneysResponseTypeDef(_RequiredJourneysResponseTypeDef, total=False):
    NextToken: str


class ListJourneysResponseTypeDef(TypedDict):
    JourneysResponse: "JourneysResponseTypeDef"


class _RequiredListRecommenderConfigurationsResponseTypeDef(TypedDict):
    Item: List["RecommenderConfigurationResponseTypeDef"]


class ListRecommenderConfigurationsResponseTypeDef(
    _RequiredListRecommenderConfigurationsResponseTypeDef, total=False
):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict):
    TagsModel: "TagsModelTypeDef"


class ListTemplateVersionsResponseTypeDef(TypedDict):
    TemplateVersionsResponse: "TemplateVersionsResponseTypeDef"


class ListTemplatesResponseTypeDef(TypedDict):
    TemplatesResponse: "TemplatesResponseTypeDef"


class MessageBodyTypeDef(TypedDict, total=False):
    Message: str
    RequestID: str


class MessageConfigurationTypeDef(TypedDict, total=False):
    ADMMessage: "MessageTypeDef"
    APNSMessage: "MessageTypeDef"
    BaiduMessage: "MessageTypeDef"
    CustomMessage: "CampaignCustomMessageTypeDef"
    DefaultMessage: "MessageTypeDef"
    EmailMessage: "CampaignEmailMessageTypeDef"
    GCMMessage: "MessageTypeDef"
    SMSMessage: "CampaignSmsMessageTypeDef"


class _RequiredMessageRequestTypeDef(TypedDict):
    MessageConfiguration: "DirectMessageConfigurationTypeDef"


class MessageRequestTypeDef(_RequiredMessageRequestTypeDef, total=False):
    Addresses: Dict[str, "AddressConfigurationTypeDef"]
    Context: Dict[str, str]
    Endpoints: Dict[str, "EndpointSendConfigurationTypeDef"]
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TraceId: str


class _RequiredMessageResponseTypeDef(TypedDict):
    ApplicationId: str


class MessageResponseTypeDef(_RequiredMessageResponseTypeDef, total=False):
    EndpointResult: Dict[str, "EndpointMessageResultTypeDef"]
    RequestId: str
    Result: Dict[str, "MessageResultTypeDef"]


class _RequiredMessageResultTypeDef(TypedDict):
    DeliveryStatus: DeliveryStatus
    StatusCode: int


class MessageResultTypeDef(_RequiredMessageResultTypeDef, total=False):
    MessageId: str
    StatusMessage: str
    UpdatedToken: str


class MessageTypeDef(TypedDict, total=False):
    Action: Action
    Body: str
    ImageIconUrl: str
    ImageSmallIconUrl: str
    ImageUrl: str
    JsonBody: str
    MediaUrl: str
    RawContent: str
    SilentPush: bool
    TimeToLive: int
    Title: str
    Url: str


class MetricDimensionTypeDef(TypedDict):
    ComparisonOperator: str
    Value: float


class MultiConditionalBranchTypeDef(TypedDict, total=False):
    Condition: "SimpleConditionTypeDef"
    NextActivity: str


class MultiConditionalSplitActivityTypeDef(TypedDict, total=False):
    Branches: List["MultiConditionalBranchTypeDef"]
    DefaultActivity: str
    EvaluationWaitTime: "WaitTimeTypeDef"


class NumberValidateRequestTypeDef(TypedDict, total=False):
    IsoCountryCode: str
    PhoneNumber: str


class NumberValidateResponseTypeDef(TypedDict, total=False):
    Carrier: str
    City: str
    CleansedPhoneNumberE164: str
    CleansedPhoneNumberNational: str
    Country: str
    CountryCodeIso2: str
    CountryCodeNumeric: str
    County: str
    OriginalCountryCodeIso2: str
    OriginalPhoneNumber: str
    PhoneType: str
    PhoneTypeCode: int
    Timezone: str
    ZipCode: str


class PhoneNumberValidateResponseTypeDef(TypedDict):
    NumberValidateResponse: "NumberValidateResponseTypeDef"


class PublicEndpointTypeDef(TypedDict, total=False):
    Address: str
    Attributes: Dict[str, List[str]]
    ChannelType: ChannelType
    Demographic: "EndpointDemographicTypeDef"
    EffectiveDate: str
    EndpointStatus: str
    Location: "EndpointLocationTypeDef"
    Metrics: Dict[str, float]
    OptOut: str
    RequestId: str
    User: "EndpointUserTypeDef"


class PushMessageActivityTypeDef(TypedDict, total=False):
    MessageConfig: "JourneyPushMessageTypeDef"
    NextActivity: str
    TemplateName: str
    TemplateVersion: str


class PushNotificationTemplateRequestTypeDef(TypedDict, total=False):
    ADM: "AndroidPushNotificationTemplateTypeDef"
    APNS: "APNSPushNotificationTemplateTypeDef"
    Baidu: "AndroidPushNotificationTemplateTypeDef"
    Default: "DefaultPushNotificationTemplateTypeDef"
    DefaultSubstitutions: str
    GCM: "AndroidPushNotificationTemplateTypeDef"
    RecommenderId: str
    tags: Dict[str, str]
    TemplateDescription: str


class _RequiredPushNotificationTemplateResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateType


class PushNotificationTemplateResponseTypeDef(
    _RequiredPushNotificationTemplateResponseTypeDef, total=False
):
    ADM: "AndroidPushNotificationTemplateTypeDef"
    APNS: "APNSPushNotificationTemplateTypeDef"
    Arn: str
    Baidu: "AndroidPushNotificationTemplateTypeDef"
    Default: "DefaultPushNotificationTemplateTypeDef"
    DefaultSubstitutions: str
    GCM: "AndroidPushNotificationTemplateTypeDef"
    RecommenderId: str
    tags: Dict[str, str]
    TemplateDescription: str
    Version: str


class PutEventStreamResponseTypeDef(TypedDict):
    EventStream: "EventStreamTypeDef"


class PutEventsResponseTypeDef(TypedDict):
    EventsResponse: "EventsResponseTypeDef"


class QuietTimeTypeDef(TypedDict, total=False):
    End: str
    Start: str


class RandomSplitActivityTypeDef(TypedDict, total=False):
    Branches: List["RandomSplitEntryTypeDef"]


class RandomSplitEntryTypeDef(TypedDict, total=False):
    NextActivity: str
    Percentage: int


class RawEmailTypeDef(TypedDict, total=False):
    Data: Union[bytes, IO[bytes]]


class RecencyDimensionTypeDef(TypedDict):
    Duration: Duration
    RecencyType: RecencyType


class _RequiredRecommenderConfigurationResponseTypeDef(TypedDict):
    CreationDate: str
    Id: str
    LastModifiedDate: str
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str


class RecommenderConfigurationResponseTypeDef(
    _RequiredRecommenderConfigurationResponseTypeDef, total=False
):
    Attributes: Dict[str, str]
    Description: str
    Name: str
    RecommendationProviderIdType: str
    RecommendationTransformerUri: str
    RecommendationsDisplayName: str
    RecommendationsPerMessage: int


class RemoveAttributesResponseTypeDef(TypedDict):
    AttributesResource: "AttributesResourceTypeDef"


class ResultRowTypeDef(TypedDict):
    GroupedBys: List["ResultRowValueTypeDef"]
    Values: List["ResultRowValueTypeDef"]


ResultRowValueTypeDef = TypedDict("ResultRowValueTypeDef", {"Key": str, "Type": str, "Value": str})


class SMSChannelRequestTypeDef(TypedDict, total=False):
    Enabled: bool
    SenderId: str
    ShortCode: str


class _RequiredSMSChannelResponseTypeDef(TypedDict):
    Platform: str


class SMSChannelResponseTypeDef(_RequiredSMSChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    PromotionalMessagesPerSecond: int
    SenderId: str
    ShortCode: str
    TransactionalMessagesPerSecond: int
    Version: int


class SMSMessageActivityTypeDef(TypedDict, total=False):
    MessageConfig: "JourneySMSMessageTypeDef"
    NextActivity: str
    TemplateName: str
    TemplateVersion: str


class SMSMessageTypeDef(TypedDict, total=False):
    Body: str
    Keyword: str
    MediaUrl: str
    MessageType: MessageType
    OriginationNumber: str
    SenderId: str
    Substitutions: Dict[str, List[str]]
    EntityId: str
    TemplateId: str


class SMSTemplateRequestTypeDef(TypedDict, total=False):
    Body: str
    DefaultSubstitutions: str
    RecommenderId: str
    tags: Dict[str, str]
    TemplateDescription: str


class _RequiredSMSTemplateResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateType


class SMSTemplateResponseTypeDef(_RequiredSMSTemplateResponseTypeDef, total=False):
    Arn: str
    Body: str
    DefaultSubstitutions: str
    RecommenderId: str
    tags: Dict[str, str]
    TemplateDescription: str
    Version: str


class _RequiredScheduleTypeDef(TypedDict):
    StartTime: str


class ScheduleTypeDef(_RequiredScheduleTypeDef, total=False):
    EndTime: str
    EventFilter: "CampaignEventFilterTypeDef"
    Frequency: Frequency
    IsLocalTime: bool
    QuietTime: "QuietTimeTypeDef"
    Timezone: str


class SegmentBehaviorsTypeDef(TypedDict, total=False):
    Recency: "RecencyDimensionTypeDef"


class SegmentConditionTypeDef(TypedDict):
    SegmentId: str


class SegmentDemographicsTypeDef(TypedDict, total=False):
    AppVersion: "SetDimensionTypeDef"
    Channel: "SetDimensionTypeDef"
    DeviceType: "SetDimensionTypeDef"
    Make: "SetDimensionTypeDef"
    Model: "SetDimensionTypeDef"
    Platform: "SetDimensionTypeDef"


class SegmentDimensionsTypeDef(TypedDict, total=False):
    Attributes: Dict[str, "AttributeDimensionTypeDef"]
    Behavior: "SegmentBehaviorsTypeDef"
    Demographic: "SegmentDemographicsTypeDef"
    Location: "SegmentLocationTypeDef"
    Metrics: Dict[str, "MetricDimensionTypeDef"]
    UserAttributes: Dict[str, "AttributeDimensionTypeDef"]


class SegmentGroupListTypeDef(TypedDict, total=False):
    Groups: List["SegmentGroupTypeDef"]
    Include: Include


SegmentGroupTypeDef = TypedDict(
    "SegmentGroupTypeDef",
    {
        "Dimensions": List["SegmentDimensionsTypeDef"],
        "SourceSegments": List["SegmentReferenceTypeDef"],
        "SourceType": SourceType,
        "Type": TypeType,
    },
    total=False,
)


class _RequiredSegmentImportResourceTypeDef(TypedDict):
    ExternalId: str
    Format: Format
    RoleArn: str
    S3Url: str
    Size: int


class SegmentImportResourceTypeDef(_RequiredSegmentImportResourceTypeDef, total=False):
    ChannelCounts: Dict[str, int]


class SegmentLocationTypeDef(TypedDict, total=False):
    Country: "SetDimensionTypeDef"
    GPSPoint: "GPSPointDimensionTypeDef"


class _RequiredSegmentReferenceTypeDef(TypedDict):
    Id: str


class SegmentReferenceTypeDef(_RequiredSegmentReferenceTypeDef, total=False):
    Version: int


class _RequiredSegmentResponseTypeDef(TypedDict):
    ApplicationId: str
    Arn: str
    CreationDate: str
    Id: str
    SegmentType: SegmentType


class SegmentResponseTypeDef(_RequiredSegmentResponseTypeDef, total=False):
    Dimensions: "SegmentDimensionsTypeDef"
    ImportDefinition: "SegmentImportResourceTypeDef"
    LastModifiedDate: str
    Name: str
    SegmentGroups: "SegmentGroupListTypeDef"
    tags: Dict[str, str]
    Version: int


class _RequiredSegmentsResponseTypeDef(TypedDict):
    Item: List["SegmentResponseTypeDef"]


class SegmentsResponseTypeDef(_RequiredSegmentsResponseTypeDef, total=False):
    NextToken: str


class SendMessagesResponseTypeDef(TypedDict):
    MessageResponse: "MessageResponseTypeDef"


class _RequiredSendUsersMessageRequestTypeDef(TypedDict):
    MessageConfiguration: "DirectMessageConfigurationTypeDef"
    Users: Dict[str, "EndpointSendConfigurationTypeDef"]


class SendUsersMessageRequestTypeDef(_RequiredSendUsersMessageRequestTypeDef, total=False):
    Context: Dict[str, str]
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TraceId: str


class _RequiredSendUsersMessageResponseTypeDef(TypedDict):
    ApplicationId: str


class SendUsersMessageResponseTypeDef(_RequiredSendUsersMessageResponseTypeDef, total=False):
    RequestId: str
    Result: Dict[str, Dict[str, "EndpointMessageResultTypeDef"]]


class SendUsersMessagesResponseTypeDef(TypedDict):
    SendUsersMessageResponse: "SendUsersMessageResponseTypeDef"


class _RequiredSessionTypeDef(TypedDict):
    Id: str
    StartTimestamp: str


class SessionTypeDef(_RequiredSessionTypeDef, total=False):
    Duration: int
    StopTimestamp: str


class _RequiredSetDimensionTypeDef(TypedDict):
    Values: List[str]


class SetDimensionTypeDef(_RequiredSetDimensionTypeDef, total=False):
    DimensionType: DimensionType


class SimpleConditionTypeDef(TypedDict, total=False):
    EventCondition: "EventConditionTypeDef"
    SegmentCondition: "SegmentConditionTypeDef"
    SegmentDimensions: "SegmentDimensionsTypeDef"


class SimpleEmailPartTypeDef(TypedDict, total=False):
    Charset: str
    Data: str


class SimpleEmailTypeDef(TypedDict, total=False):
    HtmlPart: "SimpleEmailPartTypeDef"
    Subject: "SimpleEmailPartTypeDef"
    TextPart: "SimpleEmailPartTypeDef"


class StartConditionTypeDef(TypedDict, total=False):
    Description: str
    EventStartCondition: "EventStartConditionTypeDef"
    SegmentStartCondition: "SegmentConditionTypeDef"


class TagsModelTypeDef(TypedDict):
    tags: Dict[str, str]


class TemplateActiveVersionRequestTypeDef(TypedDict, total=False):
    Version: str


class TemplateConfigurationTypeDef(TypedDict, total=False):
    EmailTemplate: "TemplateTypeDef"
    PushTemplate: "TemplateTypeDef"
    SMSTemplate: "TemplateTypeDef"
    VoiceTemplate: "TemplateTypeDef"


class _RequiredTemplateResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateType


class TemplateResponseTypeDef(_RequiredTemplateResponseTypeDef, total=False):
    Arn: str
    DefaultSubstitutions: str
    tags: Dict[str, str]
    TemplateDescription: str
    Version: str


class TemplateTypeDef(TypedDict, total=False):
    Name: str
    Version: str


class _RequiredTemplateVersionResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: str


class TemplateVersionResponseTypeDef(_RequiredTemplateVersionResponseTypeDef, total=False):
    DefaultSubstitutions: str
    TemplateDescription: str
    Version: str


class _RequiredTemplateVersionsResponseTypeDef(TypedDict):
    Item: List["TemplateVersionResponseTypeDef"]


class TemplateVersionsResponseTypeDef(_RequiredTemplateVersionsResponseTypeDef, total=False):
    Message: str
    NextToken: str
    RequestID: str


class _RequiredTemplatesResponseTypeDef(TypedDict):
    Item: List["TemplateResponseTypeDef"]


class TemplatesResponseTypeDef(_RequiredTemplatesResponseTypeDef, total=False):
    NextToken: str


class _RequiredTreatmentResourceTypeDef(TypedDict):
    Id: str
    SizePercent: int


class TreatmentResourceTypeDef(_RequiredTreatmentResourceTypeDef, total=False):
    CustomDeliveryConfiguration: "CustomDeliveryConfigurationTypeDef"
    MessageConfiguration: "MessageConfigurationTypeDef"
    Schedule: "ScheduleTypeDef"
    State: "CampaignStateTypeDef"
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TreatmentDescription: str
    TreatmentName: str


class UpdateAdmChannelResponseTypeDef(TypedDict):
    ADMChannelResponse: "ADMChannelResponseTypeDef"


class UpdateApnsChannelResponseTypeDef(TypedDict):
    APNSChannelResponse: "APNSChannelResponseTypeDef"


class UpdateApnsSandboxChannelResponseTypeDef(TypedDict):
    APNSSandboxChannelResponse: "APNSSandboxChannelResponseTypeDef"


class UpdateApnsVoipChannelResponseTypeDef(TypedDict):
    APNSVoipChannelResponse: "APNSVoipChannelResponseTypeDef"


class UpdateApnsVoipSandboxChannelResponseTypeDef(TypedDict):
    APNSVoipSandboxChannelResponse: "APNSVoipSandboxChannelResponseTypeDef"


class UpdateApplicationSettingsResponseTypeDef(TypedDict):
    ApplicationSettingsResource: "ApplicationSettingsResourceTypeDef"


class UpdateAttributesRequestTypeDef(TypedDict, total=False):
    Blacklist: List[str]


class UpdateBaiduChannelResponseTypeDef(TypedDict):
    BaiduChannelResponse: "BaiduChannelResponseTypeDef"


class UpdateCampaignResponseTypeDef(TypedDict):
    CampaignResponse: "CampaignResponseTypeDef"


class UpdateEmailChannelResponseTypeDef(TypedDict):
    EmailChannelResponse: "EmailChannelResponseTypeDef"


class UpdateEmailTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateEndpointResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateEndpointsBatchResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateGcmChannelResponseTypeDef(TypedDict):
    GCMChannelResponse: "GCMChannelResponseTypeDef"


class UpdateJourneyResponseTypeDef(TypedDict):
    JourneyResponse: "JourneyResponseTypeDef"


class UpdateJourneyStateResponseTypeDef(TypedDict):
    JourneyResponse: "JourneyResponseTypeDef"


class UpdatePushTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateRecommenderConfigurationResponseTypeDef(TypedDict):
    RecommenderConfigurationResponse: "RecommenderConfigurationResponseTypeDef"


class _RequiredUpdateRecommenderConfigurationTypeDef(TypedDict):
    RecommendationProviderRoleArn: str
    RecommendationProviderUri: str


class UpdateRecommenderConfigurationTypeDef(
    _RequiredUpdateRecommenderConfigurationTypeDef, total=False
):
    Attributes: Dict[str, str]
    Description: str
    Name: str
    RecommendationProviderIdType: str
    RecommendationTransformerUri: str
    RecommendationsDisplayName: str
    RecommendationsPerMessage: int


class UpdateSegmentResponseTypeDef(TypedDict):
    SegmentResponse: "SegmentResponseTypeDef"


class UpdateSmsChannelResponseTypeDef(TypedDict):
    SMSChannelResponse: "SMSChannelResponseTypeDef"


class UpdateSmsTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateTemplateActiveVersionResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class UpdateVoiceChannelResponseTypeDef(TypedDict):
    VoiceChannelResponse: "VoiceChannelResponseTypeDef"


class UpdateVoiceTemplateResponseTypeDef(TypedDict):
    MessageBody: "MessageBodyTypeDef"


class VoiceChannelRequestTypeDef(TypedDict, total=False):
    Enabled: bool


class _RequiredVoiceChannelResponseTypeDef(TypedDict):
    Platform: str


class VoiceChannelResponseTypeDef(_RequiredVoiceChannelResponseTypeDef, total=False):
    ApplicationId: str
    CreationDate: str
    Enabled: bool
    HasCredential: bool
    Id: str
    IsArchived: bool
    LastModifiedBy: str
    LastModifiedDate: str
    Version: int


class VoiceMessageTypeDef(TypedDict, total=False):
    Body: str
    LanguageCode: str
    OriginationNumber: str
    Substitutions: Dict[str, List[str]]
    VoiceId: str


class VoiceTemplateRequestTypeDef(TypedDict, total=False):
    Body: str
    DefaultSubstitutions: str
    LanguageCode: str
    tags: Dict[str, str]
    TemplateDescription: str
    VoiceId: str


class _RequiredVoiceTemplateResponseTypeDef(TypedDict):
    CreationDate: str
    LastModifiedDate: str
    TemplateName: str
    TemplateType: TemplateType


class VoiceTemplateResponseTypeDef(_RequiredVoiceTemplateResponseTypeDef, total=False):
    Arn: str
    Body: str
    DefaultSubstitutions: str
    LanguageCode: str
    tags: Dict[str, str]
    TemplateDescription: str
    Version: str
    VoiceId: str


class WaitActivityTypeDef(TypedDict, total=False):
    NextActivity: str
    WaitTime: "WaitTimeTypeDef"


class WaitTimeTypeDef(TypedDict, total=False):
    WaitFor: str
    WaitUntil: str


class WriteApplicationSettingsRequestTypeDef(TypedDict, total=False):
    CampaignHook: "CampaignHookTypeDef"
    CloudWatchMetricsEnabled: bool
    EventTaggingEnabled: bool
    Limits: "CampaignLimitsTypeDef"
    QuietTime: "QuietTimeTypeDef"


class WriteCampaignRequestTypeDef(TypedDict, total=False):
    AdditionalTreatments: List["WriteTreatmentResourceTypeDef"]
    CustomDeliveryConfiguration: "CustomDeliveryConfigurationTypeDef"
    Description: str
    HoldoutPercent: int
    Hook: "CampaignHookTypeDef"
    IsPaused: bool
    Limits: "CampaignLimitsTypeDef"
    MessageConfiguration: "MessageConfigurationTypeDef"
    Name: str
    Schedule: "ScheduleTypeDef"
    SegmentId: str
    SegmentVersion: int
    tags: Dict[str, str]
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TreatmentDescription: str
    TreatmentName: str


class WriteEventStreamTypeDef(TypedDict):
    DestinationStreamArn: str
    RoleArn: str


class _RequiredWriteJourneyRequestTypeDef(TypedDict):
    Name: str


class WriteJourneyRequestTypeDef(_RequiredWriteJourneyRequestTypeDef, total=False):
    Activities: Dict[str, "ActivityTypeDef"]
    CreationDate: str
    LastModifiedDate: str
    Limits: "JourneyLimitsTypeDef"
    LocalTime: bool
    QuietTime: "QuietTimeTypeDef"
    RefreshFrequency: str
    Schedule: "JourneyScheduleTypeDef"
    StartActivity: str
    StartCondition: "StartConditionTypeDef"
    State: State
    WaitForQuietTime: bool
    RefreshOnSegmentUpdate: bool


class WriteSegmentRequestTypeDef(TypedDict, total=False):
    Dimensions: "SegmentDimensionsTypeDef"
    Name: str
    SegmentGroups: "SegmentGroupListTypeDef"
    tags: Dict[str, str]


class _RequiredWriteTreatmentResourceTypeDef(TypedDict):
    SizePercent: int


class WriteTreatmentResourceTypeDef(_RequiredWriteTreatmentResourceTypeDef, total=False):
    CustomDeliveryConfiguration: "CustomDeliveryConfigurationTypeDef"
    MessageConfiguration: "MessageConfigurationTypeDef"
    Schedule: "ScheduleTypeDef"
    TemplateConfiguration: "TemplateConfigurationTypeDef"
    TreatmentDescription: str
    TreatmentName: str
