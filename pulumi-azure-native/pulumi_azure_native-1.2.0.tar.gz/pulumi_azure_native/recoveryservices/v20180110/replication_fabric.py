# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ReplicationFabricArgs', 'ReplicationFabric']

@pulumi.input_type
class ReplicationFabricArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['FabricCreationInputPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ReplicationFabric resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name: The name of the recovery services vault.
        :param pulumi.Input[str] fabric_name: Name of the ASR fabric.
        :param pulumi.Input['FabricCreationInputPropertiesArgs'] properties: Fabric creation input.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if fabric_name is not None:
            pulumi.set(__self__, "fabric_name", fabric_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the recovery services vault is present.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the recovery services vault.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ASR fabric.
        """
        return pulumi.get(self, "fabric_name")

    @fabric_name.setter
    def fabric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fabric_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['FabricCreationInputPropertiesArgs']]:
        """
        Fabric creation input.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['FabricCreationInputPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class ReplicationFabric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['FabricCreationInputPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Fabric definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fabric_name: Name of the ASR fabric.
        :param pulumi.Input[pulumi.InputType['FabricCreationInputPropertiesArgs']] properties: Fabric creation input.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name_: The name of the recovery services vault.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationFabricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Fabric definition.

        :param str resource_name: The name of the resource.
        :param ReplicationFabricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationFabricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['FabricCreationInputPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
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
            __props__ = ReplicationFabricArgs.__new__(ReplicationFabricArgs)

            __props__.__dict__["fabric_name"] = fabric_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:recoveryservices/v20180110:ReplicationFabric"), pulumi.Alias(type_="azure-native:recoveryservices:ReplicationFabric"), pulumi.Alias(type_="azure-nextgen:recoveryservices:ReplicationFabric"), pulumi.Alias(type_="azure-native:recoveryservices/v20160810:ReplicationFabric"), pulumi.Alias(type_="azure-nextgen:recoveryservices/v20160810:ReplicationFabric"), pulumi.Alias(type_="azure-native:recoveryservices/v20180710:ReplicationFabric"), pulumi.Alias(type_="azure-nextgen:recoveryservices/v20180710:ReplicationFabric"), pulumi.Alias(type_="azure-native:recoveryservices/v20210210:ReplicationFabric"), pulumi.Alias(type_="azure-nextgen:recoveryservices/v20210210:ReplicationFabric"), pulumi.Alias(type_="azure-native:recoveryservices/v20210301:ReplicationFabric"), pulumi.Alias(type_="azure-nextgen:recoveryservices/v20210301:ReplicationFabric")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReplicationFabric, __self__).__init__(
            'azure-native:recoveryservices/v20180110:ReplicationFabric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationFabric':
        """
        Get an existing ReplicationFabric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationFabricArgs.__new__(ReplicationFabricArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ReplicationFabric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.FabricPropertiesResponse']:
        """
        Fabric related data.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

