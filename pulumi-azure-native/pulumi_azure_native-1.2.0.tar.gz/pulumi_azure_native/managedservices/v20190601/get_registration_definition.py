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
    'GetRegistrationDefinitionResult',
    'AwaitableGetRegistrationDefinitionResult',
    'get_registration_definition',
]

@pulumi.output_type
class GetRegistrationDefinitionResult:
    """
    Registration definition.
    """
    def __init__(__self__, id=None, name=None, plan=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified path of the registration definition.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the registration definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.PlanResponse']:
        """
        Plan details for the managed services.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.RegistrationDefinitionPropertiesResponse':
        """
        Properties of a registration definition.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetRegistrationDefinitionResult(GetRegistrationDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistrationDefinitionResult(
            id=self.id,
            name=self.name,
            plan=self.plan,
            properties=self.properties,
            type=self.type)


def get_registration_definition(registration_definition_id: Optional[str] = None,
                                scope: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistrationDefinitionResult:
    """
    Registration definition.


    :param str registration_definition_id: Guid of the registration definition.
    :param str scope: Scope of the resource.
    """
    __args__ = dict()
    __args__['registrationDefinitionId'] = registration_definition_id
    __args__['scope'] = scope
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:managedservices/v20190601:getRegistrationDefinition', __args__, opts=opts, typ=GetRegistrationDefinitionResult).value

    return AwaitableGetRegistrationDefinitionResult(
        id=__ret__.id,
        name=__ret__.name,
        plan=__ret__.plan,
        properties=__ret__.properties,
        type=__ret__.type)
