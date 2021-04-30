"""
Main interface for dlm service type definitions.

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
    EventSourceValues,
    EventTypeValues,
    GettablePolicyStateValues,
    IntervalUnitValues,
    LocationValues,
    PolicyTypeValues,
    ResourceLocationValues,
    ResourceTypeValues,
    RetentionIntervalUnitValues,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventParametersTypeDef",
    "EventSourceTypeDef",
    "FastRestoreRuleTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsTypeDef",
    "RetainRuleTypeDef",
    "ScheduleTypeDef",
    "ShareRuleTypeDef",
    "TagTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef", {"Name": str, "CrossRegionCopy": List["CrossRegionCopyActionTypeDef"]}
)

CreateRuleTypeDef = TypedDict(
    "CreateRuleTypeDef",
    {
        "Location": LocationValues,
        "Interval": int,
        "IntervalUnit": IntervalUnitValues,
        "Times": List[str],
        "CronExpression": str,
    },
    total=False,
)

_RequiredCrossRegionCopyActionTypeDef = TypedDict(
    "_RequiredCrossRegionCopyActionTypeDef",
    {"Target": str, "EncryptionConfiguration": "EncryptionConfigurationTypeDef"},
)
_OptionalCrossRegionCopyActionTypeDef = TypedDict(
    "_OptionalCrossRegionCopyActionTypeDef",
    {"RetainRule": "CrossRegionCopyRetainRuleTypeDef"},
    total=False,
)


class CrossRegionCopyActionTypeDef(
    _RequiredCrossRegionCopyActionTypeDef, _OptionalCrossRegionCopyActionTypeDef
):
    pass


CrossRegionCopyRetainRuleTypeDef = TypedDict(
    "CrossRegionCopyRetainRuleTypeDef",
    {"Interval": int, "IntervalUnit": RetentionIntervalUnitValues},
    total=False,
)

_RequiredCrossRegionCopyRuleTypeDef = TypedDict(
    "_RequiredCrossRegionCopyRuleTypeDef", {"Encrypted": bool}
)
_OptionalCrossRegionCopyRuleTypeDef = TypedDict(
    "_OptionalCrossRegionCopyRuleTypeDef",
    {
        "TargetRegion": str,
        "Target": str,
        "CmkArn": str,
        "CopyTags": bool,
        "RetainRule": "CrossRegionCopyRetainRuleTypeDef",
    },
    total=False,
)


class CrossRegionCopyRuleTypeDef(
    _RequiredCrossRegionCopyRuleTypeDef, _OptionalCrossRegionCopyRuleTypeDef
):
    pass


_RequiredEncryptionConfigurationTypeDef = TypedDict(
    "_RequiredEncryptionConfigurationTypeDef", {"Encrypted": bool}
)
_OptionalEncryptionConfigurationTypeDef = TypedDict(
    "_OptionalEncryptionConfigurationTypeDef", {"CmkArn": str}, total=False
)


class EncryptionConfigurationTypeDef(
    _RequiredEncryptionConfigurationTypeDef, _OptionalEncryptionConfigurationTypeDef
):
    pass


EventParametersTypeDef = TypedDict(
    "EventParametersTypeDef",
    {"EventType": EventTypeValues, "SnapshotOwner": List[str], "DescriptionRegex": str},
)

_RequiredEventSourceTypeDef = TypedDict("_RequiredEventSourceTypeDef", {"Type": EventSourceValues})
_OptionalEventSourceTypeDef = TypedDict(
    "_OptionalEventSourceTypeDef", {"Parameters": "EventParametersTypeDef"}, total=False
)


class EventSourceTypeDef(_RequiredEventSourceTypeDef, _OptionalEventSourceTypeDef):
    pass


_RequiredFastRestoreRuleTypeDef = TypedDict(
    "_RequiredFastRestoreRuleTypeDef", {"AvailabilityZones": List[str]}
)
_OptionalFastRestoreRuleTypeDef = TypedDict(
    "_OptionalFastRestoreRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": RetentionIntervalUnitValues},
    total=False,
)


class FastRestoreRuleTypeDef(_RequiredFastRestoreRuleTypeDef, _OptionalFastRestoreRuleTypeDef):
    pass


LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": GettablePolicyStateValues,
        "Tags": Dict[str, str],
        "PolicyType": PolicyTypeValues,
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": GettablePolicyStateValues,
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": "PolicyDetailsTypeDef",
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)

ParametersTypeDef = TypedDict(
    "ParametersTypeDef", {"ExcludeBootVolume": bool, "NoReboot": bool}, total=False
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "PolicyType": PolicyTypeValues,
        "ResourceTypes": List[ResourceTypeValues],
        "ResourceLocations": List[ResourceLocationValues],
        "TargetTags": List["TagTypeDef"],
        "Schedules": List["ScheduleTypeDef"],
        "Parameters": "ParametersTypeDef",
        "EventSource": "EventSourceTypeDef",
        "Actions": List["ActionTypeDef"],
    },
    total=False,
)

RetainRuleTypeDef = TypedDict(
    "RetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": RetentionIntervalUnitValues},
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List["TagTypeDef"],
        "VariableTags": List["TagTypeDef"],
        "CreateRule": "CreateRuleTypeDef",
        "RetainRule": "RetainRuleTypeDef",
        "FastRestoreRule": "FastRestoreRuleTypeDef",
        "CrossRegionCopyRules": List["CrossRegionCopyRuleTypeDef"],
        "ShareRules": List["ShareRuleTypeDef"],
    },
    total=False,
)

_RequiredShareRuleTypeDef = TypedDict("_RequiredShareRuleTypeDef", {"TargetAccounts": List[str]})
_OptionalShareRuleTypeDef = TypedDict(
    "_OptionalShareRuleTypeDef",
    {"UnshareInterval": int, "UnshareIntervalUnit": RetentionIntervalUnitValues},
    total=False,
)


class ShareRuleTypeDef(_RequiredShareRuleTypeDef, _OptionalShareRuleTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef", {"PolicyId": str}, total=False
)

GetLifecyclePoliciesResponseTypeDef = TypedDict(
    "GetLifecyclePoliciesResponseTypeDef",
    {"Policies": List["LifecyclePolicySummaryTypeDef"]},
    total=False,
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef", {"Policy": "LifecyclePolicyTypeDef"}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)
