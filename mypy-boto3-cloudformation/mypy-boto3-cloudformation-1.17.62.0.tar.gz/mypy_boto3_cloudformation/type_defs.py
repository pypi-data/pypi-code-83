"""
Main interface for cloudformation service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_cloudformation.literals import (
    AccountGateStatus,
    Capability,
    ChangeAction,
    ChangeSetStatus,
    ChangeSource,
    ChangeType,
    DeprecatedStatus,
    DifferenceType,
    EvaluationType,
    ExecutionStatus,
    PermissionModels,
    ProvisioningType,
    RegionConcurrencyType,
    RegistrationStatus,
    RegistryType,
    Replacement,
    RequiresRecreation,
    ResourceAttribute,
    ResourceStatus,
    StackDriftDetectionStatus,
    StackDriftStatus,
    StackInstanceDetailedStatus,
    StackInstanceFilterName,
    StackInstanceStatus,
    StackResourceDriftStatus,
    StackSetDriftDetectionStatus,
    StackSetDriftStatus,
    StackSetOperationAction,
    StackSetOperationResultStatus,
    StackSetOperationStatus,
    StackSetStatus,
    StackStatus,
    TemplateStage,
    Visibility,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "AutoDeploymentTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "DeploymentTargetsTypeDef",
    "ExportTypeDef",
    "LoggingConfigTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResponseMetadata",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTypeOutputTypeDef",
    "ResourceToImportTypeDef",
    "StackInstanceFilterTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef", {"Status": AccountGateStatus, "StatusReason": str}, total=False
)

AccountLimitTypeDef = TypedDict("AccountLimitTypeDef", {"Name": str, "Value": int}, total=False)

AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef", {"Enabled": bool, "RetainStacksOnAccountRemoval": bool}, total=False
)

ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": str,
        "StackName": str,
        "ChangeSetId": str,
        "ChangeSetName": str,
        "ExecutionStatus": ExecutionStatus,
        "Status": ChangeSetStatus,
        "StatusReason": str,
        "CreationTime": datetime,
        "Description": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
    },
    total=False,
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef", {"Type": ChangeType, "ResourceChange": "ResourceChangeTypeDef"}, total=False
)

DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {"Accounts": List[str], "AccountsUrl": str, "OrganizationalUnitIds": List[str]},
    total=False,
)

ExportTypeDef = TypedDict(
    "ExportTypeDef", {"ExportingStackId": str, "Name": str, "Value": str}, total=False
)

LoggingConfigTypeDef = TypedDict("LoggingConfigTypeDef", {"LogRoleArn": str, "LogGroupName": str})

ModuleInfoTypeDef = TypedDict(
    "ModuleInfoTypeDef", {"TypeHierarchy": str, "LogicalIdHierarchy": str}, total=False
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputKey": str,
        "OutputValue": str,
        "Description": str,
        "ExportName": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef", {"AllowedValues": List[str]}, total=False
)

ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": str,
        "DefaultValue": str,
        "ParameterType": str,
        "NoEcho": bool,
        "Description": str,
        "ParameterConstraints": "ParameterConstraintsTypeDef",
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {"ParameterKey": str, "ParameterValue": str, "UsePreviousValue": bool, "ResolvedValue": str},
    total=False,
)

PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef", {"Key": str, "Value": str}
)

PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": DifferenceType,
    },
)

ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": "ResourceTargetDefinitionTypeDef",
        "Evaluation": EvaluationType,
        "ChangeSource": ChangeSource,
        "CausingEntity": str,
    },
    total=False,
)

ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "Action": ChangeAction,
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "Replacement": Replacement,
        "Scope": List[ResourceAttribute],
        "Details": List["ResourceChangeDetailTypeDef"],
        "ChangeSetId": str,
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)

ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {"ResourceType": str, "LogicalResourceIds": List[str], "ResourceIdentifiers": List[str]},
    total=False,
)

ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {"Attribute": ResourceAttribute, "Name": str, "RequiresRecreation": RequiresRecreation},
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {"RollbackTriggers": List["RollbackTriggerTypeDef"], "MonitoringTimeInMinutes": int},
    total=False,
)

RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})

_RequiredStackDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackDriftInformationSummaryTypeDef", {"StackDriftStatus": StackDriftStatus}
)
_OptionalStackDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackDriftInformationSummaryTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, _OptionalStackDriftInformationSummaryTypeDef
):
    pass


_RequiredStackDriftInformationTypeDef = TypedDict(
    "_RequiredStackDriftInformationTypeDef", {"StackDriftStatus": StackDriftStatus}
)
_OptionalStackDriftInformationTypeDef = TypedDict(
    "_OptionalStackDriftInformationTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackDriftInformationTypeDef(
    _RequiredStackDriftInformationTypeDef, _OptionalStackDriftInformationTypeDef
):
    pass


_RequiredStackEventTypeDef = TypedDict(
    "_RequiredStackEventTypeDef",
    {"StackId": str, "EventId": str, "StackName": str, "Timestamp": datetime},
)
_OptionalStackEventTypeDef = TypedDict(
    "_OptionalStackEventTypeDef",
    {
        "LogicalResourceId": str,
        "PhysicalResourceId": str,
        "ResourceType": str,
        "ResourceStatus": ResourceStatus,
        "ResourceStatusReason": str,
        "ResourceProperties": str,
        "ClientRequestToken": str,
    },
    total=False,
)


class StackEventTypeDef(_RequiredStackEventTypeDef, _OptionalStackEventTypeDef):
    pass


StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {"DetailedStatus": StackInstanceDetailedStatus},
    total=False,
)

StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "Status": StackInstanceStatus,
        "StatusReason": str,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatus,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": str,
        "Region": str,
        "Account": str,
        "StackId": str,
        "ParameterOverrides": List["ParameterTypeDef"],
        "Status": StackInstanceStatus,
        "StackInstanceStatus": "StackInstanceComprehensiveStatusTypeDef",
        "StatusReason": str,
        "OrganizationalUnitId": str,
        "DriftStatus": StackDriftStatus,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

_RequiredStackResourceDetailTypeDef = TypedDict(
    "_RequiredStackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatus,
    },
)
_OptionalStackResourceDetailTypeDef = TypedDict(
    "_OptionalStackResourceDetailTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "Metadata": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceDetailTypeDef(
    _RequiredStackResourceDetailTypeDef, _OptionalStackResourceDetailTypeDef
):
    pass


_RequiredStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationSummaryTypeDef",
    {"StackResourceDriftStatus": StackResourceDriftStatus},
)
_OptionalStackResourceDriftInformationSummaryTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationSummaryTypeDef",
    {"LastCheckTimestamp": datetime},
    total=False,
)


class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef,
    _OptionalStackResourceDriftInformationSummaryTypeDef,
):
    pass


_RequiredStackResourceDriftInformationTypeDef = TypedDict(
    "_RequiredStackResourceDriftInformationTypeDef",
    {"StackResourceDriftStatus": StackResourceDriftStatus},
)
_OptionalStackResourceDriftInformationTypeDef = TypedDict(
    "_OptionalStackResourceDriftInformationTypeDef", {"LastCheckTimestamp": datetime}, total=False
)


class StackResourceDriftInformationTypeDef(
    _RequiredStackResourceDriftInformationTypeDef, _OptionalStackResourceDriftInformationTypeDef
):
    pass


_RequiredStackResourceDriftTypeDef = TypedDict(
    "_RequiredStackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatus,
        "Timestamp": datetime,
    },
)
_OptionalStackResourceDriftTypeDef = TypedDict(
    "_OptionalStackResourceDriftTypeDef",
    {
        "PhysicalResourceId": str,
        "PhysicalResourceIdContext": List["PhysicalResourceIdContextKeyValuePairTypeDef"],
        "ExpectedProperties": str,
        "ActualProperties": str,
        "PropertyDifferences": List["PropertyDifferenceTypeDef"],
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceDriftTypeDef(
    _RequiredStackResourceDriftTypeDef, _OptionalStackResourceDriftTypeDef
):
    pass


_RequiredStackResourceSummaryTypeDef = TypedDict(
    "_RequiredStackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatus,
    },
)
_OptionalStackResourceSummaryTypeDef = TypedDict(
    "_OptionalStackResourceSummaryTypeDef",
    {
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "DriftInformation": "StackResourceDriftInformationSummaryTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceSummaryTypeDef(
    _RequiredStackResourceSummaryTypeDef, _OptionalStackResourceSummaryTypeDef
):
    pass


_RequiredStackResourceTypeDef = TypedDict(
    "_RequiredStackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": ResourceStatus,
    },
)
_OptionalStackResourceTypeDef = TypedDict(
    "_OptionalStackResourceTypeDef",
    {
        "StackName": str,
        "StackId": str,
        "PhysicalResourceId": str,
        "ResourceStatusReason": str,
        "Description": str,
        "DriftInformation": "StackResourceDriftInformationTypeDef",
        "ModuleInfo": "ModuleInfoTypeDef",
    },
    total=False,
)


class StackResourceTypeDef(_RequiredStackResourceTypeDef, _OptionalStackResourceTypeDef):
    pass


StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": StackSetDriftStatus,
        "DriftDetectionStatus": StackSetDriftDetectionStatus,
        "LastDriftCheckTimestamp": datetime,
        "TotalStackInstancesCount": int,
        "DriftedStackInstancesCount": int,
        "InSyncStackInstancesCount": int,
        "InProgressStackInstancesCount": int,
        "FailedStackInstancesCount": int,
    },
    total=False,
)

StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionConcurrencyType": RegionConcurrencyType,
        "RegionOrder": List[str],
        "FailureToleranceCount": int,
        "FailureTolerancePercentage": int,
        "MaxConcurrentCount": int,
        "MaxConcurrentPercentage": int,
    },
    total=False,
)

StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": str,
        "Region": str,
        "Status": StackSetOperationResultStatus,
        "StatusReason": str,
        "AccountGateResult": "AccountGateResultTypeDef",
        "OrganizationalUnitId": str,
    },
    total=False,
)

StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": str,
        "Action": StackSetOperationAction,
        "Status": StackSetOperationStatus,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
    },
    total=False,
)

StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": str,
        "StackSetId": str,
        "Action": StackSetOperationAction,
        "Status": StackSetOperationStatus,
        "OperationPreferences": "StackSetOperationPreferencesTypeDef",
        "RetainStacks": bool,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "CreationTimestamp": datetime,
        "EndTimestamp": datetime,
        "DeploymentTargets": "DeploymentTargetsTypeDef",
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
    },
    total=False,
)

StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatus,
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModels,
        "DriftStatus": StackDriftStatus,
        "LastDriftCheckTimestamp": datetime,
    },
    total=False,
)

StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": str,
        "StackSetId": str,
        "Description": str,
        "Status": StackSetStatus,
        "TemplateBody": str,
        "Parameters": List["ParameterTypeDef"],
        "Capabilities": List[Capability],
        "Tags": List["TagTypeDef"],
        "StackSetARN": str,
        "AdministrationRoleARN": str,
        "ExecutionRoleName": str,
        "StackSetDriftDetectionDetails": "StackSetDriftDetectionDetailsTypeDef",
        "AutoDeployment": "AutoDeploymentTypeDef",
        "PermissionModel": PermissionModels,
        "OrganizationalUnitIds": List[str],
    },
    total=False,
)

_RequiredStackSummaryTypeDef = TypedDict(
    "_RequiredStackSummaryTypeDef",
    {"StackName": str, "CreationTime": datetime, "StackStatus": StackStatus},
)
_OptionalStackSummaryTypeDef = TypedDict(
    "_OptionalStackSummaryTypeDef",
    {
        "StackId": str,
        "TemplateDescription": str,
        "LastUpdatedTime": datetime,
        "DeletionTime": datetime,
        "StackStatusReason": str,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationSummaryTypeDef",
    },
    total=False,
)


class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, _OptionalStackSummaryTypeDef):
    pass


_RequiredStackTypeDef = TypedDict(
    "_RequiredStackTypeDef",
    {"StackName": str, "CreationTime": datetime, "StackStatus": StackStatus},
)
_OptionalStackTypeDef = TypedDict(
    "_OptionalStackTypeDef",
    {
        "StackId": str,
        "ChangeSetId": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "DeletionTime": datetime,
        "LastUpdatedTime": datetime,
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "StackStatusReason": str,
        "DisableRollback": bool,
        "NotificationARNs": List[str],
        "TimeoutInMinutes": int,
        "Capabilities": List[Capability],
        "Outputs": List["OutputTypeDef"],
        "RoleARN": str,
        "Tags": List["TagTypeDef"],
        "EnableTerminationProtection": bool,
        "ParentId": str,
        "RootId": str,
        "DriftInformation": "StackDriftInformationTypeDef",
    },
    total=False,
)


class StackTypeDef(_RequiredStackTypeDef, _OptionalStackTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {"ParameterKey": str, "DefaultValue": str, "NoEcho": bool, "Description": str},
    total=False,
)

TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": RegistryType,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": RegistryType,
        "TypeName": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)

CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef",
    {"Id": str, "StackId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef",
    {"OperationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateStackOutputTypeDef = TypedDict(
    "CreateStackOutputTypeDef",
    {"StackId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef",
    {"StackSetId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef",
    {"OperationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List["ParameterTypeDef"],
        "CreationTime": datetime,
        "ExecutionStatus": ExecutionStatus,
        "Status": ChangeSetStatus,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": "RollbackConfigurationTypeDef",
        "Capabilities": List[Capability],
        "Tags": List["TagTypeDef"],
        "Changes": List["ChangeTypeDef"],
        "NextToken": str,
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredDescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "_RequiredDescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "DetectionStatus": StackDriftDetectionStatus,
        "Timestamp": datetime,
    },
)
_OptionalDescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "_OptionalDescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackDriftStatus": StackDriftStatus,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class DescribeStackDriftDetectionStatusOutputTypeDef(
    _RequiredDescribeStackDriftDetectionStatusOutputTypeDef,
    _OptionalDescribeStackDriftDetectionStatusOutputTypeDef,
):
    pass


DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {
        "StackEvents": List["StackEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef",
    {"StackInstance": "StackInstanceTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

_RequiredDescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "_RequiredDescribeStackResourceDriftsOutputTypeDef",
    {"StackResourceDrifts": List["StackResourceDriftTypeDef"]},
)
_OptionalDescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "_OptionalDescribeStackResourceDriftsOutputTypeDef",
    {"NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeStackResourceDriftsOutputTypeDef(
    _RequiredDescribeStackResourceDriftsOutputTypeDef,
    _OptionalDescribeStackResourceDriftsOutputTypeDef,
):
    pass


DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {"StackResourceDetail": "StackResourceDetailTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {"StackResources": List["StackResourceTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {"StackSetOperation": "StackSetOperationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef",
    {"StackSet": "StackSetTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef",
    {"Stacks": List["StackTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": RegistryType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningType,
        "DeprecatedStatus": DeprecatedStatus,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "Visibility": Visibility,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": RegistrationStatus,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredDetectStackDriftOutputTypeDef = TypedDict(
    "_RequiredDetectStackDriftOutputTypeDef", {"StackDriftDetectionId": str}
)
_OptionalDetectStackDriftOutputTypeDef = TypedDict(
    "_OptionalDetectStackDriftOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DetectStackDriftOutputTypeDef(
    _RequiredDetectStackDriftOutputTypeDef, _OptionalDetectStackDriftOutputTypeDef
):
    pass


_RequiredDetectStackResourceDriftOutputTypeDef = TypedDict(
    "_RequiredDetectStackResourceDriftOutputTypeDef",
    {"StackResourceDrift": "StackResourceDriftTypeDef"},
)
_OptionalDetectStackResourceDriftOutputTypeDef = TypedDict(
    "_OptionalDetectStackResourceDriftOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DetectStackResourceDriftOutputTypeDef(
    _RequiredDetectStackResourceDriftOutputTypeDef, _OptionalDetectStackResourceDriftOutputTypeDef
):
    pass


DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef",
    {"OperationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef",
    {"Url": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef",
    {"StackPolicyBody": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {
        "TemplateBody": str,
        "StagesAvailable": List[TemplateStage],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
    {
        "Parameters": List["ParameterDeclarationTypeDef"],
        "Description": str,
        "Capabilities": List[Capability],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List["ResourceIdentifierSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {
        "Summaries": List["ChangeSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {"Exports": List["ExportTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {"Imports": List[str], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {
        "Summaries": List["StackInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {
        "StackResourceSummaries": List["StackResourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationResultSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {
        "Summaries": List["StackSetOperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {
        "Summaries": List["StackSetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {
        "StackSummaries": List["StackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {"RegistrationTokenList": List[str], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {
        "TypeVersionSummaries": List["TypeVersionSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
    {
        "TypeSummaries": List["TypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef",
    {"RegistrationToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {"ResourceType": str, "LogicalResourceId": str, "ResourceIdentifier": Dict[str, str]},
)

StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef", {"Name": StackInstanceFilterName, "Values": str}, total=False
)

UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef",
    {"OperationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateStackOutputTypeDef = TypedDict(
    "UpdateStackOutputTypeDef",
    {"StackId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef",
    {"OperationId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef",
    {"StackId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
    {
        "Parameters": List["TemplateParameterTypeDef"],
        "Description": str,
        "Capabilities": List[Capability],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
