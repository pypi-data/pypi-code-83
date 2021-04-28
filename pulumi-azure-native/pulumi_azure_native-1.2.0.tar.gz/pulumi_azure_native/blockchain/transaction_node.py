# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TransactionNodeArgs', 'TransactionNode']

@pulumi.input_type
class TransactionNodeArgs:
    def __init__(__self__, *,
                 blockchain_member_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 transaction_node_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TransactionNode resource.
        :param pulumi.Input[str] blockchain_member_name: Blockchain member name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Sequence[pulumi.Input['FirewallRuleArgs']]] firewall_rules: Gets or sets the firewall rules.
        :param pulumi.Input[str] location: Gets or sets the transaction node location.
        :param pulumi.Input[str] password: Sets the transaction node dns endpoint basic auth password.
        :param pulumi.Input[str] transaction_node_name: Transaction node name.
        """
        pulumi.set(__self__, "blockchain_member_name", blockchain_member_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if firewall_rules is not None:
            pulumi.set(__self__, "firewall_rules", firewall_rules)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if transaction_node_name is not None:
            pulumi.set(__self__, "transaction_node_name", transaction_node_name)

    @property
    @pulumi.getter(name="blockchainMemberName")
    def blockchain_member_name(self) -> pulumi.Input[str]:
        """
        Blockchain member name.
        """
        return pulumi.get(self, "blockchain_member_name")

    @blockchain_member_name.setter
    def blockchain_member_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "blockchain_member_name", value)

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
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleArgs']]]]:
        """
        Gets or sets the firewall rules.
        """
        return pulumi.get(self, "firewall_rules")

    @firewall_rules.setter
    def firewall_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FirewallRuleArgs']]]]):
        pulumi.set(self, "firewall_rules", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the transaction node location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Sets the transaction node dns endpoint basic auth password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="transactionNodeName")
    def transaction_node_name(self) -> Optional[pulumi.Input[str]]:
        """
        Transaction node name.
        """
        return pulumi.get(self, "transaction_node_name")

    @transaction_node_name.setter
    def transaction_node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transaction_node_name", value)


class TransactionNode(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blockchain_member_name: Optional[pulumi.Input[str]] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 transaction_node_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Payload of the transaction node which is the request/response of the resource provider.
        API Version: 2018-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] blockchain_member_name: Blockchain member name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleArgs']]]] firewall_rules: Gets or sets the firewall rules.
        :param pulumi.Input[str] location: Gets or sets the transaction node location.
        :param pulumi.Input[str] password: Sets the transaction node dns endpoint basic auth password.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] transaction_node_name: Transaction node name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TransactionNodeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Payload of the transaction node which is the request/response of the resource provider.
        API Version: 2018-06-01-preview.

        :param str resource_name: The name of the resource.
        :param TransactionNodeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TransactionNodeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blockchain_member_name: Optional[pulumi.Input[str]] = None,
                 firewall_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FirewallRuleArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 transaction_node_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = TransactionNodeArgs.__new__(TransactionNodeArgs)

            if blockchain_member_name is None and not opts.urn:
                raise TypeError("Missing required property 'blockchain_member_name'")
            __props__.__dict__["blockchain_member_name"] = blockchain_member_name
            __props__.__dict__["firewall_rules"] = firewall_rules
            __props__.__dict__["location"] = location
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["transaction_node_name"] = transaction_node_name
            __props__.__dict__["dns"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_key"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:blockchain:TransactionNode"), pulumi.Alias(type_="azure-native:blockchain/v20180601preview:TransactionNode"), pulumi.Alias(type_="azure-nextgen:blockchain/v20180601preview:TransactionNode")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TransactionNode, __self__).__init__(
            'azure-native:blockchain:TransactionNode',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TransactionNode':
        """
        Get an existing TransactionNode resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TransactionNodeArgs.__new__(TransactionNodeArgs)

        __props__.__dict__["dns"] = None
        __props__.__dict__["firewall_rules"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_key"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_name"] = None
        return TransactionNode(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def dns(self) -> pulumi.Output[str]:
        """
        Gets or sets the transaction node dns endpoint.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> pulumi.Output[Optional[Sequence['outputs.FirewallRuleResponse']]]:
        """
        Gets or sets the firewall rules.
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the transaction node location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Sets the transaction node dns endpoint basic auth password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the blockchain member provision state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        Gets or sets the transaction node public key.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the service - e.g. "Microsoft.Blockchain"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Gets or sets the transaction node dns endpoint basic auth user name.
        """
        return pulumi.get(self, "user_name")

