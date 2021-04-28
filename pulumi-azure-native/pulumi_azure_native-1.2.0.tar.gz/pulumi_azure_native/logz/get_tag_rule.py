# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetTagRuleResult',
    'AwaitableGetTagRuleResult',
    'get_tag_rule',
]

@pulumi.output_type
class GetTagRuleResult:
    """
    Capture logs and metrics of Azure resources based on ARM tags.
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of the rule set.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the rule set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.MonitoringTagRulesPropertiesResponse':
        """
        Definition of the properties for a TagRules resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the rule set.
        """
        return pulumi.get(self, "type")


class AwaitableGetTagRuleResult(GetTagRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagRuleResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_tag_rule(monitor_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 rule_set_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagRuleResult:
    """
    Capture logs and metrics of Azure resources based on ARM tags.
    API Version: 2020-10-01-preview.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleSetName'] = rule_set_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:logz:getTagRule', __args__, opts=opts, typ=GetTagRuleResult).value

    return AwaitableGetTagRuleResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        system_data=__ret__.system_data,
        type=__ret__.type)
