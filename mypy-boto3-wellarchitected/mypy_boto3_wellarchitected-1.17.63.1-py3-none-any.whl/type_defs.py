"""
Type annotations for wellarchitected service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wellarchitected.type_defs import AnswerSummaryTypeDef

    data: AnswerSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_wellarchitected.literals import (
    DifferenceStatus,
    LensStatus,
    NotificationType,
    PermissionType,
    Risk,
    ShareStatus,
    WorkloadEnvironment,
    WorkloadImprovementStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnswerSummaryTypeDef",
    "AnswerTypeDef",
    "ChoiceTypeDef",
    "CreateMilestoneOutputTypeDef",
    "CreateWorkloadOutputTypeDef",
    "CreateWorkloadShareOutputTypeDef",
    "GetAnswerOutputTypeDef",
    "GetLensReviewOutputTypeDef",
    "GetLensReviewReportOutputTypeDef",
    "GetLensVersionDifferenceOutputTypeDef",
    "GetMilestoneOutputTypeDef",
    "GetWorkloadOutputTypeDef",
    "ImprovementSummaryTypeDef",
    "LensReviewReportTypeDef",
    "LensReviewSummaryTypeDef",
    "LensReviewTypeDef",
    "LensSummaryTypeDef",
    "LensUpgradeSummaryTypeDef",
    "ListAnswersOutputTypeDef",
    "ListLensReviewImprovementsOutputTypeDef",
    "ListLensReviewsOutputTypeDef",
    "ListLensesOutputTypeDef",
    "ListMilestonesOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "ListShareInvitationsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkloadSharesOutputTypeDef",
    "ListWorkloadsOutputTypeDef",
    "MilestoneSummaryTypeDef",
    "MilestoneTypeDef",
    "NotificationSummaryTypeDef",
    "PillarDifferenceTypeDef",
    "PillarReviewSummaryTypeDef",
    "QuestionDifferenceTypeDef",
    "ResponseMetadata",
    "ShareInvitationSummaryTypeDef",
    "ShareInvitationTypeDef",
    "UpdateAnswerOutputTypeDef",
    "UpdateLensReviewOutputTypeDef",
    "UpdateShareInvitationOutputTypeDef",
    "UpdateWorkloadOutputTypeDef",
    "UpdateWorkloadShareOutputTypeDef",
    "VersionDifferencesTypeDef",
    "WorkloadShareSummaryTypeDef",
    "WorkloadShareTypeDef",
    "WorkloadSummaryTypeDef",
    "WorkloadTypeDef",
)


class AnswerSummaryTypeDef(TypedDict, total=False):
    QuestionId: str
    PillarId: str
    QuestionTitle: str
    Choices: List["ChoiceTypeDef"]
    SelectedChoices: List[str]
    IsApplicable: bool
    Risk: Risk


class AnswerTypeDef(TypedDict, total=False):
    QuestionId: str
    PillarId: str
    QuestionTitle: str
    QuestionDescription: str
    ImprovementPlanUrl: str
    HelpfulResourceUrl: str
    Choices: List["ChoiceTypeDef"]
    SelectedChoices: List[str]
    IsApplicable: bool
    Risk: Risk
    Notes: str


class ChoiceTypeDef(TypedDict, total=False):
    ChoiceId: str
    Title: str
    Description: str


class CreateMilestoneOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    ResponseMetadata: "ResponseMetadata"


class CreateWorkloadOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateWorkloadShareOutputTypeDef(TypedDict):
    WorkloadId: str
    ShareId: str
    ResponseMetadata: "ResponseMetadata"


class GetAnswerOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    Answer: "AnswerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetLensReviewOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReview: "LensReviewTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetLensReviewReportOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewReport: "LensReviewReportTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetLensVersionDifferenceOutputTypeDef(TypedDict):
    LensAlias: str
    BaseLensVersion: str
    LatestLensVersion: str
    VersionDifferences: "VersionDifferencesTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetMilestoneOutputTypeDef(TypedDict):
    WorkloadId: str
    Milestone: "MilestoneTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetWorkloadOutputTypeDef(TypedDict):
    Workload: "WorkloadTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ImprovementSummaryTypeDef(TypedDict, total=False):
    QuestionId: str
    PillarId: str
    QuestionTitle: str
    Risk: Risk
    ImprovementPlanUrl: str


class LensReviewReportTypeDef(TypedDict, total=False):
    LensAlias: str
    Base64String: str


class LensReviewSummaryTypeDef(TypedDict, total=False):
    LensAlias: str
    LensVersion: str
    LensName: str
    LensStatus: LensStatus
    UpdatedAt: datetime
    RiskCounts: Dict[Risk, int]


class LensReviewTypeDef(TypedDict, total=False):
    LensAlias: str
    LensVersion: str
    LensName: str
    LensStatus: LensStatus
    PillarReviewSummaries: List["PillarReviewSummaryTypeDef"]
    UpdatedAt: datetime
    Notes: str
    RiskCounts: Dict[Risk, int]
    NextToken: str


class LensSummaryTypeDef(TypedDict, total=False):
    LensAlias: str
    LensVersion: str
    LensName: str
    Description: str


class LensUpgradeSummaryTypeDef(TypedDict, total=False):
    WorkloadId: str
    WorkloadName: str
    LensAlias: str
    CurrentLensVersion: str
    LatestLensVersion: str


class ListAnswersOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    AnswerSummaries: List["AnswerSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListLensReviewImprovementsOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensAlias: str
    ImprovementSummaries: List["ImprovementSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListLensReviewsOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneNumber: int
    LensReviewSummaries: List["LensReviewSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListLensesOutputTypeDef(TypedDict):
    LensSummaries: List["LensSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListMilestonesOutputTypeDef(TypedDict):
    WorkloadId: str
    MilestoneSummaries: List["MilestoneSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListNotificationsOutputTypeDef(TypedDict):
    NotificationSummaries: List["NotificationSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListShareInvitationsOutputTypeDef(TypedDict):
    ShareInvitationSummaries: List["ShareInvitationSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class ListWorkloadSharesOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadShareSummaries: List["WorkloadShareSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListWorkloadsOutputTypeDef(TypedDict):
    WorkloadSummaries: List["WorkloadSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class MilestoneSummaryTypeDef(TypedDict, total=False):
    MilestoneNumber: int
    MilestoneName: str
    RecordedAt: datetime
    WorkloadSummary: "WorkloadSummaryTypeDef"


class MilestoneTypeDef(TypedDict, total=False):
    MilestoneNumber: int
    MilestoneName: str
    RecordedAt: datetime
    Workload: "WorkloadTypeDef"


NotificationSummaryTypeDef = TypedDict(
    "NotificationSummaryTypeDef",
    {"Type": NotificationType, "LensUpgradeSummary": "LensUpgradeSummaryTypeDef"},
    total=False,
)


class PillarDifferenceTypeDef(TypedDict, total=False):
    PillarId: str
    DifferenceStatus: DifferenceStatus
    QuestionDifferences: List["QuestionDifferenceTypeDef"]


class PillarReviewSummaryTypeDef(TypedDict, total=False):
    PillarId: str
    PillarName: str
    Notes: str
    RiskCounts: Dict[Risk, int]


class QuestionDifferenceTypeDef(TypedDict, total=False):
    QuestionId: str
    QuestionTitle: str
    DifferenceStatus: DifferenceStatus


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class ShareInvitationSummaryTypeDef(TypedDict, total=False):
    ShareInvitationId: str
    SharedBy: str
    SharedWith: str
    PermissionType: PermissionType
    WorkloadName: str
    WorkloadId: str


class ShareInvitationTypeDef(TypedDict, total=False):
    ShareInvitationId: str
    WorkloadId: str


class UpdateAnswerOutputTypeDef(TypedDict):
    WorkloadId: str
    LensAlias: str
    Answer: "AnswerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateLensReviewOutputTypeDef(TypedDict):
    WorkloadId: str
    LensReview: "LensReviewTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateShareInvitationOutputTypeDef(TypedDict):
    ShareInvitation: "ShareInvitationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateWorkloadOutputTypeDef(TypedDict):
    Workload: "WorkloadTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateWorkloadShareOutputTypeDef(TypedDict):
    WorkloadId: str
    WorkloadShare: "WorkloadShareTypeDef"
    ResponseMetadata: "ResponseMetadata"


class VersionDifferencesTypeDef(TypedDict, total=False):
    PillarDifferences: List["PillarDifferenceTypeDef"]


class WorkloadShareSummaryTypeDef(TypedDict, total=False):
    ShareId: str
    SharedWith: str
    PermissionType: PermissionType
    Status: ShareStatus


class WorkloadShareTypeDef(TypedDict, total=False):
    ShareId: str
    SharedBy: str
    SharedWith: str
    PermissionType: PermissionType
    Status: ShareStatus
    WorkloadName: str
    WorkloadId: str


class WorkloadSummaryTypeDef(TypedDict, total=False):
    WorkloadId: str
    WorkloadArn: str
    WorkloadName: str
    Owner: str
    UpdatedAt: datetime
    Lenses: List[str]
    RiskCounts: Dict[Risk, int]
    ImprovementStatus: WorkloadImprovementStatus


class WorkloadTypeDef(TypedDict, total=False):
    WorkloadId: str
    WorkloadArn: str
    WorkloadName: str
    Description: str
    Environment: WorkloadEnvironment
    UpdatedAt: datetime
    AccountIds: List[str]
    AwsRegions: List[str]
    NonAwsRegions: List[str]
    ArchitecturalDesign: str
    ReviewOwner: str
    ReviewRestrictionDate: datetime
    IsReviewOwnerUpdateAcknowledged: bool
    IndustryType: str
    Industry: str
    Notes: str
    ImprovementStatus: WorkloadImprovementStatus
    RiskCounts: Dict[Risk, int]
    PillarPriorities: List[str]
    Lenses: List[str]
    Owner: str
    ShareInvitationId: str
    Tags: Dict[str, str]
