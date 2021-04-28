# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_live_event import *
from .get_live_output import *
from .get_streaming_endpoint import *
from .live_event import *
from .live_output import *
from .streaming_endpoint import *
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
            if typ == "azure-native:media/v20190501preview:LiveEvent":
                return LiveEvent(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:media/v20190501preview:LiveOutput":
                return LiveOutput(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:media/v20190501preview:StreamingEndpoint":
                return StreamingEndpoint(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "media/v20190501preview", _module_instance)

_register_module()
