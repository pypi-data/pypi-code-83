"""
Type annotations for iot service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/literals.html)

Usage::

    ```python
    from mypy_boto3_iot.literals import AbortAction

    data: AbortAction = "CANCEL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AbortAction",
    "ActionType",
    "AlertTargetType",
    "AuditCheckRunStatus",
    "AuditFindingSeverity",
    "AuditFrequency",
    "AuditMitigationActionsExecutionStatus",
    "AuditMitigationActionsTaskStatus",
    "AuditNotificationType",
    "AuditTaskStatus",
    "AuditTaskType",
    "AuthDecision",
    "AuthorizerStatus",
    "AutoRegistrationStatus",
    "AwsJobAbortCriteriaAbortAction",
    "AwsJobAbortCriteriaFailureType",
    "BehaviorCriteriaType",
    "CACertificateStatus",
    "CACertificateUpdateAction",
    "CannedAccessControlList",
    "CertificateMode",
    "CertificateStatus",
    "ComparisonOperator",
    "ConfidenceLevel",
    "CustomMetricType",
    "DayOfWeek",
    "DetectMitigationActionExecutionStatus",
    "DetectMitigationActionsTaskStatus",
    "DeviceCertificateUpdateAction",
    "DimensionType",
    "DimensionValueOperator",
    "DomainConfigurationStatus",
    "DomainType",
    "DynamicGroupStatus",
    "DynamoKeyType",
    "EventType",
    "FieldType",
    "GetBehaviorModelTrainingSummariesPaginatorName",
    "IndexStatus",
    "JobExecutionFailureType",
    "JobExecutionStatus",
    "JobStatus",
    "ListActiveViolationsPaginatorName",
    "ListAttachedPoliciesPaginatorName",
    "ListAuditFindingsPaginatorName",
    "ListAuditMitigationActionsExecutionsPaginatorName",
    "ListAuditMitigationActionsTasksPaginatorName",
    "ListAuditSuppressionsPaginatorName",
    "ListAuditTasksPaginatorName",
    "ListAuthorizersPaginatorName",
    "ListBillingGroupsPaginatorName",
    "ListCACertificatesPaginatorName",
    "ListCertificatesByCAPaginatorName",
    "ListCertificatesPaginatorName",
    "ListCustomMetricsPaginatorName",
    "ListDetectMitigationActionsExecutionsPaginatorName",
    "ListDetectMitigationActionsTasksPaginatorName",
    "ListDimensionsPaginatorName",
    "ListDomainConfigurationsPaginatorName",
    "ListIndicesPaginatorName",
    "ListJobExecutionsForJobPaginatorName",
    "ListJobExecutionsForThingPaginatorName",
    "ListJobsPaginatorName",
    "ListMitigationActionsPaginatorName",
    "ListOTAUpdatesPaginatorName",
    "ListOutgoingCertificatesPaginatorName",
    "ListPoliciesPaginatorName",
    "ListPolicyPrincipalsPaginatorName",
    "ListPrincipalPoliciesPaginatorName",
    "ListPrincipalThingsPaginatorName",
    "ListProvisioningTemplateVersionsPaginatorName",
    "ListProvisioningTemplatesPaginatorName",
    "ListRoleAliasesPaginatorName",
    "ListScheduledAuditsPaginatorName",
    "ListSecurityProfilesForTargetPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListStreamsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTargetsForPolicyPaginatorName",
    "ListTargetsForSecurityProfilePaginatorName",
    "ListThingGroupsForThingPaginatorName",
    "ListThingGroupsPaginatorName",
    "ListThingPrincipalsPaginatorName",
    "ListThingRegistrationTaskReportsPaginatorName",
    "ListThingRegistrationTasksPaginatorName",
    "ListThingTypesPaginatorName",
    "ListThingsInBillingGroupPaginatorName",
    "ListThingsInThingGroupPaginatorName",
    "ListThingsPaginatorName",
    "ListTopicRuleDestinationsPaginatorName",
    "ListTopicRulesPaginatorName",
    "ListV2LoggingLevelsPaginatorName",
    "ListViolationEventsPaginatorName",
    "LogLevel",
    "LogTargetType",
    "MessageFormat",
    "MitigationActionType",
    "ModelStatus",
    "OTAUpdateStatus",
    "PolicyTemplateName",
    "ProtocolType",
    "ReportType",
    "ResourceType",
    "ServerCertificateStatus",
    "ServiceType",
    "Status",
    "TargetSelection",
    "ThingConnectivityIndexingMode",
    "ThingGroupIndexingMode",
    "ThingIndexingMode",
    "TopicRuleDestinationStatus",
    "ViolationEventType",
)


AbortAction = Literal["CANCEL"]
ActionType = Literal["CONNECT", "PUBLISH", "RECEIVE", "SUBSCRIBE"]
AlertTargetType = Literal["SNS"]
AuditCheckRunStatus = Literal[
    "CANCELED",
    "COMPLETED_COMPLIANT",
    "COMPLETED_NON_COMPLIANT",
    "FAILED",
    "IN_PROGRESS",
    "WAITING_FOR_DATA_COLLECTION",
]
AuditFindingSeverity = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
AuditFrequency = Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"]
AuditMitigationActionsExecutionStatus = Literal[
    "CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"
]
AuditMitigationActionsTaskStatus = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditNotificationType = Literal["SNS"]
AuditTaskStatus = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditTaskType = Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
AuthDecision = Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"]
AuthorizerStatus = Literal["ACTIVE", "INACTIVE"]
AutoRegistrationStatus = Literal["DISABLE", "ENABLE"]
AwsJobAbortCriteriaAbortAction = Literal["CANCEL"]
AwsJobAbortCriteriaFailureType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
BehaviorCriteriaType = Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
CACertificateStatus = Literal["ACTIVE", "INACTIVE"]
CACertificateUpdateAction = Literal["DEACTIVATE"]
CannedAccessControlList = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "log-delivery-write",
    "private",
    "public-read",
    "public-read-write",
]
CertificateMode = Literal["DEFAULT", "SNI_ONLY"]
CertificateStatus = Literal[
    "ACTIVE", "INACTIVE", "PENDING_ACTIVATION", "PENDING_TRANSFER", "REGISTER_INACTIVE", "REVOKED"
]
ComparisonOperator = Literal[
    "greater-than",
    "greater-than-equals",
    "in-cidr-set",
    "in-port-set",
    "in-set",
    "less-than",
    "less-than-equals",
    "not-in-cidr-set",
    "not-in-port-set",
    "not-in-set",
]
ConfidenceLevel = Literal["HIGH", "LOW", "MEDIUM"]
CustomMetricType = Literal["ip-address-list", "number", "number-list", "string-list"]
DayOfWeek = Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
DetectMitigationActionExecutionStatus = Literal["FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESSFUL"]
DetectMitigationActionsTaskStatus = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCESSFUL"]
DeviceCertificateUpdateAction = Literal["DEACTIVATE"]
DimensionType = Literal["TOPIC_FILTER"]
DimensionValueOperator = Literal["IN", "NOT_IN"]
DomainConfigurationStatus = Literal["DISABLED", "ENABLED"]
DomainType = Literal["AWS_MANAGED", "CUSTOMER_MANAGED", "ENDPOINT"]
DynamicGroupStatus = Literal["ACTIVE", "BUILDING", "REBUILDING"]
DynamoKeyType = Literal["NUMBER", "STRING"]
EventType = Literal[
    "CA_CERTIFICATE",
    "CERTIFICATE",
    "JOB",
    "JOB_EXECUTION",
    "POLICY",
    "THING",
    "THING_GROUP",
    "THING_GROUP_HIERARCHY",
    "THING_GROUP_MEMBERSHIP",
    "THING_TYPE",
    "THING_TYPE_ASSOCIATION",
]
FieldType = Literal["Boolean", "Number", "String"]
GetBehaviorModelTrainingSummariesPaginatorName = Literal["get_behavior_model_training_summaries"]
IndexStatus = Literal["ACTIVE", "BUILDING", "REBUILDING"]
JobExecutionFailureType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
JobExecutionStatus = Literal[
    "CANCELED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "REMOVED", "SUCCEEDED", "TIMED_OUT"
]
JobStatus = Literal["CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS"]
ListActiveViolationsPaginatorName = Literal["list_active_violations"]
ListAttachedPoliciesPaginatorName = Literal["list_attached_policies"]
ListAuditFindingsPaginatorName = Literal["list_audit_findings"]
ListAuditMitigationActionsExecutionsPaginatorName = Literal[
    "list_audit_mitigation_actions_executions"
]
ListAuditMitigationActionsTasksPaginatorName = Literal["list_audit_mitigation_actions_tasks"]
ListAuditSuppressionsPaginatorName = Literal["list_audit_suppressions"]
ListAuditTasksPaginatorName = Literal["list_audit_tasks"]
ListAuthorizersPaginatorName = Literal["list_authorizers"]
ListBillingGroupsPaginatorName = Literal["list_billing_groups"]
ListCACertificatesPaginatorName = Literal["list_ca_certificates"]
ListCertificatesByCAPaginatorName = Literal["list_certificates_by_ca"]
ListCertificatesPaginatorName = Literal["list_certificates"]
ListCustomMetricsPaginatorName = Literal["list_custom_metrics"]
ListDetectMitigationActionsExecutionsPaginatorName = Literal[
    "list_detect_mitigation_actions_executions"
]
ListDetectMitigationActionsTasksPaginatorName = Literal["list_detect_mitigation_actions_tasks"]
ListDimensionsPaginatorName = Literal["list_dimensions"]
ListDomainConfigurationsPaginatorName = Literal["list_domain_configurations"]
ListIndicesPaginatorName = Literal["list_indices"]
ListJobExecutionsForJobPaginatorName = Literal["list_job_executions_for_job"]
ListJobExecutionsForThingPaginatorName = Literal["list_job_executions_for_thing"]
ListJobsPaginatorName = Literal["list_jobs"]
ListMitigationActionsPaginatorName = Literal["list_mitigation_actions"]
ListOTAUpdatesPaginatorName = Literal["list_ota_updates"]
ListOutgoingCertificatesPaginatorName = Literal["list_outgoing_certificates"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyPrincipalsPaginatorName = Literal["list_policy_principals"]
ListPrincipalPoliciesPaginatorName = Literal["list_principal_policies"]
ListPrincipalThingsPaginatorName = Literal["list_principal_things"]
ListProvisioningTemplateVersionsPaginatorName = Literal["list_provisioning_template_versions"]
ListProvisioningTemplatesPaginatorName = Literal["list_provisioning_templates"]
ListRoleAliasesPaginatorName = Literal["list_role_aliases"]
ListScheduledAuditsPaginatorName = Literal["list_scheduled_audits"]
ListSecurityProfilesForTargetPaginatorName = Literal["list_security_profiles_for_target"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListStreamsPaginatorName = Literal["list_streams"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
ListTargetsForSecurityProfilePaginatorName = Literal["list_targets_for_security_profile"]
ListThingGroupsForThingPaginatorName = Literal["list_thing_groups_for_thing"]
ListThingGroupsPaginatorName = Literal["list_thing_groups"]
ListThingPrincipalsPaginatorName = Literal["list_thing_principals"]
ListThingRegistrationTaskReportsPaginatorName = Literal["list_thing_registration_task_reports"]
ListThingRegistrationTasksPaginatorName = Literal["list_thing_registration_tasks"]
ListThingTypesPaginatorName = Literal["list_thing_types"]
ListThingsInBillingGroupPaginatorName = Literal["list_things_in_billing_group"]
ListThingsInThingGroupPaginatorName = Literal["list_things_in_thing_group"]
ListThingsPaginatorName = Literal["list_things"]
ListTopicRuleDestinationsPaginatorName = Literal["list_topic_rule_destinations"]
ListTopicRulesPaginatorName = Literal["list_topic_rules"]
ListV2LoggingLevelsPaginatorName = Literal["list_v2_logging_levels"]
ListViolationEventsPaginatorName = Literal["list_violation_events"]
LogLevel = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]
LogTargetType = Literal["DEFAULT", "THING_GROUP"]
MessageFormat = Literal["JSON", "RAW"]
MitigationActionType = Literal[
    "ADD_THINGS_TO_THING_GROUP",
    "ENABLE_IOT_LOGGING",
    "PUBLISH_FINDING_TO_SNS",
    "REPLACE_DEFAULT_POLICY_VERSION",
    "UPDATE_CA_CERTIFICATE",
    "UPDATE_DEVICE_CERTIFICATE",
]
ModelStatus = Literal["ACTIVE", "EXPIRED", "PENDING_BUILD"]
OTAUpdateStatus = Literal[
    "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "CREATE_PENDING"
]
PolicyTemplateName = Literal["BLANK_POLICY"]
ProtocolType = Literal["HTTP", "MQTT"]
ReportType = Literal["ERRORS", "RESULTS"]
ResourceType = Literal[
    "ACCOUNT_SETTINGS",
    "CA_CERTIFICATE",
    "CLIENT_ID",
    "COGNITO_IDENTITY_POOL",
    "DEVICE_CERTIFICATE",
    "IAM_ROLE",
    "IOT_POLICY",
    "ROLE_ALIAS",
]
ServerCertificateStatus = Literal["INVALID", "VALID"]
ServiceType = Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]
Status = Literal["Cancelled", "Cancelling", "Completed", "Failed", "InProgress"]
TargetSelection = Literal["CONTINUOUS", "SNAPSHOT"]
ThingConnectivityIndexingMode = Literal["OFF", "STATUS"]
ThingGroupIndexingMode = Literal["OFF", "ON"]
ThingIndexingMode = Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"]
TopicRuleDestinationStatus = Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"]
ViolationEventType = Literal["alarm-cleared", "alarm-invalidated", "in-alarm"]
