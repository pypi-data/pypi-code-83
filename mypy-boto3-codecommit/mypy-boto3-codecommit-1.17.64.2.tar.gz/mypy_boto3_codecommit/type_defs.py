"""
Type annotations for codecommit service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_codecommit.literals import (
    ApprovalState,
    ChangeTypeEnum,
    FileModeTypeEnum,
    MergeOptionTypeEnum,
    ObjectTypeEnum,
    OverrideStatus,
    PullRequestEventType,
    PullRequestStatusEnum,
    RelativeFileVersionEnum,
    ReplacementTypeEnum,
    RepositoryTriggerEventEnum,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "ApprovalRuleTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictResolutionTypeDef",
    "ConflictTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileEntryTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "DifferenceTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "IsBinaryFileTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LocationTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "PutFileEntryTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "ResponseMetadata",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
    "UserInfoTypeDef",
)


class ApprovalRuleEventMetadataTypeDef(TypedDict, total=False):
    approvalRuleName: str
    approvalRuleId: str
    approvalRuleContent: str


class ApprovalRuleOverriddenEventMetadataTypeDef(TypedDict, total=False):
    revisionId: str
    overrideStatus: OverrideStatus


class ApprovalRuleTemplateTypeDef(TypedDict, total=False):
    approvalRuleTemplateId: str
    approvalRuleTemplateName: str
    approvalRuleTemplateDescription: str
    approvalRuleTemplateContent: str
    ruleContentSha256: str
    lastModifiedDate: datetime
    creationDate: datetime
    lastModifiedUser: str


class ApprovalRuleTypeDef(TypedDict, total=False):
    approvalRuleId: str
    approvalRuleName: str
    approvalRuleContent: str
    ruleContentSha256: str
    lastModifiedDate: datetime
    creationDate: datetime
    lastModifiedUser: str
    originApprovalRuleTemplate: "OriginApprovalRuleTemplateTypeDef"


class ApprovalStateChangedEventMetadataTypeDef(TypedDict, total=False):
    revisionId: str
    approvalStatus: ApprovalState


class ApprovalTypeDef(TypedDict, total=False):
    userArn: str
    approvalState: ApprovalState


class BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef(TypedDict, total=False):
    repositoryName: str
    errorCode: str
    errorMessage: str


class BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef(TypedDict):
    associatedRepositoryNames: List[str]
    errors: List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchDescribeMergeConflictsErrorTypeDef(TypedDict):
    filePath: str
    exceptionName: str
    message: str


class BatchDescribeMergeConflictsOutputTypeDef(TypedDict):
    conflicts: List["ConflictTypeDef"]
    nextToken: str
    errors: List["BatchDescribeMergeConflictsErrorTypeDef"]
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: "ResponseMetadata"


class BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef(TypedDict, total=False):
    repositoryName: str
    errorCode: str
    errorMessage: str


class BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef(TypedDict):
    disassociatedRepositoryNames: List[str]
    errors: List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetCommitsErrorTypeDef(TypedDict, total=False):
    commitId: str
    errorCode: str
    errorMessage: str


class BatchGetCommitsOutputTypeDef(TypedDict):
    commits: List["CommitTypeDef"]
    errors: List["BatchGetCommitsErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetRepositoriesOutputTypeDef(TypedDict):
    repositories: List["RepositoryMetadataTypeDef"]
    repositoriesNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BlobMetadataTypeDef(TypedDict, total=False):
    blobId: str
    path: str
    mode: str


class BranchInfoTypeDef(TypedDict, total=False):
    branchName: str
    commitId: str


class CommentTypeDef(TypedDict, total=False):
    commentId: str
    content: str
    inReplyTo: str
    creationDate: datetime
    lastModifiedDate: datetime
    authorArn: str
    deleted: bool
    clientRequestToken: str
    callerReactions: List[str]
    reactionCounts: Dict[str, int]


class CommentsForComparedCommitTypeDef(TypedDict, total=False):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: "LocationTypeDef"
    comments: List["CommentTypeDef"]


class CommentsForPullRequestTypeDef(TypedDict, total=False):
    pullRequestId: str
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: "LocationTypeDef"
    comments: List["CommentTypeDef"]


class CommitTypeDef(TypedDict, total=False):
    commitId: str
    treeId: str
    parents: List[str]
    message: str
    author: "UserInfoTypeDef"
    committer: "UserInfoTypeDef"
    additionalData: str


class ConflictMetadataTypeDef(TypedDict, total=False):
    filePath: str
    fileSizes: "FileSizesTypeDef"
    fileModes: "FileModesTypeDef"
    objectTypes: "ObjectTypesTypeDef"
    numberOfConflicts: int
    isBinaryFile: "IsBinaryFileTypeDef"
    contentConflict: bool
    fileModeConflict: bool
    objectTypeConflict: bool
    mergeOperations: "MergeOperationsTypeDef"


class ConflictResolutionTypeDef(TypedDict, total=False):
    replaceContents: List["ReplaceContentEntryTypeDef"]
    deleteFiles: List["DeleteFileEntryTypeDef"]
    setFileModes: List["SetFileModeEntryTypeDef"]


class ConflictTypeDef(TypedDict, total=False):
    conflictMetadata: "ConflictMetadataTypeDef"
    mergeHunks: List["MergeHunkTypeDef"]


class CreateApprovalRuleTemplateOutputTypeDef(TypedDict):
    approvalRuleTemplate: "ApprovalRuleTemplateTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateCommitOutputTypeDef(TypedDict):
    commitId: str
    treeId: str
    filesAdded: List["FileMetadataTypeDef"]
    filesUpdated: List["FileMetadataTypeDef"]
    filesDeleted: List["FileMetadataTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreatePullRequestApprovalRuleOutputTypeDef(TypedDict):
    approvalRule: "ApprovalRuleTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreatePullRequestOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateRepositoryOutputTypeDef(TypedDict):
    repositoryMetadata: "RepositoryMetadataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateUnreferencedMergeCommitOutputTypeDef(TypedDict):
    commitId: str
    treeId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteApprovalRuleTemplateOutputTypeDef(TypedDict):
    approvalRuleTemplateId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteBranchOutputTypeDef(TypedDict):
    deletedBranch: "BranchInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteCommentContentOutputTypeDef(TypedDict):
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteFileEntryTypeDef(TypedDict):
    filePath: str


class DeleteFileOutputTypeDef(TypedDict):
    commitId: str
    blobId: str
    treeId: str
    filePath: str
    ResponseMetadata: "ResponseMetadata"


class DeletePullRequestApprovalRuleOutputTypeDef(TypedDict):
    approvalRuleId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteRepositoryOutputTypeDef(TypedDict):
    repositoryId: str
    ResponseMetadata: "ResponseMetadata"


class DescribeMergeConflictsOutputTypeDef(TypedDict):
    conflictMetadata: "ConflictMetadataTypeDef"
    mergeHunks: List["MergeHunkTypeDef"]
    nextToken: str
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    ResponseMetadata: "ResponseMetadata"


class DescribePullRequestEventsOutputTypeDef(TypedDict):
    pullRequestEvents: List["PullRequestEventTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class DifferenceTypeDef(TypedDict, total=False):
    beforeBlob: "BlobMetadataTypeDef"
    afterBlob: "BlobMetadataTypeDef"
    changeType: ChangeTypeEnum


class EvaluatePullRequestApprovalRulesOutputTypeDef(TypedDict):
    evaluation: "EvaluationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class EvaluationTypeDef(TypedDict, total=False):
    approved: bool
    overridden: bool
    approvalRulesSatisfied: List[str]
    approvalRulesNotSatisfied: List[str]


class FileMetadataTypeDef(TypedDict, total=False):
    absolutePath: str
    blobId: str
    fileMode: FileModeTypeEnum


class FileModesTypeDef(TypedDict, total=False):
    source: FileModeTypeEnum
    destination: FileModeTypeEnum
    base: FileModeTypeEnum


class FileSizesTypeDef(TypedDict, total=False):
    source: int
    destination: int
    base: int


class FileTypeDef(TypedDict, total=False):
    blobId: str
    absolutePath: str
    relativePath: str
    fileMode: FileModeTypeEnum


class FolderTypeDef(TypedDict, total=False):
    treeId: str
    absolutePath: str
    relativePath: str


class GetApprovalRuleTemplateOutputTypeDef(TypedDict):
    approvalRuleTemplate: "ApprovalRuleTemplateTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBlobOutputTypeDef(TypedDict):
    content: Union[bytes, IO[bytes]]
    ResponseMetadata: "ResponseMetadata"


class GetBranchOutputTypeDef(TypedDict):
    branch: "BranchInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetCommentOutputTypeDef(TypedDict):
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetCommentReactionsOutputTypeDef(TypedDict):
    reactionsForComment: List["ReactionForCommentTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetCommentsForComparedCommitOutputTypeDef(TypedDict):
    commentsForComparedCommitData: List["CommentsForComparedCommitTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetCommentsForPullRequestOutputTypeDef(TypedDict):
    commentsForPullRequestData: List["CommentsForPullRequestTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetCommitOutputTypeDef(TypedDict):
    commit: "CommitTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDifferencesOutputTypeDef(TypedDict):
    differences: List["DifferenceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetFileOutputTypeDef(TypedDict):
    commitId: str
    blobId: str
    filePath: str
    fileMode: FileModeTypeEnum
    fileSize: int
    fileContent: Union[bytes, IO[bytes]]
    ResponseMetadata: "ResponseMetadata"


class GetFolderOutputTypeDef(TypedDict):
    commitId: str
    folderPath: str
    treeId: str
    subFolders: List["FolderTypeDef"]
    files: List["FileTypeDef"]
    symbolicLinks: List["SymbolicLinkTypeDef"]
    subModules: List["SubModuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetMergeCommitOutputTypeDef(TypedDict):
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    mergedCommitId: str
    ResponseMetadata: "ResponseMetadata"


class GetMergeConflictsOutputTypeDef(TypedDict):
    mergeable: bool
    destinationCommitId: str
    sourceCommitId: str
    baseCommitId: str
    conflictMetadataList: List["ConflictMetadataTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetMergeOptionsOutputTypeDef(TypedDict):
    mergeOptions: List[MergeOptionTypeEnum]
    sourceCommitId: str
    destinationCommitId: str
    baseCommitId: str
    ResponseMetadata: "ResponseMetadata"


class GetPullRequestApprovalStatesOutputTypeDef(TypedDict):
    approvals: List["ApprovalTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetPullRequestOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetPullRequestOverrideStateOutputTypeDef(TypedDict):
    overridden: bool
    overrider: str
    ResponseMetadata: "ResponseMetadata"


class GetRepositoryOutputTypeDef(TypedDict):
    repositoryMetadata: "RepositoryMetadataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetRepositoryTriggersOutputTypeDef(TypedDict):
    configurationId: str
    triggers: List["RepositoryTriggerTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class IsBinaryFileTypeDef(TypedDict, total=False):
    source: bool
    destination: bool
    base: bool


class ListApprovalRuleTemplatesOutputTypeDef(TypedDict):
    approvalRuleTemplateNames: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef(TypedDict):
    approvalRuleTemplateNames: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBranchesOutputTypeDef(TypedDict):
    branches: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPullRequestsOutputTypeDef(TypedDict):
    pullRequestIds: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRepositoriesForApprovalRuleTemplateOutputTypeDef(TypedDict):
    repositoryNames: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRepositoriesOutputTypeDef(TypedDict):
    repositories: List["RepositoryNameIdPairTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class LocationTypeDef(TypedDict, total=False):
    filePath: str
    filePosition: int
    relativeFileVersion: RelativeFileVersionEnum


class MergeBranchesByFastForwardOutputTypeDef(TypedDict):
    commitId: str
    treeId: str
    ResponseMetadata: "ResponseMetadata"


class MergeBranchesBySquashOutputTypeDef(TypedDict):
    commitId: str
    treeId: str
    ResponseMetadata: "ResponseMetadata"


class MergeBranchesByThreeWayOutputTypeDef(TypedDict):
    commitId: str
    treeId: str
    ResponseMetadata: "ResponseMetadata"


class MergeHunkDetailTypeDef(TypedDict, total=False):
    startLine: int
    endLine: int
    hunkContent: str


class MergeHunkTypeDef(TypedDict, total=False):
    isConflict: bool
    source: "MergeHunkDetailTypeDef"
    destination: "MergeHunkDetailTypeDef"
    base: "MergeHunkDetailTypeDef"


class MergeMetadataTypeDef(TypedDict, total=False):
    isMerged: bool
    mergedBy: str
    mergeCommitId: str
    mergeOption: MergeOptionTypeEnum


class MergeOperationsTypeDef(TypedDict, total=False):
    source: ChangeTypeEnum
    destination: ChangeTypeEnum


class MergePullRequestByFastForwardOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class MergePullRequestBySquashOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class MergePullRequestByThreeWayOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ObjectTypesTypeDef(TypedDict, total=False):
    source: ObjectTypeEnum
    destination: ObjectTypeEnum
    base: ObjectTypeEnum


class OriginApprovalRuleTemplateTypeDef(TypedDict, total=False):
    approvalRuleTemplateId: str
    approvalRuleTemplateName: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PostCommentForComparedCommitOutputTypeDef(TypedDict):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: "LocationTypeDef"
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PostCommentForPullRequestOutputTypeDef(TypedDict):
    repositoryName: str
    pullRequestId: str
    beforeCommitId: str
    afterCommitId: str
    beforeBlobId: str
    afterBlobId: str
    location: "LocationTypeDef"
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PostCommentReplyOutputTypeDef(TypedDict):
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PullRequestCreatedEventMetadataTypeDef(TypedDict, total=False):
    repositoryName: str
    sourceCommitId: str
    destinationCommitId: str
    mergeBase: str


class PullRequestEventTypeDef(TypedDict, total=False):
    pullRequestId: str
    eventDate: datetime
    pullRequestEventType: PullRequestEventType
    actorArn: str
    pullRequestCreatedEventMetadata: "PullRequestCreatedEventMetadataTypeDef"
    pullRequestStatusChangedEventMetadata: "PullRequestStatusChangedEventMetadataTypeDef"
    pullRequestSourceReferenceUpdatedEventMetadata: "PullRequestSourceReferenceUpdatedEventMetadataTypeDef"
    pullRequestMergedStateChangedEventMetadata: "PullRequestMergedStateChangedEventMetadataTypeDef"
    approvalRuleEventMetadata: "ApprovalRuleEventMetadataTypeDef"
    approvalStateChangedEventMetadata: "ApprovalStateChangedEventMetadataTypeDef"
    approvalRuleOverriddenEventMetadata: "ApprovalRuleOverriddenEventMetadataTypeDef"


class PullRequestMergedStateChangedEventMetadataTypeDef(TypedDict, total=False):
    repositoryName: str
    destinationReference: str
    mergeMetadata: "MergeMetadataTypeDef"


class PullRequestSourceReferenceUpdatedEventMetadataTypeDef(TypedDict, total=False):
    repositoryName: str
    beforeCommitId: str
    afterCommitId: str
    mergeBase: str


class PullRequestStatusChangedEventMetadataTypeDef(TypedDict, total=False):
    pullRequestStatus: PullRequestStatusEnum


class PullRequestTargetTypeDef(TypedDict, total=False):
    repositoryName: str
    sourceReference: str
    destinationReference: str
    destinationCommit: str
    sourceCommit: str
    mergeBase: str
    mergeMetadata: "MergeMetadataTypeDef"


class PullRequestTypeDef(TypedDict, total=False):
    pullRequestId: str
    title: str
    description: str
    lastActivityDate: datetime
    creationDate: datetime
    pullRequestStatus: PullRequestStatusEnum
    authorArn: str
    pullRequestTargets: List["PullRequestTargetTypeDef"]
    clientRequestToken: str
    revisionId: str
    approvalRules: List["ApprovalRuleTypeDef"]


class _RequiredPutFileEntryTypeDef(TypedDict):
    filePath: str


class PutFileEntryTypeDef(_RequiredPutFileEntryTypeDef, total=False):
    fileMode: FileModeTypeEnum
    fileContent: Union[bytes, IO[bytes]]
    sourceFile: "SourceFileSpecifierTypeDef"


class PutFileOutputTypeDef(TypedDict):
    commitId: str
    blobId: str
    treeId: str
    ResponseMetadata: "ResponseMetadata"


class PutRepositoryTriggersOutputTypeDef(TypedDict):
    configurationId: str
    ResponseMetadata: "ResponseMetadata"


class ReactionForCommentTypeDef(TypedDict, total=False):
    reaction: "ReactionValueFormatsTypeDef"
    reactionUsers: List[str]
    reactionsFromDeletedUsersCount: int


class ReactionValueFormatsTypeDef(TypedDict, total=False):
    emoji: str
    shortCode: str
    unicode: str


class _RequiredReplaceContentEntryTypeDef(TypedDict):
    filePath: str
    replacementType: ReplacementTypeEnum


class ReplaceContentEntryTypeDef(_RequiredReplaceContentEntryTypeDef, total=False):
    content: Union[bytes, IO[bytes]]
    fileMode: FileModeTypeEnum


class RepositoryMetadataTypeDef(TypedDict, total=False):
    accountId: str
    repositoryId: str
    repositoryName: str
    repositoryDescription: str
    defaultBranch: str
    lastModifiedDate: datetime
    creationDate: datetime
    cloneUrlHttp: str
    cloneUrlSsh: str
    Arn: str


class RepositoryNameIdPairTypeDef(TypedDict, total=False):
    repositoryName: str
    repositoryId: str


class RepositoryTriggerExecutionFailureTypeDef(TypedDict, total=False):
    trigger: str
    failureMessage: str


class _RequiredRepositoryTriggerTypeDef(TypedDict):
    name: str
    destinationArn: str
    events: List[RepositoryTriggerEventEnum]


class RepositoryTriggerTypeDef(_RequiredRepositoryTriggerTypeDef, total=False):
    customData: str
    branches: List[str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SetFileModeEntryTypeDef(TypedDict):
    filePath: str
    fileMode: FileModeTypeEnum


class _RequiredSourceFileSpecifierTypeDef(TypedDict):
    filePath: str


class SourceFileSpecifierTypeDef(_RequiredSourceFileSpecifierTypeDef, total=False):
    isMove: bool


class SubModuleTypeDef(TypedDict, total=False):
    commitId: str
    absolutePath: str
    relativePath: str


class SymbolicLinkTypeDef(TypedDict, total=False):
    blobId: str
    absolutePath: str
    relativePath: str
    fileMode: FileModeTypeEnum


class _RequiredTargetTypeDef(TypedDict):
    repositoryName: str
    sourceReference: str


class TargetTypeDef(_RequiredTargetTypeDef, total=False):
    destinationReference: str


class TestRepositoryTriggersOutputTypeDef(TypedDict):
    successfulExecutions: List[str]
    failedExecutions: List["RepositoryTriggerExecutionFailureTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UpdateApprovalRuleTemplateContentOutputTypeDef(TypedDict):
    approvalRuleTemplate: "ApprovalRuleTemplateTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateApprovalRuleTemplateDescriptionOutputTypeDef(TypedDict):
    approvalRuleTemplate: "ApprovalRuleTemplateTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateApprovalRuleTemplateNameOutputTypeDef(TypedDict):
    approvalRuleTemplate: "ApprovalRuleTemplateTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateCommentOutputTypeDef(TypedDict):
    comment: "CommentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdatePullRequestApprovalRuleContentOutputTypeDef(TypedDict):
    approvalRule: "ApprovalRuleTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdatePullRequestDescriptionOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdatePullRequestStatusOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdatePullRequestTitleOutputTypeDef(TypedDict):
    pullRequest: "PullRequestTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UserInfoTypeDef(TypedDict, total=False):
    name: str
    email: str
    date: str
