"""
Type annotations for pinpoint-email service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.type_defs import BlacklistEntryTypeDef

    data: BlacklistEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_pinpoint_email.literals import (
    BehaviorOnMxFailure,
    DeliverabilityDashboardAccountStatus,
    DeliverabilityTestStatus,
    DimensionValueSource,
    DkimStatus,
    EventType,
    IdentityType,
    MailFromDomainStatus,
    TlsPolicy,
    WarmupStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContentTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "IdentityInfoTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PaginatorConfigTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "RawMessageTypeDef",
    "ReputationOptionsTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TrackingOptionsTypeDef",
    "VolumeStatisticsTypeDef",
)


class BlacklistEntryTypeDef(TypedDict, total=False):
    RblName: str
    ListingTime: datetime
    Description: str


BodyTypeDef = TypedDict(
    "BodyTypeDef", {"Text": "ContentTypeDef", "Html": "ContentTypeDef"}, total=False
)


class CloudWatchDestinationTypeDef(TypedDict):
    DimensionConfigurations: List["CloudWatchDimensionConfigurationTypeDef"]


class CloudWatchDimensionConfigurationTypeDef(TypedDict):
    DimensionName: str
    DimensionValueSource: DimensionValueSource
    DefaultDimensionValue: str


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


class GetAccountResponseTypeDef(TypedDict, total=False):
    SendQuota: "SendQuotaTypeDef"
    SendingEnabled: bool
    DedicatedIpAutoWarmupEnabled: bool
    EnforcementStatus: str
    ProductionAccessEnabled: bool


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


class GetEmailIdentityResponseTypeDef(TypedDict, total=False):
    IdentityType: IdentityType
    FeedbackForwardingStatus: bool
    VerifiedForSendingStatus: bool
    DkimAttributes: "DkimAttributesTypeDef"
    MailFromAttributes: "MailFromAttributesTypeDef"
    Tags: List["TagTypeDef"]


class IdentityInfoTypeDef(TypedDict, total=False):
    IdentityType: IdentityType
    IdentityName: str
    SendingEnabled: bool


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


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PinpointDestinationTypeDef(TypedDict, total=False):
    ApplicationArn: str


class PlacementStatisticsTypeDef(TypedDict, total=False):
    InboxPercentage: float
    SpamPercentage: float
    MissingPercentage: float
    SpfPercentage: float
    DkimPercentage: float


class RawMessageTypeDef(TypedDict):
    Data: Union[bytes, IO[bytes]]


class ReputationOptionsTypeDef(TypedDict, total=False):
    ReputationMetricsEnabled: bool
    LastFreshStart: datetime


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


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TemplateTypeDef(TypedDict, total=False):
    TemplateArn: str
    TemplateData: str


class TrackingOptionsTypeDef(TypedDict):
    CustomRedirectDomain: str


class VolumeStatisticsTypeDef(TypedDict, total=False):
    InboxRawCount: int
    SpamRawCount: int
    ProjectedInbox: int
    ProjectedSpam: int
