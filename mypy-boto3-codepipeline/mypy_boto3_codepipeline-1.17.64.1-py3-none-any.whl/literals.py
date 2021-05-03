"""
Type annotations for codepipeline service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/literals.html)

Usage::

    ```python
    from mypy_boto3_codepipeline.literals import ActionCategory

    data: ActionCategory = "Approval"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionCategory",
    "ActionConfigurationPropertyType",
    "ActionExecutionStatus",
    "ActionOwner",
    "ApprovalStatus",
    "ArtifactLocationType",
    "ArtifactStoreType",
    "BlockerType",
    "EncryptionKeyType",
    "ExecutorType",
    "FailureType",
    "JobStatus",
    "ListActionExecutionsPaginatorName",
    "ListActionTypesPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelinesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListWebhooksPaginatorName",
    "PipelineExecutionStatus",
    "StageExecutionStatus",
    "StageRetryMode",
    "StageTransitionType",
    "TriggerType",
    "WebhookAuthenticationType",
)


ActionCategory = Literal["Approval", "Build", "Deploy", "Invoke", "Source", "Test"]
ActionConfigurationPropertyType = Literal["Boolean", "Number", "String"]
ActionExecutionStatus = Literal["Abandoned", "Failed", "InProgress", "Succeeded"]
ActionOwner = Literal["AWS", "Custom", "ThirdParty"]
ApprovalStatus = Literal["Approved", "Rejected"]
ArtifactLocationType = Literal["S3"]
ArtifactStoreType = Literal["S3"]
BlockerType = Literal["Schedule"]
EncryptionKeyType = Literal["KMS"]
ExecutorType = Literal["JobWorker", "Lambda"]
FailureType = Literal[
    "ConfigurationError",
    "JobFailed",
    "PermissionError",
    "RevisionOutOfSync",
    "RevisionUnavailable",
    "SystemUnavailable",
]
JobStatus = Literal[
    "Created", "Dispatched", "Failed", "InProgress", "Queued", "Succeeded", "TimedOut"
]
ListActionExecutionsPaginatorName = Literal["list_action_executions"]
ListActionTypesPaginatorName = Literal["list_action_types"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListWebhooksPaginatorName = Literal["list_webhooks"]
PipelineExecutionStatus = Literal[
    "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded", "Superseded"
]
StageExecutionStatus = Literal[
    "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded"
]
StageRetryMode = Literal["FAILED_ACTIONS"]
StageTransitionType = Literal["Inbound", "Outbound"]
TriggerType = Literal[
    "CloudWatchEvent",
    "CreatePipeline",
    "PollForSourceChanges",
    "PutActionRevision",
    "StartPipelineExecution",
    "Webhook",
]
WebhookAuthenticationType = Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"]
