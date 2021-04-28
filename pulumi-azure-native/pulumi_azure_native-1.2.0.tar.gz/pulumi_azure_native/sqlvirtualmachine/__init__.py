# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .availability_group_listener import *
from .get_availability_group_listener import *
from .get_sql_virtual_machine import *
from .get_sql_virtual_machine_group import *
from .sql_virtual_machine import *
from .sql_virtual_machine_group import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20170301preview,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:sqlvirtualmachine:AvailabilityGroupListener":
                return AvailabilityGroupListener(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:sqlvirtualmachine:SqlVirtualMachine":
                return SqlVirtualMachine(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:sqlvirtualmachine:SqlVirtualMachineGroup":
                return SqlVirtualMachineGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "sqlvirtualmachine", _module_instance)

_register_module()
