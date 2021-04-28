# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .autoscaling_policy import *
from .cluster import *
from .cluster_iam_binding import *
from .cluster_iam_member import *
from .cluster_iam_policy import *
from .job import *
from .job_iam_binding import *
from .job_iam_member import *
from .job_iam_policy import *
from .metastore_service import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp:dataproc/autoscalingPolicy:AutoscalingPolicy":
                return AutoscalingPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/cluster:Cluster":
                return Cluster(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/clusterIAMBinding:ClusterIAMBinding":
                return ClusterIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/clusterIAMMember:ClusterIAMMember":
                return ClusterIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/clusterIAMPolicy:ClusterIAMPolicy":
                return ClusterIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/job:Job":
                return Job(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/jobIAMBinding:JobIAMBinding":
                return JobIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/jobIAMMember:JobIAMMember":
                return JobIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/jobIAMPolicy:JobIAMPolicy":
                return JobIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:dataproc/metastoreService:MetastoreService":
                return MetastoreService(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "dataproc/autoscalingPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/cluster", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/clusterIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/clusterIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/clusterIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/job", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/jobIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/jobIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/jobIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "dataproc/metastoreService", _module_instance)

_register_module()
