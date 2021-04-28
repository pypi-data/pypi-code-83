# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_monitor import *
from .get_tag_rule import *
from .list_deployment_info import *
from .list_monitored_resource import *
from .list_vm_host import *
from .monitor import *
from .tag_rule import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20200701preview,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:elastic:Monitor":
                return Monitor(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:elastic:TagRule":
                return TagRule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "elastic", _module_instance)

_register_module()
