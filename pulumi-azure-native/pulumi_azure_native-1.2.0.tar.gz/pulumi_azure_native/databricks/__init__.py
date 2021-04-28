# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_workspace import *
from .getv_net_peering import *
from .v_net_peering import *
from .workspace import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20180401,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:databricks:Workspace":
                return Workspace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:databricks:vNetPeering":
                return VNetPeering(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "databricks", _module_instance)

_register_module()
