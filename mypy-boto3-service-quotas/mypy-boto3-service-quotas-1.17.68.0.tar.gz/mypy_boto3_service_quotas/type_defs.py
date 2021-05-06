"""
Type annotations for service-quotas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.type_defs import ErrorReasonTypeDef

    data: ErrorReasonTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_service_quotas.literals import (
    ErrorCode,
    PeriodUnit,
    RequestStatus,
    ServiceQuotaTemplateAssociationStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ErrorReasonTypeDef",
    "GetAWSDefaultServiceQuotaResponseTypeDef",
    "GetAssociationForServiceQuotaTemplateResponseTypeDef",
    "GetRequestedServiceQuotaChangeResponseTypeDef",
    "GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef",
    "GetServiceQuotaResponseTypeDef",
    "ListAWSDefaultServiceQuotasResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef",
    "ListRequestedServiceQuotaChangeHistoryResponseTypeDef",
    "ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef",
    "ListServiceQuotasResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef",
    "QuotaPeriodTypeDef",
    "RequestServiceQuotaIncreaseResponseTypeDef",
    "RequestedServiceQuotaChangeTypeDef",
    "ServiceInfoTypeDef",
    "ServiceQuotaIncreaseRequestInTemplateTypeDef",
    "ServiceQuotaTypeDef",
    "TagTypeDef",
)


class ErrorReasonTypeDef(TypedDict, total=False):
    ErrorCode: ErrorCode
    ErrorMessage: str


class GetAWSDefaultServiceQuotaResponseTypeDef(TypedDict, total=False):
    Quota: "ServiceQuotaTypeDef"


class GetAssociationForServiceQuotaTemplateResponseTypeDef(TypedDict, total=False):
    ServiceQuotaTemplateAssociationStatus: ServiceQuotaTemplateAssociationStatus


class GetRequestedServiceQuotaChangeResponseTypeDef(TypedDict, total=False):
    RequestedQuota: "RequestedServiceQuotaChangeTypeDef"


class GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef(TypedDict, total=False):
    ServiceQuotaIncreaseRequestInTemplate: "ServiceQuotaIncreaseRequestInTemplateTypeDef"


class GetServiceQuotaResponseTypeDef(TypedDict, total=False):
    Quota: "ServiceQuotaTypeDef"


class ListAWSDefaultServiceQuotasResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Quotas: List["ServiceQuotaTypeDef"]


class ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef(TypedDict, total=False):
    NextToken: str
    RequestedQuotas: List["RequestedServiceQuotaChangeTypeDef"]


class ListRequestedServiceQuotaChangeHistoryResponseTypeDef(TypedDict, total=False):
    NextToken: str
    RequestedQuotas: List["RequestedServiceQuotaChangeTypeDef"]


class ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef(TypedDict, total=False):
    ServiceQuotaIncreaseRequestInTemplateList: List["ServiceQuotaIncreaseRequestInTemplateTypeDef"]
    NextToken: str


class ListServiceQuotasResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Quotas: List["ServiceQuotaTypeDef"]


class ListServicesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Services: List["ServiceInfoTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class MetricInfoTypeDef(TypedDict, total=False):
    MetricNamespace: str
    MetricName: str
    MetricDimensions: Dict[str, str]
    MetricStatisticRecommendation: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef(TypedDict, total=False):
    ServiceQuotaIncreaseRequestInTemplate: "ServiceQuotaIncreaseRequestInTemplateTypeDef"


class QuotaPeriodTypeDef(TypedDict, total=False):
    PeriodValue: int
    PeriodUnit: PeriodUnit


class RequestServiceQuotaIncreaseResponseTypeDef(TypedDict, total=False):
    RequestedQuota: "RequestedServiceQuotaChangeTypeDef"


class RequestedServiceQuotaChangeTypeDef(TypedDict, total=False):
    Id: str
    CaseId: str
    ServiceCode: str
    ServiceName: str
    QuotaCode: str
    QuotaName: str
    DesiredValue: float
    Status: RequestStatus
    Created: datetime
    LastUpdated: datetime
    Requester: str
    QuotaArn: str
    GlobalQuota: bool
    Unit: str


class ServiceInfoTypeDef(TypedDict, total=False):
    ServiceCode: str
    ServiceName: str


class ServiceQuotaIncreaseRequestInTemplateTypeDef(TypedDict, total=False):
    ServiceCode: str
    ServiceName: str
    QuotaCode: str
    QuotaName: str
    DesiredValue: float
    AwsRegion: str
    Unit: str
    GlobalQuota: bool


class ServiceQuotaTypeDef(TypedDict, total=False):
    ServiceCode: str
    ServiceName: str
    QuotaArn: str
    QuotaCode: str
    QuotaName: str
    Value: float
    Unit: str
    Adjustable: bool
    GlobalQuota: bool
    UsageMetric: "MetricInfoTypeDef"
    Period: "QuotaPeriodTypeDef"
    ErrorReason: "ErrorReasonTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str
