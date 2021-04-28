# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .function import *
from .get_function import *
from .get_input import *
from .get_output import *
from .get_streaming_job import *
from .input import *
from .output import *
from .streaming_job import *
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
            if typ == "azure-native:streamanalytics/v20160301:Function":
                return Function(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:streamanalytics/v20160301:Input":
                return Input(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:streamanalytics/v20160301:Output":
                return Output(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:streamanalytics/v20160301:StreamingJob":
                return StreamingJob(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "streamanalytics/v20160301", _module_instance)

_register_module()
