"""
Type annotations for lambda service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lambda import LambdaClient

    client: LambdaClient = boto3.client("lambda")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_lambda.literals import (
    EventSourcePosition,
    InvocationType,
    LogType,
    PackageType,
    Runtime,
)
from mypy_boto3_lambda.paginator import (
    ListAliasesPaginator,
    ListCodeSigningConfigsPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListFunctionsByCodeSigningConfigPaginator,
    ListFunctionsPaginator,
    ListLayersPaginator,
    ListLayerVersionsPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListVersionsByFunctionPaginator,
)
from mypy_boto3_lambda.type_defs import (
    AddLayerVersionPermissionResponseTypeDef,
    AddPermissionResponseTypeDef,
    AliasConfigurationTypeDef,
    AliasRoutingConfigurationTypeDef,
    AllowedPublishersTypeDef,
    CodeSigningPoliciesTypeDef,
    ConcurrencyTypeDef,
    CreateCodeSigningConfigResponseTypeDef,
    DeadLetterConfigTypeDef,
    DestinationConfigTypeDef,
    EnvironmentTypeDef,
    EventSourceMappingConfigurationTypeDef,
    FileSystemConfigTypeDef,
    FunctionCodeTypeDef,
    FunctionConfigurationTypeDef,
    FunctionEventInvokeConfigTypeDef,
    GetAccountSettingsResponseTypeDef,
    GetCodeSigningConfigResponseTypeDef,
    GetFunctionCodeSigningConfigResponseTypeDef,
    GetFunctionConcurrencyResponseTypeDef,
    GetFunctionResponseTypeDef,
    GetLayerVersionPolicyResponseTypeDef,
    GetLayerVersionResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProvisionedConcurrencyConfigResponseTypeDef,
    ImageConfigTypeDef,
    InvocationResponseTypeDef,
    InvokeAsyncResponseTypeDef,
    LayerVersionContentInputTypeDef,
    ListAliasesResponseTypeDef,
    ListCodeSigningConfigsResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsByCodeSigningConfigResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListLayersResponseTypeDef,
    ListLayerVersionsResponseTypeDef,
    ListProvisionedConcurrencyConfigsResponseTypeDef,
    ListTagsResponseTypeDef,
    ListVersionsByFunctionResponseTypeDef,
    PublishLayerVersionResponseTypeDef,
    PutFunctionCodeSigningConfigResponseTypeDef,
    PutProvisionedConcurrencyConfigResponseTypeDef,
    SelfManagedEventSourceTypeDef,
    SourceAccessConfigurationTypeDef,
    TracingConfigTypeDef,
    UpdateCodeSigningConfigResponseTypeDef,
    VpcConfigTypeDef,
)
from mypy_boto3_lambda.waiter import (
    FunctionActiveWaiter,
    FunctionExistsWaiter,
    FunctionUpdatedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LambdaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeSigningConfigNotFoundException: Type[BotocoreClientError]
    CodeStorageExceededException: Type[BotocoreClientError]
    CodeVerificationFailedException: Type[BotocoreClientError]
    EC2AccessDeniedException: Type[BotocoreClientError]
    EC2ThrottledException: Type[BotocoreClientError]
    EC2UnexpectedException: Type[BotocoreClientError]
    EFSIOException: Type[BotocoreClientError]
    EFSMountConnectivityException: Type[BotocoreClientError]
    EFSMountFailureException: Type[BotocoreClientError]
    EFSMountTimeoutException: Type[BotocoreClientError]
    ENILimitReachedException: Type[BotocoreClientError]
    InvalidCodeSignatureException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestContentException: Type[BotocoreClientError]
    InvalidRuntimeException: Type[BotocoreClientError]
    InvalidSecurityGroupIDException: Type[BotocoreClientError]
    InvalidSubnetIDException: Type[BotocoreClientError]
    InvalidZipFileException: Type[BotocoreClientError]
    KMSAccessDeniedException: Type[BotocoreClientError]
    KMSDisabledException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KMSNotFoundException: Type[BotocoreClientError]
    PolicyLengthExceededException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ProvisionedConcurrencyConfigNotFoundException: Type[BotocoreClientError]
    RequestTooLargeException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    SubnetIPAddressLimitReachedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedMediaTypeException: Type[BotocoreClientError]


class LambdaClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str = None,
        RevisionId: str = None,
    ) -> AddLayerVersionPermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.add_layer_version_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#add-layer-version-permission)
        """

    def add_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str = None,
        SourceAccount: str = None,
        EventSourceToken: str = None,
        Qualifier: str = None,
        RevisionId: str = None,
    ) -> AddPermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#add-permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#can-paginate)
        """

    def create_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str = None,
        RoutingConfig: "AliasRoutingConfigurationTypeDef" = None,
    ) -> "AliasConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.create_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create-alias)
        """

    def create_code_signing_config(
        self,
        AllowedPublishers: "AllowedPublishersTypeDef",
        Description: str = None,
        CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None,
    ) -> CreateCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.create_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create-code-signing-config)
        """

    def create_event_source_mapping(
        self,
        FunctionName: str,
        EventSourceArn: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        ParallelizationFactor: int = None,
        StartingPosition: EventSourcePosition = None,
        StartingPositionTimestamp: datetime = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        TumblingWindowInSeconds: int = None,
        Topics: List[str] = None,
        Queues: List[str] = None,
        SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
        SelfManagedEventSource: "SelfManagedEventSourceTypeDef" = None,
        FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]] = None,
    ) -> "EventSourceMappingConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.create_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create-event-source-mapping)
        """

    def create_function(
        self,
        FunctionName: str,
        Role: str,
        Code: FunctionCodeTypeDef,
        Runtime: Runtime = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        Publish: bool = None,
        VpcConfig: VpcConfigTypeDef = None,
        PackageType: PackageType = None,
        DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
        Environment: EnvironmentTypeDef = None,
        KMSKeyArn: str = None,
        TracingConfig: TracingConfigTypeDef = None,
        Tags: Dict[str, str] = None,
        Layers: List[str] = None,
        FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
        ImageConfig: "ImageConfigTypeDef" = None,
        CodeSigningConfigArn: str = None,
    ) -> "FunctionConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.create_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#create-function)
        """

    def delete_alias(self, FunctionName: str, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-alias)
        """

    def delete_code_signing_config(self, CodeSigningConfigArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-code-signing-config)
        """

    def delete_event_source_mapping(self, UUID: str) -> "EventSourceMappingConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-event-source-mapping)
        """

    def delete_function(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-function)
        """

    def delete_function_code_signing_config(self, FunctionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-function-code-signing-config)
        """

    def delete_function_concurrency(self, FunctionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-function-concurrency)
        """

    def delete_function_event_invoke_config(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-function-event-invoke-config)
        """

    def delete_layer_version(self, LayerName: str, VersionNumber: int) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-layer-version)
        """

    def delete_provisioned_concurrency_config(self, FunctionName: str, Qualifier: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.delete_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#delete-provisioned-concurrency-config)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#generate-presigned-url)
        """

    def get_account_settings(self) -> GetAccountSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-account-settings)
        """

    def get_alias(self, FunctionName: str, Name: str) -> "AliasConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-alias)
        """

    def get_code_signing_config(
        self, CodeSigningConfigArn: str
    ) -> GetCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-code-signing-config)
        """

    def get_event_source_mapping(self, UUID: str) -> "EventSourceMappingConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-event-source-mapping)
        """

    def get_function(self, FunctionName: str, Qualifier: str = None) -> GetFunctionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-function)
        """

    def get_function_code_signing_config(
        self, FunctionName: str
    ) -> GetFunctionCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-function-code-signing-config)
        """

    def get_function_concurrency(self, FunctionName: str) -> GetFunctionConcurrencyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-function-concurrency)
        """

    def get_function_configuration(
        self, FunctionName: str, Qualifier: str = None
    ) -> "FunctionConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_function_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-function-configuration)
        """

    def get_function_event_invoke_config(
        self, FunctionName: str, Qualifier: str = None
    ) -> "FunctionEventInvokeConfigTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-function-event-invoke-config)
        """

    def get_layer_version(
        self, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-layer-version)
        """

    def get_layer_version_by_arn(self, Arn: str) -> GetLayerVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_layer_version_by_arn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-layer-version-by-arn)
        """

    def get_layer_version_policy(
        self, LayerName: str, VersionNumber: int
    ) -> GetLayerVersionPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_layer_version_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-layer-version-policy)
        """

    def get_policy(self, FunctionName: str, Qualifier: str = None) -> GetPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-policy)
        """

    def get_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str
    ) -> GetProvisionedConcurrencyConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.get_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#get-provisioned-concurrency-config)
        """

    def invoke(
        self,
        FunctionName: str,
        InvocationType: InvocationType = None,
        LogType: LogType = None,
        ClientContext: str = None,
        Payload: Union[bytes, IO[bytes]] = None,
        Qualifier: str = None,
    ) -> InvocationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.invoke)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#invoke)
        """

    def invoke_async(
        self, FunctionName: str, InvokeArgs: Union[bytes, IO[bytes]]
    ) -> InvokeAsyncResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.invoke_async)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#invoke-async)
        """

    def list_aliases(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListAliasesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_aliases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-aliases)
        """

    def list_code_signing_configs(
        self, Marker: str = None, MaxItems: int = None
    ) -> ListCodeSigningConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_code_signing_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-code-signing-configs)
        """

    def list_event_source_mappings(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListEventSourceMappingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_event_source_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-event-source-mappings)
        """

    def list_function_event_invoke_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionEventInvokeConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_function_event_invoke_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-function-event-invoke-configs)
        """

    def list_functions(
        self,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListFunctionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_functions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-functions)
        """

    def list_functions_by_code_signing_config(
        self, CodeSigningConfigArn: str, Marker: str = None, MaxItems: int = None
    ) -> ListFunctionsByCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_functions_by_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-functions-by-code-signing-config)
        """

    def list_layer_versions(
        self,
        LayerName: str,
        CompatibleRuntime: Runtime = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ListLayerVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_layer_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-layer-versions)
        """

    def list_layers(
        self, CompatibleRuntime: Runtime = None, Marker: str = None, MaxItems: int = None
    ) -> ListLayersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_layers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-layers)
        """

    def list_provisioned_concurrency_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListProvisionedConcurrencyConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_provisioned_concurrency_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-provisioned-concurrency-configs)
        """

    def list_tags(self, Resource: str) -> ListTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-tags)
        """

    def list_versions_by_function(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ListVersionsByFunctionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.list_versions_by_function)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#list-versions-by-function)
        """

    def publish_layer_version(
        self,
        LayerName: str,
        Content: LayerVersionContentInputTypeDef,
        Description: str = None,
        CompatibleRuntimes: List[Runtime] = None,
        LicenseInfo: str = None,
    ) -> PublishLayerVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.publish_layer_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#publish-layer-version)
        """

    def publish_version(
        self,
        FunctionName: str,
        CodeSha256: str = None,
        Description: str = None,
        RevisionId: str = None,
    ) -> "FunctionConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.publish_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#publish-version)
        """

    def put_function_code_signing_config(
        self, CodeSigningConfigArn: str, FunctionName: str
    ) -> PutFunctionCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.put_function_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put-function-code-signing-config)
        """

    def put_function_concurrency(
        self, FunctionName: str, ReservedConcurrentExecutions: int
    ) -> "ConcurrencyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.put_function_concurrency)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put-function-concurrency)
        """

    def put_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
    ) -> "FunctionEventInvokeConfigTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.put_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put-function-event-invoke-config)
        """

    def put_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str, ProvisionedConcurrentExecutions: int
    ) -> PutProvisionedConcurrencyConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.put_provisioned_concurrency_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#put-provisioned-concurrency-config)
        """

    def remove_layer_version_permission(
        self, LayerName: str, VersionNumber: int, StatementId: str, RevisionId: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.remove_layer_version_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#remove-layer-version-permission)
        """

    def remove_permission(
        self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#remove-permission)
        """

    def tag_resource(self, Resource: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#tag-resource)
        """

    def untag_resource(self, Resource: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#untag-resource)
        """

    def update_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str = None,
        Description: str = None,
        RoutingConfig: "AliasRoutingConfigurationTypeDef" = None,
        RevisionId: str = None,
    ) -> "AliasConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-alias)
        """

    def update_code_signing_config(
        self,
        CodeSigningConfigArn: str,
        Description: str = None,
        AllowedPublishers: "AllowedPublishersTypeDef" = None,
        CodeSigningPolicies: "CodeSigningPoliciesTypeDef" = None,
    ) -> UpdateCodeSigningConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_code_signing_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-code-signing-config)
        """

    def update_event_source_mapping(
        self,
        UUID: str,
        FunctionName: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        ParallelizationFactor: int = None,
        SourceAccessConfigurations: List["SourceAccessConfigurationTypeDef"] = None,
        TumblingWindowInSeconds: int = None,
        FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]] = None,
    ) -> "EventSourceMappingConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_event_source_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-event-source-mapping)
        """

    def update_function_code(
        self,
        FunctionName: str,
        ZipFile: Union[bytes, IO[bytes]] = None,
        S3Bucket: str = None,
        S3Key: str = None,
        S3ObjectVersion: str = None,
        ImageUri: str = None,
        Publish: bool = None,
        DryRun: bool = None,
        RevisionId: str = None,
    ) -> "FunctionConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_function_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-function-code)
        """

    def update_function_configuration(
        self,
        FunctionName: str,
        Role: str = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        VpcConfig: VpcConfigTypeDef = None,
        Environment: EnvironmentTypeDef = None,
        Runtime: Runtime = None,
        DeadLetterConfig: "DeadLetterConfigTypeDef" = None,
        KMSKeyArn: str = None,
        TracingConfig: TracingConfigTypeDef = None,
        RevisionId: str = None,
        Layers: List[str] = None,
        FileSystemConfigs: List["FileSystemConfigTypeDef"] = None,
        ImageConfig: "ImageConfigTypeDef" = None,
    ) -> "FunctionConfigurationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_function_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-function-configuration)
        """

    def update_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: "DestinationConfigTypeDef" = None,
    ) -> "FunctionEventInvokeConfigTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Client.update_function_event_invoke_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/client.html#update-function-event-invoke-config)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_aliases"]) -> ListAliasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListAliases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listaliasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_signing_configs"]
    ) -> ListCodeSigningConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListCodeSigningConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listcodesigningconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_event_source_mappings"]
    ) -> ListEventSourceMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listeventsourcemappingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_function_event_invoke_configs"]
    ) -> ListFunctionEventInvokeConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctioneventinvokeconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_functions"]) -> ListFunctionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListFunctions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_functions_by_code_signing_config"]
    ) -> ListFunctionsByCodeSigningConfigPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListFunctionsByCodeSigningConfig)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionsbycodesigningconfigpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_layer_versions"]
    ) -> ListLayerVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_layers"]) -> ListLayersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListLayers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_concurrency_configs"]
    ) -> ListProvisionedConcurrencyConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listprovisionedconcurrencyconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_versions_by_function"]
    ) -> ListVersionsByFunctionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listversionsbyfunctionpaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["function_active"]) -> FunctionActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Waiter.function_active)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["function_exists"]) -> FunctionExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Waiter.function_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["function_updated"]) -> FunctionUpdatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lambda.html#Lambda.Waiter.function_updated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/waiters.html#functionupdatedwaiter)
        """
