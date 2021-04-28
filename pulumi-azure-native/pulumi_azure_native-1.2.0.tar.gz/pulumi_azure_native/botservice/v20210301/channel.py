# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ChannelArgs', 'Channel']

@pulumi.input_type
class ChannelArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 channel_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['AlexaChannelArgs', 'DirectLineChannelArgs', 'DirectLineSpeechChannelArgs', 'EmailChannelArgs', 'FacebookChannelArgs', 'KikChannelArgs', 'LineChannelArgs', 'MsTeamsChannelArgs', 'SkypeChannelArgs', 'SlackChannelArgs', 'SmsChannelArgs', 'TelegramChannelArgs', 'WebChatChannelArgs']]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Channel resource.
        :param pulumi.Input[str] resource_group_name: The name of the Bot resource group in the user subscription.
        :param pulumi.Input[str] resource_name: The name of the Bot resource.
        :param pulumi.Input[str] channel_name: The name of the Channel resource.
        :param pulumi.Input[str] etag: Entity Tag
        :param pulumi.Input[Union[str, 'Kind']] kind: Required. Gets or sets the Kind of the resource.
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input[Union['AlexaChannelArgs', 'DirectLineChannelArgs', 'DirectLineSpeechChannelArgs', 'EmailChannelArgs', 'FacebookChannelArgs', 'KikChannelArgs', 'LineChannelArgs', 'MsTeamsChannelArgs', 'SkypeChannelArgs', 'SlackChannelArgs', 'SmsChannelArgs', 'TelegramChannelArgs', 'WebChatChannelArgs']] properties: The set of properties specific to bot channel resource
        :param pulumi.Input['SkuArgs'] sku: Gets or sets the SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Bot resource group in the user subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the Bot resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Channel resource.
        """
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Entity Tag
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'Kind']]]:
        """
        Required. Gets or sets the Kind of the resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'Kind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Union['AlexaChannelArgs', 'DirectLineChannelArgs', 'DirectLineSpeechChannelArgs', 'EmailChannelArgs', 'FacebookChannelArgs', 'KikChannelArgs', 'LineChannelArgs', 'MsTeamsChannelArgs', 'SkypeChannelArgs', 'SlackChannelArgs', 'SmsChannelArgs', 'TelegramChannelArgs', 'WebChatChannelArgs']]]:
        """
        The set of properties specific to bot channel resource
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Union['AlexaChannelArgs', 'DirectLineChannelArgs', 'DirectLineSpeechChannelArgs', 'EmailChannelArgs', 'FacebookChannelArgs', 'KikChannelArgs', 'LineChannelArgs', 'MsTeamsChannelArgs', 'SkypeChannelArgs', 'SlackChannelArgs', 'SmsChannelArgs', 'TelegramChannelArgs', 'WebChatChannelArgs']]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Gets or sets the SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Channel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['AlexaChannelArgs'], pulumi.InputType['DirectLineChannelArgs'], pulumi.InputType['DirectLineSpeechChannelArgs'], pulumi.InputType['EmailChannelArgs'], pulumi.InputType['FacebookChannelArgs'], pulumi.InputType['KikChannelArgs'], pulumi.InputType['LineChannelArgs'], pulumi.InputType['MsTeamsChannelArgs'], pulumi.InputType['SkypeChannelArgs'], pulumi.InputType['SlackChannelArgs'], pulumi.InputType['SmsChannelArgs'], pulumi.InputType['TelegramChannelArgs'], pulumi.InputType['WebChatChannelArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Bot channel resource definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] channel_name: The name of the Channel resource.
        :param pulumi.Input[str] etag: Entity Tag
        :param pulumi.Input[Union[str, 'Kind']] kind: Required. Gets or sets the Kind of the resource.
        :param pulumi.Input[str] location: Specifies the location of the resource.
        :param pulumi.Input[Union[pulumi.InputType['AlexaChannelArgs'], pulumi.InputType['DirectLineChannelArgs'], pulumi.InputType['DirectLineSpeechChannelArgs'], pulumi.InputType['EmailChannelArgs'], pulumi.InputType['FacebookChannelArgs'], pulumi.InputType['KikChannelArgs'], pulumi.InputType['LineChannelArgs'], pulumi.InputType['MsTeamsChannelArgs'], pulumi.InputType['SkypeChannelArgs'], pulumi.InputType['SlackChannelArgs'], pulumi.InputType['SmsChannelArgs'], pulumi.InputType['TelegramChannelArgs'], pulumi.InputType['WebChatChannelArgs']]] properties: The set of properties specific to bot channel resource
        :param pulumi.Input[str] resource_group_name: The name of the Bot resource group in the user subscription.
        :param pulumi.Input[str] resource_name_: The name of the Bot resource.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Gets or sets the SKU of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Contains resource tags defined as key/value pairs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Bot channel resource definition

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
                 channel_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union[pulumi.InputType['AlexaChannelArgs'], pulumi.InputType['DirectLineChannelArgs'], pulumi.InputType['DirectLineSpeechChannelArgs'], pulumi.InputType['EmailChannelArgs'], pulumi.InputType['FacebookChannelArgs'], pulumi.InputType['KikChannelArgs'], pulumi.InputType['LineChannelArgs'], pulumi.InputType['MsTeamsChannelArgs'], pulumi.InputType['SkypeChannelArgs'], pulumi.InputType['SlackChannelArgs'], pulumi.InputType['SmsChannelArgs'], pulumi.InputType['TelegramChannelArgs'], pulumi.InputType['WebChatChannelArgs']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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

            __props__.__dict__["channel_name"] = channel_name
            __props__.__dict__["etag"] = etag
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:botservice/v20210301:Channel"), pulumi.Alias(type_="azure-native:botservice:Channel"), pulumi.Alias(type_="azure-nextgen:botservice:Channel"), pulumi.Alias(type_="azure-native:botservice/v20171201:Channel"), pulumi.Alias(type_="azure-nextgen:botservice/v20171201:Channel"), pulumi.Alias(type_="azure-native:botservice/v20180712:Channel"), pulumi.Alias(type_="azure-nextgen:botservice/v20180712:Channel"), pulumi.Alias(type_="azure-native:botservice/v20200602:Channel"), pulumi.Alias(type_="azure-nextgen:botservice/v20200602:Channel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Channel, __self__).__init__(
            'azure-native:botservice/v20210301:Channel',
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

        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Channel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Entity Tag
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Required. Gets or sets the Kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        The set of properties specific to bot channel resource
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Gets or sets the SKU of the resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

