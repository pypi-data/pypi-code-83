"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_codepipeline.literals import (
    ActionCategory,
    ActionConfigurationPropertyType,
    ActionExecutionStatus,
    ActionOwner,
    ApprovalStatus,
    ExecutorType,
    FailureType,
    JobStatus,
    PipelineExecutionStatus,
    StageExecutionStatus,
    TriggerType,
    WebhookAuthenticationType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ActionTypeExecutorTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeSettingsTypeDef",
    "ActionTypeTypeDef",
    "ActionTypeUrlsTypeDef",
    "ApprovalResultTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactDetailsTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "ArtifactStoreTypeDef",
    "ArtifactTypeDef",
    "BlockerDeclarationTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "CreatePipelineOutputTypeDef",
    "CurrentRevisionTypeDef",
    "EncryptionKeyTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "ExecutorConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeOutputTypeDef",
    "GetJobDetailsOutputTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "GetPipelineOutputTypeDef",
    "GetPipelineStateOutputTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListActionTypesOutputTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListPipelinesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWebhookItemTypeDef",
    "ListWebhooksOutputTypeDef",
    "OutputArtifactTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "PollForJobsOutputTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultOutputTypeDef",
    "PutWebhookOutputTypeDef",
    "ResponseMetadata",
    "RetryStageExecutionOutputTypeDef",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopExecutionTriggerTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TransitionStateTypeDef",
    "UpdatePipelineOutputTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookFilterRuleTypeDef",
)


class AWSSessionCredentialsTypeDef(TypedDict):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str


class AcknowledgeJobOutputTypeDef(TypedDict):
    status: JobStatus
    ResponseMetadata: "ResponseMetadata"


class AcknowledgeThirdPartyJobOutputTypeDef(TypedDict):
    status: JobStatus
    ResponseMetadata: "ResponseMetadata"


_RequiredActionConfigurationPropertyTypeDef = TypedDict(
    "_RequiredActionConfigurationPropertyTypeDef",
    {"name": str, "required": bool, "key": bool, "secret": bool},
)
_OptionalActionConfigurationPropertyTypeDef = TypedDict(
    "_OptionalActionConfigurationPropertyTypeDef",
    {"queryable": bool, "description": str, "type": ActionConfigurationPropertyType},
    total=False,
)


class ActionConfigurationPropertyTypeDef(
    _RequiredActionConfigurationPropertyTypeDef, _OptionalActionConfigurationPropertyTypeDef
):
    pass


class ActionConfigurationTypeDef(TypedDict, total=False):
    configuration: Dict[str, str]


class ActionContextTypeDef(TypedDict, total=False):
    name: str
    actionExecutionId: str


class _RequiredActionDeclarationTypeDef(TypedDict):
    name: str
    actionTypeId: "ActionTypeIdTypeDef"


class ActionDeclarationTypeDef(_RequiredActionDeclarationTypeDef, total=False):
    runOrder: int
    configuration: Dict[str, str]
    outputArtifacts: List["OutputArtifactTypeDef"]
    inputArtifacts: List["InputArtifactTypeDef"]
    roleArn: str
    region: str
    namespace: str


ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": ActionExecutionStatus,
        "input": "ActionExecutionInputTypeDef",
        "output": "ActionExecutionOutputTypeDef",
    },
    total=False,
)


class ActionExecutionFilterTypeDef(TypedDict, total=False):
    pipelineExecutionId: str


class ActionExecutionInputTypeDef(TypedDict, total=False):
    actionTypeId: "ActionTypeIdTypeDef"
    configuration: Dict[str, str]
    resolvedConfiguration: Dict[str, str]
    roleArn: str
    region: str
    inputArtifacts: List["ArtifactDetailTypeDef"]
    namespace: str


class ActionExecutionOutputTypeDef(TypedDict):
    outputArtifacts: List["ArtifactDetailTypeDef"]
    executionResult: "ActionExecutionResultTypeDef"
    outputVariables: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class ActionExecutionResultTypeDef(TypedDict, total=False):
    externalExecutionId: str
    externalExecutionSummary: str
    externalExecutionUrl: str


class ActionExecutionTypeDef(TypedDict, total=False):
    actionExecutionId: str
    status: ActionExecutionStatus
    summary: str
    lastStatusChange: datetime
    token: str
    lastUpdatedBy: str
    externalExecutionId: str
    externalExecutionUrl: str
    percentComplete: int
    errorDetails: "ErrorDetailsTypeDef"


class ActionRevisionTypeDef(TypedDict):
    revisionId: str
    revisionChangeId: str
    created: datetime


