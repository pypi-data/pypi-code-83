# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .cloud_endpoint import *
from .get_cloud_endpoint import *
from .get_registered_server import *
from .get_server_endpoint import *
from .get_storage_sync_service import *
from .get_sync_group import *
from .registered_server import *
from .server_endpoint import *
from .storage_sync_service import *
from .sync_group import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:storagesync/v20181001:CloudEndpoint":
                return CloudEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:storagesync/v20181001:RegisteredServer":
                return RegisteredServer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:storagesync/v20181001:ServerEndpoint":
                return ServerEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:storagesync/v20181001:StorageSyncService":
                return StorageSyncService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:storagesync/v20181001:SyncGroup":
                return SyncGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "storagesync/v20181001", _module_instance)

_register_module()
