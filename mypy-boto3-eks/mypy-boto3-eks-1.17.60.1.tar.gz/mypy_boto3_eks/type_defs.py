"""
Main interface for eks service type definitions.

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
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityProviderConfigResponseTypeDef",
    "IdentityProviderConfigTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "OIDCTypeDef",
    "OidcIdentityProviderConfigTypeDef",
    "ProviderTypeDef",
    "RemoteAccessConfigTypeDef",
    "UpdateParamTypeDef",
    "UpdateTypeDef",
    "VpcConfigResponseTypeDef",
    "AssociateEncryptionConfigResponseTypeDef",
    "AssociateIdentityProviderConfigResponseTypeDef",
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
    "KubernetesNetworkConfigRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListIdentityProviderConfigsResponseTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesResponseTypeDef",
    "OidcIdentityProviderConfigRequestTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "VpcConfigRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef", {"issues": List["AddonIssueTypeDef"]}, total=False
)

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {"addonName": str, "type": str, "addonVersions": List["AddonVersionInfoTypeDef"]},
    total=False,
)

AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {"code": AddonIssueCode, "message": str, "resourceIds": List[str]},
    total=False,
)

AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": str,
        "clusterName": str,
        "status": AddonStatus,
        "addonVersion": str,
        "health": "AddonHealthTypeDef",
        "addonArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "serviceAccountRoleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": str,
        "architecture": List[str],
        "compatibilities": List["CompatibilityTypeDef"],
    },
    total=False,
)

AutoScalingGroupTypeDef = TypedDict("AutoScalingGroupTypeDef", {"name": str}, total=False)

CertificateTypeDef = TypedDict("CertificateTypeDef", {"data": str}, total=False)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigResponseTypeDef",
        "kubernetesNetworkConfig": "KubernetesNetworkConfigResponseTypeDef",
        "logging": "LoggingTypeDef",
        "identity": "IdentityTypeDef",
        "status": ClusterStatus,
        "certificateAuthority": "CertificateTypeDef",
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)

CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {"clusterVersion": str, "platformVersions": List[str], "defaultVersion": bool},
    total=False,
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef", {"resources": List[str], "provider": "ProviderTypeDef"}, total=False
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {"errorCode": ErrorCode, "errorMessage": str, "resourceIds": List[str]},
    total=False,
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef", {"namespace": str, "labels": Dict[str, str]}, total=False
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "status": FargateProfileStatus,
        "tags": Dict[str, str],
    },
    total=False,
)

IdentityProviderConfigResponseTypeDef = TypedDict(
    "IdentityProviderConfigResponseTypeDef",
    {"oidc": "OidcIdentityProviderConfigTypeDef"},
    total=False,
)

IdentityProviderConfigTypeDef = TypedDict(
    "IdentityProviderConfigTypeDef", {"type": str, "name": str}
)

IdentityTypeDef = TypedDict("IdentityTypeDef", {"oidc": "OIDCTypeDef"}, total=False)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {"code": NodegroupIssueCode, "message": str, "resourceIds": List[str]},
    total=False,
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef", {"serviceIpv4Cidr": str}, total=False
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef", {"name": str, "version": str, "id": str}, total=False
)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef", {"types": List[LogType], "enabled": bool}, total=False
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef", {"clusterLogging": List["LogSetupTypeDef"]}, total=False
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef", {"issues": List["IssueTypeDef"]}, total=False
)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {"autoScalingGroups": List["AutoScalingGroupTypeDef"], "remoteAccessSecurityGroup": str},
    total=False,
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": NodegroupStatus,
        "capacityType": CapacityTypes,
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "amiType": AMITypes,
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": "NodegroupResourcesTypeDef",
        "diskSize": int,
        "health": "NodegroupHealthTypeDef",
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

OIDCTypeDef = TypedDict("OIDCTypeDef", {"issuer": str}, total=False)

OidcIdentityProviderConfigTypeDef = TypedDict(
    "OidcIdentityProviderConfigTypeDef",
    {
        "identityProviderConfigName": str,
        "identityProviderConfigArn": str,
        "clusterName": str,
        "issuerUrl": str,
        "clientId": str,
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
        "tags": Dict[str, str],
        "status": configStatus,
    },
    total=False,
)

ProviderTypeDef = TypedDict("ProviderTypeDef", {"keyArn": str}, total=False)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef", {"ec2SshKey": str, "sourceSecurityGroups": List[str]}, total=False
)

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

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

AssociateEncryptionConfigResponseTypeDef = TypedDict(
    "AssociateEncryptionConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

AssociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "AssociateIdentityProviderConfigResponseTypeDef",
    {"update": "UpdateTypeDef", "tags": Dict[str, str]},
    total=False,
)

CreateAddonResponseTypeDef = TypedDict(
    "CreateAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef", {"fargateProfile": "FargateProfileTypeDef"}, total=False
)

CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DeleteAddonResponseTypeDef = TypedDict(
    "DeleteAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef", {"fargateProfile": "FargateProfileTypeDef"}, total=False
)

DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DescribeAddonResponseTypeDef = TypedDict(
    "DescribeAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

DescribeAddonVersionsResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseTypeDef",
    {"addons": List["AddonInfoTypeDef"], "nextToken": str},
    total=False,
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef",
    {"fargateProfile": "FargateProfileTypeDef"},
    total=False,
)

DescribeIdentityProviderConfigResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigResponseTypeDef",
    {"identityProviderConfig": "IdentityProviderConfigResponseTypeDef"},
    total=False,
)

DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

DisassociateIdentityProviderConfigResponseTypeDef = TypedDict(
    "DisassociateIdentityProviderConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef", {"serviceIpv4Cidr": str}, total=False
)

ListAddonsResponseTypeDef = TypedDict(
    "ListAddonsResponseTypeDef", {"addons": List[str], "nextToken": str}, total=False
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)

ListIdentityProviderConfigsResponseTypeDef = TypedDict(
    "ListIdentityProviderConfigsResponseTypeDef",
    {"identityProviderConfigs": List["IdentityProviderConfigTypeDef"], "nextToken": str},
    total=False,
)

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)

_RequiredOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_RequiredOidcIdentityProviderConfigRequestTypeDef",
    {"identityProviderConfigName": str, "issuerUrl": str, "clientId": str},
)
_OptionalOidcIdentityProviderConfigRequestTypeDef = TypedDict(
    "_OptionalOidcIdentityProviderConfigRequestTypeDef",
    {
        "usernameClaim": str,
        "usernamePrefix": str,
        "groupsClaim": str,
        "groupsPrefix": str,
        "requiredClaims": Dict[str, str],
    },
    total=False,
)


class OidcIdentityProviderConfigRequestTypeDef(
    _RequiredOidcIdentityProviderConfigRequestTypeDef,
    _OptionalOidcIdentityProviderConfigRequestTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateAddonResponseTypeDef = TypedDict(
    "UpdateAddonResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)

UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