class ActionStateTypeDef(TypedDict, total=False):
    actionName: str
    currentRevision: "ActionRevisionTypeDef"
    latestExecution: "ActionExecutionTypeDef"
    entityUrl: str
    revisionUrl: str


class ActionTypeArtifactDetailsTypeDef(TypedDict):
    minimumCount: int
    maximumCount: int


_RequiredActionTypeDeclarationTypeDef = TypedDict(
    "_RequiredActionTypeDeclarationTypeDef",
    {
        "executor": "ActionTypeExecutorTypeDef",
        "id": "ActionTypeIdentifierTypeDef",
        "inputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
        "outputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeDeclarationTypeDef = TypedDict(
    "_OptionalActionTypeDeclarationTypeDef",
    {
        "description": str,
        "permissions": "ActionTypePermissionsTypeDef",
        "properties": List["ActionTypePropertyTypeDef"],
        "urls": "ActionTypeUrlsTypeDef",
    },
    total=False,
)


class ActionTypeDeclarationTypeDef(
    _RequiredActionTypeDeclarationTypeDef, _OptionalActionTypeDeclarationTypeDef
):
    pass


_RequiredActionTypeExecutorTypeDef = TypedDict(
    "_RequiredActionTypeExecutorTypeDef",
    {"configuration": "ExecutorConfigurationTypeDef", "type": ExecutorType},
)
_OptionalActionTypeExecutorTypeDef = TypedDict(
    "_OptionalActionTypeExecutorTypeDef",
    {"policyStatementsTemplate": str, "jobTimeout": int},
    total=False,
)


class ActionTypeExecutorTypeDef(
    _RequiredActionTypeExecutorTypeDef, _OptionalActionTypeExecutorTypeDef
):
    pass


class ActionTypeIdTypeDef(TypedDict):
    category: ActionCategory
    owner: ActionOwner
    provider: str
    version: str


class ActionTypeIdentifierTypeDef(TypedDict):
    category: ActionCategory
    owner: str
    provider: str
    version: str


class ActionTypePermissionsTypeDef(TypedDict):
    allowedAccounts: List[str]


class _RequiredActionTypePropertyTypeDef(TypedDict):
    name: str
    optional: bool
    key: bool
    noEcho: bool


class ActionTypePropertyTypeDef(_RequiredActionTypePropertyTypeDef, total=False):
    queryable: bool
    description: str


class ActionTypeSettingsTypeDef(TypedDict, total=False):
    thirdPartyConfigurationUrl: str
    entityUrlTemplate: str
    executionUrlTemplate: str
    revisionUrlTemplate: str


_RequiredActionTypeTypeDef = TypedDict(
    "_RequiredActionTypeTypeDef",
    {
        "id": "ActionTypeIdTypeDef",
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeTypeDef = TypedDict(
    "_OptionalActionTypeTypeDef",
    {
        "settings": "ActionTypeSettingsTypeDef",
        "actionConfigurationProperties": List["ActionConfigurationPropertyTypeDef"],
    },
    total=False,
)


class ActionTypeTypeDef(_RequiredActionTypeTypeDef, _OptionalActionTypeTypeDef):
    pass


class ActionTypeUrlsTypeDef(TypedDict, total=False):
    configurationUrl: str
    entityUrlTemplate: str
    executionUrlTemplate: str
    revisionUrlTemplate: str


class ApprovalResultTypeDef(TypedDict):
    summary: str
    status: ApprovalStatus


class ArtifactDetailTypeDef(TypedDict, total=False):
    name: str
    s3location: "S3LocationTypeDef"


class ArtifactDetailsTypeDef(TypedDict):
    minimumCount: int
    maximumCount: int


ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {"type": Literal["S3"], "s3Location": "S3ArtifactLocationTypeDef"},
    total=False,
)


class ArtifactRevisionTypeDef(TypedDict, total=False):
    name: str
    revisionId: str
    revisionChangeIdentifier: str
    revisionSummary: str
    created: datetime
    revisionUrl: str


_RequiredArtifactStoreTypeDef = TypedDict(
    "_RequiredArtifactStoreTypeDef", {"type": Literal["S3"], "location": str}
)
_OptionalArtifactStoreTypeDef = TypedDict(
    "_OptionalArtifactStoreTypeDef", {"encryptionKey": "EncryptionKeyTypeDef"}, total=False
)


class ArtifactStoreTypeDef(_RequiredArtifactStoreTypeDef, _OptionalArtifactStoreTypeDef):
    pass


class ArtifactTypeDef(TypedDict, total=False):
    name: str
    revision: str
    location: "ArtifactLocationTypeDef"


BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef", {"name": str, "type": Literal["Schedule"]}
)


class CreateCustomActionTypeOutputTypeDef(TypedDict):
    actionType: "ActionTypeTypeDef"
    tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreatePipelineOutputTypeDef(TypedDict):
    pipeline: "PipelineDeclarationTypeDef"
    tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredCurrentRevisionTypeDef(TypedDict):
    revision: str
    changeIdentifier: str


class CurrentRevisionTypeDef(_RequiredCurrentRevisionTypeDef, total=False):
    created: datetime
    revisionSummary: str


EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"id": str, "type": Literal["KMS"]})


