"""
Type annotations for eks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AddonHealthTypeDef

    data: AddonHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_eks.literals import (
    AddonIssueCode,
    AddonStatus,
    AMITypes,
    CapacityTypes,
    ClusterStatus,
    ErrorCode,
    FargateProfileStatus,
    LogType,
    NodegroupIssueCode,
    NodegroupStatus,
    UpdateParamType,
    UpdateStatus,
    UpdateType,
    configStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupResponseTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeIdentityProviderConfigResponseTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribeUpdateResponseTypeDef",
    "DisassociateIdentityProviderConfigResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesResponseTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderTypeDef",
    "RemoteAccessConfigTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "UpdateParamTypeDef",
    "UpdateTypeDef",
    "VpcConfigRequestTypeDef",
    "VpcConfigResponseTypeDef",
    "WaiterConfigTypeDef",
)


class AddonHealthTypeDef(TypedDict, total=False):
    issues: List["AddonIssueTypeDef"]


AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {"addonName": str, "type": str, "addonVersions": List["AddonVersionInfoTypeDef"]},
    total=False,
)


class AddonIssueTypeDef(TypedDict, total=False):
    code: AddonIssueCode
    message: str
    resourceIds: List[str]


class AddonTypeDef(TypedDict, total=False):
    addonName: str
    clusterName: str
    status: AddonStatus
    addonVersion: str
    health: "AddonHealthTypeDef"
    addonArn: str
    createdAt: datetime
    modifiedAt: datetime
    serviceAccountRoleArn: str
    tags: Dict[str, str]


class AddonVersionInfoTypeDef(TypedDict, total=False):
    addonVersion: str
    architecture: List[str]
    compatibilities: List["CompatibilityTypeDef"]


class AssociateEncryptionConfigResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class AssociateIdentityProviderConfigResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"
    tags: Dict[str, str]


class AutoScalingGroupTypeDef(TypedDict, total=False):
    name: str


class CertificateTypeDef(TypedDict, total=False):
    data: str


class ClusterTypeDef(TypedDict, total=False):
    name: str
    arn: str
    createdAt: datetime
    version: str
    endpoint: str
    roleArn: str
    resourcesVpcConfig: "VpcConfigResponseTypeDef"
    kubernetesNetworkConfig: "KubernetesNetworkConfigResponseTypeDef"
    logging: "LoggingTypeDef"
    identity: "IdentityTypeDef"
    status: ClusterStatus
    certificateAuthority: "CertificateTypeDef"
    clientRequestToken: str
    platformVersion: str
    tags: Dict[str, str]
    encryptionConfig: List["EncryptionConfigTypeDef"]


class CompatibilityTypeDef(TypedDict, total=False):
    clusterVersion: str
    platformVersions: List[str]
    defaultVersion: bool


class CreateAddonResponseTypeDef(TypedDict, total=False):
    addon: "AddonTypeDef"


class CreateClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class CreateFargateProfileResponseTypeDef(TypedDict, total=False):
    fargateProfile: "FargateProfileTypeDef"


class CreateNodegroupResponseTypeDef(TypedDict, total=False):
    nodegroup: "NodegroupTypeDef"


class DeleteAddonResponseTypeDef(TypedDict, total=False):
    addon: "AddonTypeDef"


class DeleteClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class DeleteFargateProfileResponseTypeDef(TypedDict, total=False):
    fargateProfile: "FargateProfileTypeDef"


class DeleteNodegroupResponseTypeDef(TypedDict, total=False):
    nodegroup: "NodegroupTypeDef"


class DescribeAddonResponseTypeDef(TypedDict, total=False):
    addon: "AddonTypeDef"


class DescribeAddonVersionsResponseTypeDef(TypedDict, total=False):
    addons: List["AddonInfoTypeDef"]
    nextToken: str


class DescribeClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class DescribeFargateProfileResponseTypeDef(TypedDict, total=False):
    fargateProfile: "FargateProfileTypeDef"


class DescribeIdentityProviderConfigResponseTypeDef(TypedDict, total=False):
    identityProviderConfig: "IdentityProviderConfigResponseTypeDef"


class DescribeNodegroupResponseTypeDef(TypedDict, total=False):
    nodegroup: "NodegroupTypeDef"


class DescribeUpdateResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class DisassociateIdentityProviderConfigResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class EncryptionConfigTypeDef(TypedDict, total=False):
    resources: List[str]
    provider: "ProviderTypeDef"


class ErrorDetailTypeDef(TypedDict, total=False):
    errorCode: ErrorCode
    errorMessage: str
    resourceIds: List[str]


class FargateProfileSelectorTypeDef(TypedDict, total=False):
    namespace: str
    labels: Dict[str, str]


class FargateProfileTypeDef(TypedDict, total=False):
    fargateProfileName: str
    fargateProfileArn: str
    clusterName: str
    createdAt: datetime
    podExecutionRoleArn: str
    subnets: List[str]
    selectors: List["FargateProfileSelectorTypeDef"]
    status: FargateProfileStatus
    tags: Dict[str, str]


class IdentityProviderConfigResponseTypeDef(TypedDict, total=False):
    oidc: "OidcIdentityProviderConfigTypeDef"


IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef", {"type": str, "name": str}
)


class IdentityTypeDef(TypedDict, total=False):
    oidc: "OIDCTypeDef"


class IssueTypeDef(TypedDict, total=False):
    code: NodegroupIssueCode
    message: str
    resourceIds: List[str]


class KubernetesNetworkConfigRequestTypeDef(TypedDict, total=False):
    serviceIpv4Cidr: str


class KubernetesNetworkConfigResponseTypeDef(TypedDict, total=False):
    serviceIpv4Cidr: str


LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef", {"name": str, "version": str, "id": str}, total=False
)


class ListAddonsResponseTypeDef(TypedDict, total=False):
    addons: List[str]
    nextToken: str


class ListClustersResponseTypeDef(TypedDict, total=False):
    clusters: List[str]
    nextToken: str


class ListFargateProfilesResponseTypeDef(TypedDict, total=False):
    fargateProfileNames: List[str]
    nextToken: str


class ListIdentityProviderConfigsResponseTypeDef(TypedDict, total=False):
    identityProviderConfigs: List["IdentityProviderConfigTypeDef"]
    nextToken: str


class ListNodegroupsResponseTypeDef(TypedDict, total=False):
    nodegroups: List[str]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ListUpdatesResponseTypeDef(TypedDict, total=False):
    updateIds: List[str]
    nextToken: str


LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef", {"types": List[LogType], "enabled": bool}, total=False
)


class LoggingTypeDef(TypedDict, total=False):
    clusterLogging: List["LogSetupTypeDef"]


class NodegroupHealthTypeDef(TypedDict, total=False):
    issues: List["IssueTypeDef"]


class NodegroupResourcesTypeDef(TypedDict, total=False):
    autoScalingGroups: List["AutoScalingGroupTypeDef"]
    remoteAccessSecurityGroup: str


class NodegroupScalingConfigTypeDef(TypedDict, total=False):
    minSize: int
    maxSize: int
    desiredSize: int


class NodegroupTypeDef(TypedDict, total=False):
    nodegroupName: str
    nodegroupArn: str
    clusterName: str
    version: str
    releaseVersion: str
    createdAt: datetime
    modifiedAt: datetime
    status: NodegroupStatus
    capacityType: CapacityTypes
    scalingConfig: "NodegroupScalingConfigTypeDef"
    instanceTypes: List[str]
    subnets: List[str]
    remoteAccess: "RemoteAccessConfigTypeDef"
    amiType: AMITypes
    nodeRole: str
    labels: Dict[str, str]
    resources: "NodegroupResourcesTypeDef"
    diskSize: int
    health: "NodegroupHealthTypeDef"
    launchTemplate: "LaunchTemplateSpecificationTypeDef"
    tags: Dict[str, str]


class OIDCTypeDef(TypedDict, total=False):
    issuer: str


class _RequiredOidcIdentityProviderConfigRequestTypeDef(TypedDict):
    identityProviderConfigName: str
    issuerUrl: str
    clientId: str


class OidcIdentityProviderConfigRequestTypeDef(
    _RequiredOidcIdentityProviderConfigRequestTypeDef, total=False
):
    usernameClaim: str
    usernamePrefix: str
    groupsClaim: str
    groupsPrefix: str
    requiredClaims: Dict[str, str]


class OidcIdentityProviderConfigTypeDef(TypedDict, total=False):
    identityProviderConfigName: str
    identityProviderConfigArn: str
    clusterName: str
    issuerUrl: str
    clientId: str
    usernameClaim: str
    usernamePrefix: str
    groupsClaim: str
    groupsPrefix: str
    requiredClaims: Dict[str, str]
    tags: Dict[str, str]
    status: configStatus


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProviderTypeDef(TypedDict, total=False):
    keyArn: str


class RemoteAccessConfigTypeDef(TypedDict, total=False):
    ec2SshKey: str
    sourceSecurityGroups: List[str]


class UpdateAddonResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class UpdateClusterConfigResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class UpdateClusterVersionResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class UpdateLabelsPayloadTypeDef(TypedDict, total=False):
    addOrUpdateLabels: Dict[str, str]
    removeLabels: List[str]


class UpdateNodegroupConfigResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


class UpdateNodegroupVersionResponseTypeDef(TypedDict, total=False):
    update: "UpdateTypeDef"


UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef", {"type": UpdateParamType, "value": str}, total=False
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": str,
        "status": UpdateStatus,
        "type": UpdateType,
        "params": List["UpdateParamTypeDef"],
        "createdAt": datetime,
        "errors": List["ErrorDetailTypeDef"],
    },
    total=False,
)


class VpcConfigRequestTypeDef(TypedDict, total=False):
    subnetIds: List[str]
    securityGroupIds: List[str]
    endpointPublicAccess: bool
    endpointPrivateAccess: bool
    publicAccessCidrs: List[str]


class VpcConfigResponseTypeDef(TypedDict, total=False):
    subnetIds: List[str]
    securityGroupIds: List[str]
    clusterSecurityGroupId: str
    vpcId: str
    endpointPublicAccess: bool
    endpointPrivateAccess: bool
    publicAccessCidrs: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
