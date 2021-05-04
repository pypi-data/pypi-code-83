"""
Type annotations for codecommit service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecommit/literals.html)

Usage::

    ```python
    from mypy_boto3_codecommit.literals import ApprovalState

    data: ApprovalState = "APPROVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApprovalState",
    "ChangeTypeEnum",
    "ConflictDetailLevelTypeEnum",
    "ConflictResolutionStrategyTypeEnum",
    "DescribePullRequestEventsPaginatorName",
    "FileModeTypeEnum",
    "GetCommentsForComparedCommitPaginatorName",
    "GetCommentsForPullRequestPaginatorName",
    "GetDifferencesPaginatorName",
    "ListBranchesPaginatorName",
    "ListPullRequestsPaginatorName",
    "ListRepositoriesPaginatorName",
    "MergeOptionTypeEnum",
    "ObjectTypeEnum",
    "OrderEnum",
    "OverrideStatus",
    "PullRequestEventType",
    "PullRequestStatusEnum",
    "RelativeFileVersionEnum",
    "ReplacementTypeEnum",
    "RepositoryTriggerEventEnum",
    "SortByEnum",
)


ApprovalState = Literal["APPROVE", "REVOKE"]
ChangeTypeEnum = Literal["A", "D", "M"]
ConflictDetailLevelTypeEnum = Literal["FILE_LEVEL", "LINE_LEVEL"]
ConflictResolutionStrategyTypeEnum = Literal[
    "ACCEPT_DESTINATION", "ACCEPT_SOURCE", "AUTOMERGE", "NONE"
]
DescribePullRequestEventsPaginatorName = Literal["describe_pull_request_events"]
FileModeTypeEnum = Literal["EXECUTABLE", "NORMAL", "SYMLINK"]
GetCommentsForComparedCommitPaginatorName = Literal["get_comments_for_compared_commit"]
GetCommentsForPullRequestPaginatorName = Literal["get_comments_for_pull_request"]
GetDifferencesPaginatorName = Literal["get_differences"]
ListBranchesPaginatorName = Literal["list_branches"]
ListPullRequestsPaginatorName = Literal["list_pull_requests"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
MergeOptionTypeEnum = Literal["FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE"]
ObjectTypeEnum = Literal["DIRECTORY", "FILE", "GIT_LINK", "SYMBOLIC_LINK"]
OrderEnum = Literal["ascending", "descending"]
OverrideStatus = Literal["OVERRIDE", "REVOKE"]
PullRequestEventType = Literal[
    "PULL_REQUEST_APPROVAL_RULE_CREATED",
    "PULL_REQUEST_APPROVAL_RULE_DELETED",
    "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN",
    "PULL_REQUEST_APPROVAL_RULE_UPDATED",
    "PULL_REQUEST_APPROVAL_STATE_CHANGED",
    "PULL_REQUEST_CREATED",
    "PULL_REQUEST_MERGE_STATE_CHANGED",
    "PULL_REQUEST_SOURCE_REFERENCE_UPDATED",
    "PULL_REQUEST_STATUS_CHANGED",
]
PullRequestStatusEnum = Literal["CLOSED", "OPEN"]
RelativeFileVersionEnum = Literal["AFTER", "BEFORE"]
ReplacementTypeEnum = Literal["KEEP_BASE", "KEEP_DESTINATION", "KEEP_SOURCE", "USE_NEW_CONTENT"]
RepositoryTriggerEventEnum = Literal["all", "createReference", "deleteReference", "updateReference"]
SortByEnum = Literal["lastModifiedDate", "repositoryName"]
