# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['WebAppVnetConnectionArgs', 'WebAppVnetConnection']

@pulumi.input_type
class WebAppVnetConnectionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cert_blob: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[str]] = None,
                 is_swift: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 vnet_resource_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppVnetConnection resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] cert_blob: A certificate file (.cer) blob containing the public key of the private key used to authenticate a 
               Point-To-Site VPN connection.
        :param pulumi.Input[str] dns_servers: DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.
        :param pulumi.Input[bool] is_swift: Flag that is used to denote if this is VNET injection
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] vnet_name: Name of an existing Virtual Network.
        :param pulumi.Input[str] vnet_resource_id: The Virtual Network's resource ID.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cert_blob is not None:
            pulumi.set(__self__, "cert_blob", cert_blob)
        if dns_servers is not None:
            pulumi.set(__self__, "dns_servers", dns_servers)
        if is_swift is not None:
            pulumi.set(__self__, "is_swift", is_swift)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if vnet_name is not None:
            pulumi.set(__self__, "vnet_name", vnet_name)
        if vnet_resource_id is not None:
            pulumi.set(__self__, "vnet_resource_id", vnet_resource_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
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
    @pulumi.getter(name="certBlob")
    def cert_blob(self) -> Optional[pulumi.Input[str]]:
        """
        A certificate file (.cer) blob containing the public key of the private key used to authenticate a 
        Point-To-Site VPN connection.
        """
        return pulumi.get(self, "cert_blob")

    @cert_blob.setter
    def cert_blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_blob", value)

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[pulumi.Input[str]]:
        """
        DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.
        """
        return pulumi.get(self, "dns_servers")

    @dns_servers.setter
    def dns_servers(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_servers", value)

    @property
    @pulumi.getter(name="isSwift")
    def is_swift(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag that is used to denote if this is VNET injection
        """
        return pulumi.get(self, "is_swift")

    @is_swift.setter
    def is_swift(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_swift", value)

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
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of an existing Virtual Network.
        """
        return pulumi.get(self, "vnet_name")

    @vnet_name.setter
    def vnet_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_name", value)

    @property
    @pulumi.getter(name="vnetResourceId")
    def vnet_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Virtual Network's resource ID.
        """
        return pulumi.get(self, "vnet_resource_id")

    @vnet_resource_id.setter
    def vnet_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_resource_id", value)


class WebAppVnetConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert_blob: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[str]] = None,
                 is_swift: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 vnet_resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Virtual Network information contract.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert_blob: A certificate file (.cer) blob containing the public key of the private key used to authenticate a 
               Point-To-Site VPN connection.
        :param pulumi.Input[str] dns_servers: DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.
        :param pulumi.Input[bool] is_swift: Flag that is used to denote if this is VNET injection
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] vnet_name: Name of an existing Virtual Network.
        :param pulumi.Input[str] vnet_resource_id: The Virtual Network's resource ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppVnetConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual Network information contract.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param WebAppVnetConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppVnetConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert_blob: Optional[pulumi.Input[str]] = None,
                 dns_servers: Optional[pulumi.Input[str]] = None,
                 is_swift: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 vnet_resource_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppVnetConnectionArgs.__new__(WebAppVnetConnectionArgs)

            __props__.__dict__["cert_blob"] = cert_blob
            __props__.__dict__["dns_servers"] = dns_servers
            __props__.__dict__["is_swift"] = is_swift
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["vnet_name"] = vnet_name
            __props__.__dict__["vnet_resource_id"] = vnet_resource_id
            __props__.__dict__["cert_thumbprint"] = None
            __props__.__dict__["resync_required"] = None
            __props__.__dict__["routes"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:web:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20150801:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20150801:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20160801:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20160801:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20180201:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20181101:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20190801:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20200601:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20200901:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20201001:WebAppVnetConnection"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppVnetConnection"), pulumi.Alias(type_="azure-nextgen:web/v20201201:WebAppVnetConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppVnetConnection, __self__).__init__(
            'azure-native:web:WebAppVnetConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppVnetConnection':
        """
        Get an existing WebAppVnetConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppVnetConnectionArgs.__new__(WebAppVnetConnectionArgs)

        __props__.__dict__["cert_blob"] = None
        __props__.__dict__["cert_thumbprint"] = None
        __props__.__dict__["dns_servers"] = None
        __props__.__dict__["is_swift"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resync_required"] = None
        __props__.__dict__["routes"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vnet_resource_id"] = None
        return WebAppVnetConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certBlob")
    def cert_blob(self) -> pulumi.Output[Optional[str]]:
        """
        A certificate file (.cer) blob containing the public key of the private key used to authenticate a 
        Point-To-Site VPN connection.
        """
        return pulumi.get(self, "cert_blob")

    @property
    @pulumi.getter(name="certThumbprint")
    def cert_thumbprint(self) -> pulumi.Output[str]:
        """
        The client certificate thumbprint.
        """
        return pulumi.get(self, "cert_thumbprint")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> pulumi.Output[Optional[str]]:
        """
        DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.
        """
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter(name="isSwift")
    def is_swift(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag that is used to denote if this is VNET injection
        """
        return pulumi.get(self, "is_swift")

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
    @pulumi.getter(name="resyncRequired")
    def resync_required(self) -> pulumi.Output[bool]:
        """
        <code>true</code> if a resync is required; otherwise, <code>false</code>.
        """
        return pulumi.get(self, "resync_required")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Sequence['outputs.VnetRouteResponse']]:
        """
        The routes that this Virtual Network connection uses.
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vnetResourceId")
    def vnet_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Virtual Network's resource ID.
        """
        return pulumi.get(self, "vnet_resource_id")

