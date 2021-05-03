"""
Type annotations for mturk service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mturk/literals.html)

Usage::

    ```python
    from mypy_boto3_mturk.literals import AssignmentStatus

    data: AssignmentStatus = "Approved"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AssignmentStatus",
    "Comparator",
    "EventType",
    "HITAccessActions",
    "HITReviewStatus",
    "HITStatus",
    "ListAssignmentsForHITPaginatorName",
    "ListBonusPaymentsPaginatorName",
    "ListHITsForQualificationTypePaginatorName",
    "ListHITsPaginatorName",
    "ListQualificationRequestsPaginatorName",
    "ListQualificationTypesPaginatorName",
    "ListReviewableHITsPaginatorName",
    "ListWorkerBlocksPaginatorName",
    "ListWorkersWithQualificationTypePaginatorName",
    "NotificationTransport",
    "NotifyWorkersFailureCode",
    "QualificationStatus",
    "QualificationTypeStatus",
    "ReviewActionStatus",
    "ReviewPolicyLevel",
    "ReviewableHITStatus",
)


AssignmentStatus = Literal["Approved", "Rejected", "Submitted"]
Comparator = Literal[
    "DoesNotExist",
    "EqualTo",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEqualTo",
    "NotIn",
]
EventType = Literal[
    "AssignmentAbandoned",
    "AssignmentAccepted",
    "AssignmentApproved",
    "AssignmentRejected",
    "AssignmentReturned",
    "AssignmentSubmitted",
    "HITCreated",
    "HITDisposed",
    "HITExpired",
    "HITExtended",
    "HITReviewable",
    "Ping",
]
HITAccessActions = Literal["Accept", "DiscoverPreviewAndAccept", "PreviewAndAccept"]
HITReviewStatus = Literal[
    "MarkedForReview", "NotReviewed", "ReviewedAppropriate", "ReviewedInappropriate"
]
HITStatus = Literal["Assignable", "Disposed", "Reviewable", "Reviewing", "Unassignable"]
ListAssignmentsForHITPaginatorName = Literal["list_assignments_for_hit"]
ListBonusPaymentsPaginatorName = Literal["list_bonus_payments"]
ListHITsForQualificationTypePaginatorName = Literal["list_hits_for_qualification_type"]
ListHITsPaginatorName = Literal["list_hits"]
ListQualificationRequestsPaginatorName = Literal["list_qualification_requests"]
ListQualificationTypesPaginatorName = Literal["list_qualification_types"]
ListReviewableHITsPaginatorName = Literal["list_reviewable_hits"]
ListWorkerBlocksPaginatorName = Literal["list_worker_blocks"]
ListWorkersWithQualificationTypePaginatorName = Literal["list_workers_with_qualification_type"]
NotificationTransport = Literal["Email", "SNS", "SQS"]
NotifyWorkersFailureCode = Literal["HardFailure", "SoftFailure"]
QualificationStatus = Literal["Granted", "Revoked"]
QualificationTypeStatus = Literal["Active", "Inactive"]
ReviewActionStatus = Literal["Cancelled", "Failed", "Intended", "Succeeded"]
ReviewPolicyLevel = Literal["Assignment", "HIT"]
ReviewableHITStatus = Literal["Reviewable", "Reviewing"]
