"""
Type annotations for organizations service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/type_defs.html)

Usage::

    ```python
    from mypy_boto3_organizations.type_defs import AcceptHandshakeResponseTypeDef

    data: AcceptHandshakeResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_organizations.literals import (
    AccountJoinedMethod,
    AccountStatus,
    ActionType,
    ChildType,
    CreateAccountFailureReason,
    CreateAccountState,
    EffectivePolicyType,
    HandshakePartyType,
    HandshakeResourceType,
    HandshakeState,
    OrganizationFeatureSet,
    ParentType,
    PolicyType,
    PolicyTypeStatus,
    TargetType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptHandshakeResponseTypeDef",
    "AccountTypeDef",
    "CancelHandshakeResponseTypeDef",
    "ChildTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAccountStatusTypeDef",
    "CreateGovCloudAccountResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateOrganizationalUnitResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "DeclineHandshakeResponseTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "DescribeAccountResponseTypeDef",
    "DescribeCreateAccountStatusResponseTypeDef",
    "DescribeEffectivePolicyResponseTypeDef",
    "DescribeHandshakeResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeOrganizationalUnitResponseTypeDef",
    "DescribePolicyResponseTypeDef",
    "DisablePolicyTypeResponseTypeDef",
    "EffectivePolicyTypeDef",
    "EnableAllFeaturesResponseTypeDef",
    "EnablePolicyTypeResponseTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakeFilterTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourceTypeDef",
    "HandshakeTypeDef",
    "InviteAccountToOrganizationResponseTypeDef",
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    "ListAccountsForParentResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "ListChildrenResponseTypeDef",
    "ListCreateAccountStatusResponseTypeDef",
    "ListDelegatedAdministratorsResponseTypeDef",
    "ListDelegatedServicesForAccountResponseTypeDef",
    "ListHandshakesForAccountResponseTypeDef",
    "ListHandshakesForOrganizationResponseTypeDef",
    "ListOrganizationalUnitsForParentResponseTypeDef",
    "ListParentsResponseTypeDef",
    "ListPoliciesForTargetResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListRootsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "OrganizationTypeDef",
    "OrganizationalUnitTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTargetSummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RootTypeDef",
    "TagTypeDef",
    "UpdateOrganizationalUnitResponseTypeDef",
    "UpdatePolicyResponseTypeDef",
)


class AcceptHandshakeResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


class AccountTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Email: str
    Name: str
    Status: AccountStatus
    JoinedMethod: AccountJoinedMethod
    JoinedTimestamp: datetime


class CancelHandshakeResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


ChildTypeDef = TypedDict("ChildTypeDef", {"Id": str, "Type": ChildType}, total=False)


class CreateAccountResponseTypeDef(TypedDict, total=False):
    CreateAccountStatus: "CreateAccountStatusTypeDef"


class CreateAccountStatusTypeDef(TypedDict, total=False):
    Id: str
    AccountName: str
    State: CreateAccountState
    RequestedTimestamp: datetime
    CompletedTimestamp: datetime
    AccountId: str
    GovCloudAccountId: str
    FailureReason: CreateAccountFailureReason


class CreateGovCloudAccountResponseTypeDef(TypedDict, total=False):
    CreateAccountStatus: "CreateAccountStatusTypeDef"


class CreateOrganizationResponseTypeDef(TypedDict, total=False):
    Organization: "OrganizationTypeDef"


class CreateOrganizationalUnitResponseTypeDef(TypedDict, total=False):
    OrganizationalUnit: "OrganizationalUnitTypeDef"


class CreatePolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"


class DeclineHandshakeResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


class DelegatedAdministratorTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Email: str
    Name: str
    Status: AccountStatus
    JoinedMethod: AccountJoinedMethod
    JoinedTimestamp: datetime
    DelegationEnabledDate: datetime


class DelegatedServiceTypeDef(TypedDict, total=False):
    ServicePrincipal: str
    DelegationEnabledDate: datetime


class DescribeAccountResponseTypeDef(TypedDict, total=False):
    Account: "AccountTypeDef"


class DescribeCreateAccountStatusResponseTypeDef(TypedDict, total=False):
    CreateAccountStatus: "CreateAccountStatusTypeDef"


class DescribeEffectivePolicyResponseTypeDef(TypedDict, total=False):
    EffectivePolicy: "EffectivePolicyTypeDef"


class DescribeHandshakeResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


class DescribeOrganizationResponseTypeDef(TypedDict, total=False):
    Organization: "OrganizationTypeDef"


class DescribeOrganizationalUnitResponseTypeDef(TypedDict, total=False):
    OrganizationalUnit: "OrganizationalUnitTypeDef"


class DescribePolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"


class DisablePolicyTypeResponseTypeDef(TypedDict, total=False):
    Root: "RootTypeDef"


class EffectivePolicyTypeDef(TypedDict, total=False):
    PolicyContent: str
    LastUpdatedTimestamp: datetime
    TargetId: str
    PolicyType: EffectivePolicyType


class EnableAllFeaturesResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


class EnablePolicyTypeResponseTypeDef(TypedDict, total=False):
    Root: "RootTypeDef"


class EnabledServicePrincipalTypeDef(TypedDict, total=False):
    ServicePrincipal: str
    DateEnabled: datetime


class HandshakeFilterTypeDef(TypedDict, total=False):
    ActionType: ActionType
    ParentHandshakeId: str


HandshakePartyTypeDef = TypedDict("HandshakePartyTypeDef", {"Id": str, "Type": HandshakePartyType})

HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {"Value": str, "Type": HandshakeResourceType, "Resources": List[Dict[str, Any]]},
    total=False,
)


class HandshakeTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Parties: List["HandshakePartyTypeDef"]
    State: HandshakeState
    RequestedTimestamp: datetime
    ExpirationTimestamp: datetime
    Action: ActionType
    Resources: List["HandshakeResourceTypeDef"]


class InviteAccountToOrganizationResponseTypeDef(TypedDict, total=False):
    Handshake: "HandshakeTypeDef"


class ListAWSServiceAccessForOrganizationResponseTypeDef(TypedDict, total=False):
    EnabledServicePrincipals: List["EnabledServicePrincipalTypeDef"]
    NextToken: str


class ListAccountsForParentResponseTypeDef(TypedDict, total=False):
    Accounts: List["AccountTypeDef"]
    NextToken: str


class ListAccountsResponseTypeDef(TypedDict, total=False):
    Accounts: List["AccountTypeDef"]
    NextToken: str


class ListChildrenResponseTypeDef(TypedDict, total=False):
    Children: List["ChildTypeDef"]
    NextToken: str


class ListCreateAccountStatusResponseTypeDef(TypedDict, total=False):
    CreateAccountStatuses: List["CreateAccountStatusTypeDef"]
    NextToken: str


class ListDelegatedAdministratorsResponseTypeDef(TypedDict, total=False):
    DelegatedAdministrators: List["DelegatedAdministratorTypeDef"]
    NextToken: str


class ListDelegatedServicesForAccountResponseTypeDef(TypedDict, total=False):
    DelegatedServices: List["DelegatedServiceTypeDef"]
    NextToken: str


class ListHandshakesForAccountResponseTypeDef(TypedDict, total=False):
    Handshakes: List["HandshakeTypeDef"]
    NextToken: str


class ListHandshakesForOrganizationResponseTypeDef(TypedDict, total=False):
    Handshakes: List["HandshakeTypeDef"]
    NextToken: str


class ListOrganizationalUnitsForParentResponseTypeDef(TypedDict, total=False):
    OrganizationalUnits: List["OrganizationalUnitTypeDef"]
    NextToken: str


class ListParentsResponseTypeDef(TypedDict, total=False):
    Parents: List["ParentTypeDef"]
    NextToken: str


class ListPoliciesForTargetResponseTypeDef(TypedDict, total=False):
    Policies: List["PolicySummaryTypeDef"]
    NextToken: str


class ListPoliciesResponseTypeDef(TypedDict, total=False):
    Policies: List["PolicySummaryTypeDef"]
    NextToken: str


class ListRootsResponseTypeDef(TypedDict, total=False):
    Roots: List["RootTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class ListTargetsForPolicyResponseTypeDef(TypedDict, total=False):
    Targets: List["PolicyTargetSummaryTypeDef"]
    NextToken: str


class OrganizationTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    FeatureSet: OrganizationFeatureSet
    MasterAccountArn: str
    MasterAccountId: str
    MasterAccountEmail: str
    AvailablePolicyTypes: List["PolicyTypeSummaryTypeDef"]


class OrganizationalUnitTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


ParentTypeDef = TypedDict("ParentTypeDef", {"Id": str, "Type": ParentType}, total=False)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Type": PolicyType,
        "AwsManaged": bool,
    },
    total=False,
)

PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {"TargetId": str, "Arn": str, "Name": str, "Type": TargetType},
    total=False,
)


class PolicyTypeDef(TypedDict, total=False):
    PolicySummary: "PolicySummaryTypeDef"
    Content: str


PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef", {"Type": PolicyType, "Status": PolicyTypeStatus}, total=False
)


class RootTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    PolicyTypes: List["PolicyTypeSummaryTypeDef"]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateOrganizationalUnitResponseTypeDef(TypedDict, total=False):
    OrganizationalUnit: "OrganizationalUnitTypeDef"


class UpdatePolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"
