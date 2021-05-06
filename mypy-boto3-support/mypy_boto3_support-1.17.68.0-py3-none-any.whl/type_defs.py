"""
Type annotations for support service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support/type_defs.html)

Usage::

    ```python
    from mypy_boto3_support.type_defs import AddAttachmentsToSetResponseTypeDef

    data: AddAttachmentsToSetResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddAttachmentsToSetResponseTypeDef",
    "AddCommunicationToCaseResponseTypeDef",
    "AttachmentDetailsTypeDef",
    "AttachmentTypeDef",
    "CaseDetailsTypeDef",
    "CategoryTypeDef",
    "CommunicationTypeDef",
    "CreateCaseResponseTypeDef",
    "DescribeAttachmentResponseTypeDef",
    "DescribeCasesResponseTypeDef",
    "DescribeCommunicationsResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeSeverityLevelsResponseTypeDef",
    "DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef",
    "DescribeTrustedAdvisorCheckResultResponseTypeDef",
    "DescribeTrustedAdvisorCheckSummariesResponseTypeDef",
    "DescribeTrustedAdvisorChecksResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecentCaseCommunicationsTypeDef",
    "RefreshTrustedAdvisorCheckResponseTypeDef",
    "ResolveCaseResponseTypeDef",
    "ServiceTypeDef",
    "SeverityLevelTypeDef",
    "TrustedAdvisorCategorySpecificSummaryTypeDef",
    "TrustedAdvisorCheckDescriptionTypeDef",
    "TrustedAdvisorCheckRefreshStatusTypeDef",
    "TrustedAdvisorCheckResultTypeDef",
    "TrustedAdvisorCheckSummaryTypeDef",
    "TrustedAdvisorCostOptimizingSummaryTypeDef",
    "TrustedAdvisorResourceDetailTypeDef",
    "TrustedAdvisorResourcesSummaryTypeDef",
)


class AddAttachmentsToSetResponseTypeDef(TypedDict, total=False):
    attachmentSetId: str
    expiryTime: str


class AddCommunicationToCaseResponseTypeDef(TypedDict, total=False):
    result: bool


class AttachmentDetailsTypeDef(TypedDict, total=False):
    attachmentId: str
    fileName: str


class AttachmentTypeDef(TypedDict, total=False):
    fileName: str
    data: Union[bytes, IO[bytes]]


class CaseDetailsTypeDef(TypedDict, total=False):
    caseId: str
    displayId: str
    subject: str
    status: str
    serviceCode: str
    categoryCode: str
    severityCode: str
    submittedBy: str
    timeCreated: str
    recentCommunications: "RecentCaseCommunicationsTypeDef"
    ccEmailAddresses: List[str]
    language: str


class CategoryTypeDef(TypedDict, total=False):
    code: str
    name: str


class CommunicationTypeDef(TypedDict, total=False):
    caseId: str
    body: str
    submittedBy: str
    timeCreated: str
    attachmentSet: List["AttachmentDetailsTypeDef"]


class CreateCaseResponseTypeDef(TypedDict, total=False):
    caseId: str


class DescribeAttachmentResponseTypeDef(TypedDict, total=False):
    attachment: "AttachmentTypeDef"


class DescribeCasesResponseTypeDef(TypedDict, total=False):
    cases: List["CaseDetailsTypeDef"]
    nextToken: str


class DescribeCommunicationsResponseTypeDef(TypedDict, total=False):
    communications: List["CommunicationTypeDef"]
    nextToken: str


class DescribeServicesResponseTypeDef(TypedDict, total=False):
    services: List["ServiceTypeDef"]


class DescribeSeverityLevelsResponseTypeDef(TypedDict, total=False):
    severityLevels: List["SeverityLevelTypeDef"]


class DescribeTrustedAdvisorCheckRefreshStatusesResponseTypeDef(TypedDict):
    statuses: List["TrustedAdvisorCheckRefreshStatusTypeDef"]


class DescribeTrustedAdvisorCheckResultResponseTypeDef(TypedDict, total=False):
    result: "TrustedAdvisorCheckResultTypeDef"


class DescribeTrustedAdvisorCheckSummariesResponseTypeDef(TypedDict):
    summaries: List["TrustedAdvisorCheckSummaryTypeDef"]


class DescribeTrustedAdvisorChecksResponseTypeDef(TypedDict):
    checks: List["TrustedAdvisorCheckDescriptionTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RecentCaseCommunicationsTypeDef(TypedDict, total=False):
    communications: List["CommunicationTypeDef"]
    nextToken: str


class RefreshTrustedAdvisorCheckResponseTypeDef(TypedDict):
    status: "TrustedAdvisorCheckRefreshStatusTypeDef"


class ResolveCaseResponseTypeDef(TypedDict, total=False):
    initialCaseStatus: str
    finalCaseStatus: str


class ServiceTypeDef(TypedDict, total=False):
    code: str
    name: str
    categories: List["CategoryTypeDef"]


class SeverityLevelTypeDef(TypedDict, total=False):
    code: str
    name: str


class TrustedAdvisorCategorySpecificSummaryTypeDef(TypedDict, total=False):
    costOptimizing: "TrustedAdvisorCostOptimizingSummaryTypeDef"


TrustedAdvisorCheckDescriptionTypeDef = TypedDict(
    "TrustedAdvisorCheckDescriptionTypeDef",
    {"id": str, "name": str, "description": str, "category": str, "metadata": List[str]},
)


class TrustedAdvisorCheckRefreshStatusTypeDef(TypedDict):
    checkId: str
    status: str
    millisUntilNextRefreshable: int


class TrustedAdvisorCheckResultTypeDef(TypedDict):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: "TrustedAdvisorResourcesSummaryTypeDef"
    categorySpecificSummary: "TrustedAdvisorCategorySpecificSummaryTypeDef"
    flaggedResources: List["TrustedAdvisorResourceDetailTypeDef"]


class _RequiredTrustedAdvisorCheckSummaryTypeDef(TypedDict):
    checkId: str
    timestamp: str
    status: str
    resourcesSummary: "TrustedAdvisorResourcesSummaryTypeDef"
    categorySpecificSummary: "TrustedAdvisorCategorySpecificSummaryTypeDef"


class TrustedAdvisorCheckSummaryTypeDef(_RequiredTrustedAdvisorCheckSummaryTypeDef, total=False):
    hasFlaggedResources: bool


class TrustedAdvisorCostOptimizingSummaryTypeDef(TypedDict):
    estimatedMonthlySavings: float
    estimatedPercentMonthlySavings: float


class _RequiredTrustedAdvisorResourceDetailTypeDef(TypedDict):
    status: str
    resourceId: str
    metadata: List[str]


class TrustedAdvisorResourceDetailTypeDef(
    _RequiredTrustedAdvisorResourceDetailTypeDef, total=False
):
    region: str
    isSuppressed: bool


class TrustedAdvisorResourcesSummaryTypeDef(TypedDict):
    resourcesProcessed: int
    resourcesFlagged: int
    resourcesIgnored: int
    resourcesSuppressed: int
