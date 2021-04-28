# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .get_policy_assignment import *
from .get_policy_definition import *
from .get_policy_definition_at_management_group import *
from .get_policy_set_definition import *
from .get_policy_set_definition_at_management_group import *
from .policy_assignment import *
from .policy_definition import *
from .policy_definition_at_management_group import *
from .policy_set_definition import *
from .policy_set_definition_at_management_group import *
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
            if typ == "azure-native:authorization/v20180501:PolicyAssignment":
                return PolicyAssignment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:authorization/v20180501:PolicyDefinition":
                return PolicyDefinition(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:authorization/v20180501:PolicyDefinitionAtManagementGroup":
                return PolicyDefinitionAtManagementGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:authorization/v20180501:PolicySetDefinition":
                return PolicySetDefinition(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:authorization/v20180501:PolicySetDefinitionAtManagementGroup":
                return PolicySetDefinitionAtManagementGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "authorization/v20180501", _module_instance)

_register_module()
