"""
Type annotations for ses service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/literals.html)

Usage::

    ```python
    from mypy_boto3_ses.literals import BehaviorOnMXFailure

    data: BehaviorOnMXFailure = "RejectMessage"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BehaviorOnMXFailure",
    "BounceType",
    "BulkEmailStatus",
    "ConfigurationSetAttribute",
    "CustomMailFromStatus",
    "DimensionValueSource",
    "DsnAction",
    "EventType",
    "IdentityExistsWaiterName",
    "IdentityType",
    "InvocationType",
    "ListConfigurationSetsPaginatorName",
    "ListCustomVerificationEmailTemplatesPaginatorName",
    "ListIdentitiesPaginatorName",
    "ListReceiptRuleSetsPaginatorName",
    "ListTemplatesPaginatorName",
    "NotificationType",
    "ReceiptFilterPolicy",
    "SNSActionEncoding",
    "StopScope",
    "TlsPolicy",
    "VerificationStatus",
)


BehaviorOnMXFailure = Literal["RejectMessage", "UseDefaultValue"]
BounceType = Literal[
    "ContentRejected",
    "DoesNotExist",
    "ExceededQuota",
    "MessageTooLarge",
    "TemporaryFailure",
    "Undefined",
]
BulkEmailStatus = Literal[
    "AccountDailyQuotaExceeded",
    "AccountSendingPaused",
    "AccountSuspended",
    "AccountThrottled",
    "ConfigurationSetDoesNotExist",
    "ConfigurationSetSendingPaused",
    "Failed",
    "InvalidParameterValue",
    "InvalidSendingPoolName",
    "MailFromDomainNotVerified",
    "MessageRejected",
    "Success",
    "TemplateDoesNotExist",
    "TransientFailure",
]
ConfigurationSetAttribute = Literal[
    "deliveryOptions", "eventDestinations", "reputationOptions", "trackingOptions"
]
CustomMailFromStatus = Literal["Failed", "Pending", "Success", "TemporaryFailure"]
DimensionValueSource = Literal["emailHeader", "linkTag", "messageTag"]
DsnAction = Literal["delayed", "delivered", "expanded", "failed", "relayed"]
EventType = Literal[
    "bounce", "click", "complaint", "delivery", "open", "reject", "renderingFailure", "send"
]
IdentityExistsWaiterName = Literal["identity_exists"]
IdentityType = Literal["Domain", "EmailAddress"]
InvocationType = Literal["Event", "RequestResponse"]
ListConfigurationSetsPaginatorName = Literal["list_configuration_sets"]
ListCustomVerificationEmailTemplatesPaginatorName = Literal[
    "list_custom_verification_email_templates"
]
ListIdentitiesPaginatorName = Literal["list_identities"]
ListReceiptRuleSetsPaginatorName = Literal["list_receipt_rule_sets"]
ListTemplatesPaginatorName = Literal["list_templates"]
NotificationType = Literal["Bounce", "Complaint", "Delivery"]
ReceiptFilterPolicy = Literal["Allow", "Block"]
SNSActionEncoding = Literal["Base64", "UTF-8"]
StopScope = Literal["RuleSet"]
TlsPolicy = Literal["Optional", "Require"]
VerificationStatus = Literal["Failed", "NotStarted", "Pending", "Success", "TemporaryFailure"]
