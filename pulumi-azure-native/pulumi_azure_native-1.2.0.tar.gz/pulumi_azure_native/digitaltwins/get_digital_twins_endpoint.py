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
    'GetDigitalTwinsEndpointResult',
    'AwaitableGetDigitalTwinsEndpointResult',
    'get_digital_twins_endpoint',
]

@pulumi.output_type
class GetDigitalTwinsEndpointResult:
    """
    DigitalTwinsInstance endpoint resource.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Extension resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        DigitalTwinsInstance endpoint resource properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetDigitalTwinsEndpointResult(GetDigitalTwinsEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDigitalTwinsEndpointResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_digital_twins_endpoint(endpoint_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               resource_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDigitalTwinsEndpointResult:
    """
    DigitalTwinsInstance endpoint resource.
    API Version: 2020-12-01.


    :param str endpoint_name: Name of Endpoint Resource.
    :param str resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :param str resource_name: The name of the DigitalTwinsInstance.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:digitaltwins:getDigitalTwinsEndpoint', __args__, opts=opts, typ=GetDigitalTwinsEndpointResult).value

    return AwaitableGetDigitalTwinsEndpointResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)
