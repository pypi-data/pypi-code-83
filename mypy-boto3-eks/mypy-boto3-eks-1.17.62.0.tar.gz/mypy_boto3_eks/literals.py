"""
Main interface for eks service literal definitions.

Usage::

    ```python
    from mypy_boto3_eks.literals import AMITypes

    data: AMITypes = "AL2_ARM_64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AMITypes",
    "AddonActiveWaiterName",
    "AddonDeletedWaiterName",
    "AddonIssueCode",
    "AddonStatus",
    "CapacityTypes",
    "ClusterActiveWaiterName",
    "ClusterDeletedWaiterName",
    "ClusterStatus",
    "DescribeAddonVersionsPaginatorName",
    "ErrorCode",
    "FargateProfileStatus",
    "ListAddonsPaginatorName",
    "ListClustersPaginatorName",
    "ListFargateProfilesPaginatorName",
    "ListIdentityProviderConfigsPaginatorName",
    "ListNodegroupsPaginatorName",
    "ListUpdatesPaginatorName",
    "LogType",
    "NodegroupActiveWaiterName",
    "NodegroupDeletedWaiterName",
    "NodegroupIssueCode",
    "NodegroupStatus",
    "ResolveConflicts",
    "UpdateParamType",
    "UpdateStatus",
    "UpdateType",
    "configStatus",
)


AMITypes = Literal["AL2_ARM_64", "AL2_x86_64", "AL2_x86_64_GPU", "CUSTOM"]
AddonActiveWaiterName = Literal["addon_active"]
AddonDeletedWaiterName = Literal["addon_deleted"]
AddonIssueCode = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "InsufficientNumberOfReplicas",
    "InternalFailure",
]
AddonStatus = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DEGRADED", "DELETE_FAILED", "DELETING", "UPDATING"
]
CapacityTypes = Literal["ON_DEMAND", "SPOT"]
ClusterActiveWaiterName = Literal["cluster_active"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DescribeAddonVersionsPaginatorName = Literal["describe_addon_versions"]
ErrorCode = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "EniLimitReached",
    "InsufficientFreeAddresses",
    "InsufficientNumberOfReplicas",
    "IpNotAvailable",
    "NodeCreationFailure",
    "OperationNotPermitted",
    "PodEvictionFailure",
    "SecurityGroupNotFound",
    "SubnetNotFound",
    "Unknown",
    "VpcIdNotFound",
]
FargateProfileStatus = Literal["ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
ListAddonsPaginatorName = Literal["list_addons"]
ListClustersPaginatorName = Literal["list_clusters"]
ListFargateProfilesPaginatorName = Literal["list_fargate_profiles"]
ListIdentityProviderConfigsPaginatorName = Literal["list_identity_provider_configs"]
ListNodegroupsPaginatorName = Literal["list_nodegroups"]
ListUpdatesPaginatorName = Literal["list_updates"]
LogType = Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]
NodegroupActiveWaiterName = Literal["nodegroup_active"]
NodegroupDeletedWaiterName = Literal["nodegroup_deleted"]
NodegroupIssueCode = Literal[
    "AccessDenied",
    "AsgInstanceLaunchFailures",
    "AutoScalingGroupInvalidConfiguration",
    "AutoScalingGroupNotFound",
    "ClusterUnreachable",
    "Ec2LaunchTemplateNotFound",
    "Ec2LaunchTemplateVersionMismatch",
    "Ec2SecurityGroupDeletionFailure",
    "Ec2SecurityGroupNotFound",
    "Ec2SubnetInvalidConfiguration",
    "Ec2SubnetNotFound",
    "IamInstanceProfileNotFound",
    "IamLimitExceeded",
    "IamNodeRoleNotFound",
    "InstanceLimitExceeded",
    "InsufficientFreeAddresses",
    "InternalFailure",
    "NodeCreationFailure",
]
NodegroupStatus = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DEGRADED", "DELETE_FAILED", "DELETING", "UPDATING"
]
ResolveConflicts = Literal["NONE", "OVERWRITE"]
UpdateParamType = Literal[
    "AddonVersion",
    "ClusterLogging",
    "DesiredSize",
    "EncryptionConfig",
    "EndpointPrivateAccess",
    "EndpointPublicAccess",
    "IdentityProviderConfig",
    "LabelsToAdd",
    "LabelsToRemove",
    "LaunchTemplateName",
    "LaunchTemplateVersion",
    "MaxSize",
    "MinSize",
    "PlatformVersion",
    "PublicAccessCidrs",
    "ReleaseVersion",
    "ResolveConflicts",
    "ServiceAccountRoleArn",
    "Version",
]
UpdateStatus = Literal["Cancelled", "Failed", "InProgress", "Successful"]
UpdateType = Literal[
    "AddonUpdate",
    "AssociateEncryptionConfig",
    "AssociateIdentityProviderConfig",
    "ConfigUpdate",
    "DisassociateIdentityProviderConfig",
    "EndpointAccessUpdate",
    "LoggingUpdate",
    "VersionUpdate",
]
configStatus = Literal["ACTIVE", "CREATING", "DELETING"]
