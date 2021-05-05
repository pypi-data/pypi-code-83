"""
Type annotations for sesv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sesv2 import SESV2Client

    client: SESV2Client = boto3.client("sesv2")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sesv2.literals import (
    BehaviorOnMxFailure,
    ContactLanguage,
    DkimSigningAttributesOrigin,
    ImportDestinationType,
    MailType,
    SuppressionListReason,
    TlsPolicy,
)
from mypy_boto3_sesv2.type_defs import (
    BulkEmailContentTypeDef,
    BulkEmailEntryTypeDef,
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    CreateImportJobResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DkimSigningAttributesTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EmailTemplateContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetContactListResponseTypeDef,
    GetContactResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityPoliciesResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetSuppressedDestinationResponseTypeDef,
    ImportDataSourceTypeDef,
    ImportDestinationTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListContactListsResponseTypeDef,
    ListContactsFilterTypeDef,
    ListContactsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListEmailTemplatesResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListManagementOptionsTypeDef,
    ListSuppressedDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    PutEmailIdentityDkimSigningAttributesResponseTypeDef,
    ReputationOptionsTypeDef,
    SendBulkEmailResponseTypeDef,
    SendCustomVerificationEmailResponseTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    SuppressionOptionsTypeDef,
    TagTypeDef,
    TestRenderEmailTemplateResponseTypeDef,
    TopicPreferenceTypeDef,
    TopicTypeDef,
    TrackingOptionsTypeDef,
)

__all__ = ("SESV2Client",)


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
    ConflictException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class SESV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#can-paginate)
        """

    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        SuppressionOptions: "SuppressionOptionsTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-configuration-set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-configuration-set-event-destination)
        """

    def create_contact(
        self,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-contact)
        """

    def create_contact_list(
        self,
        ContactListName: str,
        Topics: List["TopicTypeDef"] = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-contact-list)
        """

    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-custom-verification-email-template)
        """

    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-dedicated-ip-pool)
        """

    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-deliverability-test-report)
        """

    def create_email_identity(
        self,
        EmailIdentity: str,
        Tags: List["TagTypeDef"] = None,
        DkimSigningAttributes: DkimSigningAttributesTypeDef = None,
        ConfigurationSetName: str = None,
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-email-identity)
        """

    def create_email_identity_policy(
        self, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-email-identity-policy)
        """

    def create_email_template(
        self, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-email-template)
        """

    def create_import_job(
        self,
        ImportDestination: "ImportDestinationTypeDef",
        ImportDataSource: "ImportDataSourceTypeDef",
    ) -> CreateImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.create_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create-import-job)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-configuration-set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-configuration-set-event-destination)
        """

    def delete_contact(self, ContactListName: str, EmailAddress: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-contact)
        """

    def delete_contact_list(self, ContactListName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-contact-list)
        """

    def delete_custom_verification_email_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-custom-verification-email-template)
        """

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-dedicated-ip-pool)
        """

    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-email-identity)
        """

    def delete_email_identity_policy(self, EmailIdentity: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-email-identity-policy)
        """

    def delete_email_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-email-template)
        """

    def delete_suppressed_destination(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.delete_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete-suppressed-destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#generate-presigned-url)
        """

    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-account)
        """

    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_blacklist_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-blacklist-reports)
        """

    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-configuration-set)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-configuration-set-event-destinations)
        """

    def get_contact(self, ContactListName: str, EmailAddress: str) -> GetContactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-contact)
        """

    def get_contact_list(self, ContactListName: str) -> GetContactListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-contact-list)
        """

    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-custom-verification-email-template)
        """

    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-dedicated-ip)
        """

    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_dedicated_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-dedicated-ips)
        """

    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_deliverability_dashboard_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-deliverability-dashboard-options)
        """

    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-deliverability-test-report)
        """

    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_domain_deliverability_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-domain-deliverability-campaign)
        """

    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_domain_statistics_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-domain-statistics-report)
        """

    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-email-identity)
        """

    def get_email_identity_policies(
        self, EmailIdentity: str
    ) -> GetEmailIdentityPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_email_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-email-identity-policies)
        """

    def get_email_template(self, TemplateName: str) -> GetEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-email-template)
        """

    def get_import_job(self, JobId: str) -> GetImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-import-job)
        """

    def get_suppressed_destination(
        self, EmailAddress: str
    ) -> GetSuppressedDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.get_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get-suppressed-destination)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-configuration-sets)
        """

    def list_contact_lists(
        self, PageSize: int = None, NextToken: str = None
    ) -> ListContactListsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_contact_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-contact-lists)
        """

    def list_contacts(
        self,
        ContactListName: str,
        Filter: ListContactsFilterTypeDef = None,
        PageSize: int = None,
        NextToken: str = None,
    ) -> ListContactsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-contacts)
        """

    def list_custom_verification_email_templates(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_custom_verification_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-custom-verification-email-templates)
        """

    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_dedicated_ip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-dedicated-ip-pools)
        """

    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_deliverability_test_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-deliverability-test-reports)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_domain_deliverability_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-domain-deliverability-campaigns)
        """

    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_email_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-email-identities)
        """

    def list_email_templates(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-email-templates)
        """

    def list_import_jobs(
        self,
        ImportDestinationType: ImportDestinationType = None,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListImportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-import-jobs)
        """

    def list_suppressed_destinations(
        self,
        Reasons: List[SuppressionListReason] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListSuppressedDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_suppressed_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-suppressed-destinations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list-tags-for-resource)
        """

    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_account_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-account-dedicated-ip-warmup-attributes)
        """

    def put_account_details(
        self,
        MailType: MailType,
        WebsiteURL: str,
        UseCaseDescription: str,
        ContactLanguage: ContactLanguage = None,
        AdditionalContactEmailAddresses: List[str] = None,
        ProductionAccessEnabled: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_account_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-account-details)
        """

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_account_sending_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-account-sending-attributes)
        """

    def put_account_suppression_attributes(
        self, SuppressedReasons: List[SuppressionListReason] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_account_suppression_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-account-suppression-attributes)
        """

    def put_configuration_set_delivery_options(
        self, ConfigurationSetName: str, TlsPolicy: TlsPolicy = None, SendingPoolName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-configuration-set-delivery-options)
        """

    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_configuration_set_reputation_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-configuration-set-reputation-options)
        """

    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_configuration_set_sending_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-configuration-set-sending-options)
        """

    def put_configuration_set_suppression_options(
        self, ConfigurationSetName: str, SuppressedReasons: List[SuppressionListReason] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_configuration_set_suppression_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-configuration-set-suppression-options)
        """

    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-configuration-set-tracking-options)
        """

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_in_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-dedicated-ip-in-pool)
        """

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-dedicated-ip-warmup-attributes)
        """

    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_deliverability_dashboard_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-deliverability-dashboard-option)
        """

    def put_email_identity_configuration_set_attributes(
        self, EmailIdentity: str, ConfigurationSetName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_email_identity_configuration_set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-email-identity-configuration-set-attributes)
        """

    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-email-identity-dkim-attributes)
        """

    def put_email_identity_dkim_signing_attributes(
        self,
        EmailIdentity: str,
        SigningAttributesOrigin: DkimSigningAttributesOrigin,
        SigningAttributes: DkimSigningAttributesTypeDef = None,
    ) -> PutEmailIdentityDkimSigningAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_signing_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-email-identity-dkim-signing-attributes)
        """

    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_email_identity_feedback_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-email-identity-feedback-attributes)
        """

    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: BehaviorOnMxFailure = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_email_identity_mail_from_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-email-identity-mail-from-attributes)
        """

    def put_suppressed_destination(
        self, EmailAddress: str, Reason: SuppressionListReason
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.put_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put-suppressed-destination)
        """

    def send_bulk_email(
        self,
        DefaultContent: BulkEmailContentTypeDef,
        BulkEmailEntries: List[BulkEmailEntryTypeDef],
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        DefaultEmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
    ) -> SendBulkEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.send_bulk_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send-bulk-email)
        """

    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.send_custom_verification_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send-custom-verification-email)
        """

    def send_email(
        self,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        Destination: "DestinationTypeDef" = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        EmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
        ListManagementOptions: ListManagementOptionsTypeDef = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send-email)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#tag-resource)
        """

    def test_render_email_template(
        self, TemplateName: str, TemplateData: str
    ) -> TestRenderEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.test_render_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#test-render-email-template)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#untag-resource)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-configuration-set-event-destination)
        """

    def update_contact(
        self,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-contact)
        """

    def update_contact_list(
        self, ContactListName: str, Topics: List["TopicTypeDef"] = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-contact-list)
        """

    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-custom-verification-email-template)
        """

    def update_email_identity_policy(
        self, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-email-identity-policy)
        """

    def update_email_template(
        self, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/sesv2.html#SESV2.Client.update_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update-email-template)
        """
