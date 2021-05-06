"""
Type annotations for lambda service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/type_defs.html)

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
    EventSourcePosition,
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
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountLimitTypeDef",
    "AccountUsageTypeDef",
    "AddLayerVersionPermissionResponseTypeDef",
    "AddPermissionResponseTypeDef",
    "AliasConfigurationTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AllowedPublishersTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyTypeDef",
    "CreateCodeSigningConfigResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DestinationConfigTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EventSourceMappingConfigurationTypeDef",
    "FileSystemConfigTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionCodeTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionEventInvokeConfigTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetCodeSigningConfigResponseTypeDef",
    "GetFunctionCodeSigningConfigResponseTypeDef",
    "GetFunctionConcurrencyResponseTypeDef",
    "GetFunctionResponseTypeDef",
    "GetLayerVersionPolicyResponseTypeDef",
    "GetLayerVersionResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncResponseTypeDef",
    "LayerTypeDef",
    "LayerVersionContentInputTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
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
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "PublishLayerVersionResponseTypeDef",
    "PutFunctionCodeSigningConfigResponseTypeDef",
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    "ResponseMetadata",
    "SelfManagedEventSourceTypeDef",
    "SourceAccessConfigurationTypeDef",
    "TracingConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UpdateCodeSigningConfigResponseTypeDef",
    "VpcConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)


class AccountLimitTypeDef(TypedDict, total=False):
    TotalCodeSize: int
    CodeSizeUnzipped: int
    CodeSizeZipped: int
    ConcurrentExecutions: int
    UnreservedConcurrentExecutions: int


class AccountUsageTypeDef(TypedDict, total=False):
    TotalCodeSize: int
    FunctionCount: int


class AddLayerVersionPermissionResponseTypeDef(TypedDict, total=False):
    Statement: str
    RevisionId: str


class AddPermissionResponseTypeDef(TypedDict, total=False):
    Statement: str


class AliasConfigurationTypeDef(TypedDict, total=False):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: "AliasRoutingConfigurationTypeDef"
    RevisionId: str


class AliasRoutingConfigurationTypeDef(TypedDict, total=False):
    AdditionalVersionWeights: Dict[str, float]


class AllowedPublishersTypeDef(TypedDict):
    SigningProfileVersionArns: List[str]


class _RequiredCodeSigningConfigTypeDef(TypedDict):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: "AllowedPublishersTypeDef"
    CodeSigningPolicies: "CodeSigningPoliciesTypeDef"
    LastModified: str


class CodeSigningConfigTypeDef(_RequiredCodeSigningConfigTypeDef, total=False):
    Description: str


class CodeSigningPoliciesTypeDef(TypedDict, total=False):
    UntrustedArtifactOnDeployment: CodeSigningPolicy


class ConcurrencyTypeDef(TypedDict, total=False):
    ReservedConcurrentExecutions: int


class CreateCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: "CodeSigningConfigTypeDef"


class DeadLetterConfigTypeDef(TypedDict, total=False):
    TargetArn: str


class DestinationConfigTypeDef(TypedDict, total=False):
    OnSuccess: "OnSuccessTypeDef"
    OnFailure: "OnFailureTypeDef"


class EnvironmentErrorTypeDef(TypedDict, total=False):
    ErrorCode: str
    Message: str


class EnvironmentResponseTypeDef(TypedDict, total=False):
    Variables: Dict[str, str]
    Error: "EnvironmentErrorTypeDef"


class EnvironmentTypeDef(TypedDict, total=False):
    Variables: Dict[str, str]


class EventSourceMappingConfigurationTypeDef(TypedDict, total=False):
    UUID: str
    StartingPosition: EventSourcePosition
    StartingPositionTimestamp: datetime
    BatchSize: int
    MaximumBatchingWindowInSeconds: int
    ParallelizationFactor: int
    EventSourceArn: str
    FunctionArn: str
    LastModified: datetime
    LastProcessingResult: str
    State: str
    StateTransitionReason: str
    DestinationConfig: "DestinationConfigTypeDef"
    Topics: List[str]
    Queues: List[str]
    SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"]
    SelfManagedEventSource: "SelfManagedEventSourceTypeDef"
    MaximumRecordAgeInSeconds: int
    BisectBatchOnFunctionError: bool
    MaximumRetryAttempts: int
    TumblingWindowInSeconds: int
    FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]]


class FileSystemConfigTypeDef(TypedDict):
    Arn: str
    LocalMountPath: str


class FunctionCodeLocationTypeDef(TypedDict, total=False):
    RepositoryType: str
    Location: str
    ImageUri: str
    ResolvedImageUri: str


class FunctionCodeTypeDef(TypedDict, total=False):
    ZipFile: Union[bytes, IO[bytes]]
    S3Bucket: str
    S3Key: str
    S3ObjectVersion: str
    ImageUri: str


class FunctionConfigurationTypeDef(TypedDict, total=False):
    FunctionName: str
    FunctionArn: str
    Runtime: Runtime
    Role: str
    Handler: str
    CodeSize: int
    Description: str
    Timeout: int
    MemorySize: int
    LastModified: str
    CodeSha256: str
    Version: str
    VpcConfig: "VpcConfigResponseTypeDef"
    DeadLetterConfig: "DeadLetterConfigTypeDef"
    Environment: "EnvironmentResponseTypeDef"
    KMSKeyArn: str
    TracingConfig: "TracingConfigResponseTypeDef"
    MasterArn: str
    RevisionId: str
    Layers: List["LayerTypeDef"]
    State: State
    StateReason: str
    StateReasonCode: StateReasonCode
    LastUpdateStatus: LastUpdateStatus
    LastUpdateStatusReason: str
    LastUpdateStatusReasonCode: LastUpdateStatusReasonCode
    FileSystemConfigs: List["FileSystemConfigTypeDef"]
    PackageType: PackageType
    ImageConfigResponse: "ImageConfigResponseTypeDef"
    SigningProfileVersionArn: str
    SigningJobArn: str


class FunctionEventInvokeConfigTypeDef(TypedDict, total=False):
    LastModified: datetime
    FunctionArn: str
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int
    DestinationConfig: "DestinationConfigTypeDef"


class GetAccountSettingsResponseTypeDef(TypedDict, total=False):
    AccountLimit: "AccountLimitTypeDef"
    AccountUsage: "AccountUsageTypeDef"


class GetCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: "CodeSigningConfigTypeDef"


class GetFunctionCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfigArn: str
    FunctionName: str


class GetFunctionConcurrencyResponseTypeDef(TypedDict, total=False):
    ReservedConcurrentExecutions: int


class GetFunctionResponseTypeDef(TypedDict, total=False):
    Configuration: "FunctionConfigurationTypeDef"
    Code: "FunctionCodeLocationTypeDef"
    Tags: Dict[str, str]
    Concurrency: "ConcurrencyTypeDef"


class GetLayerVersionPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str
    RevisionId: str


class GetLayerVersionResponseTypeDef(TypedDict, total=False):
    Content: "LayerVersionContentOutputTypeDef"
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[Runtime]
    LicenseInfo: str


class GetPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str
    RevisionId: str


class GetProvisionedConcurrencyConfigResponseTypeDef(TypedDict, total=False):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnum
    StatusReason: str
    LastModified: str


class ImageConfigErrorTypeDef(TypedDict, total=False):
    ErrorCode: str
    Message: str


class ImageConfigResponseTypeDef(TypedDict, total=False):
    ImageConfig: "ImageConfigTypeDef"
    Error: "ImageConfigErrorTypeDef"


class ImageConfigTypeDef(TypedDict, total=False):
    EntryPoint: List[str]
    Command: List[str]
    WorkingDirectory: str


class InvocationResponseTypeDef(TypedDict, total=False):
    StatusCode: int
    FunctionError: str
    LogResult: str
    Payload: IO[bytes]
    ExecutedVersion: str


class InvokeAsyncResponseTypeDef(TypedDict, total=False):
    Status: int


class LayerTypeDef(TypedDict, total=False):
    Arn: str
    CodeSize: int
    SigningProfileVersionArn: str
    SigningJobArn: str


class LayerVersionContentInputTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Key: str
    S3ObjectVersion: str
    ZipFile: Union[bytes, IO[bytes]]


class LayerVersionContentOutputTypeDef(TypedDict):
    Location: str
    CodeSha256: str
    CodeSize: int
    SigningProfileVersionArn: str
    SigningJobArn: str
    ResponseMetadata: "ResponseMetadata"


class LayerVersionsListItemTypeDef(TypedDict, total=False):
    LayerVersionArn: str
    Version: int
    Description: str
    CreatedDate: str
    CompatibleRuntimes: List[Runtime]
    LicenseInfo: str


class LayersListItemTypeDef(TypedDict, total=False):
    LayerName: str
    LayerArn: str
    LatestMatchingVersion: "LayerVersionsListItemTypeDef"


class ListAliasesResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Aliases: List["AliasConfigurationTypeDef"]


class ListCodeSigningConfigsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    CodeSigningConfigs: List["CodeSigningConfigTypeDef"]


class ListEventSourceMappingsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    EventSourceMappings: List["EventSourceMappingConfigurationTypeDef"]


class ListFunctionEventInvokeConfigsResponseTypeDef(TypedDict, total=False):
    FunctionEventInvokeConfigs: List["FunctionEventInvokeConfigTypeDef"]
    NextMarker: str


class ListFunctionsByCodeSigningConfigResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    FunctionArns: List[str]


class ListFunctionsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Functions: List["FunctionConfigurationTypeDef"]


class ListLayerVersionsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    LayerVersions: List["LayerVersionsListItemTypeDef"]


class ListLayersResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Layers: List["LayersListItemTypeDef"]


class ListProvisionedConcurrencyConfigsResponseTypeDef(TypedDict, total=False):
    ProvisionedConcurrencyConfigs: List["ProvisionedConcurrencyConfigListItemTypeDef"]
    NextMarker: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListVersionsByFunctionResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Versions: List["FunctionConfigurationTypeDef"]


class OnFailureTypeDef(TypedDict, total=False):
    Destination: str


class OnSuccessTypeDef(TypedDict, total=False):
    Destination: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProvisionedConcurrencyConfigListItemTypeDef(TypedDict, total=False):
    FunctionArn: str
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnum
    StatusReason: str
    LastModified: str


class PublishLayerVersionResponseTypeDef(TypedDict, total=False):
    Content: "LayerVersionContentOutputTypeDef"
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[Runtime]
    LicenseInfo: str


class PutFunctionCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfigArn: str
    FunctionName: str


class PutProvisionedConcurrencyConfigResponseTypeDef(TypedDict, total=False):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnum
    StatusReason: str
    LastModified: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SelfManagedEventSourceTypeDef(TypedDict, total=False):
    Endpoints: Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]


SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef", {"Type": SourceAccessType, "URI": str}, total=False
)


class TracingConfigResponseTypeDef(TypedDict, total=False):
    Mode: TracingMode


class TracingConfigTypeDef(TypedDict, total=False):
    Mode: TracingMode


class UpdateCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: "CodeSigningConfigTypeDef"


class VpcConfigResponseTypeDef(TypedDict, total=False):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    VpcId: str


class VpcConfigTypeDef(TypedDict, total=False):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
