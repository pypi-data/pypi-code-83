"""
Main interface for organizations service type definitions.

Usage::

    ```python
    from mypy_boto3_organizations.type_defs import AccountTypeDef

    data: AccountTypeDef = {...}
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
    "AccountTypeDef",
    "ChildTypeDef",
    "CreateAccountStatusTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "EffectivePolicyTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeTypeDef",
    "OrganizationTypeDef",
    "OrganizationalUnitTypeDef",
    "ParentTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTargetSummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RootTypeDef",
    "TagTypeDef",
    "AcceptHandshakeResponseTypeDef",
    "CancelHandshakeResponseTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateGovCloudAccountResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateOrganizationalUnitResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "DeclineHandshakeResponseTypeDef",
    "DescribeAccountResponseTypeDef",
    "DescribeCreateAccountStatusResponseTypeDef",
    "DescribeEffectivePolicyResponseTypeDef",
    "DescribeHandshakeResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeOrganizationalUnitResponseTypeDef",
    "DescribePolicyResponseTypeDef",
    "HandshakeResourceTypeDef",
    "DisablePolicyTypeResponseTypeDef",
    "EnableAllFeaturesResponseTypeDef",
    "EnablePolicyTypeResponseTypeDef",
    "HandshakeFilterTypeDef",
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
    "PaginatorConfigTypeDef",
    "UpdateOrganizationalUnitResponseTypeDef",
    "UpdatePolicyResponseTypeDef",
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": AccountStatus,
        "JoinedMethod": AccountJoinedMethod,
        "JoinedTimestamp": datetime,
    },
    total=False,
)

ChildTypeDef = TypedDict("ChildTypeDef", {"Id": str, "Type": ChildType}, total=False)

CreateAccountStatusTypeDef = TypedDict(
    "CreateAccountStatusTypeDef",
    {
        "Id": str,
        "AccountName": str,
        "State": CreateAccountState,
        "RequestedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "AccountId": str,
        "GovCloudAccountId": str,
        "FailureReason": CreateAccountFailureReason,
    },
    total=False,
)

DelegatedAdministratorTypeDef = TypedDict(
    "DelegatedAdministratorTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Email": str,
        "Name": str,
        "Status": AccountStatus,
        "JoinedMethod": AccountJoinedMethod,
        "JoinedTimestamp": datetime,
        "DelegationEnabledDate": datetime,
    },
    total=False,
)

DelegatedServiceTypeDef = TypedDict(
    "DelegatedServiceTypeDef",
    {"ServicePrincipal": str, "DelegationEnabledDate": datetime},
    total=False,
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "PolicyContent": str,
        "LastUpdatedTimestamp": datetime,
        "TargetId": str,
        "PolicyType": EffectivePolicyType,
    },
    total=False,
)

EnabledServicePrincipalTypeDef = TypedDict(
    "EnabledServicePrincipalTypeDef",
    {"ServicePrincipal": str, "DateEnabled": datetime},
    total=False,
)

HandshakePartyTypeDef = TypedDict("HandshakePartyTypeDef", {"Id": str, "Type": HandshakePartyType})

HandshakeTypeDef = TypedDict(
    "HandshakeTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Parties": List["HandshakePartyTypeDef"],
        "State": HandshakeState,
        "RequestedTimestamp": datetime,
        "ExpirationTimestamp": datetime,
        "Action": ActionType,
        "Resources": List[Dict[str, Any]],
    },
    total=False,
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Id": str,
        "Arn": str,
        "FeatureSet": OrganizationFeatureSet,
        "MasterAccountArn": str,
        "MasterAccountId": str,
        "MasterAccountEmail": str,
        "AvailablePolicyTypes": List["PolicyTypeSummaryTypeDef"],
    },
    total=False,
)

OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

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

PolicyTypeDef = TypedDict(
    "PolicyTypeDef", {"PolicySummary": "PolicySummaryTypeDef", "Content": str}, total=False
)

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef", {"Type": PolicyType, "Status": PolicyTypeStatus}, total=False
)

RootTypeDef = TypedDict(
    "RootTypeDef",
    {"Id": str, "Arn": str, "Name": str, "PolicyTypes": List["PolicyTypeSummaryTypeDef"]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

AcceptHandshakeResponseTypeDef = TypedDict(
    "AcceptHandshakeResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

CancelHandshakeResponseTypeDef = TypedDict(
    "CancelHandshakeResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {"CreateAccountStatus": "CreateAccountStatusTypeDef"},
    total=False,
)

CreateGovCloudAccountResponseTypeDef = TypedDict(
    "CreateGovCloudAccountResponseTypeDef",
    {"CreateAccountStatus": "CreateAccountStatusTypeDef"},
    total=False,
)

CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef", {"Organization": "OrganizationTypeDef"}, total=False
)

CreateOrganizationalUnitResponseTypeDef = TypedDict(
    "CreateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": "OrganizationalUnitTypeDef"},
    total=False,
)

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef", {"Policy": "PolicyTypeDef"}, total=False
)

DeclineHandshakeResponseTypeDef = TypedDict(
    "DeclineHandshakeResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

DescribeAccountResponseTypeDef = TypedDict(
    "DescribeAccountResponseTypeDef", {"Account": "AccountTypeDef"}, total=False
)

DescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "DescribeCreateAccountStatusResponseTypeDef",
    {"CreateAccountStatus": "CreateAccountStatusTypeDef"},
    total=False,
)

DescribeEffectivePolicyResponseTypeDef = TypedDict(
    "DescribeEffectivePolicyResponseTypeDef",
    {"EffectivePolicy": "EffectivePolicyTypeDef"},
    total=False,
)

DescribeHandshakeResponseTypeDef = TypedDict(
    "DescribeHandshakeResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef", {"Organization": "OrganizationTypeDef"}, total=False
)

DescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "DescribeOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": "OrganizationalUnitTypeDef"},
    total=False,
)

DescribePolicyResponseTypeDef = TypedDict(
    "DescribePolicyResponseTypeDef", {"Policy": "PolicyTypeDef"}, total=False
)

HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {"Value": str, "Type": HandshakeResourceType, "Resources": List[Dict[str, Any]]},
    total=False,
)

DisablePolicyTypeResponseTypeDef = TypedDict(
    "DisablePolicyTypeResponseTypeDef", {"Root": "RootTypeDef"}, total=False
)

EnableAllFeaturesResponseTypeDef = TypedDict(
    "EnableAllFeaturesResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

EnablePolicyTypeResponseTypeDef = TypedDict(
    "EnablePolicyTypeResponseTypeDef", {"Root": "RootTypeDef"}, total=False
)

HandshakeFilterTypeDef = TypedDict(
    "HandshakeFilterTypeDef", {"ActionType": ActionType, "ParentHandshakeId": str}, total=False
)

InviteAccountToOrganizationResponseTypeDef = TypedDict(
    "InviteAccountToOrganizationResponseTypeDef", {"Handshake": "HandshakeTypeDef"}, total=False
)

ListAWSServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    {"EnabledServicePrincipals": List["EnabledServicePrincipalTypeDef"], "NextToken": str},
    total=False,
)

ListAccountsForParentResponseTypeDef = TypedDict(
    "ListAccountsForParentResponseTypeDef",
    {"Accounts": List["AccountTypeDef"], "NextToken": str},
    total=False,
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {"Accounts": List["AccountTypeDef"], "NextToken": str},
    total=False,
)

ListChildrenResponseTypeDef = TypedDict(
    "ListChildrenResponseTypeDef", {"Children": List["ChildTypeDef"], "NextToken": str}, total=False
)

ListCreateAccountStatusResponseTypeDef = TypedDict(
    "ListCreateAccountStatusResponseTypeDef",
    {"CreateAccountStatuses": List["CreateAccountStatusTypeDef"], "NextToken": str},
    total=False,
)

ListDelegatedAdministratorsResponseTypeDef = TypedDict(
    "ListDelegatedAdministratorsResponseTypeDef",
    {"DelegatedAdministrators": List["DelegatedAdministratorTypeDef"], "NextToken": str},
    total=False,
)

ListDelegatedServicesForAccountResponseTypeDef = TypedDict(
    "ListDelegatedServicesForAccountResponseTypeDef",
    {"DelegatedServices": List["DelegatedServiceTypeDef"], "NextToken": str},
    total=False,
)

ListHandshakesForAccountResponseTypeDef = TypedDict(
    "ListHandshakesForAccountResponseTypeDef",
    {"Handshakes": List["HandshakeTypeDef"], "NextToken": str},
    total=False,
)

ListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponseTypeDef",
    {"Handshakes": List["HandshakeTypeDef"], "NextToken": str},
    total=False,
)

ListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentResponseTypeDef",
    {"OrganizationalUnits": List["OrganizationalUnitTypeDef"], "NextToken": str},
    total=False,
)

ListParentsResponseTypeDef = TypedDict(
    "ListParentsResponseTypeDef", {"Parents": List["ParentTypeDef"], "NextToken": str}, total=False
)

ListPoliciesForTargetResponseTypeDef = TypedDict(
    "ListPoliciesForTargetResponseTypeDef",
    {"Policies": List["PolicySummaryTypeDef"], "NextToken": str},
    total=False,
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {"Policies": List["PolicySummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRootsResponseTypeDef = TypedDict(
    "ListRootsResponseTypeDef", {"Roots": List["RootTypeDef"], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {"Targets": List["PolicyTargetSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "UpdateOrganizationalUnitResponseTypeDef",
    {"OrganizationalUnit": "OrganizationalUnitTypeDef"},
    total=False,
)

UpdatePolicyResponseTypeDef = TypedDict(
    "UpdatePolicyResponseTypeDef", {"Policy": "PolicyTypeDef"}, total=False
)
