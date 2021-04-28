# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .application import *
from .application_type import *
from .application_type_version import *
from .cluster import *
from .get_application import *
from .get_application_type import *
from .get_application_type_version import *
from .get_cluster import *
from .get_service import *
from .service import *
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
            if typ == "azure-native:servicefabric/v20190301preview:Application":
                return Application(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:servicefabric/v20190301preview:ApplicationType":
                return ApplicationType(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:servicefabric/v20190301preview:ApplicationTypeVersion":
                return ApplicationTypeVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:servicefabric/v20190301preview:Cluster":
                return Cluster(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:servicefabric/v20190301preview:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "servicefabric/v20190301preview", _module_instance)

_register_module()
