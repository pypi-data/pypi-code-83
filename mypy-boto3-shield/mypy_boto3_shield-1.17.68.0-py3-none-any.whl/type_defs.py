"""
Type annotations for shield service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/type_defs.html)

Usage::

    ```python
    from mypy_boto3_shield.type_defs import AttackDetailTypeDef

    data: AttackDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_shield.literals import (
    AttackLayer,
    AttackPropertyIdentifier,
    AutoRenew,
    ProactiveEngagementStatus,
    ProtectedResourceType,
    ProtectionGroupAggregation,
    ProtectionGroupPattern,
    SubResourceType,
    SubscriptionState,
    Unit,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "CreateProtectionResponseTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "EmergencyContactTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "LimitTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "ListProtectionsResponseTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MitigationTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TagTypeDef",
    "TimeRangeTypeDef",
)


class AttackDetailTypeDef(TypedDict, total=False):
    AttackId: str
    ResourceArn: str
    SubResources: List["SubResourceSummaryTypeDef"]
    StartTime: datetime
    EndTime: datetime
    AttackCounters: List["SummarizedCounterTypeDef"]
    AttackProperties: List["AttackPropertyTypeDef"]
    Mitigations: List["MitigationTypeDef"]


class AttackPropertyTypeDef(TypedDict, total=False):
    AttackLayer: AttackLayer
    AttackPropertyIdentifier: AttackPropertyIdentifier
    TopContributors: List["ContributorTypeDef"]
    Unit: Unit
    Total: int


class _RequiredAttackStatisticsDataItemTypeDef(TypedDict):
    AttackCount: int


class AttackStatisticsDataItemTypeDef(_RequiredAttackStatisticsDataItemTypeDef, total=False):
    AttackVolume: "AttackVolumeTypeDef"


class AttackSummaryTypeDef(TypedDict, total=False):
    AttackId: str
    ResourceArn: str
    StartTime: datetime
    EndTime: datetime
    AttackVectors: List["AttackVectorDescriptionTypeDef"]


class AttackVectorDescriptionTypeDef(TypedDict):
    VectorType: str


class AttackVolumeStatisticsTypeDef(TypedDict):
    Max: float


class AttackVolumeTypeDef(TypedDict, total=False):
    BitsPerSecond: "AttackVolumeStatisticsTypeDef"
    PacketsPerSecond: "AttackVolumeStatisticsTypeDef"
    RequestsPerSecond: "AttackVolumeStatisticsTypeDef"


class ContributorTypeDef(TypedDict, total=False):
    Name: str
    Value: int


class CreateProtectionResponseTypeDef(TypedDict, total=False):
    ProtectionId: str


class DescribeAttackResponseTypeDef(TypedDict, total=False):
    Attack: "AttackDetailTypeDef"


class DescribeAttackStatisticsResponseTypeDef(TypedDict):
    TimeRange: "TimeRangeTypeDef"
    DataItems: List["AttackStatisticsDataItemTypeDef"]


class DescribeDRTAccessResponseTypeDef(TypedDict, total=False):
    RoleArn: str
    LogBucketList: List[str]


class DescribeEmergencyContactSettingsResponseTypeDef(TypedDict, total=False):
    EmergencyContactList: List["EmergencyContactTypeDef"]


class DescribeProtectionGroupResponseTypeDef(TypedDict):
    ProtectionGroup: "ProtectionGroupTypeDef"


class DescribeProtectionResponseTypeDef(TypedDict, total=False):
    Protection: "ProtectionTypeDef"


class DescribeSubscriptionResponseTypeDef(TypedDict, total=False):
    Subscription: "SubscriptionTypeDef"


class _RequiredEmergencyContactTypeDef(TypedDict):
    EmailAddress: str


class EmergencyContactTypeDef(_RequiredEmergencyContactTypeDef, total=False):
    PhoneNumber: str
    ContactNotes: str


class GetSubscriptionStateResponseTypeDef(TypedDict):
    SubscriptionState: SubscriptionState


LimitTypeDef = TypedDict("LimitTypeDef", {"Type": str, "Max": int}, total=False)


class ListAttacksResponseTypeDef(TypedDict, total=False):
    AttackSummaries: List["AttackSummaryTypeDef"]
    NextToken: str


class _RequiredListProtectionGroupsResponseTypeDef(TypedDict):
    ProtectionGroups: List["ProtectionGroupTypeDef"]


class ListProtectionGroupsResponseTypeDef(
    _RequiredListProtectionGroupsResponseTypeDef, total=False
):
    NextToken: str


class ListProtectionsResponseTypeDef(TypedDict, total=False):
    Protections: List["ProtectionTypeDef"]
    NextToken: str


class _RequiredListResourcesInProtectionGroupResponseTypeDef(TypedDict):
    ResourceArns: List[str]


class ListResourcesInProtectionGroupResponseTypeDef(
    _RequiredListResourcesInProtectionGroupResponseTypeDef, total=False
):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class MitigationTypeDef(TypedDict, total=False):
    MitigationName: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProtectionGroupArbitraryPatternLimitsTypeDef(TypedDict):
    MaxMembers: int


class ProtectionGroupLimitsTypeDef(TypedDict):
    MaxProtectionGroups: int
    PatternTypeLimits: "ProtectionGroupPatternTypeLimitsTypeDef"


class ProtectionGroupPatternTypeLimitsTypeDef(TypedDict):
    ArbitraryPatternLimits: "ProtectionGroupArbitraryPatternLimitsTypeDef"


_RequiredProtectionGroupTypeDef = TypedDict(
    "_RequiredProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregation,
        "Pattern": ProtectionGroupPattern,
        "Members": List[str],
    },
)
_OptionalProtectionGroupTypeDef = TypedDict(
    "_OptionalProtectionGroupTypeDef",
    {"ResourceType": ProtectedResourceType, "ProtectionGroupArn": str},
    total=False,
)


class ProtectionGroupTypeDef(_RequiredProtectionGroupTypeDef, _OptionalProtectionGroupTypeDef):
    pass


class ProtectionLimitsTypeDef(TypedDict):
    ProtectedResourceTypeLimits: List["LimitTypeDef"]


class ProtectionTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    ResourceArn: str
    HealthCheckIds: List[str]
    ProtectionArn: str


SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": SubResourceType,
        "Id": str,
        "AttackVectors": List["SummarizedAttackVectorTypeDef"],
        "Counters": List["SummarizedCounterTypeDef"],
    },
    total=False,
)


class SubscriptionLimitsTypeDef(TypedDict):
    ProtectionLimits: "ProtectionLimitsTypeDef"
    ProtectionGroupLimits: "ProtectionGroupLimitsTypeDef"


class _RequiredSubscriptionTypeDef(TypedDict):
    SubscriptionLimits: "SubscriptionLimitsTypeDef"


class SubscriptionTypeDef(_RequiredSubscriptionTypeDef, total=False):
    StartTime: datetime
    EndTime: datetime
    TimeCommitmentInSeconds: int
    AutoRenew: AutoRenew
    Limits: List["LimitTypeDef"]
    ProactiveEngagementStatus: ProactiveEngagementStatus
    SubscriptionArn: str


class _RequiredSummarizedAttackVectorTypeDef(TypedDict):
    VectorType: str


class SummarizedAttackVectorTypeDef(_RequiredSummarizedAttackVectorTypeDef, total=False):
    VectorCounters: List["SummarizedCounterTypeDef"]


class SummarizedCounterTypeDef(TypedDict, total=False):
    Name: str
    Max: float
    Average: float
    Sum: float
    N: int
    Unit: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TimeRangeTypeDef(TypedDict, total=False):
    FromInclusive: datetime
    ToExclusive: datetime
