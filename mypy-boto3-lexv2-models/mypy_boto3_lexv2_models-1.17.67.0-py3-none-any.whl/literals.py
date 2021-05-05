"""
Type annotations for lexv2-models service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_models/literals.html)

Usage::

    ```python
    from mypy_boto3_lexv2_models.literals import BotAliasStatus

    data: BotAliasStatus = "Available"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BotAliasStatus",
    "BotFilterName",
    "BotFilterOperator",
    "BotLocaleFilterName",
    "BotLocaleFilterOperator",
    "BotLocaleSortAttribute",
    "BotLocaleStatus",
    "BotSortAttribute",
    "BotStatus",
    "BotVersionSortAttribute",
    "BuiltInIntentSortAttribute",
    "BuiltInSlotTypeSortAttribute",
    "IntentFilterName",
    "IntentFilterOperator",
    "IntentSortAttribute",
    "ObfuscationSettingType",
    "SlotConstraint",
    "SlotFilterName",
    "SlotFilterOperator",
    "SlotSortAttribute",
    "SlotTypeFilterName",
    "SlotTypeFilterOperator",
    "SlotTypeSortAttribute",
    "SlotValueResolutionStrategy",
    "SortOrder",
)


BotAliasStatus = Literal["Available", "Creating", "Deleting", "Failed"]
BotFilterName = Literal["BotName"]
BotFilterOperator = Literal["CO", "EQ"]
BotLocaleFilterName = Literal["BotLocaleName"]
BotLocaleFilterOperator = Literal["CO", "EQ"]
BotLocaleSortAttribute = Literal["BotLocaleName"]
BotLocaleStatus = Literal[
    "Building", "Built", "Creating", "Deleting", "Failed", "NotBuilt", "ReadyExpressTesting"
]
BotSortAttribute = Literal["BotName"]
BotStatus = Literal["Available", "Creating", "Deleting", "Failed", "Inactive", "Versioning"]
BotVersionSortAttribute = Literal["BotVersion"]
BuiltInIntentSortAttribute = Literal["IntentSignature"]
BuiltInSlotTypeSortAttribute = Literal["SlotTypeSignature"]
IntentFilterName = Literal["IntentName"]
IntentFilterOperator = Literal["CO", "EQ"]
IntentSortAttribute = Literal["IntentName", "LastUpdatedDateTime"]
ObfuscationSettingType = Literal["DefaultObfuscation", "None"]
SlotConstraint = Literal["Optional", "Required"]
SlotFilterName = Literal["SlotName"]
SlotFilterOperator = Literal["CO", "EQ"]
SlotSortAttribute = Literal["LastUpdatedDateTime", "SlotName"]
SlotTypeFilterName = Literal["SlotTypeName"]
SlotTypeFilterOperator = Literal["CO", "EQ"]
SlotTypeSortAttribute = Literal["LastUpdatedDateTime", "SlotTypeName"]
SlotValueResolutionStrategy = Literal["OriginalValue", "TopResolution"]
SortOrder = Literal["Ascending", "Descending"]
