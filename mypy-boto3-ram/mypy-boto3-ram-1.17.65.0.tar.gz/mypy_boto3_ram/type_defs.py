"""
Type annotations for ram service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationResponseTypeDef

    data: AcceptResourceShareInvitationResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_ram.literals import (
    ResourceShareAssociationStatus,
    ResourceShareAssociationType,
    ResourceShareFeatureSet,
    ResourceShareInvitationStatus,
    ResourceShareStatus,
    ResourceStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptResourceShareInvitationResponseTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "CreateResourceShareResponseTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetPermissionResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "GetResourceSharesResponseTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "ListResourceTypesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrincipalTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "ResourceShareAssociationTypeDef",
    "ResourceShareInvitationTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "ResourceTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "UpdateResourceShareResponseTypeDef",
)


class AcceptResourceShareInvitationResponseTypeDef(TypedDict, total=False):
    resourceShareInvitation: "ResourceShareInvitationTypeDef"
    clientToken: str


class AssociateResourceSharePermissionResponseTypeDef(TypedDict, total=False):
    returnValue: bool
    clientToken: str


class AssociateResourceShareResponseTypeDef(TypedDict, total=False):
    resourceShareAssociations: List["ResourceShareAssociationTypeDef"]
    clientToken: str


class CreateResourceShareResponseTypeDef(TypedDict, total=False):
    resourceShare: "ResourceShareTypeDef"
    clientToken: str


class DeleteResourceShareResponseTypeDef(TypedDict, total=False):
    returnValue: bool
    clientToken: str


class DisassociateResourceSharePermissionResponseTypeDef(TypedDict, total=False):
    returnValue: bool
    clientToken: str


class DisassociateResourceShareResponseTypeDef(TypedDict, total=False):
    resourceShareAssociations: List["ResourceShareAssociationTypeDef"]
    clientToken: str


class EnableSharingWithAwsOrganizationResponseTypeDef(TypedDict, total=False):
    returnValue: bool


class GetPermissionResponseTypeDef(TypedDict, total=False):
    permission: "ResourceSharePermissionDetailTypeDef"


class GetResourcePoliciesResponseTypeDef(TypedDict, total=False):
    policies: List[str]
    nextToken: str


class GetResourceShareAssociationsResponseTypeDef(TypedDict, total=False):
    resourceShareAssociations: List["ResourceShareAssociationTypeDef"]
    nextToken: str


class GetResourceShareInvitationsResponseTypeDef(TypedDict, total=False):
    resourceShareInvitations: List["ResourceShareInvitationTypeDef"]
    nextToken: str


class GetResourceSharesResponseTypeDef(TypedDict, total=False):
    resourceShares: List["ResourceShareTypeDef"]
    nextToken: str


class ListPendingInvitationResourcesResponseTypeDef(TypedDict, total=False):
    resources: List["ResourceTypeDef"]
    nextToken: str


class ListPermissionsResponseTypeDef(TypedDict, total=False):
    permissions: List["ResourceSharePermissionSummaryTypeDef"]
    nextToken: str


class ListPrincipalsResponseTypeDef(TypedDict, total=False):
    principals: List["PrincipalTypeDef"]
    nextToken: str


class ListResourceSharePermissionsResponseTypeDef(TypedDict, total=False):
    permissions: List["ResourceSharePermissionSummaryTypeDef"]
    nextToken: str


class ListResourceTypesResponseTypeDef(TypedDict, total=False):
    resourceTypes: List["ServiceNameAndResourceTypeTypeDef"]
    nextToken: str


class ListResourcesResponseTypeDef(TypedDict, total=False):
    resources: List["ResourceTypeDef"]
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": str,
        "resourceShareArn": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
        "external": bool,
    },
    total=False,
)


class PromoteResourceShareCreatedFromPolicyResponseTypeDef(TypedDict, total=False):
    returnValue: bool


class RejectResourceShareInvitationResponseTypeDef(TypedDict, total=False):
    resourceShareInvitation: "ResourceShareInvitationTypeDef"
    clientToken: str


class ResourceShareAssociationTypeDef(TypedDict, total=False):
    resourceShareArn: str
    resourceShareName: str
    associatedEntity: str
    associationType: ResourceShareAssociationType
    status: ResourceShareAssociationStatus
    statusMessage: str
    creationTime: datetime
    lastUpdatedTime: datetime
    external: bool


class ResourceShareInvitationTypeDef(TypedDict, total=False):
    resourceShareInvitationArn: str
    resourceShareName: str
    resourceShareArn: str
    senderAccountId: str
    receiverAccountId: str
    invitationTimestamp: datetime
    status: ResourceShareInvitationStatus
    resourceShareAssociations: List["ResourceShareAssociationTypeDef"]


class ResourceSharePermissionDetailTypeDef(TypedDict, total=False):
    arn: str
    version: str
    defaultVersion: bool
    name: str
    resourceType: str
    permission: str
    creationTime: datetime
    lastUpdatedTime: datetime


class ResourceSharePermissionSummaryTypeDef(TypedDict, total=False):
    arn: str
    version: str
    defaultVersion: bool
    name: str
    resourceType: str
    status: str
    creationTime: datetime
    lastUpdatedTime: datetime


class ResourceShareTypeDef(TypedDict, total=False):
    resourceShareArn: str
    name: str
    owningAccountId: str
    allowExternalPrincipals: bool
    status: ResourceShareStatus
    statusMessage: str
    tags: List["TagTypeDef"]
    creationTime: datetime
    lastUpdatedTime: datetime
    featureSet: ResourceShareFeatureSet


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": str,
        "type": str,
        "resourceShareArn": str,
        "resourceGroupArn": str,
        "status": ResourceStatus,
        "statusMessage": str,
        "creationTime": datetime,
        "lastUpdatedTime": datetime,
    },
    total=False,
)


class ServiceNameAndResourceTypeTypeDef(TypedDict, total=False):
    resourceType: str
    serviceName: str


class TagFilterTypeDef(TypedDict, total=False):
    tagKey: str
    tagValues: List[str]


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


class UpdateResourceShareResponseTypeDef(TypedDict, total=False):
    resourceShare: "ResourceShareTypeDef"
    clientToken: str
