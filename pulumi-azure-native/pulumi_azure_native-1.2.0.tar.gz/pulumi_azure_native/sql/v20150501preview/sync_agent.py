# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SyncAgentArgs', 'SyncAgent']

@pulumi.input_type
class SyncAgentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 sync_agent_name: Optional[pulumi.Input[str]] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SyncAgent resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server on which the sync agent is hosted.
        :param pulumi.Input[str] sync_agent_name: The name of the sync agent.
        :param pulumi.Input[str] sync_database_id: ARM resource id of the sync database in the sync agent.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if sync_agent_name is not None:
            pulumi.set(__self__, "sync_agent_name", sync_agent_name)
        if sync_database_id is not None:
            pulumi.set(__self__, "sync_database_id", sync_database_id)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server on which the sync agent is hosted.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="syncAgentName")
    def sync_agent_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sync agent.
        """
        return pulumi.get(self, "sync_agent_name")

    @sync_agent_name.setter
    def sync_agent_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_agent_name", value)

    @property
    @pulumi.getter(name="syncDatabaseId")
    def sync_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource id of the sync database in the sync agent.
        """
        return pulumi.get(self, "sync_database_id")

    @sync_database_id.setter
    def sync_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_database_id", value)


class SyncAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sync_agent_name: Optional[pulumi.Input[str]] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure SQL Database sync agent.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server on which the sync agent is hosted.
        :param pulumi.Input[str] sync_agent_name: The name of the sync agent.
        :param pulumi.Input[str] sync_database_id: ARM resource id of the sync database in the sync agent.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyncAgentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL Database sync agent.

        :param str resource_name: The name of the resource.
        :param SyncAgentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyncAgentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sync_agent_name: Optional[pulumi.Input[str]] = None,
                 sync_database_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SyncAgentArgs.__new__(SyncAgentArgs)

            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sync_agent_name"] = sync_agent_name
            __props__.__dict__["sync_database_id"] = sync_database_id
            __props__.__dict__["expiry_time"] = None
            __props__.__dict__["is_up_to_date"] = None
            __props__.__dict__["last_alive_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:sql/v20150501preview:SyncAgent"), pulumi.Alias(type_="azure-native:sql:SyncAgent"), pulumi.Alias(type_="azure-nextgen:sql:SyncAgent"), pulumi.Alias(type_="azure-native:sql/v20200202preview:SyncAgent"), pulumi.Alias(type_="azure-nextgen:sql/v20200202preview:SyncAgent"), pulumi.Alias(type_="azure-native:sql/v20200801preview:SyncAgent"), pulumi.Alias(type_="azure-nextgen:sql/v20200801preview:SyncAgent"), pulumi.Alias(type_="azure-native:sql/v20201101preview:SyncAgent"), pulumi.Alias(type_="azure-nextgen:sql/v20201101preview:SyncAgent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SyncAgent, __self__).__init__(
            'azure-native:sql/v20150501preview:SyncAgent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SyncAgent':
        """
        Get an existing SyncAgent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SyncAgentArgs.__new__(SyncAgentArgs)

        __props__.__dict__["expiry_time"] = None
        __props__.__dict__["is_up_to_date"] = None
        __props__.__dict__["last_alive_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["sync_database_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return SyncAgent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> pulumi.Output[str]:
        """
        Expiration time of the sync agent version.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter(name="isUpToDate")
    def is_up_to_date(self) -> pulumi.Output[bool]:
        """
        If the sync agent version is up to date.
        """
        return pulumi.get(self, "is_up_to_date")

    @property
    @pulumi.getter(name="lastAliveTime")
    def last_alive_time(self) -> pulumi.Output[str]:
        """
        Last alive time of the sync agent.
        """
        return pulumi.get(self, "last_alive_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the sync agent.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="syncDatabaseId")
    def sync_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource id of the sync database in the sync agent.
        """
        return pulumi.get(self, "sync_database_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the sync agent.
        """
        return pulumi.get(self, "version")