class ErrorDetailsTypeDef(TypedDict, total=False):
    code: str
    message: str


class ExecutionDetailsTypeDef(TypedDict, total=False):
    summary: str
    externalExecutionId: str
    percentComplete: int


class ExecutionTriggerTypeDef(TypedDict, total=False):
    triggerType: TriggerType
    triggerDetail: str


class ExecutorConfigurationTypeDef(TypedDict, total=False):
    lambdaExecutorConfiguration: "LambdaExecutorConfigurationTypeDef"
    jobWorkerExecutorConfiguration: "JobWorkerExecutorConfigurationTypeDef"


_RequiredFailureDetailsTypeDef = TypedDict(
    "_RequiredFailureDetailsTypeDef", {"type": FailureType, "message": str}
)
_OptionalFailureDetailsTypeDef = TypedDict(
    "_OptionalFailureDetailsTypeDef", {"externalExecutionId": str}, total=False
)


class FailureDetailsTypeDef(_RequiredFailureDetailsTypeDef, _OptionalFailureDetailsTypeDef):
    pass


class GetActionTypeOutputTypeDef(TypedDict):
    actionType: "ActionTypeDeclarationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetJobDetailsOutputTypeDef(TypedDict):
    jobDetails: "JobDetailsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecution: "PipelineExecutionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetPipelineOutputTypeDef(TypedDict):
    pipeline: "PipelineDeclarationTypeDef"
    metadata: "PipelineMetadataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetPipelineStateOutputTypeDef(TypedDict):
    pipelineName: str
    pipelineVersion: int
    stageStates: List["StageStateTypeDef"]
    created: datetime
    updated: datetime
    ResponseMetadata: "ResponseMetadata"


class GetThirdPartyJobDetailsOutputTypeDef(TypedDict):
    jobDetails: "ThirdPartyJobDetailsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class InputArtifactTypeDef(TypedDict):
    name: str


class JobDataTypeDef(TypedDict, total=False):
    actionTypeId: "ActionTypeIdTypeDef"
    actionConfiguration: "ActionConfigurationTypeDef"
    pipelineContext: "PipelineContextTypeDef"
    inputArtifacts: List["ArtifactTypeDef"]
    outputArtifacts: List["ArtifactTypeDef"]
    artifactCredentials: "AWSSessionCredentialsTypeDef"
    continuationToken: str
    encryptionKey: "EncryptionKeyTypeDef"


JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef", {"id": str, "data": "JobDataTypeDef", "accountId": str}, total=False
)

JobTypeDef = TypedDict(
    "JobTypeDef", {"id": str, "data": "JobDataTypeDef", "nonce": str, "accountId": str}, total=False
)


class JobWorkerExecutorConfigurationTypeDef(TypedDict, total=False):
    pollingAccounts: List[str]
    pollingServicePrincipals: List[str]


class LambdaExecutorConfigurationTypeDef(TypedDict):
    lambdaFunctionArn: str


