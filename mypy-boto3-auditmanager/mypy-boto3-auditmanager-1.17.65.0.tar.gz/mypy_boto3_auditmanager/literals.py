"""
Type annotations for auditmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_auditmanager.literals import AccountStatus

    data: AccountStatus = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountStatus",
    "ActionEnum",
    "AssessmentReportDestinationType",
    "AssessmentReportStatus",
    "AssessmentStatus",
    "ControlResponse",
    "ControlSetStatus",
    "ControlStatus",
    "ControlType",
    "DelegationStatus",
    "FrameworkType",
    "KeywordInputType",
    "ObjectTypeEnum",
    "RoleType",
    "SettingAttribute",
    "SourceFrequency",
    "SourceSetUpOption",
    "SourceType",
)


AccountStatus = Literal["ACTIVE", "INACTIVE", "PENDING_ACTIVATION"]
ActionEnum = Literal[
    "ACTIVE",
    "CREATE",
    "DELETE",
    "IMPORT_EVIDENCE",
    "INACTIVE",
    "REVIEWED",
    "UNDER_REVIEW",
    "UPDATE_METADATA",
]
AssessmentReportDestinationType = Literal["S3"]
AssessmentReportStatus = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
AssessmentStatus = Literal["ACTIVE", "INACTIVE"]
ControlResponse = Literal["AUTOMATE", "DEFER", "IGNORE", "MANUAL"]
ControlSetStatus = Literal["ACTIVE", "REVIEWED", "UNDER_REVIEW"]
ControlStatus = Literal["INACTIVE", "REVIEWED", "UNDER_REVIEW"]
ControlType = Literal["Custom", "Standard"]
DelegationStatus = Literal["COMPLETE", "IN_PROGRESS", "UNDER_REVIEW"]
FrameworkType = Literal["Custom", "Standard"]
KeywordInputType = Literal["SELECT_FROM_LIST"]
ObjectTypeEnum = Literal["ASSESSMENT", "ASSESSMENT_REPORT", "CONTROL", "CONTROL_SET", "DELEGATION"]
RoleType = Literal["PROCESS_OWNER", "RESOURCE_OWNER"]
SettingAttribute = Literal[
    "ALL",
    "DEFAULT_ASSESSMENT_REPORTS_DESTINATION",
    "DEFAULT_PROCESS_OWNERS",
    "IS_AWS_ORG_ENABLED",
    "SNS_TOPIC",
]
SourceFrequency = Literal["DAILY", "MONTHLY", "WEEKLY"]
SourceSetUpOption = Literal["Procedural_Controls_Mapping", "System_Controls_Mapping"]
SourceType = Literal["AWS_API_Call", "AWS_Cloudtrail", "AWS_Config", "AWS_Security_Hub", "MANUAL"]
