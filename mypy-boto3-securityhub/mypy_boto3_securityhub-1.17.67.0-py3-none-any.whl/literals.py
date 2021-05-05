"""
Type annotations for securityhub service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/literals.html)

Usage::

    ```python
    from mypy_boto3_securityhub.literals import AdminStatus

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
    "AwsIamAccessKeyStatus",
    "ComplianceStatus",
    "ControlStatus",
    "DateRangeUnit",
    "GetEnabledStandardsPaginatorName",
    "GetFindingsPaginatorName",
    "GetInsightsPaginatorName",
    "IntegrationType",
    "ListEnabledProductsForImportPaginatorName",
    "ListInvitationsPaginatorName",
    "ListMembersPaginatorName",
    "MalwareState",
    "MalwareType",
    "MapFilterComparison",
    "NetworkDirection",
    "Partition",
    "RecordState",
    "SeverityLabel",
    "SeverityRating",
    "SortOrder",
    "StandardsStatus",
    "StringFilterComparison",
    "ThreatIntelIndicatorCategory",
    "ThreatIntelIndicatorType",
    "VerificationState",
    "WorkflowState",
    "WorkflowStatus",
)


AdminStatus = Literal["DISABLE_IN_PROGRESS", "ENABLED"]
AwsIamAccessKeyStatus = Literal["Active", "Inactive"]
ComplianceStatus = Literal["FAILED", "NOT_AVAILABLE", "PASSED", "WARNING"]
ControlStatus = Literal["DISABLED", "ENABLED"]
DateRangeUnit = Literal["DAYS"]
GetEnabledStandardsPaginatorName = Literal["get_enabled_standards"]
GetFindingsPaginatorName = Literal["get_findings"]
GetInsightsPaginatorName = Literal["get_insights"]
IntegrationType = Literal[
    "RECEIVE_FINDINGS_FROM_SECURITY_HUB",
    "SEND_FINDINGS_TO_SECURITY_HUB",
    "UPDATE_FINDINGS_IN_SECURITY_HUB",
]
ListEnabledProductsForImportPaginatorName = Literal["list_enabled_products_for_import"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListMembersPaginatorName = Literal["list_members"]
MalwareState = Literal["OBSERVED", "REMOVAL_FAILED", "REMOVED"]
MalwareType = Literal[
    "ADWARE",
    "BLENDED_THREAT",
    "BOTNET_AGENT",
    "COIN_MINER",
    "EXPLOIT_KIT",
    "KEYLOGGER",
    "MACRO",
    "POTENTIALLY_UNWANTED",
    "RANSOMWARE",
    "REMOTE_ACCESS",
    "ROOTKIT",
    "SPYWARE",
    "TROJAN",
    "VIRUS",
    "WORM",
]
MapFilterComparison = Literal["EQUALS", "NOT_EQUALS"]
NetworkDirection = Literal["IN", "OUT"]
Partition = Literal["aws", "aws-cn", "aws-us-gov"]
RecordState = Literal["ACTIVE", "ARCHIVED"]
SeverityLabel = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM"]
SeverityRating = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
SortOrder = Literal["asc", "desc"]
StandardsStatus = Literal["DELETING", "FAILED", "INCOMPLETE", "PENDING", "READY"]
StringFilterComparison = Literal["EQUALS", "NOT_EQUALS", "PREFIX", "PREFIX_NOT_EQUALS"]
ThreatIntelIndicatorCategory = Literal[
    "BACKDOOR", "CARD_STEALER", "COMMAND_AND_CONTROL", "DROP_SITE", "EXPLOIT_SITE", "KEYLOGGER"
]
ThreatIntelIndicatorType = Literal[
    "DOMAIN",
    "EMAIL_ADDRESS",
    "HASH_MD5",
    "HASH_SHA1",
    "HASH_SHA256",
    "HASH_SHA512",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MUTEX",
    "PROCESS",
    "URL",
]
VerificationState = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
WorkflowState = Literal["ASSIGNED", "DEFERRED", "IN_PROGRESS", "NEW", "RESOLVED"]
WorkflowStatus = Literal["NEW", "NOTIFIED", "RESOLVED", "SUPPRESSED"]