class ListActionExecutionsOutputTypeDef(TypedDict):
    actionExecutionDetails: List["ActionExecutionDetailTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListActionTypesOutputTypeDef(TypedDict):
    actionTypes: List["ActionTypeTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPipelineExecutionsOutputTypeDef(TypedDict):
    pipelineExecutionSummaries: List["PipelineExecutionSummaryTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPipelinesOutputTypeDef(TypedDict):
    pipelines: List["PipelineSummaryTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List["TagTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListWebhookItemTypeDef(TypedDict):
    definition: "WebhookDefinitionTypeDef"
    url: str


class ListWebhookItemTypeDef(_RequiredListWebhookItemTypeDef, total=False):
    errorMessage: str
    errorCode: str
    lastTriggered: datetime
    arn: str
    tags: List["TagTypeDef"]


class ListWebhooksOutputTypeDef(TypedDict):
    webhooks: List["ListWebhookItemTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class OutputArtifactTypeDef(TypedDict):
    name: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PipelineContextTypeDef(TypedDict, total=False):
    pipelineName: str
    stage: "StageContextTypeDef"
    action: "ActionContextTypeDef"
    pipelineArn: str
    pipelineExecutionId: str


class _RequiredPipelineDeclarationTypeDef(TypedDict):
    name: str
    roleArn: str
    stages: List["StageDeclarationTypeDef"]


class PipelineDeclarationTypeDef(_RequiredPipelineDeclarationTypeDef, total=False):
    artifactStore: "ArtifactStoreTypeDef"
    artifactStores: Dict[str, "ArtifactStoreTypeDef"]
    version: int


class PipelineExecutionSummaryTypeDef(TypedDict, total=False):
    pipelineExecutionId: str
    status: PipelineExecutionStatus
    startTime: datetime
    lastUpdateTime: datetime
    sourceRevisions: List["SourceRevisionTypeDef"]
    trigger: "ExecutionTriggerTypeDef"
    stopTrigger: "StopExecutionTriggerTypeDef"


class PipelineExecutionTypeDef(TypedDict, total=False):
    pipelineName: str
    pipelineVersion: int
    pipelineExecutionId: str
    status: PipelineExecutionStatus
    statusSummary: str
    artifactRevisions: List["ArtifactRevisionTypeDef"]


class PipelineMetadataTypeDef(TypedDict, total=False):
    pipelineArn: str
    created: datetime
    updated: datetime


class PipelineSummaryTypeDef(TypedDict, total=False):
    name: str
    version: int
    created: datetime
    updated: datetime


class PollForJobsOutputTypeDef(TypedDict):
    jobs: List["JobTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PollForThirdPartyJobsOutputTypeDef(TypedDict):
    jobs: List["ThirdPartyJobTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PutActionRevisionOutputTypeDef(TypedDict):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class PutApprovalResultOutputTypeDef(TypedDict):
    approvedAt: datetime
    ResponseMetadata: "ResponseMetadata"


class PutWebhookOutputTypeDef(TypedDict):
    webhook: "ListWebhookItemTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RetryStageExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class S3ArtifactLocationTypeDef(TypedDict):
    bucketName: str
    objectKey: str


class S3LocationTypeDef(TypedDict, total=False):
    bucket: str
    key: str


class _RequiredSourceRevisionTypeDef(TypedDict):
    actionName: str


class SourceRevisionTypeDef(_RequiredSourceRevisionTypeDef, total=False):
    revisionId: str
    revisionSummary: str
    revisionUrl: str


class StageContextTypeDef(TypedDict, total=False):
    name: str


class _RequiredStageDeclarationTypeDef(TypedDict):
    name: str
    actions: List["ActionDeclarationTypeDef"]


class StageDeclarationTypeDef(_RequiredStageDeclarationTypeDef, total=False):
    blockers: List["BlockerDeclarationTypeDef"]


class StageExecutionTypeDef(TypedDict):
    pipelineExecutionId: str
    status: StageExecutionStatus


class StageStateTypeDef(TypedDict, total=False):
    stageName: str
    inboundExecution: "StageExecutionTypeDef"
    inboundTransitionState: "TransitionStateTypeDef"
    actionStates: List["ActionStateTypeDef"]
    latestExecution: "StageExecutionTypeDef"


class StartPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class StopExecutionTriggerTypeDef(TypedDict, total=False):
    reason: str


class StopPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class TagTypeDef(TypedDict):
    key: str
    value: str


class ThirdPartyJobDataTypeDef(TypedDict, total=False):
    actionTypeId: "ActionTypeIdTypeDef"
    actionConfiguration: "ActionConfigurationTypeDef"
    pipelineContext: "PipelineContextTypeDef"
    inputArtifacts: List["ArtifactTypeDef"]
    outputArtifacts: List["ArtifactTypeDef"]
    artifactCredentials: "AWSSessionCredentialsTypeDef"
    continuationToken: str
    encryptionKey: "EncryptionKeyTypeDef"


ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {"id": str, "data": "ThirdPartyJobDataTypeDef", "nonce": str},
    total=False,
)


class ThirdPartyJobTypeDef(TypedDict, total=False):
    clientId: str
    jobId: str


class TransitionStateTypeDef(TypedDict, total=False):
    enabled: bool
    lastChangedBy: str
    lastChangedAt: datetime
    disabledReason: str


class UpdatePipelineOutputTypeDef(TypedDict):
    pipeline: "PipelineDeclarationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class WebhookAuthConfigurationTypeDef(TypedDict, total=False):
    AllowedIPRange: str
    SecretToken: str


class WebhookDefinitionTypeDef(TypedDict):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List["WebhookFilterRuleTypeDef"]
    authentication: WebhookAuthenticationType
    authenticationConfiguration: "WebhookAuthConfigurationTypeDef"


class _RequiredWebhookFilterRuleTypeDef(TypedDict):
    jsonPath: str


class WebhookFilterRuleTypeDef(_RequiredWebhookFilterRuleTypeDef, total=False):
    matchEquals: str
