"""
Type annotations for pinpoint-email service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_email import PinpointEmailClient

    client: PinpointEmailClient = boto3.client("pinpoint-email")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_pinpoint_email.literals import BehaviorOnMxFailure, TlsPolicy
from mypy_boto3_pinpoint_email.paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)
from mypy_boto3_pinpoint_email.type_defs import (
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    ReputationOptionsTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    TagTypeDef,
    TrackingOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PinpointEmailClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccountSuspendedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class PinpointEmailClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#can-paginate)
        """

    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create-configuration-set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create-configuration-set-event-destination)
        """

    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.create_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create-dedicated-ip-pool)
        """

    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.create_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create-deliverability-test-report)
        """

    def create_email_identity(
        self, EmailIdentity: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.create_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create-email-identity)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete-configuration-set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete-configuration-set-event-destination)
        """

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete-dedicated-ip-pool)
        """

    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete-email-identity)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#generate-presigned-url)
        """

    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-account)
        """

    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_blacklist_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-blacklist-reports)
        """

    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-configuration-set)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-configuration-set-event-destinations)
        """

    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-dedicated-ip)
        """

    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-dedicated-ips)
        """

    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_dashboard_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-deliverability-dashboard-options)
        """

    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-deliverability-test-report)
        """

    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_deliverability_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-domain-deliverability-campaign)
        """

    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_statistics_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-domain-statistics-report)
        """

    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.get_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get-email-identity)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-configuration-sets)
        """

    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_dedicated_ip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-dedicated-ip-pools)
        """

    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_deliverability_test_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-deliverability-test-reports)
        """

    def list_domain_deliverability_campaigns(
        self,
        StartDate: datetime,
        EndDate: datetime,
        SubscribedDomain: str,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_domain_deliverability_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-domain-deliverability-campaigns)
        """

    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_email_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-email-identities)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list-tags-for-resource)
        """

    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-account-dedicated-ip-warmup-attributes)
        """

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_sending_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-account-sending-attributes)
        """

    def put_configuration_set_delivery_options(
        self, ConfigurationSetName: str, TlsPolicy: TlsPolicy = None, SendingPoolName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-configuration-set-delivery-options)
        """

    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_reputation_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-configuration-set-reputation-options)
        """

    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_sending_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-configuration-set-sending-options)
        """

    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-configuration-set-tracking-options)
        """

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_in_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-dedicated-ip-in-pool)
        """

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-dedicated-ip-warmup-attributes)
        """

    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_deliverability_dashboard_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-deliverability-dashboard-option)
        """

    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-email-identity-dkim-attributes)
        """

    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_feedback_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-email-identity-feedback-attributes)
        """

    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: BehaviorOnMxFailure = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_mail_from_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put-email-identity-mail-from-attributes)
        """

    def send_email(
        self,
        Destination: DestinationTypeDef,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        EmailTags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#send-email)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#untag-resource)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#update-configuration-set-event-destination)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_dedicated_ips"]
    ) -> GetDedicatedIpsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#getdedicatedipspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listconfigurationsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dedicated_ip_pools"]
    ) -> ListDedicatedIpPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdedicatedippoolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deliverability_test_reports"]
    ) -> ListDeliverabilityTestReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdeliverabilitytestreportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_email_identities"]
    ) -> ListEmailIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listemailidentitiespaginator)
        """
