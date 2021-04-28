# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .cluster import *
from .consumer_group import *
from .disaster_recovery_config import *
from .event_hub import *
from .event_hub_authorization_rule import *
from .get_cluster import *
from .get_consumer_group import *
from .get_disaster_recovery_config import *
from .get_event_hub import *
from .get_event_hub_authorization_rule import *
from .get_namespace import *
from .get_namespace_authorization_rule import *
from .get_namespace_ip_filter_rule import *
from .get_namespace_network_rule_set import *
from .get_namespace_virtual_network_rule import *
from .get_private_endpoint_connection import *
from .list_disaster_recovery_config_keys import *
from .list_event_hub_keys import *
from .list_namespace_keys import *
from .namespace import *
from .namespace_authorization_rule import *
from .namespace_ip_filter_rule import *
from .namespace_network_rule_set import *
from .namespace_virtual_network_rule import *
from .private_endpoint_connection import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20140901,
    v20150801,
    v20170401,
    v20180101preview,
    v20210101preview,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:eventhub:Cluster":
                return Cluster(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:ConsumerGroup":
                return ConsumerGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:DisasterRecoveryConfig":
                return DisasterRecoveryConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:EventHub":
                return EventHub(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:EventHubAuthorizationRule":
                return EventHubAuthorizationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:Namespace":
                return Namespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:NamespaceAuthorizationRule":
                return NamespaceAuthorizationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:NamespaceIpFilterRule":
                return NamespaceIpFilterRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:NamespaceNetworkRuleSet":
                return NamespaceNetworkRuleSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:NamespaceVirtualNetworkRule":
                return NamespaceVirtualNetworkRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventhub:PrivateEndpointConnection":
                return PrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "eventhub", _module_instance)

_register_module()
