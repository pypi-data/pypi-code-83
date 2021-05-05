"""
Type annotations for sesv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sesv2.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_sesv2.literals import (
    BehaviorOnMxFailure,
    BulkEmailStatus,
    ContactLanguage,
    ContactListImportAction,
    DataFormat,
    DeliverabilityDashboardAccountStatus,
    DeliverabilityTestStatus,
    DimensionValueSource,
    DkimSigningAttributesOrigin,
    DkimStatus,
    EventType,
    IdentityType,
    JobStatus,
    MailFromDomainStatus,
    MailType,
    ReviewStatus,
    SubscriptionStatus,
    SuppressionListImportAction,
    SuppressionListReason,
    TlsPolicy,
    WarmupStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountDetailsTypeDef",
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "BulkEmailContentTypeDef",
    "BulkEmailEntryResultTypeDef",
    "BulkEmailEntryTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "CreateImportJobResponseTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DkimSigningAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EmailTemplateContentTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "FailureInfoTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetContactListResponseTypeDef",
    "GetContactResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityPoliciesResponseTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "GetSuppressedDestinationResponseTypeDef",
    "IdentityInfoTypeDef",
    "ImportDataSourceTypeDef",
    "ImportDestinationTypeDef",
    "ImportJobSummaryTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListContactListsResponseTypeDef",
    "ListContactsFilterTypeDef",
    "ListContactsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListEmailTemplatesResponseTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListManagementOptionsTypeDef",
    "ListSuppressedDestinationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "RawMessageTypeDef",
    "ReplacementEmailContentTypeDef",
    "ReplacementTemplateTypeDef",
    "ReputationOptionsTypeDef",
    "ReviewDetailsTypeDef",
    "SendBulkEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "SuppressedDestinationTypeDef",
    "SuppressionAttributesTypeDef",
    "SuppressionListDestinationTypeDef",
    "SuppressionOptionsTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TestRenderEmailTemplateResponseTypeDef",
    "TopicFilterTypeDef",
    "TopicPreferenceTypeDef",
    "TopicTypeDef",
    "TrackingOptionsTypeDef",
    "VolumeStatisticsTypeDef",
)


class AccountDetailsTypeDef(TypedDict, total=False):
    MailType: MailType
    WebsiteURL: str
    ContactLanguage: ContactLanguage
    UseCaseDescription: str
    AdditionalContactEmailAddresses: List[str]
    ReviewDetails: "ReviewDetailsTypeDef"


class BlacklistEntryTypeDef(TypedDict, total=False):
    RblName: str
    ListingTime: datetime
    Description: str


BodyTypeDef = TypedDict(
    "BodyTypeDef", {"Text": "ContentTypeDef", "Html": "ContentTypeDef"}, total=False
)


class BulkEmailContentTypeDef(TypedDict, total=False):
    Template: "TemplateTypeDef"


class BulkEmailEntryResultTypeDef(TypedDict, total=False):
    Status: BulkEmailStatus
    Error: str
    MessageId: str


class _RequiredBulkEmailEntryTypeDef(TypedDict):
    Destination: "DestinationTypeDef"


class BulkEmailEntryTypeDef(_RequiredBulkEmailEntryTypeDef, total=False):
    ReplacementTags: List["MessageTagTypeDef"]
    ReplacementEmailContent: "ReplacementEmailContentTypeDef"


class CloudWatchDestinationTypeDef(TypedDict):
    DimensionConfigurations: List["CloudWatchDimensionConfigurationTypeDef"]


class CloudWatchDimensionConfigurationTypeDef(TypedDict):
    DimensionName: str
    DimensionValueSource: DimensionValueSource
    DefaultDimensionValue: str


class ContactListDestinationTypeDef(TypedDict):
    ContactListName: str
    ContactListImportAction: ContactListImportAction


class ContactListTypeDef(TypedDict, total=False):
    ContactListName: str
    LastUpdatedTimestamp: datetime


class ContactTypeDef(TypedDict, total=False):
    EmailAddress: str
    TopicPreferences: List["TopicPreferenceTypeDef"]
    TopicDefaultPreferences: List["TopicPreferenceTypeDef"]
    UnsubscribeAll: bool
    LastUpdatedTimestamp: datetime


class _RequiredContentTypeDef(TypedDict):
    Data: str


class ContentTypeDef(_RequiredContentTypeDef, total=False):
    Charset: str


class CreateDeliverabilityTestReportResponseTypeDef(TypedDict):
    ReportId: str
    DeliverabilityTestStatus: DeliverabilityTestStatus


class CreateEmailIdentityResponseTypeDef(TypedDict, total=False):
    IdentityType: IdentityType
    VerifiedForSendingStatus: bool
    DkimAttributes: "DkimAttributesTypeDef"


class CreateImportJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class CustomVerificationEmailTemplateMetadataTypeDef(TypedDict, total=False):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class DailyVolumeTypeDef(TypedDict, total=False):
    StartDate: datetime
    VolumeStatistics: "VolumeStatisticsTypeDef"
    DomainIspPlacements: List["DomainIspPlacementTypeDef"]


class _RequiredDedicatedIpTypeDef(TypedDict):
    Ip: str
    WarmupStatus: WarmupStatus
    WarmupPercentage: int


class DedicatedIpTypeDef(_RequiredDedicatedIpTypeDef, total=False):
    PoolName: str


class DeliverabilityTestReportTypeDef(TypedDict, total=False):
    ReportId: str
    ReportName: str
    Subject: str
    FromEmailAddress: str
    CreateDate: datetime
    DeliverabilityTestStatus: DeliverabilityTestStatus


class DeliveryOptionsTypeDef(TypedDict, total=False):
    TlsPolicy: TlsPolicy
    SendingPoolName: str


class DestinationTypeDef(TypedDict, total=False):
    ToAddresses: List[str]
    CcAddresses: List[str]
    BccAddresses: List[str]


class DkimAttributesTypeDef(TypedDict, total=False):
    SigningEnabled: bool
    Status: DkimStatus
    Tokens: List[str]
    SigningAttributesOrigin: DkimSigningAttributesOrigin


class DkimSigningAttributesTypeDef(TypedDict):
    DomainSigningSelector: str
    DomainSigningPrivateKey: str


class DomainDeliverabilityCampaignTypeDef(TypedDict, total=False):
    CampaignId: str
    ImageUrl: str
    Subject: str
    FromAddress: str
    SendingIps: List[str]
    FirstSeenDateTime: datetime
    LastSeenDateTime: datetime
    InboxCount: int
    SpamCount: int
    ReadRate: float
    DeleteRate: float
    ReadDeleteRate: float
    ProjectedVolume: int
    Esps: List[str]


class DomainDeliverabilityTrackingOptionTypeDef(TypedDict, total=False):
    Domain: str
    SubscriptionStartDate: datetime
    InboxPlacementTrackingOption: "InboxPlacementTrackingOptionTypeDef"


class DomainIspPlacementTypeDef(TypedDict, total=False):
    IspName: str
    InboxRawCount: int
    SpamRawCount: int
    InboxPercentage: float
    SpamPercentage: float


class EmailContentTypeDef(TypedDict, total=False):
    Simple: "MessageTypeDef"
    Raw: "RawMessageTypeDef"
    Template: "TemplateTypeDef"


EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef", {"Subject": str, "Text": str, "Html": str}, total=False
)


class EmailTemplateMetadataTypeDef(TypedDict, total=False):
    TemplateName: str
    CreatedTimestamp: datetime


class EventDestinationDefinitionTypeDef(TypedDict, total=False):
    Enabled: bool
    MatchingEventTypes: List[EventType]
    KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef"
    CloudWatchDestination: "CloudWatchDestinationTypeDef"
    SnsDestination: "SnsDestinationTypeDef"
    PinpointDestination: "PinpointDestinationTypeDef"


class _RequiredEventDestinationTypeDef(TypedDict):
    Name: str
    MatchingEventTypes: List[EventType]


class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, total=False):
    Enabled: bool
    KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef"
    CloudWatchDestination: "CloudWatchDestinationTypeDef"
    SnsDestination: "SnsDestinationTypeDef"
    PinpointDestination: "PinpointDestinationTypeDef"


class FailureInfoTypeDef(TypedDict, total=False):
    FailedRecordsS3Url: str
    ErrorMessage: str


class GetAccountResponseTypeDef(TypedDict, total=False):
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool
    SendQuota: "SendQuotaTypeDef"
    SendingEnabled: bool
    SuppressionAttributes: "SuppressionAttributesTypeDef"
    Details: "AccountDetailsTypeDef"


class GetBlacklistReportsResponseTypeDef(TypedDict):
    BlacklistReport: Dict[str, List["BlacklistEntryTypeDef"]]


class GetConfigurationSetEventDestinationsResponseTypeDef(TypedDict, total=False):
    EventDestinations: List["EventDestinationTypeDef"]


class GetConfigurationSetResponseTypeDef(TypedDict, total=False):
    ConfigurationSetName: str
    TrackingOptions: "TrackingOptionsTypeDef"
    DeliveryOptions: "DeliveryOptionsTypeDef"
    ReputationOptions: "ReputationOptionsTypeDef"
    SendingOptions: "SendingOptionsTypeDef"
    Tags: List["TagTypeDef"]
    SuppressionOptions: "SuppressionOptionsTypeDef"


class GetContactListResponseTypeDef(TypedDict, total=False):
    ContactListName: str
    Topics: List["TopicTypeDef"]
    Description: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime
    Tags: List["TagTypeDef"]


class GetContactResponseTypeDef(TypedDict, total=False):
    ContactListName: str
    EmailAddress: str
    TopicPreferences: List["TopicPreferenceTypeDef"]
    TopicDefaultPreferences: List["TopicPreferenceTypeDef"]
    UnsubscribeAll: bool
    AttributesData: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime


class GetCustomVerificationEmailTemplateResponseTypeDef(TypedDict, total=False):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class GetDedicatedIpResponseTypeDef(TypedDict, total=False):
    DedicatedIp: "DedicatedIpTypeDef"


class GetDedicatedIpsResponseTypeDef(TypedDict, total=False):
    DedicatedIps: List["DedicatedIpTypeDef"]
    NextToken: str


class _RequiredGetDeliverabilityDashboardOptionsResponseTypeDef(TypedDict):
    DashboardEnabled: bool


class GetDeliverabilityDashboardOptionsResponseTypeDef(
    _RequiredGetDeliverabilityDashboardOptionsResponseTypeDef, total=False
):
    SubscriptionExpiryDate: datetime
    AccountStatus: DeliverabilityDashboardAccountStatus
    ActiveSubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"]
    PendingExpirationSubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"]


class _RequiredGetDeliverabilityTestReportResponseTypeDef(TypedDict):
    DeliverabilityTestReport: "DeliverabilityTestReportTypeDef"
    OverallPlacement: "PlacementStatisticsTypeDef"
    IspPlacements: List["IspPlacementTypeDef"]


class GetDeliverabilityTestReportResponseTypeDef(
    _RequiredGetDeliverabilityTestReportResponseTypeDef, total=False
):
    Message: str
    Tags: List["TagTypeDef"]


class GetDomainDeliverabilityCampaignResponseTypeDef(TypedDict):
    DomainDeliverabilityCampaign: "DomainDeliverabilityCampaignTypeDef"


class GetDomainStatisticsReportResponseTypeDef(TypedDict):
    OverallVolume: "OverallVolumeTypeDef"
    DailyVolumes: List["DailyVolumeTypeDef"]


class GetEmailIdentityPoliciesResponseTypeDef(TypedDict, total=False):
    Policies: Dict[str, str]


class GetEmailIdentityResponseTypeDef(TypedDict, total=False):
    IdentityType: IdentityType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: "DkimAttributesTypeDef"
    MailFromAttributes: "MailFromAttributesTypeDef"
    Policies: Dict[str, str]
    Tags: List["TagTypeDef"]
    ConfigurationSetName: str


class GetEmailTemplateResponseTypeDef(TypedDict):
    TemplateName: str
    TemplateContent: "EmailTemplateContentTypeDef"


class GetImportJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    ImportDestination: "ImportDestinationTypeDef"
    ImportDataSource: "ImportDataSourceTypeDef"
    FailureInfo: "FailureInfoTypeDef"
    JobStatus: JobStatus
    CreatedTimestamp: datetime
    CompletedTimestamp: datetime
    ProcessedRecordsCount: int
    FailedRecordsCount: int


class GetSuppressedDestinationResponseTypeDef(TypedDict):
    SuppressedDestination: "SuppressedDestinationTypeDef"


class IdentityInfoTypeDef(TypedDict, total=False):
    IdentityType: IdentityType
    IdentityName: str
    SendingEnabled: bool


class ImportDataSourceTypeDef(TypedDict):
    S3Url: str
    DataFormat: DataFormat


class ImportDestinationTypeDef(TypedDict, total=False):
    SuppressionListDestination: "SuppressionListDestinationTypeDef"
    ContactListDestination: "ContactListDestinationTypeDef"


class ImportJobSummaryTypeDef(TypedDict, total=False):
    JobId: str
    ImportDestination: "ImportDestinationTypeDef"
    JobStatus: JobStatus
    CreatedTimestamp: datetime


class InboxPlacementTrackingOptionTypeDef(TypedDict, total=False):
    Global: bool
    TrackedIsps: List[str]


class IspPlacementTypeDef(TypedDict, total=False):
    IspName: str
    PlacementStatistics: "PlacementStatisticsTypeDef"


class KinesisFirehoseDestinationTypeDef(TypedDict):
    IamRoleArn: str
    DeliveryStreamArn: str


class ListConfigurationSetsResponseTypeDef(TypedDict, total=False):
    ConfigurationSets: List[str]
    NextToken: str


class ListContactListsResponseTypeDef(TypedDict, total=False):
    ContactLists: List["ContactListTypeDef"]
    NextToken: str


class ListContactsFilterTypeDef(TypedDict, total=False):
    FilteredStatus: SubscriptionStatus
    TopicFilter: "TopicFilterTypeDef"


class ListContactsResponseTypeDef(TypedDict, total=False):
    Contacts: List["ContactTypeDef"]
    NextToken: str


class ListCustomVerificationEmailTemplatesResponseTypeDef(TypedDict, total=False):
    CustomVerificationEmailTemplates: List["CustomVerificationEmailTemplateMetadataTypeDef"]
    NextToken: str


class ListDedicatedIpPoolsResponseTypeDef(TypedDict, total=False):
    DedicatedIpPools: List[str]
    NextToken: str


class _RequiredListDeliverabilityTestReportsResponseTypeDef(TypedDict):
    DeliverabilityTestReports: List["DeliverabilityTestReportTypeDef"]


class ListDeliverabilityTestReportsResponseTypeDef(
    _RequiredListDeliverabilityTestReportsResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListDomainDeliverabilityCampaignsResponseTypeDef(TypedDict):
    DomainDeliverabilityCampaigns: List["DomainDeliverabilityCampaignTypeDef"]


class ListDomainDeliverabilityCampaignsResponseTypeDef(
    _RequiredListDomainDeliverabilityCampaignsResponseTypeDef, total=False
):
    NextToken: str


class ListEmailIdentitiesResponseTypeDef(TypedDict, total=False):
    EmailIdentities: List["IdentityInfoTypeDef"]
    NextToken: str


class ListEmailTemplatesResponseTypeDef(TypedDict, total=False):
    TemplatesMetadata: List["EmailTemplateMetadataTypeDef"]
    NextToken: str


class ListImportJobsResponseTypeDef(TypedDict, total=False):
    ImportJobs: List["ImportJobSummaryTypeDef"]
    NextToken: str


class _RequiredListManagementOptionsTypeDef(TypedDict):
    ContactListName: str


class ListManagementOptionsTypeDef(_RequiredListManagementOptionsTypeDef, total=False):
    TopicName: str


class ListSuppressedDestinationsResponseTypeDef(TypedDict, total=False):
    SuppressedDestinationSummaries: List["SuppressedDestinationSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class MailFromAttributesTypeDef(TypedDict):
    MailFromDomain: str
    MailFromDomainStatus: MailFromDomainStatus
    BehaviorOnMxFailure: BehaviorOnMxFailure


class MessageTagTypeDef(TypedDict):
    Name: str
    Value: str


class MessageTypeDef(TypedDict):
    Subject: "ContentTypeDef"
    Body: "BodyTypeDef"


class OverallVolumeTypeDef(TypedDict, total=False):
    VolumeStatistics: "VolumeStatisticsTypeDef"
    ReadRatePercent: float
    DomainIspPlacements: List["DomainIspPlacementTypeDef"]


class PinpointDestinationTypeDef(TypedDict, total=False):
    ApplicationArn: str


class PlacementStatisticsTypeDef(TypedDict, total=False):
    InboxPercentage: float
    SpamPercentage: float
    MissingPercentage: float
    SpfPercentage: float
    DkimPercentage: float


class PutEmailIdentityDkimSigningAttributesResponseTypeDef(TypedDict, total=False):
    DkimStatus: DkimStatus
    DkimTokens: List[str]


class RawMessageTypeDef(TypedDict):
    Data: Union[bytes, IO[bytes]]


class ReplacementEmailContentTypeDef(TypedDict, total=False):
    ReplacementTemplate: "ReplacementTemplateTypeDef"


class ReplacementTemplateTypeDef(TypedDict, total=False):
    ReplacementTemplateData: str


class ReputationOptionsTypeDef(TypedDict, total=False):
    ReputationMetricsEnabled: bool
    LastFreshStart: datetime


class ReviewDetailsTypeDef(TypedDict, total=False):
    Status: ReviewStatus
    CaseId: str


class SendBulkEmailResponseTypeDef(TypedDict):
    BulkEmailEntryResults: List["BulkEmailEntryResultTypeDef"]


class SendCustomVerificationEmailResponseTypeDef(TypedDict, total=False):
    MessageId: str


class SendEmailResponseTypeDef(TypedDict, total=False):
    MessageId: str


class SendQuotaTypeDef(TypedDict, total=False):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float


class SendingOptionsTypeDef(TypedDict, total=False):
    SendingEnabled: bool


class SnsDestinationTypeDef(TypedDict):
    TopicArn: str


class SuppressedDestinationAttributesTypeDef(TypedDict, total=False):
    MessageId: str
    FeedbackId: str


class SuppressedDestinationSummaryTypeDef(TypedDict):
    EmailAddress: str
    Reason: SuppressionListReason
    LastUpdateTime: datetime


class _RequiredSuppressedDestinationTypeDef(TypedDict):
    EmailAddress: str
    Reason: SuppressionListReason
    LastUpdateTime: datetime


class SuppressedDestinationTypeDef(_RequiredSuppressedDestinationTypeDef, total=False):
    Attributes: "SuppressedDestinationAttributesTypeDef"


class SuppressionAttributesTypeDef(TypedDict, total=False):
    SuppressedReasons: List[SuppressionListReason]


class SuppressionListDestinationTypeDef(TypedDict):
    SuppressionListImportAction: SuppressionListImportAction


class SuppressionOptionsTypeDef(TypedDict, total=False):
    SuppressedReasons: List[SuppressionListReason]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TemplateTypeDef(TypedDict, total=False):
    TemplateName: str
    TemplateArn: str
    TemplateData: str


class TestRenderEmailTemplateResponseTypeDef(TypedDict):
    RenderedTemplate: str


class TopicFilterTypeDef(TypedDict, total=False):
    TopicName: str
    UseDefaultIfPreferenceUnavailable: bool


class TopicPreferenceTypeDef(TypedDict):
    TopicName: str
    SubscriptionStatus: SubscriptionStatus


class _RequiredTopicTypeDef(TypedDict):
    TopicName: str
    DisplayName: str
    DefaultSubscriptionStatus: SubscriptionStatus


class TopicTypeDef(_RequiredTopicTypeDef, total=False):
    Description: str


class TrackingOptionsTypeDef(TypedDict):
    CustomRedirectDomain: str


class VolumeStatisticsTypeDef(TypedDict, total=False):
    InboxRawCount: int
    SpamRawCount: int
    ProjectedInbox: int
    ProjectedSpam: int
