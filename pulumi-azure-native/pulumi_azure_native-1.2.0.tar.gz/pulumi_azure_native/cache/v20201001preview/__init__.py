# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .database import *
from .get_database import *
from .get_private_endpoint_connection import *
from .get_redis_enterprise import *
from .list_database_keys import *
from .private_endpoint_connection import *
from .redis_enterprise import *
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
            if typ == "azure-native:cache/v20201001preview:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cache/v20201001preview:PrivateEndpointConnection":
                return PrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cache/v20201001preview:RedisEnterprise":
                return RedisEnterprise(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "cache/v20201001preview", _module_instance)

_register_module()
