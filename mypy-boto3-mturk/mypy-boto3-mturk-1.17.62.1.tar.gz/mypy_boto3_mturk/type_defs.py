"""
Type annotations for mturk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mturk.type_defs import AssignmentTypeDef

    data: AssignmentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_mturk.literals import (
    AssignmentStatus,
    Comparator,
    EventType,
    HITAccessActions,
    HITReviewStatus,
    HITStatus,
    NotificationTransport,
    NotifyWorkersFailureCode,
    QualificationStatus,
    QualificationTypeStatus,
    ReviewActionStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssignmentTypeDef",
    "BonusPaymentTypeDef",
    "CreateHITResponseTypeDef",
    "CreateHITTypeResponseTypeDef",
    "CreateHITWithHITTypeResponseTypeDef",
    "CreateQualificationTypeResponseTypeDef",
    "GetAccountBalanceResponseTypeDef",
    "GetAssignmentResponseTypeDef",
    "GetFileUploadURLResponseTypeDef",
    "GetHITResponseTypeDef",
    "GetQualificationScoreResponseTypeDef",
    "GetQualificationTypeResponseTypeDef",
    "HITLayoutParameterTypeDef",
    "HITTypeDef",
    "ListAssignmentsForHITResponseTypeDef",
    "ListBonusPaymentsResponseTypeDef",
    "ListHITsForQualificationTypeResponseTypeDef",
    "ListHITsResponseTypeDef",
    "ListQualificationRequestsResponseTypeDef",
    "ListQualificationTypesResponseTypeDef",
    "ListReviewPolicyResultsForHITResponseTypeDef",
    "ListReviewableHITsResponseTypeDef",
    "ListWorkerBlocksResponseTypeDef",
    "ListWorkersWithQualificationTypeResponseTypeDef",
    "LocaleTypeDef",
    "NotificationSpecificationTypeDef",
    "NotifyWorkersFailureStatusTypeDef",
    "NotifyWorkersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMapEntryTypeDef",
    "PolicyParameterTypeDef",
    "QualificationRequestTypeDef",
    "QualificationRequirementTypeDef",
    "QualificationTypeDef",
    "QualificationTypeTypeDef",
    "ReviewActionDetailTypeDef",
    "ReviewPolicyTypeDef",
    "ReviewReportTypeDef",
    "ReviewResultDetailTypeDef",
    "UpdateQualificationTypeResponseTypeDef",
    "WorkerBlockTypeDef",
)


class AssignmentTypeDef(TypedDict, total=False):
    AssignmentId: str
    WorkerId: str
    HITId: str
    AssignmentStatus: AssignmentStatus
    AutoApprovalTime: datetime
    AcceptTime: datetime
    SubmitTime: datetime
    ApprovalTime: datetime
    RejectionTime: datetime
    Deadline: datetime
    Answer: str
    RequesterFeedback: str


class BonusPaymentTypeDef(TypedDict, total=False):
    WorkerId: str
    BonusAmount: str
    AssignmentId: str
    Reason: str
    GrantTime: datetime


class CreateHITResponseTypeDef(TypedDict, total=False):
    HIT: "HITTypeDef"


class CreateHITTypeResponseTypeDef(TypedDict, total=False):
    HITTypeId: str


class CreateHITWithHITTypeResponseTypeDef(TypedDict, total=False):
    HIT: "HITTypeDef"


class CreateQualificationTypeResponseTypeDef(TypedDict, total=False):
    QualificationType: "QualificationTypeTypeDef"


class GetAccountBalanceResponseTypeDef(TypedDict, total=False):
    AvailableBalance: str
    OnHoldBalance: str


class GetAssignmentResponseTypeDef(TypedDict, total=False):
    Assignment: "AssignmentTypeDef"
    HIT: "HITTypeDef"


class GetFileUploadURLResponseTypeDef(TypedDict, total=False):
    FileUploadURL: str


class GetHITResponseTypeDef(TypedDict, total=False):
    HIT: "HITTypeDef"


class GetQualificationScoreResponseTypeDef(TypedDict, total=False):
    Qualification: "QualificationTypeDef"


class GetQualificationTypeResponseTypeDef(TypedDict, total=False):
    QualificationType: "QualificationTypeTypeDef"


class HITLayoutParameterTypeDef(TypedDict):
    Name: str
    Value: str


class HITTypeDef(TypedDict, total=False):
    HITId: str
    HITTypeId: str
    HITGroupId: str
    HITLayoutId: str
    CreationTime: datetime
    Title: str
    Description: str
    Question: str
    Keywords: str
    HITStatus: HITStatus
    MaxAssignments: int
    Reward: str
    AutoApprovalDelayInSeconds: int
    Expiration: datetime
    AssignmentDurationInSeconds: int
    RequesterAnnotation: str
    QualificationRequirements: List["QualificationRequirementTypeDef"]
    HITReviewStatus: HITReviewStatus
    NumberOfAssignmentsPending: int
    NumberOfAssignmentsAvailable: int
    NumberOfAssignmentsCompleted: int


class ListAssignmentsForHITResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    Assignments: List["AssignmentTypeDef"]


class ListBonusPaymentsResponseTypeDef(TypedDict, total=False):
    NumResults: int
    NextToken: str
    BonusPayments: List["BonusPaymentTypeDef"]


class ListHITsForQualificationTypeResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    HITs: List["HITTypeDef"]


class ListHITsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    HITs: List["HITTypeDef"]


class ListQualificationRequestsResponseTypeDef(TypedDict, total=False):
    NumResults: int
    NextToken: str
    QualificationRequests: List["QualificationRequestTypeDef"]


class ListQualificationTypesResponseTypeDef(TypedDict, total=False):
    NumResults: int
    NextToken: str
    QualificationTypes: List["QualificationTypeTypeDef"]


class ListReviewPolicyResultsForHITResponseTypeDef(TypedDict, total=False):
    HITId: str
    AssignmentReviewPolicy: "ReviewPolicyTypeDef"
    HITReviewPolicy: "ReviewPolicyTypeDef"
    AssignmentReviewReport: "ReviewReportTypeDef"
    HITReviewReport: "ReviewReportTypeDef"
    NextToken: str


class ListReviewableHITsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    HITs: List["HITTypeDef"]


class ListWorkerBlocksResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    WorkerBlocks: List["WorkerBlockTypeDef"]


class ListWorkersWithQualificationTypeResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NumResults: int
    Qualifications: List["QualificationTypeDef"]


class _RequiredLocaleTypeDef(TypedDict):
    Country: str


class LocaleTypeDef(_RequiredLocaleTypeDef, total=False):
    Subdivision: str


class NotificationSpecificationTypeDef(TypedDict):
    Destination: str
    Transport: NotificationTransport
    Version: str
    EventTypes: List[EventType]


class NotifyWorkersFailureStatusTypeDef(TypedDict, total=False):
    NotifyWorkersFailureCode: NotifyWorkersFailureCode
    NotifyWorkersFailureMessage: str
    WorkerId: str


class NotifyWorkersResponseTypeDef(TypedDict, total=False):
    NotifyWorkersFailureStatuses: List["NotifyWorkersFailureStatusTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterMapEntryTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class PolicyParameterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]
    MapEntries: List["ParameterMapEntryTypeDef"]


class QualificationRequestTypeDef(TypedDict, total=False):
    QualificationRequestId: str
    QualificationTypeId: str
    WorkerId: str
    Test: str
    Answer: str
    SubmitTime: datetime


class _RequiredQualificationRequirementTypeDef(TypedDict):
    QualificationTypeId: str
    Comparator: Comparator


class QualificationRequirementTypeDef(_RequiredQualificationRequirementTypeDef, total=False):
    IntegerValues: List[int]
    LocaleValues: List["LocaleTypeDef"]
    RequiredToPreview: bool
    ActionsGuarded: HITAccessActions


class QualificationTypeDef(TypedDict, total=False):
    QualificationTypeId: str
    WorkerId: str
    GrantTime: datetime
    IntegerValue: int
    LocaleValue: "LocaleTypeDef"
    Status: QualificationStatus


class QualificationTypeTypeDef(TypedDict, total=False):
    QualificationTypeId: str
    CreationTime: datetime
    Name: str
    Description: str
    Keywords: str
    QualificationTypeStatus: QualificationTypeStatus
    Test: str
    TestDurationInSeconds: int
    AnswerKey: str
    RetryDelayInSeconds: int
    IsRequestable: bool
    AutoGranted: bool
    AutoGrantedValue: int


class ReviewActionDetailTypeDef(TypedDict, total=False):
    ActionId: str
    ActionName: str
    TargetId: str
    TargetType: str
    Status: ReviewActionStatus
    CompleteTime: datetime
    Result: str
    ErrorCode: str


class _RequiredReviewPolicyTypeDef(TypedDict):
    PolicyName: str


class ReviewPolicyTypeDef(_RequiredReviewPolicyTypeDef, total=False):
    Parameters: List["PolicyParameterTypeDef"]


class ReviewReportTypeDef(TypedDict, total=False):
    ReviewResults: List["ReviewResultDetailTypeDef"]
    ReviewActions: List["ReviewActionDetailTypeDef"]


class ReviewResultDetailTypeDef(TypedDict, total=False):
    ActionId: str
    SubjectId: str
    SubjectType: str
    QuestionId: str
    Key: str
    Value: str


class UpdateQualificationTypeResponseTypeDef(TypedDict, total=False):
    QualificationType: "QualificationTypeTypeDef"


class WorkerBlockTypeDef(TypedDict, total=False):
    WorkerId: str
    Reason: str
