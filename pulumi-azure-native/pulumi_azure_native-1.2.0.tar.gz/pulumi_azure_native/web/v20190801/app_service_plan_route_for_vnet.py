# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['AppServicePlanRouteForVnetArgs', 'AppServicePlanRouteForVnet']

@pulumi.input_type
class AppServicePlanRouteForVnetArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vnet_name: pulumi.Input[str],
                 end_address: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[Union[str, 'RouteType']]] = None,
                 start_address: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AppServicePlanRouteForVnet resource.
        :param pulumi.Input[str] name: Name of the App Service plan.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] vnet_name: Name of the Virtual Network.
        :param pulumi.Input[str] end_address: The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] route_name: Name of the Virtual Network route.
        :param pulumi.Input[Union[str, 'RouteType']] route_type: The type of route this is:
               DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
               INHERITED - Routes inherited from the real Virtual Network routes
               STATIC - Static route set on the app only
               
               These values will be used for syncing an app's routes with those from a Virtual Network.
        :param pulumi.Input[str] start_address: The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vnet_name", vnet_name)
        if end_address is not None:
            pulumi.set(__self__, "end_address", end_address)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if route_name is not None:
            pulumi.set(__self__, "route_name", route_name)
        if route_type is not None:
            pulumi.set(__self__, "route_type", route_type)
        if start_address is not None:
            pulumi.set(__self__, "start_address", start_address)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the App Service plan.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> pulumi.Input[str]:
        """
        Name of the Virtual Network.
        """
        return pulumi.get(self, "vnet_name")

    @vnet_name.setter
    def vnet_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vnet_name", value)

    @property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> Optional[pulumi.Input[str]]:
        """
        The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        """
        return pulumi.get(self, "end_address")

    @end_address.setter
    def end_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_address", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Virtual Network route.
        """
        return pulumi.get(self, "route_name")

    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_name", value)

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[pulumi.Input[Union[str, 'RouteType']]]:
        """
        The type of route this is:
        DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
        INHERITED - Routes inherited from the real Virtual Network routes
        STATIC - Static route set on the app only

        These values will be used for syncing an app's routes with those from a Virtual Network.
        """
        return pulumi.get(self, "route_type")

    @route_type.setter
    def route_type(self, value: Optional[pulumi.Input[Union[str, 'RouteType']]]):
        pulumi.set(self, "route_type", value)

    @property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> Optional[pulumi.Input[str]]:
        """
        The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        """
        return pulumi.get(self, "start_address")

    @start_address.setter
    def start_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_address", value)


class AppServicePlanRouteForVnet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_address: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[Union[str, 'RouteType']]] = None,
                 start_address: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Virtual Network route contract used to pass routing information for a Virtual Network.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_address: The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the App Service plan.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] route_name: Name of the Virtual Network route.
        :param pulumi.Input[Union[str, 'RouteType']] route_type: The type of route this is:
               DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
               INHERITED - Routes inherited from the real Virtual Network routes
               STATIC - Static route set on the app only
               
               These values will be used for syncing an app's routes with those from a Virtual Network.
        :param pulumi.Input[str] start_address: The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        :param pulumi.Input[str] vnet_name: Name of the Virtual Network.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppServicePlanRouteForVnetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Network route contract used to pass routing information for a Virtual Network.

        :param str resource_name: The name of the resource.
        :param AppServicePlanRouteForVnetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppServicePlanRouteForVnetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_address: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[Union[str, 'RouteType']]] = None,
                 start_address: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppServicePlanRouteForVnetArgs.__new__(AppServicePlanRouteForVnetArgs)

            __props__.__dict__["end_address"] = end_address
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_name"] = route_name
            __props__.__dict__["route_type"] = route_type
            __props__.__dict__["start_address"] = start_address
            if vnet_name is None and not opts.urn:
                raise TypeError("Missing required property 'vnet_name'")
            __props__.__dict__["vnet_name"] = vnet_name
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web/v20190801:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20150801:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20150801:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20160901:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20160901:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20180201:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20180201:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20200601:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20200601:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20200901:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20200901:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20201001:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20201001:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20201201:AppServicePlanRouteForVnet"), pulumi.Alias(type_="azure-nextgen:web/v20201201:AppServicePlanRouteForVnet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AppServicePlanRouteForVnet, __self__).__init__(
            'azure-native:web/v20190801:AppServicePlanRouteForVnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AppServicePlanRouteForVnet':
        """
        Get an existing AppServicePlanRouteForVnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppServicePlanRouteForVnetArgs.__new__(AppServicePlanRouteForVnetArgs)

        __props__.__dict__["end_address"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["route_type"] = None
        __props__.__dict__["start_address"] = None
        __props__.__dict__["type"] = None
        return AppServicePlanRouteForVnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> pulumi.Output[Optional[str]]:
        """
        The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        """
        return pulumi.get(self, "end_address")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of route this is:
        DEFAULT - By default, every app has routes to the local address ranges specified by RFC1918
        INHERITED - Routes inherited from the real Virtual Network routes
        STATIC - Static route set on the app only

        These values will be used for syncing an app's routes with those from a Virtual Network.
        """
        return pulumi.get(self, "route_type")

    @property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> pulumi.Output[Optional[str]]:
        """
        The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        """
        return pulumi.get(self, "start_address")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

