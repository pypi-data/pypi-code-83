"""
Type annotations for ses service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_ses.literals import (
    BehaviorOnMXFailure,
    BounceType,
    BulkEmailStatus,
    CustomMailFromStatus,
    DimensionValueSource,
    DsnAction,
    EventType,
    InvocationType,
    ReceiptFilterPolicy,
    SNSActionEncoding,
    TlsPolicy,
    VerificationStatus,
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
    "AddHeaderActionTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "BulkEmailDestinationTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReputationOptionsTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "TrackingOptionsTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "WaiterConfigTypeDef",
    "WorkmailActionTypeDef",
)


class AddHeaderActionTypeDef(TypedDict):
    HeaderName: str
    HeaderValue: str


BodyTypeDef = TypedDict(
    "BodyTypeDef", {"Text": "ContentTypeDef", "Html": "ContentTypeDef"}, total=False
)


class _RequiredBounceActionTypeDef(TypedDict):
    SmtpReplyCode: str
    Message: str
    Sender: str


class BounceActionTypeDef(_RequiredBounceActionTypeDef, total=False):
    TopicArn: str
    StatusCode: str


class _RequiredBouncedRecipientInfoTypeDef(TypedDict):
    Recipient: str


class BouncedRecipientInfoTypeDef(_RequiredBouncedRecipientInfoTypeDef, total=False):
    RecipientArn: str
    BounceType: BounceType
    RecipientDsnFields: "RecipientDsnFieldsTypeDef"


class BulkEmailDestinationStatusTypeDef(TypedDict, total=False):
    Status: BulkEmailStatus
    Error: str
    MessageId: str


class _RequiredBulkEmailDestinationTypeDef(TypedDict):
    Destination: "DestinationTypeDef"


class BulkEmailDestinationTypeDef(_RequiredBulkEmailDestinationTypeDef, total=False):
    ReplacementTags: List["MessageTagTypeDef"]
    ReplacementTemplateData: str


class CloudWatchDestinationTypeDef(TypedDict):
    DimensionConfigurations: List["CloudWatchDimensionConfigurationTypeDef"]


class CloudWatchDimensionConfigurationTypeDef(TypedDict):
    DimensionName: str
    DimensionValueSource: DimensionValueSource
    DefaultDimensionValue: str


class ConfigurationSetTypeDef(TypedDict):
    Name: str


class _RequiredContentTypeDef(TypedDict):
    Data: str


class ContentTypeDef(_RequiredContentTypeDef, total=False):
    Charset: str


class CustomVerificationEmailTemplateTypeDef(TypedDict, total=False):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class DeliveryOptionsTypeDef(TypedDict, total=False):
    TlsPolicy: TlsPolicy


class DescribeActiveReceiptRuleSetResponseTypeDef(TypedDict, total=False):
    Metadata: "ReceiptRuleSetMetadataTypeDef"
    Rules: List["ReceiptRuleTypeDef"]


class DescribeConfigurationSetResponseTypeDef(TypedDict, total=False):
    ConfigurationSet: "ConfigurationSetTypeDef"
    EventDestinations: List["EventDestinationTypeDef"]
    TrackingOptions: "TrackingOptionsTypeDef"
    DeliveryOptions: "DeliveryOptionsTypeDef"
    ReputationOptions: "ReputationOptionsTypeDef"


class DescribeReceiptRuleResponseTypeDef(TypedDict, total=False):
    Rule: "ReceiptRuleTypeDef"


class DescribeReceiptRuleSetResponseTypeDef(TypedDict, total=False):
    Metadata: "ReceiptRuleSetMetadataTypeDef"
    Rules: List["ReceiptRuleTypeDef"]


class DestinationTypeDef(TypedDict, total=False):
    ToAddresses: List[str]
    CcAddresses: List[str]
    BccAddresses: List[str]


class _RequiredEventDestinationTypeDef(TypedDict):
    Name: str
    MatchingEventTypes: List[EventType]


class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, total=False):
    Enabled: bool
    KinesisFirehoseDestination: "KinesisFirehoseDestinationTypeDef"
    CloudWatchDestination: "CloudWatchDestinationTypeDef"
    SNSDestination: "SNSDestinationTypeDef"


class ExtensionFieldTypeDef(TypedDict):
    Name: str
    Value: str


class GetAccountSendingEnabledResponseTypeDef(TypedDict, total=False):
    Enabled: bool


class GetCustomVerificationEmailTemplateResponseTypeDef(TypedDict, total=False):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str


class GetIdentityDkimAttributesResponseTypeDef(TypedDict):
    DkimAttributes: Dict[str, "IdentityDkimAttributesTypeDef"]


class GetIdentityMailFromDomainAttributesResponseTypeDef(TypedDict):
    MailFromDomainAttributes: Dict[str, "IdentityMailFromDomainAttributesTypeDef"]


class GetIdentityNotificationAttributesResponseTypeDef(TypedDict):
    NotificationAttributes: Dict[str, "IdentityNotificationAttributesTypeDef"]


class GetIdentityPoliciesResponseTypeDef(TypedDict):
    Policies: Dict[str, str]


class GetIdentityVerificationAttributesResponseTypeDef(TypedDict):
    VerificationAttributes: Dict[str, "IdentityVerificationAttributesTypeDef"]


class GetSendQuotaResponseTypeDef(TypedDict, total=False):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float


class GetSendStatisticsResponseTypeDef(TypedDict, total=False):
    SendDataPoints: List["SendDataPointTypeDef"]


class GetTemplateResponseTypeDef(TypedDict, total=False):
    Template: "TemplateTypeDef"


class _RequiredIdentityDkimAttributesTypeDef(TypedDict):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatus


class IdentityDkimAttributesTypeDef(_RequiredIdentityDkimAttributesTypeDef, total=False):
    DkimTokens: List[str]


class IdentityMailFromDomainAttributesTypeDef(TypedDict):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatus
    BehaviorOnMXFailure: BehaviorOnMXFailure


class _RequiredIdentityNotificationAttributesTypeDef(TypedDict):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool


class IdentityNotificationAttributesTypeDef(
    _RequiredIdentityNotificationAttributesTypeDef, total=False
):
    HeadersInBounceNotificationsEnabled: bool
    HeadersInComplaintNotificationsEnabled: bool
    HeadersInDeliveryNotificationsEnabled: bool


class _RequiredIdentityVerificationAttributesTypeDef(TypedDict):
    VerificationStatus: VerificationStatus


class IdentityVerificationAttributesTypeDef(
    _RequiredIdentityVerificationAttributesTypeDef, total=False
):
    VerificationToken: str


class KinesisFirehoseDestinationTypeDef(TypedDict):
    IAMRoleARN: str
    DeliveryStreamARN: str


class _RequiredLambdaActionTypeDef(TypedDict):
    FunctionArn: str


class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, total=False):
    TopicArn: str
    InvocationType: InvocationType


class ListConfigurationSetsResponseTypeDef(TypedDict, total=False):
    ConfigurationSets: List["ConfigurationSetTypeDef"]
    NextToken: str


class ListCustomVerificationEmailTemplatesResponseTypeDef(TypedDict, total=False):
    CustomVerificationEmailTemplates: List["CustomVerificationEmailTemplateTypeDef"]
    NextToken: str


class _RequiredListIdentitiesResponseTypeDef(TypedDict):
    Identities: List[str]


class ListIdentitiesResponseTypeDef(_RequiredListIdentitiesResponseTypeDef, total=False):
    NextToken: str


class ListIdentityPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]


class ListReceiptFiltersResponseTypeDef(TypedDict, total=False):
    Filters: List["ReceiptFilterTypeDef"]


class ListReceiptRuleSetsResponseTypeDef(TypedDict, total=False):
    RuleSets: List["ReceiptRuleSetMetadataTypeDef"]
    NextToken: str


class ListTemplatesResponseTypeDef(TypedDict, total=False):
    TemplatesMetadata: List["TemplateMetadataTypeDef"]
    NextToken: str


class ListVerifiedEmailAddressesResponseTypeDef(TypedDict, total=False):
    VerifiedEmailAddresses: List[str]


class _RequiredMessageDsnTypeDef(TypedDict):
    ReportingMta: str


class MessageDsnTypeDef(_RequiredMessageDsnTypeDef, total=False):
    ArrivalDate: datetime
    ExtensionFields: List["ExtensionFieldTypeDef"]


class MessageTagTypeDef(TypedDict):
    Name: str
    Value: str


class MessageTypeDef(TypedDict):
    Subject: "ContentTypeDef"
    Body: "BodyTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RawMessageTypeDef(TypedDict):
    Data: Union[bytes, IO[bytes]]


class ReceiptActionTypeDef(TypedDict, total=False):
    S3Action: "S3ActionTypeDef"
    BounceAction: "BounceActionTypeDef"
    WorkmailAction: "WorkmailActionTypeDef"
    LambdaAction: "LambdaActionTypeDef"
    StopAction: "StopActionTypeDef"
    AddHeaderAction: "AddHeaderActionTypeDef"
    SNSAction: "SNSActionTypeDef"


class ReceiptFilterTypeDef(TypedDict):
    Name: str
    IpFilter: "ReceiptIpFilterTypeDef"


class ReceiptIpFilterTypeDef(TypedDict):
    Policy: ReceiptFilterPolicy
    Cidr: str


class ReceiptRuleSetMetadataTypeDef(TypedDict, total=False):
    Name: str
    CreatedTimestamp: datetime


class _RequiredReceiptRuleTypeDef(TypedDict):
    Name: str


class ReceiptRuleTypeDef(_RequiredReceiptRuleTypeDef, total=False):
    Enabled: bool
    TlsPolicy: TlsPolicy
    Recipients: List[str]
    Actions: List["ReceiptActionTypeDef"]
    ScanEnabled: bool


class _RequiredRecipientDsnFieldsTypeDef(TypedDict):
    Action: DsnAction
    Status: str


class RecipientDsnFieldsTypeDef(_RequiredRecipientDsnFieldsTypeDef, total=False):
    FinalRecipient: str
    RemoteMta: str
    DiagnosticCode: str
    LastAttemptDate: datetime
    ExtensionFields: List["ExtensionFieldTypeDef"]


class ReputationOptionsTypeDef(TypedDict, total=False):
    SendingEnabled: bool
    ReputationMetricsEnabled: bool
    LastFreshStart: datetime


class _RequiredS3ActionTypeDef(TypedDict):
    BucketName: str


class S3ActionTypeDef(_RequiredS3ActionTypeDef, total=False):
    TopicArn: str
    ObjectKeyPrefix: str
    KmsKeyArn: str


class _RequiredSNSActionTypeDef(TypedDict):
    TopicArn: str


class SNSActionTypeDef(_RequiredSNSActionTypeDef, total=False):
    Encoding: SNSActionEncoding


class SNSDestinationTypeDef(TypedDict):
    TopicARN: str


class SendBounceResponseTypeDef(TypedDict, total=False):
    MessageId: str


class SendBulkTemplatedEmailResponseTypeDef(TypedDict):
    Status: List["BulkEmailDestinationStatusTypeDef"]


class SendCustomVerificationEmailResponseTypeDef(TypedDict, total=False):
    MessageId: str


class SendDataPointTypeDef(TypedDict, total=False):
    Timestamp: datetime
    DeliveryAttempts: int
    Bounces: int
    Complaints: int
    Rejects: int


class SendEmailResponseTypeDef(TypedDict):
    MessageId: str


class SendRawEmailResponseTypeDef(TypedDict):
    MessageId: str


class SendTemplatedEmailResponseTypeDef(TypedDict):
    MessageId: str


class _RequiredStopActionTypeDef(TypedDict):
    Scope: Literal["RuleSet"]


class StopActionTypeDef(_RequiredStopActionTypeDef, total=False):
    TopicArn: str


class TemplateMetadataTypeDef(TypedDict, total=False):
    Name: str
    CreatedTimestamp: datetime


class _RequiredTemplateTypeDef(TypedDict):
    TemplateName: str


class TemplateTypeDef(_RequiredTemplateTypeDef, total=False):
    SubjectPart: str
    TextPart: str
    HtmlPart: str


class TestRenderTemplateResponseTypeDef(TypedDict, total=False):
    RenderedTemplate: str


class TrackingOptionsTypeDef(TypedDict, total=False):
    CustomRedirectDomain: str


class VerifyDomainDkimResponseTypeDef(TypedDict):
    DkimTokens: List[str]


class VerifyDomainIdentityResponseTypeDef(TypedDict):
    VerificationToken: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class _RequiredWorkmailActionTypeDef(TypedDict):
    OrganizationArn: str


class WorkmailActionTypeDef(_RequiredWorkmailActionTypeDef, total=False):
    TopicArn: str
