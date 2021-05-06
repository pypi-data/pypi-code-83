"""
Type annotations for guardduty service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/literals.html)

Usage::

    ```python
    from mypy_boto3_guardduty.literals import AdminStatus

    data: AdminStatus = "DISABLE_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdminStatus",
    "DataSource",
    "DataSourceStatus",
    "DestinationType",
    "DetectorStatus",
    "Feedback",
    "FilterAction",
    "FindingPublishingFrequency",
    "FindingStatisticType",
    "IpSetFormat",
    "IpSetStatus",
    "ListDetectorsPaginatorName",
    "ListFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListIPSetsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "ListThreatIntelSetsPaginatorName",
    "OrderBy",
    "PublishingStatus",
    "ThreatIntelSetFormat",
    "ThreatIntelSetStatus",
    "UsageStatisticType",
)


AdminStatus = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
DataSource = Literal["CLOUD_TRAIL", "DNS_LOGS", "FLOW_LOGS", "S3_LOGS"]
DataSourceStatus = Literal["DISABLED", "ENABLED"]
DestinationType = Literal["S3"]
DetectorStatus = Literal["DISABLED", "ENABLED"]
Feedback = Literal["NOT_USEFUL", "USEFUL"]
FilterAction = Literal["ARCHIVE", "NOOP"]
FindingPublishingFrequency = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingStatisticType = Literal["COUNT_BY_SEVERITY"]
IpSetFormat = Literal["ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"]
IpSetStatus = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
ListDetectorsPaginatorName = Literal["list_detectors"]
ListFiltersPaginatorName = Literal["list_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListIPSetsPaginatorName = Literal["list_ip_sets"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
ListThreatIntelSetsPaginatorName = Literal["list_threat_intel_sets"]
OrderBy = Literal["ASC", "DESC"]
PublishingStatus = Literal[
    "PENDING_VERIFICATION", "PUBLISHING", "STOPPED", "UNABLE_TO_PUBLISH_FIX_DESTINATION_PROPERTY"
]
ThreatIntelSetFormat = Literal["ALIEN_VAULT", "FIRE_EYE", "OTX_CSV", "PROOF_POINT", "STIX", "TXT"]
ThreatIntelSetStatus = Literal[
    "ACTIVATING", "ACTIVE", "DEACTIVATING", "DELETED", "DELETE_PENDING", "ERROR", "INACTIVE"
]
UsageStatisticType = Literal[
    "SUM_BY_ACCOUNT", "SUM_BY_DATA_SOURCE", "SUM_BY_RESOURCE", "TOP_RESOURCES"
]
