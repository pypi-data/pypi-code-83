"""
Type annotations for sesv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/literals.html)

Usage::

    ```python
    from mypy_boto3_sesv2.literals import BehaviorOnMxFailure

    data: BehaviorOnMxFailure = "REJECT_MESSAGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BehaviorOnMxFailure",
    "BulkEmailStatus",
    "ContactLanguage",
    "ContactListImportAction",
    "DataFormat",
    "DeliverabilityDashboardAccountStatus",
    "DeliverabilityTestStatus",
    "DimensionValueSource",
    "DkimSigningAttributesOrigin",
    "DkimStatus",
    "EventType",
    "IdentityType",
    "ImportDestinationType",
    "JobStatus",
    "MailFromDomainStatus",
    "MailType",
    "ReviewStatus",
    "SubscriptionStatus",
    "SuppressionListImportAction",
    "SuppressionListReason",
    "TlsPolicy",
    "WarmupStatus",
)


BehaviorOnMxFailure = Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
BulkEmailStatus = Literal[
    "ACCOUNT_DAILY_QUOTA_EXCEEDED",
    "ACCOUNT_SENDING_PAUSED",
    "ACCOUNT_SUSPENDED",
    "ACCOUNT_THROTTLED",
    "CONFIGURATION_SET_NOT_FOUND",
    "CONFIGURATION_SET_SENDING_PAUSED",
    "FAILED",
    "INVALID_PARAMETER",
    "INVALID_SENDING_POOL_NAME",
    "MAIL_FROM_DOMAIN_NOT_VERIFIED",
    "MESSAGE_REJECTED",
    "SUCCESS",
    "TEMPLATE_NOT_FOUND",
    "TRANSIENT_FAILURE",
]
ContactLanguage = Literal["EN", "JA"]
ContactListImportAction = Literal["DELETE", "PUT"]
DataFormat = Literal["CSV", "JSON"]
DeliverabilityDashboardAccountStatus = Literal["ACTIVE", "DISABLED", "PENDING_EXPIRATION"]
DeliverabilityTestStatus = Literal["COMPLETED", "IN_PROGRESS"]
DimensionValueSource = Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"]
DkimSigningAttributesOrigin = Literal["AWS_SES", "EXTERNAL"]
DkimStatus = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
EventType = Literal[
    "BOUNCE",
    "CLICK",
    "COMPLAINT",
    "DELIVERY",
    "DELIVERY_DELAY",
    "OPEN",
    "REJECT",
    "RENDERING_FAILURE",
    "SEND",
    "SUBSCRIPTION",
]
IdentityType = Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
ImportDestinationType = Literal["CONTACT_LIST", "SUPPRESSION_LIST"]
JobStatus = Literal["COMPLETED", "CREATED", "FAILED", "PROCESSING"]
MailFromDomainStatus = Literal["FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
MailType = Literal["MARKETING", "TRANSACTIONAL"]
ReviewStatus = Literal["DENIED", "FAILED", "GRANTED", "PENDING"]
SubscriptionStatus = Literal["OPT_IN", "OPT_OUT"]
SuppressionListImportAction = Literal["DELETE", "PUT"]
SuppressionListReason = Literal["BOUNCE", "COMPLAINT"]
TlsPolicy = Literal["OPTIONAL", "REQUIRE"]
WarmupStatus = Literal["DONE", "IN_PROGRESS"]
