# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionRuleStatus',
    'ScopeType',
    'SuppressionType',
]


class ActionRuleStatus(str, Enum):
    """
    Indicates if the given action rule is enabled or disabled
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class ScopeType(str, Enum):
    """
    type of target scope
    """
    RESOURCE_GROUP = "ResourceGroup"
    RESOURCE = "Resource"


class SuppressionType(str, Enum):
    """
    Specifies when the suppression should be applied
    """
    ALWAYS = "Always"
    ONCE = "Once"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
