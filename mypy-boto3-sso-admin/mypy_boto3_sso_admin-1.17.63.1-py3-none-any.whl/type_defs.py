"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef

    data: AccessControlAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_sso_admin.literals import (
    InstanceAccessControlAttributeConfigurationStatus,
    PrincipalType,
    StatusValues,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlAttributeTypeDef",
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "AttachedManagedPolicyTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "InstanceMetadataTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListInstancesResponseTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "TagTypeDef",
)


class AccessControlAttributeTypeDef(TypedDict):
    Key: str
    Value: "AccessControlAttributeValueTypeDef"


class AccessControlAttributeValueTypeDef(TypedDict):
    Source: List[str]


class AccountAssignmentOperationStatusMetadataTypeDef(TypedDict, total=False):
    Status: StatusValues
    RequestId: str
    CreatedDate: datetime


class AccountAssignmentOperationStatusTypeDef(TypedDict, total=False):
    Status: StatusValues
    RequestId: str
    FailureReason: str
    TargetId: str
    TargetType: Literal["AWS_ACCOUNT"]
    PermissionSetArn: str
    PrincipalType: PrincipalType
    PrincipalId: str
    CreatedDate: datetime


class AccountAssignmentTypeDef(TypedDict, total=False):
    AccountId: str
    PermissionSetArn: str
    PrincipalType: PrincipalType
    PrincipalId: str


class AttachedManagedPolicyTypeDef(TypedDict, total=False):
    Name: str
    Arn: str


class CreateAccountAssignmentResponseTypeDef(TypedDict, total=False):
    AccountAssignmentCreationStatus: "AccountAssignmentOperationStatusTypeDef"


class CreatePermissionSetResponseTypeDef(TypedDict, total=False):
    PermissionSet: "PermissionSetTypeDef"


class DeleteAccountAssignmentResponseTypeDef(TypedDict, total=False):
    AccountAssignmentDeletionStatus: "AccountAssignmentOperationStatusTypeDef"


class DescribeAccountAssignmentCreationStatusResponseTypeDef(TypedDict, total=False):
    AccountAssignmentCreationStatus: "AccountAssignmentOperationStatusTypeDef"


class DescribeAccountAssignmentDeletionStatusResponseTypeDef(TypedDict, total=False):
    AccountAssignmentDeletionStatus: "AccountAssignmentOperationStatusTypeDef"


class DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef(TypedDict, total=False):
    Status: InstanceAccessControlAttributeConfigurationStatus
    StatusReason: str
    InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"


class DescribePermissionSetProvisioningStatusResponseTypeDef(TypedDict, total=False):
    PermissionSetProvisioningStatus: "PermissionSetProvisioningStatusTypeDef"


class DescribePermissionSetResponseTypeDef(TypedDict, total=False):
    PermissionSet: "PermissionSetTypeDef"


class GetInlinePolicyForPermissionSetResponseTypeDef(TypedDict, total=False):
    InlinePolicy: str


class InstanceAccessControlAttributeConfigurationTypeDef(TypedDict):
    AccessControlAttributes: List["AccessControlAttributeTypeDef"]


class InstanceMetadataTypeDef(TypedDict, total=False):
    InstanceArn: str
    IdentityStoreId: str


class ListAccountAssignmentCreationStatusResponseTypeDef(TypedDict, total=False):
    AccountAssignmentsCreationStatus: List["AccountAssignmentOperationStatusMetadataTypeDef"]
    NextToken: str


class ListAccountAssignmentDeletionStatusResponseTypeDef(TypedDict, total=False):
    AccountAssignmentsDeletionStatus: List["AccountAssignmentOperationStatusMetadataTypeDef"]
    NextToken: str


class ListAccountAssignmentsResponseTypeDef(TypedDict, total=False):
    AccountAssignments: List["AccountAssignmentTypeDef"]
    NextToken: str


class ListAccountsForProvisionedPermissionSetResponseTypeDef(TypedDict, total=False):
    AccountIds: List[str]
    NextToken: str


class ListInstancesResponseTypeDef(TypedDict, total=False):
    Instances: List["InstanceMetadataTypeDef"]
    NextToken: str


class ListManagedPoliciesInPermissionSetResponseTypeDef(TypedDict, total=False):
    AttachedManagedPolicies: List["AttachedManagedPolicyTypeDef"]
    NextToken: str


class ListPermissionSetProvisioningStatusResponseTypeDef(TypedDict, total=False):
    PermissionSetsProvisioningStatus: List["PermissionSetProvisioningStatusMetadataTypeDef"]
    NextToken: str


class ListPermissionSetsProvisionedToAccountResponseTypeDef(TypedDict, total=False):
    NextToken: str
    PermissionSets: List[str]


class ListPermissionSetsResponseTypeDef(TypedDict, total=False):
    PermissionSets: List[str]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class OperationStatusFilterTypeDef(TypedDict, total=False):
    Status: StatusValues


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionSetProvisioningStatusMetadataTypeDef(TypedDict, total=False):
    Status: StatusValues
    RequestId: str
    CreatedDate: datetime


class PermissionSetProvisioningStatusTypeDef(TypedDict, total=False):
    Status: StatusValues
    RequestId: str
    AccountId: str
    PermissionSetArn: str
    FailureReason: str
    CreatedDate: datetime


class PermissionSetTypeDef(TypedDict, total=False):
    Name: str
    PermissionSetArn: str
    Description: str
    CreatedDate: datetime
    SessionDuration: str
    RelayState: str


class ProvisionPermissionSetResponseTypeDef(TypedDict, total=False):
    PermissionSetProvisioningStatus: "PermissionSetProvisioningStatusTypeDef"


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str
