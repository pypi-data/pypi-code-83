"""
Main interface for lambda service type definitions.

Usage::

    ```python
    from mypy_boto3_lambda.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_lambda.literals import (
    CodeSigningPolicy,
    EndPointType,
    EventSourcePosition,
    FunctionResponseType,
    LastUpdateStatus,
    LastUpdateStatusReasonCode,
    PackageType,
    ProvisionedConcurrencyStatusEnum,
    Runtime,
    SourceAccessType,
    State,
    StateReasonCode,
    TracingMode,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountLimitTypeDef",
    "AccountUsageTypeDef",
    "AliasConfigurationTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AllowedPublishersTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyTypeDef",
    "DeadLetterConfigTypeDef",
    "DestinationConfigTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EventSourceMappingConfigurationTypeDef",
    "FileSystemConfigTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionEventInvokeConfigTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "LayerTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "ResponseMetadata",
    "SelfManagedEventSourceTypeDef",
    "SourceAccessConfigurationTypeDef",
    "TracingConfigResponseTypeDef",
    "VpcConfigResponseTypeDef",
    "AddLayerVersionPermissionResponseTypeDef",
    "AddPermissionResponseTypeDef",
    "CreateCodeSigningConfigResponseTypeDef",
    "EnvironmentTypeDef",
    "FunctionCodeTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetCodeSigningConfigResponseTypeDef",
    "GetFunctionCodeSigningConfigResponseTypeDef",
    "GetFunctionConcurrencyResponseTypeDef",
    "GetFunctionResponseTypeDef",
    "GetLayerVersionPolicyResponseTypeDef",
    "GetLayerVersionResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncResponseTypeDef",
    "LayerVersionContentInputTypeDef",
    "ListAliasesResponseTypeDef",
    "ListCodeSigningConfigsResponseTypeDef",
    "ListEventSourceMappingsResponseTypeDef",
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListLayerVersionsResponseTypeDef",
    "ListLayersResponseTypeDef",
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsByFunctionResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishLayerVersionResponseTypeDef",
    "PutFunctionCodeSigningConfigResponseTypeDef",
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UpdateCodeSigningConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)

AccountUsageTypeDef = TypedDict(
    "AccountUsageTypeDef", {"TotalCodeSize": int, "FunctionCount": int}, total=False
)

AliasConfigurationTypeDef = TypedDict(
    "AliasConfigurationTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
    },
    total=False,
)

AliasRoutingConfigurationTypeDef = TypedDict(
    "AliasRoutingConfigurationTypeDef", {"AdditionalVersionWeights": Dict[str, float]}, total=False
)

AllowedPublishersTypeDef = TypedDict(
    "AllowedPublishersTypeDef", {"SigningProfileVersionArns": List[str]}
)

_RequiredCodeSigningConfigTypeDef = TypedDict(
    "_RequiredCodeSigningConfigTypeDef",
    {
        "CodeSigningConfigId": str,
        "CodeSigningConfigArn": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
        "LastModified": str,
    },
)
_OptionalCodeSigningConfigTypeDef = TypedDict(
    "_OptionalCodeSigningConfigTypeDef", {"Description": str}, total=False
)


class CodeSigningConfigTypeDef(
    _RequiredCodeSigningConfigTypeDef, _OptionalCodeSigningConfigTypeDef
):
    pass


CodeSigningPoliciesTypeDef = TypedDict(
    "CodeSigningPoliciesTypeDef", {"UntrustedArtifactOnDeployment": CodeSigningPolicy}, total=False
)

ConcurrencyTypeDef = TypedDict(
    "ConcurrencyTypeDef", {"ReservedConcurrentExecutions": int}, total=False
)

DeadLetterConfigTypeDef = TypedDict("DeadLetterConfigTypeDef", {"TargetArn": str}, total=False)

DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {"OnSuccess": "OnSuccessTypeDef", "OnFailure": "OnFailureTypeDef"},
    total=False,
)

EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef", {"ErrorCode": str, "Message": str}, total=False
)

EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {"Variables": Dict[str, str], "Error": "EnvironmentErrorTypeDef"},
    total=False,
)

EventSourceMappingConfigurationTypeDef = TypedDict(
    "EventSourceMappingConfigurationTypeDef",
    {
        "UUID": str,
        "StartingPosition": EventSourcePosition,
        "StartingPositionTimestamp": datetime,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": "DestinationConfigTypeDef",
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[FunctionResponseType],
    },
    total=False,
)

FileSystemConfigTypeDef = TypedDict("FileSystemConfigTypeDef", {"Arn": str, "LocalMountPath": str})

FunctionCodeLocationTypeDef = TypedDict(
    "FunctionCodeLocationTypeDef",
    {"RepositoryType": str, "Location": str, "ImageUri": str, "ResolvedImageUri": str},
    total=False,
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": Runtime,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": "VpcConfigResponseTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentResponseTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigResponseTypeDef",
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List["LayerTypeDef"],
        "State": State,
        "StateReason": str,
        "StateReasonCode": StateReasonCode,
        "LastUpdateStatus": LastUpdateStatus,
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": LastUpdateStatusReasonCode,
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "PackageType": PackageType,
        "ImageConfigResponse": "ImageConfigResponseTypeDef",
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
    },
    total=False,
)

FunctionEventInvokeConfigTypeDef = TypedDict(
    "FunctionEventInvokeConfigTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)

ImageConfigErrorTypeDef = TypedDict(
    "ImageConfigErrorTypeDef", {"ErrorCode": str, "Message": str}, total=False
)

ImageConfigResponseTypeDef = TypedDict(
    "ImageConfigResponseTypeDef",
    {"ImageConfig": "ImageConfigTypeDef", "Error": "ImageConfigErrorTypeDef"},
    total=False,
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef",
    {"EntryPoint": List[str], "Command": List[str], "WorkingDirectory": str},
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {"Arn": str, "CodeSize": int, "SigningProfileVersionArn": str, "SigningJobArn": str},
    total=False,
)

LayerVersionContentOutputTypeDef = TypedDict(
    "LayerVersionContentOutputTypeDef",
    {
        "Location": str,
        "CodeSha256": str,
        "CodeSize": int,
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

LayerVersionsListItemTypeDef = TypedDict(
    "LayerVersionsListItemTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[Runtime],
        "LicenseInfo": str,
    },
    total=False,
)

LayersListItemTypeDef = TypedDict(
    "LayersListItemTypeDef",
    {"LayerName": str, "LayerArn": str, "LatestMatchingVersion": "LayerVersionsListItemTypeDef"},
    total=False,
)

OnFailureTypeDef = TypedDict("OnFailureTypeDef", {"Destination": str}, total=False)

OnSuccessTypeDef = TypedDict("OnSuccessTypeDef", {"Destination": str}, total=False)

ProvisionedConcurrencyConfigListItemTypeDef = TypedDict(
    "ProvisionedConcurrencyConfigListItemTypeDef",
    {
        "FunctionArn": str,
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnum,
        "StatusReason": str,
        "LastModified": str,
    },
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

SelfManagedEventSourceTypeDef = TypedDict(
    "SelfManagedEventSourceTypeDef", {"Endpoints": Dict[EndPointType, List[str]]}, total=False
)

SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef", {"Type": SourceAccessType, "URI": str}, total=False
)

TracingConfigResponseTypeDef = TypedDict(
    "TracingConfigResponseTypeDef", {"Mode": TracingMode}, total=False
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {"SubnetIds": List[str], "SecurityGroupIds": List[str], "VpcId": str},
    total=False,
)

AddLayerVersionPermissionResponseTypeDef = TypedDict(
    "AddLayerVersionPermissionResponseTypeDef", {"Statement": str, "RevisionId": str}, total=False
)

AddPermissionResponseTypeDef = TypedDict(
    "AddPermissionResponseTypeDef", {"Statement": str}, total=False
)

CreateCodeSigningConfigResponseTypeDef = TypedDict(
    "CreateCodeSigningConfigResponseTypeDef", {"CodeSigningConfig": "CodeSigningConfigTypeDef"}
)

EnvironmentTypeDef = TypedDict("EnvironmentTypeDef", {"Variables": Dict[str, str]}, total=False)

FunctionCodeTypeDef = TypedDict(
    "FunctionCodeTypeDef",
    {
        "ZipFile": Union[bytes, IO[bytes]],
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ImageUri": str,
    },
    total=False,
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {"AccountLimit": "AccountLimitTypeDef", "AccountUsage": "AccountUsageTypeDef"},
    total=False,
)

GetCodeSigningConfigResponseTypeDef = TypedDict(
    "GetCodeSigningConfigResponseTypeDef", {"CodeSigningConfig": "CodeSigningConfigTypeDef"}
)

GetFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigResponseTypeDef",
    {"CodeSigningConfigArn": str, "FunctionName": str},
)

GetFunctionConcurrencyResponseTypeDef = TypedDict(
    "GetFunctionConcurrencyResponseTypeDef", {"ReservedConcurrentExecutions": int}, total=False
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "Configuration": "FunctionConfigurationTypeDef",
        "Code": "FunctionCodeLocationTypeDef",
        "Tags": Dict[str, str],
        "Concurrency": "ConcurrencyTypeDef",
    },
    total=False,
)

GetLayerVersionPolicyResponseTypeDef = TypedDict(
    "GetLayerVersionPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

GetLayerVersionResponseTypeDef = TypedDict(
    "GetLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[Runtime],
        "LicenseInfo": str,
    },
    total=False,
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

GetProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnum,
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

InvocationResponseTypeDef = TypedDict(
    "InvocationResponseTypeDef",
    {
        "StatusCode": int,
        "FunctionError": str,
        "LogResult": str,
        "Payload": IO[bytes],
        "ExecutedVersion": str,
    },
    total=False,
)

InvokeAsyncResponseTypeDef = TypedDict("InvokeAsyncResponseTypeDef", {"Status": int}, total=False)

LayerVersionContentInputTypeDef = TypedDict(
    "LayerVersionContentInputTypeDef",
    {"S3Bucket": str, "S3Key": str, "S3ObjectVersion": str, "ZipFile": Union[bytes, IO[bytes]]},
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {"NextMarker": str, "Aliases": List["AliasConfigurationTypeDef"]},
    total=False,
)

ListCodeSigningConfigsResponseTypeDef = TypedDict(
    "ListCodeSigningConfigsResponseTypeDef",
    {"NextMarker": str, "CodeSigningConfigs": List["CodeSigningConfigTypeDef"]},
    total=False,
)

ListEventSourceMappingsResponseTypeDef = TypedDict(
    "ListEventSourceMappingsResponseTypeDef",
    {"NextMarker": str, "EventSourceMappings": List["EventSourceMappingConfigurationTypeDef"]},
    total=False,
)

ListFunctionEventInvokeConfigsResponseTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    {"FunctionEventInvokeConfigs": List["FunctionEventInvokeConfigTypeDef"], "NextMarker": str},
    total=False,
)

ListFunctionsByCodeSigningConfigResponseTypeDef = TypedDict(
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    {"NextMarker": str, "FunctionArns": List[str]},
    total=False,
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {"NextMarker": str, "Functions": List["FunctionConfigurationTypeDef"]},
    total=False,
)

ListLayerVersionsResponseTypeDef = TypedDict(
    "ListLayerVersionsResponseTypeDef",
    {"NextMarker": str, "LayerVersions": List["LayerVersionsListItemTypeDef"]},
    total=False,
)

ListLayersResponseTypeDef = TypedDict(
    "ListLayersResponseTypeDef",
    {"NextMarker": str, "Layers": List["LayersListItemTypeDef"]},
    total=False,
)

ListProvisionedConcurrencyConfigsResponseTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List["ProvisionedConcurrencyConfigListItemTypeDef"],
        "NextMarker": str,
    },
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ListVersionsByFunctionResponseTypeDef = TypedDict(
    "ListVersionsByFunctionResponseTypeDef",
    {"NextMarker": str, "Versions": List["FunctionConfigurationTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PublishLayerVersionResponseTypeDef = TypedDict(
    "PublishLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[Runtime],
        "LicenseInfo": str,
    },
    total=False,
)

PutFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigResponseTypeDef",
    {"CodeSigningConfigArn": str, "FunctionName": str},
)

PutProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnum,
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

TracingConfigTypeDef = TypedDict("TracingConfigTypeDef", {"Mode": TracingMode}, total=False)

UpdateCodeSigningConfigResponseTypeDef = TypedDict(
    "UpdateCodeSigningConfigResponseTypeDef", {"CodeSigningConfig": "CodeSigningConfigTypeDef"}
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
