# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .automation_account import *
from .certificate import *
from .connection import *
from .connection_type import *
from .credential import *
from .dsc_configuration import *
from .dsc_node_configuration import *
from .get_automation_account import *
from .get_certificate import *
from .get_connection import *
from .get_connection_type import *
from .get_credential import *
from .get_dsc_configuration import *
from .get_dsc_node_configuration import *
from .get_job_schedule import *
from .get_module import *
from .get_runbook import *
from .get_schedule import *
from .get_variable import *
from .get_watcher import *
from .get_webhook import *
from .job_schedule import *
from .list_key_by_automation_account import *
from .module import *
from .runbook import *
from .schedule import *
from .variable import *
from .watcher import *
from .webhook import *
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
            if typ == "azure-native:automation/v20151031:AutomationAccount":
                return AutomationAccount(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Connection":
                return Connection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:ConnectionType":
                return ConnectionType(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Credential":
                return Credential(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:DscConfiguration":
                return DscConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:DscNodeConfiguration":
                return DscNodeConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:JobSchedule":
                return JobSchedule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Module":
                return Module(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Runbook":
                return Runbook(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Schedule":
                return Schedule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Variable":
                return Variable(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Watcher":
                return Watcher(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:automation/v20151031:Webhook":
                return Webhook(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "automation/v20151031", _module_instance)

_register_module()
