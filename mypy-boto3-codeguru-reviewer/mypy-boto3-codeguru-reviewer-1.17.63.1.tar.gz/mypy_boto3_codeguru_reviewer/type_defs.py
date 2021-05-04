"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import AssociateRepositoryResponseTypeDef

    data: AssociateRepositoryResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_codeguru_reviewer.literals import (
    EncryptionOption,
    JobState,
    ProviderType,
    Reaction,
    RepositoryAssociationState,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRepositoryResponseTypeDef",
    "CodeCommitRepositoryTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "CodeReviewTypeTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "KMSKeyDetailsTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "RecommendationFeedbackTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryAnalysisTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "RepositoryAssociationTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "RepositoryTypeDef",
    "SourceCodeTypeTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
)


class AssociateRepositoryResponseTypeDef(TypedDict, total=False):
    RepositoryAssociation: "RepositoryAssociationTypeDef"
    Tags: Dict[str, str]


class CodeCommitRepositoryTypeDef(TypedDict):
    Name: str


CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderType,
        "State": JobState,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "MetricsSummary": "MetricsSummaryTypeDef",
    },
    total=False,
)

CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": str,
        "CodeReviewArn": str,
        "RepositoryName": str,
        "Owner": str,
        "ProviderType": ProviderType,
        "State": JobState,
        "StateReason": str,
        "CreatedTimeStamp": datetime,
        "LastUpdatedTimeStamp": datetime,
        "Type": TypeType,
        "PullRequestId": str,
        "SourceCodeType": "SourceCodeTypeTypeDef",
        "AssociationArn": str,
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)


class CodeReviewTypeTypeDef(TypedDict):
    RepositoryAnalysis: "RepositoryAnalysisTypeDef"


class CommitDiffSourceCodeTypeTypeDef(TypedDict, total=False):
    SourceCommit: str
    DestinationCommit: str


class CreateCodeReviewResponseTypeDef(TypedDict, total=False):
    CodeReview: "CodeReviewTypeDef"


class DescribeCodeReviewResponseTypeDef(TypedDict, total=False):
    CodeReview: "CodeReviewTypeDef"


class DescribeRecommendationFeedbackResponseTypeDef(TypedDict, total=False):
    RecommendationFeedback: "RecommendationFeedbackTypeDef"


class DescribeRepositoryAssociationResponseTypeDef(TypedDict, total=False):
    RepositoryAssociation: "RepositoryAssociationTypeDef"
    Tags: Dict[str, str]


class DisassociateRepositoryResponseTypeDef(TypedDict, total=False):
    RepositoryAssociation: "RepositoryAssociationTypeDef"
    Tags: Dict[str, str]


class KMSKeyDetailsTypeDef(TypedDict, total=False):
    KMSKeyId: str
    EncryptionOption: EncryptionOption


class ListCodeReviewsResponseTypeDef(TypedDict, total=False):
    CodeReviewSummaries: List["CodeReviewSummaryTypeDef"]
    NextToken: str


class ListRecommendationFeedbackResponseTypeDef(TypedDict, total=False):
    RecommendationFeedbackSummaries: List["RecommendationFeedbackSummaryTypeDef"]
    NextToken: str


class ListRecommendationsResponseTypeDef(TypedDict, total=False):
    RecommendationSummaries: List["RecommendationSummaryTypeDef"]
    NextToken: str


class ListRepositoryAssociationsResponseTypeDef(TypedDict, total=False):
    RepositoryAssociationSummaries: List["RepositoryAssociationSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class MetricsSummaryTypeDef(TypedDict, total=False):
    MeteredLinesOfCodeCount: int
    FindingsCount: int


class MetricsTypeDef(TypedDict, total=False):
    MeteredLinesOfCodeCount: int
    FindingsCount: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RecommendationFeedbackSummaryTypeDef(TypedDict, total=False):
    RecommendationId: str
    Reactions: List[Reaction]
    UserId: str


class RecommendationFeedbackTypeDef(TypedDict, total=False):
    CodeReviewArn: str
    RecommendationId: str
    Reactions: List[Reaction]
    UserId: str
    CreatedTimeStamp: datetime
    LastUpdatedTimeStamp: datetime


class RecommendationSummaryTypeDef(TypedDict, total=False):
    FilePath: str
    RecommendationId: str
    StartLine: int
    EndLine: int
    Description: str


class RepositoryAnalysisTypeDef(TypedDict):
    RepositoryHead: "RepositoryHeadSourceCodeTypeTypeDef"


class RepositoryAssociationSummaryTypeDef(TypedDict, total=False):
    AssociationArn: str
    ConnectionArn: str
    LastUpdatedTimeStamp: datetime
    AssociationId: str
    Name: str
    Owner: str
    ProviderType: ProviderType
    State: RepositoryAssociationState


class RepositoryAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    AssociationArn: str
    ConnectionArn: str
    Name: str
    Owner: str
    ProviderType: ProviderType
    State: RepositoryAssociationState
    StateReason: str
    LastUpdatedTimeStamp: datetime
    CreatedTimeStamp: datetime
    KMSKeyDetails: "KMSKeyDetailsTypeDef"


class RepositoryHeadSourceCodeTypeTypeDef(TypedDict):
    BranchName: str


class RepositoryTypeDef(TypedDict, total=False):
    CodeCommit: "CodeCommitRepositoryTypeDef"
    Bitbucket: "ThirdPartySourceRepositoryTypeDef"
    GitHubEnterpriseServer: "ThirdPartySourceRepositoryTypeDef"


class SourceCodeTypeTypeDef(TypedDict, total=False):
    CommitDiff: "CommitDiffSourceCodeTypeTypeDef"
    RepositoryHead: "RepositoryHeadSourceCodeTypeTypeDef"


class ThirdPartySourceRepositoryTypeDef(TypedDict):
    Name: str
    ConnectionArn: str
    Owner: str
