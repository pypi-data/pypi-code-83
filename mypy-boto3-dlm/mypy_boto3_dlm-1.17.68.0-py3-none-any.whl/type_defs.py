"""
Type annotations for dlm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dlm.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_dlm.literals import (
    GettablePolicyStateValues,
    LocationValues,
    PolicyTypeValues,
    ResourceLocationValues,
    ResourceTypeValues,
    RetentionIntervalUnitValues,
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
    "ActionTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventParametersTypeDef",
    "EventSourceTypeDef",
    "FastRestoreRuleTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsTypeDef",
    "RetainRuleTypeDef",
    "ScheduleTypeDef",
    "ShareRuleTypeDef",
    "TagTypeDef",
)


class ActionTypeDef(TypedDict):
    Name: str
    CrossRegionCopy: List["CrossRegionCopyActionTypeDef"]


class CreateLifecyclePolicyResponseTypeDef(TypedDict, total=False):
    PolicyId: str


class CreateRuleTypeDef(TypedDict, total=False):
    Location: LocationValues
    Interval: int
    IntervalUnit: Literal["HOURS"]
    Times: List[str]
    CronExpression: str


class _RequiredCrossRegionCopyActionTypeDef(TypedDict):
    Target: str
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"


class CrossRegionCopyActionTypeDef(_RequiredCrossRegionCopyActionTypeDef, total=False):
    RetainRule: "CrossRegionCopyRetainRuleTypeDef"


class CrossRegionCopyRetainRuleTypeDef(TypedDict, total=False):
    Interval: int
    IntervalUnit: RetentionIntervalUnitValues


class _RequiredCrossRegionCopyRuleTypeDef(TypedDict):
    Encrypted: bool


class CrossRegionCopyRuleTypeDef(_RequiredCrossRegionCopyRuleTypeDef, total=False):
    TargetRegion: str
    Target: str
    CmkArn: str
    CopyTags: bool
    RetainRule: "CrossRegionCopyRetainRuleTypeDef"


class _RequiredEncryptionConfigurationTypeDef(TypedDict):
    Encrypted: bool


class EncryptionConfigurationTypeDef(_RequiredEncryptionConfigurationTypeDef, total=False):
    CmkArn: str


class EventParametersTypeDef(TypedDict):
    EventType: Literal["shareSnapshot"]
    SnapshotOwner: List[str]
    DescriptionRegex: str


_RequiredEventSourceTypeDef = TypedDict(
    "_RequiredEventSourceTypeDef", {"Type": Literal["MANAGED_CWE"]}
)
_OptionalEventSourceTypeDef = TypedDict(
    "_OptionalEventSourceTypeDef", {"Parameters": "EventParametersTypeDef"}, total=False
)


class EventSourceTypeDef(_RequiredEventSourceTypeDef, _OptionalEventSourceTypeDef):
    pass


class _RequiredFastRestoreRuleTypeDef(TypedDict):
    AvailabilityZones: List[str]


class FastRestoreRuleTypeDef(_RequiredFastRestoreRuleTypeDef, total=False):
    Count: int
    Interval: int
    IntervalUnit: RetentionIntervalUnitValues


class GetLifecyclePoliciesResponseTypeDef(TypedDict, total=False):
    Policies: List["LifecyclePolicySummaryTypeDef"]


class GetLifecyclePolicyResponseTypeDef(TypedDict, total=False):
    Policy: "LifecyclePolicyTypeDef"


class LifecyclePolicySummaryTypeDef(TypedDict, total=False):
    PolicyId: str
    Description: str
    State: GettablePolicyStateValues
    Tags: Dict[str, str]
    PolicyType: PolicyTypeValues


class LifecyclePolicyTypeDef(TypedDict, total=False):
    PolicyId: str
    Description: str
    State: GettablePolicyStateValues
    StatusMessage: str
    ExecutionRoleArn: str
    DateCreated: datetime
    DateModified: datetime
    PolicyDetails: "PolicyDetailsTypeDef"
    Tags: Dict[str, str]
    PolicyArn: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ParametersTypeDef(TypedDict, total=False):
    ExcludeBootVolume: bool
    NoReboot: bool


class PolicyDetailsTypeDef(TypedDict, total=False):
    PolicyType: PolicyTypeValues
    ResourceTypes: List[ResourceTypeValues]
    ResourceLocations: List[ResourceLocationValues]
    TargetTags: List["TagTypeDef"]
    Schedules: List["ScheduleTypeDef"]
    Parameters: "ParametersTypeDef"
    EventSource: "EventSourceTypeDef"
    Actions: List["ActionTypeDef"]


class RetainRuleTypeDef(TypedDict, total=False):
    Count: int
    Interval: int
    IntervalUnit: RetentionIntervalUnitValues


class ScheduleTypeDef(TypedDict, total=False):
    Name: str
    CopyTags: bool
    TagsToAdd: List["TagTypeDef"]
    VariableTags: List["TagTypeDef"]
    CreateRule: "CreateRuleTypeDef"
    RetainRule: "RetainRuleTypeDef"
    FastRestoreRule: "FastRestoreRuleTypeDef"
    CrossRegionCopyRules: List["CrossRegionCopyRuleTypeDef"]
    ShareRules: List["ShareRuleTypeDef"]


class _RequiredShareRuleTypeDef(TypedDict):
    TargetAccounts: List[str]


class ShareRuleTypeDef(_RequiredShareRuleTypeDef, total=False):
    UnshareInterval: int
    UnshareIntervalUnit: RetentionIntervalUnitValues


class TagTypeDef(TypedDict):
    Key: str
    Value: str
