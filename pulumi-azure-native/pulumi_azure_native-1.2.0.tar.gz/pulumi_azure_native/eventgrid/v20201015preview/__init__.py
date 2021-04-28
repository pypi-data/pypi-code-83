# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .domain import *
from .domain_topic import *
from .event_channel import *
from .event_subscription import *
from .get_domain import *
from .get_domain_topic import *
from .get_event_channel import *
from .get_event_subscription import *
from .get_event_subscription_delivery_attributes import *
from .get_event_subscription_full_url import *
from .get_partner_namespace import *
from .get_partner_registration import *
from .get_partner_topic_event_subscription import *
from .get_partner_topic_event_subscription_delivery_attributes import *
from .get_partner_topic_event_subscription_full_url import *
from .get_private_endpoint_connection import *
from .get_system_topic import *
from .get_system_topic_event_subscription import *
from .get_system_topic_event_subscription_delivery_attributes import *
from .get_system_topic_event_subscription_full_url import *
from .get_topic import *
from .list_domain_shared_access_keys import *
from .list_partner_namespace_shared_access_keys import *
from .list_topic_shared_access_keys import *
from .partner_namespace import *
from .partner_registration import *
from .partner_topic_event_subscription import *
from .private_endpoint_connection import *
from .system_topic import *
from .system_topic_event_subscription import *
from .topic import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:eventgrid/v20201015preview:Domain":
                return Domain(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:DomainTopic":
                return DomainTopic(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:EventChannel":
                return EventChannel(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:EventSubscription":
                return EventSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:PartnerNamespace":
                return PartnerNamespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:PartnerRegistration":
                return PartnerRegistration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:PartnerTopicEventSubscription":
                return PartnerTopicEventSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:PrivateEndpointConnection":
                return PrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:SystemTopic":
                return SystemTopic(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:SystemTopicEventSubscription":
                return SystemTopicEventSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:eventgrid/v20201015preview:Topic":
                return Topic(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "eventgrid/v20201015preview", _module_instance)

_register_module()
