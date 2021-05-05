"""
Type annotations for ses service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ses import SESClient

    client: SESClient = boto3.client("ses")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ses.literals import (
    BehaviorOnMXFailure,
    ConfigurationSetAttribute,
    IdentityType,
    NotificationType,
)
from mypy_boto3_ses.paginator import (
    ListConfigurationSetsPaginator,
    ListCustomVerificationEmailTemplatesPaginator,
    ListIdentitiesPaginator,
    ListReceiptRuleSetsPaginator,
    ListTemplatesPaginator,
)
from mypy_boto3_ses.type_defs import (
    BouncedRecipientInfoTypeDef,
    BulkEmailDestinationTypeDef,
    ConfigurationSetTypeDef,
    DeliveryOptionsTypeDef,
    DescribeActiveReceiptRuleSetResponseTypeDef,
    DescribeConfigurationSetResponseTypeDef,
    DescribeReceiptRuleResponseTypeDef,
    DescribeReceiptRuleSetResponseTypeDef,
    DestinationTypeDef,
    EventDestinationTypeDef,
    GetAccountSendingEnabledResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetIdentityDkimAttributesResponseTypeDef,
    GetIdentityMailFromDomainAttributesResponseTypeDef,
    GetIdentityNotificationAttributesResponseTypeDef,
    GetIdentityPoliciesResponseTypeDef,
    GetIdentityVerificationAttributesResponseTypeDef,
    GetSendQuotaResponseTypeDef,
    GetSendStatisticsResponseTypeDef,
    GetTemplateResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoliciesResponseTypeDef,
    ListReceiptFiltersResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListVerifiedEmailAddressesResponseTypeDef,
    MessageDsnTypeDef,
    MessageTagTypeDef,
    MessageTypeDef,
    RawMessageTypeDef,
    ReceiptFilterTypeDef,
    ReceiptRuleTypeDef,
    SendBounceResponseTypeDef,
    SendBulkTemplatedEmailResponseTypeDef,
    SendCustomVerificationEmailResponseTypeDef,
    SendEmailResponseTypeDef,
    SendRawEmailResponseTypeDef,
    SendTemplatedEmailResponseTypeDef,
    TemplateTypeDef,
    TestRenderTemplateResponseTypeDef,
    TrackingOptionsTypeDef,
    VerifyDomainDkimResponseTypeDef,
    VerifyDomainIdentityResponseTypeDef,
)
from mypy_boto3_ses.waiter import IdentityExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SESClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccountSendingPausedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    CannotDeleteException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConfigurationSetAlreadyExistsException: Type[BotocoreClientError]
    ConfigurationSetDoesNotExistException: Type[BotocoreClientError]
    ConfigurationSetSendingPausedException: Type[BotocoreClientError]
    CustomVerificationEmailInvalidContentException: Type[BotocoreClientError]
    CustomVerificationEmailTemplateAlreadyExistsException: Type[BotocoreClientError]
    CustomVerificationEmailTemplateDoesNotExistException: Type[BotocoreClientError]
    EventDestinationAlreadyExistsException: Type[BotocoreClientError]
    EventDestinationDoesNotExistException: Type[BotocoreClientError]
    FromEmailAddressNotVerifiedException: Type[BotocoreClientError]
    InvalidCloudWatchDestinationException: Type[BotocoreClientError]
    InvalidConfigurationSetException: Type[BotocoreClientError]
    InvalidDeliveryOptionsException: Type[BotocoreClientError]
    InvalidFirehoseDestinationException: Type[BotocoreClientError]
    InvalidLambdaFunctionException: Type[BotocoreClientError]
    InvalidPolicyException: Type[BotocoreClientError]
    InvalidRenderingParameterException: Type[BotocoreClientError]
    InvalidS3ConfigurationException: Type[BotocoreClientError]
    InvalidSNSDestinationException: Type[BotocoreClientError]
    InvalidSnsTopicException: Type[BotocoreClientError]
    InvalidTemplateException: Type[BotocoreClientError]
    InvalidTrackingOptionsException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    MissingRenderingAttributeException: Type[BotocoreClientError]
    ProductionAccessNotGrantedException: Type[BotocoreClientError]
    RuleDoesNotExistException: Type[BotocoreClientError]
    RuleSetDoesNotExistException: Type[BotocoreClientError]
    TemplateDoesNotExistException: Type[BotocoreClientError]
    TrackingOptionsAlreadyExistsException: Type[BotocoreClientError]
    TrackingOptionsDoesNotExistException: Type[BotocoreClientError]


class SESClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#can-paginate)
        """

    def clone_receipt_rule_set(self, RuleSetName: str, OriginalRuleSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.clone_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#clone-receipt-rule-set)
        """

    def create_configuration_set(
        self, ConfigurationSet: "ConfigurationSetTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-configuration-set)
        """

    def create_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: "EventDestinationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-configuration-set-event-destination)
        """

    def create_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: "TrackingOptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-configuration-set-tracking-options)
        """

    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-custom-verification-email-template)
        """

    def create_receipt_filter(self, Filter: "ReceiptFilterTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_receipt_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-receipt-filter)
        """

    def create_receipt_rule(
        self, RuleSetName: str, Rule: "ReceiptRuleTypeDef", After: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-receipt-rule)
        """

    def create_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-receipt-rule-set)
        """

    def create_template(self, Template: "TemplateTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create-template)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-configuration-set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-configuration-set-event-destination)
        """

    def delete_configuration_set_tracking_options(
        self, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-configuration-set-tracking-options)
        """

    def delete_custom_verification_email_template(self, TemplateName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-custom-verification-email-template)
        """

    def delete_identity(self, Identity: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-identity)
        """

    def delete_identity_policy(self, Identity: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-identity-policy)
        """

    def delete_receipt_filter(self, FilterName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_receipt_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-receipt-filter)
        """

    def delete_receipt_rule(self, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-receipt-rule)
        """

    def delete_receipt_rule_set(self, RuleSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-receipt-rule-set)
        """

    def delete_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-template)
        """

    def delete_verified_email_address(self, EmailAddress: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.delete_verified_email_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete-verified-email-address)
        """

    def describe_active_receipt_rule_set(self) -> DescribeActiveReceiptRuleSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.describe_active_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe-active-receipt-rule-set)
        """

    def describe_configuration_set(
        self,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: List[ConfigurationSetAttribute] = None,
    ) -> DescribeConfigurationSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.describe_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe-configuration-set)
        """

    def describe_receipt_rule(
        self, RuleSetName: str, RuleName: str
    ) -> DescribeReceiptRuleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.describe_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe-receipt-rule)
        """

    def describe_receipt_rule_set(self, RuleSetName: str) -> DescribeReceiptRuleSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.describe_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe-receipt-rule-set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#generate-presigned-url)
        """

    def get_account_sending_enabled(self) -> GetAccountSendingEnabledResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_account_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-account-sending-enabled)
        """

    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-custom-verification-email-template)
        """

    def get_identity_dkim_attributes(
        self, Identities: List[str]
    ) -> GetIdentityDkimAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-identity-dkim-attributes)
        """

    def get_identity_mail_from_domain_attributes(
        self, Identities: List[str]
    ) -> GetIdentityMailFromDomainAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_identity_mail_from_domain_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-identity-mail-from-domain-attributes)
        """

    def get_identity_notification_attributes(
        self, Identities: List[str]
    ) -> GetIdentityNotificationAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_identity_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-identity-notification-attributes)
        """

    def get_identity_policies(
        self, Identity: str, PolicyNames: List[str]
    ) -> GetIdentityPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-identity-policies)
        """

    def get_identity_verification_attributes(
        self, Identities: List[str]
    ) -> GetIdentityVerificationAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_identity_verification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-identity-verification-attributes)
        """

    def get_send_quota(self) -> GetSendQuotaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_send_quota)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-send-quota)
        """

    def get_send_statistics(self) -> GetSendStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_send_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-send-statistics)
        """

    def get_template(self, TemplateName: str) -> GetTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get-template)
        """

    def list_configuration_sets(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-configuration-sets)
        """

    def list_custom_verification_email_templates(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_custom_verification_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-custom-verification-email-templates)
        """

    def list_identities(
        self, IdentityType: IdentityType = None, NextToken: str = None, MaxItems: int = None
    ) -> ListIdentitiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-identities)
        """

    def list_identity_policies(self, Identity: str) -> ListIdentityPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-identity-policies)
        """

    def list_receipt_filters(self) -> ListReceiptFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_receipt_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-receipt-filters)
        """

    def list_receipt_rule_sets(self, NextToken: str = None) -> ListReceiptRuleSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_receipt_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-receipt-rule-sets)
        """

    def list_templates(
        self, NextToken: str = None, MaxItems: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-templates)
        """

    def list_verified_email_addresses(self) -> ListVerifiedEmailAddressesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.list_verified_email_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list-verified-email-addresses)
        """

    def put_configuration_set_delivery_options(
        self, ConfigurationSetName: str, DeliveryOptions: "DeliveryOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#put-configuration-set-delivery-options)
        """

    def put_identity_policy(self, Identity: str, PolicyName: str, Policy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.put_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#put-identity-policy)
        """

    def reorder_receipt_rule_set(self, RuleSetName: str, RuleNames: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.reorder_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#reorder-receipt-rule-set)
        """

    def send_bounce(
        self,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List[BouncedRecipientInfoTypeDef],
        Explanation: str = None,
        MessageDsn: MessageDsnTypeDef = None,
        BounceSenderArn: str = None,
    ) -> SendBounceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_bounce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-bounce)
        """

    def send_bulk_templated_email(
        self,
        Source: str,
        Template: str,
        Destinations: List[BulkEmailDestinationTypeDef],
        SourceArn: str = None,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        ReturnPathArn: str = None,
        ConfigurationSetName: str = None,
        DefaultTags: List["MessageTagTypeDef"] = None,
        TemplateArn: str = None,
        DefaultTemplateData: str = None,
    ) -> SendBulkTemplatedEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_bulk_templated_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-bulk-templated-email)
        """

    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_custom_verification_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-custom-verification-email)
        """

    def send_email(
        self,
        Source: str,
        Destination: "DestinationTypeDef",
        Message: MessageTypeDef,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-email)
        """

    def send_raw_email(
        self,
        RawMessage: RawMessageTypeDef,
        Source: str = None,
        Destinations: List[str] = None,
        FromArn: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
    ) -> SendRawEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_raw_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-raw-email)
        """

    def send_templated_email(
        self,
        Source: str,
        Destination: "DestinationTypeDef",
        Template: str,
        TemplateData: str,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
        TemplateArn: str = None,
    ) -> SendTemplatedEmailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.send_templated_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send-templated-email)
        """

    def set_active_receipt_rule_set(self, RuleSetName: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_active_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-active-receipt-rule-set)
        """

    def set_identity_dkim_enabled(self, Identity: str, DkimEnabled: bool) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_identity_dkim_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-identity-dkim-enabled)
        """

    def set_identity_feedback_forwarding_enabled(
        self, Identity: str, ForwardingEnabled: bool
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_identity_feedback_forwarding_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-identity-feedback-forwarding-enabled)
        """

    def set_identity_headers_in_notifications_enabled(
        self, Identity: str, NotificationType: NotificationType, Enabled: bool
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_identity_headers_in_notifications_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-identity-headers-in-notifications-enabled)
        """

    def set_identity_mail_from_domain(
        self,
        Identity: str,
        MailFromDomain: str = None,
        BehaviorOnMXFailure: BehaviorOnMXFailure = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_identity_mail_from_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-identity-mail-from-domain)
        """

    def set_identity_notification_topic(
        self, Identity: str, NotificationType: NotificationType, SnsTopic: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_identity_notification_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-identity-notification-topic)
        """

    def set_receipt_rule_position(
        self, RuleSetName: str, RuleName: str, After: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.set_receipt_rule_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set-receipt-rule-position)
        """

    def test_render_template(
        self, TemplateName: str, TemplateData: str
    ) -> TestRenderTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.test_render_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#test-render-template)
        """

    def update_account_sending_enabled(self, Enabled: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_account_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-account-sending-enabled)
        """

    def update_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestination: "EventDestinationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-configuration-set-event-destination)
        """

    def update_configuration_set_reputation_metrics_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_configuration_set_reputation_metrics_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-configuration-set-reputation-metrics-enabled)
        """

    def update_configuration_set_sending_enabled(
        self, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_configuration_set_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-configuration-set-sending-enabled)
        """

    def update_configuration_set_tracking_options(
        self, ConfigurationSetName: str, TrackingOptions: "TrackingOptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-configuration-set-tracking-options)
        """

    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str = None,
        TemplateSubject: str = None,
        TemplateContent: str = None,
        SuccessRedirectionURL: str = None,
        FailureRedirectionURL: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-custom-verification-email-template)
        """

    def update_receipt_rule(self, RuleSetName: str, Rule: "ReceiptRuleTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-receipt-rule)
        """

    def update_template(self, Template: "TemplateTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update-template)
        """

    def verify_domain_dkim(self, Domain: str) -> VerifyDomainDkimResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.verify_domain_dkim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify-domain-dkim)
        """

    def verify_domain_identity(self, Domain: str) -> VerifyDomainIdentityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.verify_domain_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify-domain-identity)
        """

    def verify_email_address(self, EmailAddress: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.verify_email_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify-email-address)
        """

    def verify_email_identity(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Client.verify_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify-email-identity)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Paginator.ListConfigurationSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listconfigurationsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_verification_email_templates"]
    ) -> ListCustomVerificationEmailTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listcustomverificationemailtemplatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_identities"]) -> ListIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Paginator.ListIdentities)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listidentitiespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_receipt_rule_sets"]
    ) -> ListReceiptRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listreceiptrulesetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Paginator.ListTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listtemplatespaginator)
        """

    def get_waiter(self, waiter_name: Literal["identity_exists"]) -> IdentityExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ses.html#SES.Waiter.identity_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/waiters.html#identityexistswaiter)
        """
