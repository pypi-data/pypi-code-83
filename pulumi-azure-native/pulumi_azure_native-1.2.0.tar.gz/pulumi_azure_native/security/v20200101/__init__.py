# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .adaptive_application_control import *
from .assessment import *
from .assessment_metadata_in_subscription import *
from .get_adaptive_application_control import *
from .get_assessment import *
from .get_assessment_metadata_in_subscription import *
from .get_jit_network_access_policy import *
from .get_server_vulnerability_assessment import *
from .jit_network_access_policy import *
from .server_vulnerability_assessment import *
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
            if typ == "azure-native:security/v20200101:AdaptiveApplicationControl":
                return AdaptiveApplicationControl(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:security/v20200101:Assessment":
                return Assessment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:security/v20200101:AssessmentMetadataInSubscription":
                return AssessmentMetadataInSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:security/v20200101:JitNetworkAccessPolicy":
                return JitNetworkAccessPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:security/v20200101:ServerVulnerabilityAssessment":
                return ServerVulnerabilityAssessment(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "security/v20200101", _module_instance)

_register_module()
