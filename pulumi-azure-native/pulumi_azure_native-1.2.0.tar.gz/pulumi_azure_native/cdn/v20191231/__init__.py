# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .custom_domain import *
from .endpoint import *
from .get_custom_domain import *
from .get_endpoint import *
from .get_origin import *
from .get_origin_group import *
from .get_profile import *
from .get_profile_supported_optimization_types import *
from .origin import *
from .origin_group import *
from .profile import *
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
            if typ == "azure-native:cdn/v20191231:CustomDomain":
                return CustomDomain(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cdn/v20191231:Endpoint":
                return Endpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cdn/v20191231:Origin":
                return Origin(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cdn/v20191231:OriginGroup":
                return OriginGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:cdn/v20191231:Profile":
                return Profile(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "cdn/v20191231", _module_instance)

_register_module()
