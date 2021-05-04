"""
Type annotations for pinpoint-email service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/literals.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.literals import BehaviorOnMxFailure

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
    "DeliverabilityDashboardAccountStatus",
    "DeliverabilityTestStatus",
    "DimensionValueSource",
    "DkimStatus",
    "EventType",
    "GetDedicatedIpsPaginatorName",
    "IdentityType",
    "ListConfigurationSetsPaginatorName",
    "ListDedicatedIpPoolsPaginatorName",
    "ListDeliverabilityTestReportsPaginatorName",
    "ListEmailIdentitiesPaginatorName",
    "MailFromDomainStatus",
    "TlsPolicy",
    "WarmupStatus",
)


BehaviorOnMxFailure = Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
DeliverabilityDashboardAccountStatus = Literal["ACTIVE", "DISABLED", "PENDING_EXPIRATION"]
DeliverabilityTestStatus = Literal["COMPLETED", "IN_PROGRESS"]
DimensionValueSource = Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"]
DkimStatus = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
EventType = Literal[
    "BOUNCE", "CLICK", "COMPLAINT", "DELIVERY", "OPEN", "REJECT", "RENDERING_FAILURE", "SEND"
]
GetDedicatedIpsPaginatorName = Literal["get_dedicated_ips"]
IdentityType = Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
ListConfigurationSetsPaginatorName = Literal["list_configuration_sets"]
ListDedicatedIpPoolsPaginatorName = Literal["list_dedicated_ip_pools"]
ListDeliverabilityTestReportsPaginatorName = Literal["list_deliverability_test_reports"]
ListEmailIdentitiesPaginatorName = Literal["list_email_identities"]
MailFromDomainStatus = Literal["FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
TlsPolicy = Literal["OPTIONAL", "REQUIRE"]
WarmupStatus = Literal["DONE", "IN_PROGRESS"]
