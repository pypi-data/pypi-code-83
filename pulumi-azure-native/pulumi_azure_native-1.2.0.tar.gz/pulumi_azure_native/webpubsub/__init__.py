# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_web_pub_sub import *
from .get_web_pub_sub_private_endpoint_connection import *
from .get_web_pub_sub_shared_private_link_resource import *
from .list_web_pub_sub_keys import *
from .web_pub_sub import *
from .web_pub_sub_private_endpoint_connection import *
from .web_pub_sub_shared_private_link_resource import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20210401preview,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:webpubsub:WebPubSub":
                return WebPubSub(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:webpubsub:WebPubSubPrivateEndpointConnection":
                return WebPubSubPrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:webpubsub:WebPubSubSharedPrivateLinkResource":
                return WebPubSubSharedPrivateLinkResource(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "webpubsub", _module_instance)

_register_module()
