# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetSolutionResult',
    'AwaitableGetSolutionResult',
    'get_solution',
]

@pulumi.output_type
class GetSolutionResult:
    """
    The container for solution.
    """
    def __init__(__self__, id=None, location=None, name=None, plan=None, properties=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.SolutionPlanResponse']:
        """
        Plan for solution object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SolutionPropertiesResponse':
        """
        Properties for solution object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetSolutionResult(GetSolutionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSolutionResult(
            id=self.id,
            location=self.location,
            name=self.name,
            plan=self.plan,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_solution(resource_group_name: Optional[str] = None,
                 solution_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSolutionResult:
    """
    The container for solution.


    :param str resource_group_name: The name of the resource group to get. The name is case insensitive.
    :param str solution_name: User Solution Name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['solutionName'] = solution_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:operationsmanagement/v20151101preview:getSolution', __args__, opts=opts, typ=GetSolutionResult).value

    return AwaitableGetSolutionResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        plan=__ret__.plan,
        properties=__ret__.properties,
        tags=__ret__.tags,
        type=__ret__.type)
