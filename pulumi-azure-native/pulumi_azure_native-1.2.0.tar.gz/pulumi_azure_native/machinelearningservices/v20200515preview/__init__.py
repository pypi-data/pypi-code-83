# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_linked_workspace import *
from .get_machine_learning_compute import *
from .get_machine_learning_service import *
from .get_private_endpoint_connection import *
from .get_workspace import *
from .linked_workspace import *
from .list_machine_learning_compute_keys import *
from .list_machine_learning_compute_nodes import *
from .list_workspace_keys import *
from .machine_learning_compute import *
from .machine_learning_service import *
from .private_endpoint_connection import *
from .workspace import *
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
            if typ == "azure-native:machinelearningservices/v20200515preview:LinkedWorkspace":
                return LinkedWorkspace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:machinelearningservices/v20200515preview:MachineLearningCompute":
                return MachineLearningCompute(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:machinelearningservices/v20200515preview:MachineLearningService":
                return MachineLearningService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:machinelearningservices/v20200515preview:PrivateEndpointConnection":
                return PrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:machinelearningservices/v20200515preview:Workspace":
                return Workspace(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "machinelearningservices/v20200515preview", _module_instance)

_register_module()
