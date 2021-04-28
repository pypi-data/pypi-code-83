# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 channel_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 channel_functions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[str] account_name: Account Name
        :param pulumi.Input[str] channel_type: The channel type
        :param pulumi.Input[str] resource_group_name: Resource Group Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] channel_functions: The functions to be enabled for the channel
        :param pulumi.Input[str] channel_name: Channel Name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] credentials: The channel credentials
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "channel_type", channel_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if channel_functions is not None:
            pulumi.set(__self__, "channel_functions", channel_functions)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account Name
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Input[str]:
        """
        The channel type
        """
        return pulumi.get(self, "channel_type")

    @channel_type.setter
    def channel_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Resource Group Name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The functions to be enabled for the channel
        """
        return pulumi.get(self, "channel_functions")

    @channel_functions.setter
    def channel_functions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "channel_functions", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        """
        Channel Name
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The channel credentials
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "credentials", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 channel_functions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_type: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The EngagementFabric channel

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] channel_functions: The functions to be enabled for the channel
        :param pulumi.Input[str] channel_name: Channel Name
        :param pulumi.Input[str] channel_type: The channel type
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] credentials: The channel credentials
        :param pulumi.Input[str] resource_group_name: Resource Group Name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The EngagementFabric channel

        :param str resource_name: The name of the resource.
        :param ChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 channel_functions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 channel_type: Optional[pulumi.Input[str]] = None,
                 credentials: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ChannelArgs.__new__(ChannelArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["channel_functions"] = channel_functions
            __props__.__dict__["channel_name"] = channel_name
            if channel_type is None and not opts.urn:
                raise TypeError("Missing required property 'channel_type'")
            __props__.__dict__["channel_type"] = channel_type
            __props__.__dict__["credentials"] = credentials
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:engagementfabric/v20180901preview:Channel"), pulumi.Alias(type_="azure-native:engagementfabric:Channel"), pulumi.Alias(type_="azure-nextgen:engagementfabric:Channel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Channel, __self__).__init__(
            'azure-native:engagementfabric/v20180901preview:Channel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Channel':
        """
        Get an existing Channel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ChannelArgs.__new__(ChannelArgs)

        __props__.__dict__["channel_functions"] = None
        __props__.__dict__["channel_type"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="channelFunctions")
    def channel_functions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The functions to be enabled for the channel
        """
        return pulumi.get(self, "channel_functions")

    @property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> pulumi.Output[str]:
        """
        The channel type
        """
        return pulumi.get(self, "channel_type")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The channel credentials
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The fully qualified type of the resource
        """
        return pulumi.get(self, "type")

