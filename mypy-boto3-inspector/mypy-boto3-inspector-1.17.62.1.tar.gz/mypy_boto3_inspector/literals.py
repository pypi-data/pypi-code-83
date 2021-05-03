"""
Type annotations for inspector service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/literals.html)

Usage::

    ```python
    from mypy_boto3_inspector.literals import AgentHealth

    data: AgentHealth = "HEALTHY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AgentHealth",
    "AgentHealthCode",
    "AssessmentRunNotificationSnsStatusCode",
    "AssessmentRunState",
    "AssetType",
    "FailedItemErrorCode",
    "InspectorEvent",
    "ListAssessmentRunAgentsPaginatorName",
    "ListAssessmentRunsPaginatorName",
    "ListAssessmentTargetsPaginatorName",
    "ListAssessmentTemplatesPaginatorName",
    "ListEventSubscriptionsPaginatorName",
    "ListExclusionsPaginatorName",
    "ListFindingsPaginatorName",
    "ListRulesPackagesPaginatorName",
    "Locale",
    "PreviewAgentsPaginatorName",
    "PreviewStatus",
    "ReportFileFormat",
    "ReportStatus",
    "ReportType",
    "ScopeType",
    "Severity",
    "StopAction",
)


AgentHealth = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
AgentHealthCode = Literal["IDLE", "RUNNING", "SHUTDOWN", "THROTTLED", "UNHEALTHY", "UNKNOWN"]
AssessmentRunNotificationSnsStatusCode = Literal[
    "ACCESS_DENIED", "INTERNAL_ERROR", "SUCCESS", "TOPIC_DOES_NOT_EXIST"
]
AssessmentRunState = Literal[
    "CANCELED",
    "COLLECTING_DATA",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "CREATED",
    "DATA_COLLECTED",
    "ERROR",
    "EVALUATING_RULES",
    "FAILED",
    "START_DATA_COLLECTION_IN_PROGRESS",
    "START_DATA_COLLECTION_PENDING",
    "START_EVALUATING_RULES_PENDING",
    "STOP_DATA_COLLECTION_PENDING",
]
AssetType = Literal["ec2-instance"]
FailedItemErrorCode = Literal[
    "ACCESS_DENIED",
    "DUPLICATE_ARN",
    "INTERNAL_ERROR",
    "INVALID_ARN",
    "ITEM_DOES_NOT_EXIST",
    "LIMIT_EXCEEDED",
]
InspectorEvent = Literal[
    "ASSESSMENT_RUN_COMPLETED",
    "ASSESSMENT_RUN_STARTED",
    "ASSESSMENT_RUN_STATE_CHANGED",
    "FINDING_REPORTED",
    "OTHER",
]
ListAssessmentRunAgentsPaginatorName = Literal["list_assessment_run_agents"]
ListAssessmentRunsPaginatorName = Literal["list_assessment_runs"]
ListAssessmentTargetsPaginatorName = Literal["list_assessment_targets"]
ListAssessmentTemplatesPaginatorName = Literal["list_assessment_templates"]
ListEventSubscriptionsPaginatorName = Literal["list_event_subscriptions"]
ListExclusionsPaginatorName = Literal["list_exclusions"]
ListFindingsPaginatorName = Literal["list_findings"]
ListRulesPackagesPaginatorName = Literal["list_rules_packages"]
Locale = Literal["EN_US"]
PreviewAgentsPaginatorName = Literal["preview_agents"]
PreviewStatus = Literal["COMPLETED", "WORK_IN_PROGRESS"]
ReportFileFormat = Literal["HTML", "PDF"]
ReportStatus = Literal["COMPLETED", "FAILED", "WORK_IN_PROGRESS"]
ReportType = Literal["FINDING", "FULL"]
ScopeType = Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"]
Severity = Literal["High", "Informational", "Low", "Medium", "Undefined"]
StopAction = Literal["SKIP_EVALUATION", "START_EVALUATION"]
