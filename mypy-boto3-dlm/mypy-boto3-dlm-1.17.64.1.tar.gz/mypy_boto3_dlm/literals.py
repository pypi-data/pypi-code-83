"""
Type annotations for dlm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dlm/literals.html)

Usage::

    ```python
    from mypy_boto3_dlm.literals import EventSourceValues

    data: EventSourceValues = "MANAGED_CWE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EventSourceValues",
    "EventTypeValues",
    "GettablePolicyStateValues",
    "IntervalUnitValues",
    "LocationValues",
    "PolicyTypeValues",
    "ResourceLocationValues",
    "ResourceTypeValues",
    "RetentionIntervalUnitValues",
    "SettablePolicyStateValues",
)


EventSourceValues = Literal["MANAGED_CWE"]
EventTypeValues = Literal["shareSnapshot"]
GettablePolicyStateValues = Literal["DISABLED", "ENABLED", "ERROR"]
IntervalUnitValues = Literal["HOURS"]
LocationValues = Literal["CLOUD", "OUTPOST_LOCAL"]
PolicyTypeValues = Literal["EBS_SNAPSHOT_MANAGEMENT", "EVENT_BASED_POLICY", "IMAGE_MANAGEMENT"]
ResourceLocationValues = Literal["CLOUD", "OUTPOST"]
ResourceTypeValues = Literal["INSTANCE", "VOLUME"]
RetentionIntervalUnitValues = Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]
SettablePolicyStateValues = Literal["DISABLED", "ENABLED"]
