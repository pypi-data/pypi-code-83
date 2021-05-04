"""
Type annotations for lambda service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/literals.html)

Usage::

    ```python
    from mypy_boto3_lambda.literals import CodeSigningPolicy

    data: CodeSigningPolicy = "Enforce"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CodeSigningPolicy",
    "EndPointType",
    "EventSourcePosition",
    "FunctionActiveWaiterName",
    "FunctionExistsWaiterName",
    "FunctionResponseType",
    "FunctionUpdatedWaiterName",
    "FunctionVersion",
    "InvocationType",
    "LastUpdateStatus",
    "LastUpdateStatusReasonCode",
    "ListAliasesPaginatorName",
    "ListCodeSigningConfigsPaginatorName",
    "ListEventSourceMappingsPaginatorName",
    "ListFunctionEventInvokeConfigsPaginatorName",
    "ListFunctionsByCodeSigningConfigPaginatorName",
    "ListFunctionsPaginatorName",
    "ListLayerVersionsPaginatorName",
    "ListLayersPaginatorName",
    "ListProvisionedConcurrencyConfigsPaginatorName",
    "ListVersionsByFunctionPaginatorName",
    "LogType",
    "PackageType",
    "ProvisionedConcurrencyStatusEnum",
    "Runtime",
    "SourceAccessType",
    "State",
    "StateReasonCode",
    "TracingMode",
)


CodeSigningPolicy = Literal["Enforce", "Warn"]
EndPointType = Literal["KAFKA_BOOTSTRAP_SERVERS"]
EventSourcePosition = Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
FunctionActiveWaiterName = Literal["function_active"]
FunctionExistsWaiterName = Literal["function_exists"]
FunctionResponseType = Literal["ReportBatchItemFailures"]
FunctionUpdatedWaiterName = Literal["function_updated"]
FunctionVersion = Literal["ALL"]
InvocationType = Literal["DryRun", "Event", "RequestResponse"]
LastUpdateStatus = Literal["Failed", "InProgress", "Successful"]
LastUpdateStatusReasonCode = Literal[
    "EniLimitExceeded",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "SubnetOutOfIPAddresses",
]
ListAliasesPaginatorName = Literal["list_aliases"]
ListCodeSigningConfigsPaginatorName = Literal["list_code_signing_configs"]
ListEventSourceMappingsPaginatorName = Literal["list_event_source_mappings"]
ListFunctionEventInvokeConfigsPaginatorName = Literal["list_function_event_invoke_configs"]
ListFunctionsByCodeSigningConfigPaginatorName = Literal["list_functions_by_code_signing_config"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListLayerVersionsPaginatorName = Literal["list_layer_versions"]
ListLayersPaginatorName = Literal["list_layers"]
ListProvisionedConcurrencyConfigsPaginatorName = Literal["list_provisioned_concurrency_configs"]
ListVersionsByFunctionPaginatorName = Literal["list_versions_by_function"]
LogType = Literal["None", "Tail"]
PackageType = Literal["Image", "Zip"]
ProvisionedConcurrencyStatusEnum = Literal["FAILED", "IN_PROGRESS", "READY"]
Runtime = Literal[
    "dotnetcore1.0",
    "dotnetcore2.0",
    "dotnetcore2.1",
    "dotnetcore3.1",
    "go1.x",
    "java11",
    "java8",
    "java8.al2",
    "nodejs",
    "nodejs10.x",
    "nodejs12.x",
    "nodejs14.x",
    "nodejs4.3",
    "nodejs4.3-edge",
    "nodejs6.10",
    "nodejs8.10",
    "provided",
    "provided.al2",
    "python2.7",
    "python3.6",
    "python3.7",
    "python3.8",
    "ruby2.5",
    "ruby2.7",
]
SourceAccessType = Literal[
    "BASIC_AUTH", "SASL_SCRAM_256_AUTH", "SASL_SCRAM_512_AUTH", "VPC_SECURITY_GROUP", "VPC_SUBNET"
]
State = Literal["Active", "Failed", "Inactive", "Pending"]
StateReasonCode = Literal[
    "Creating",
    "EniLimitExceeded",
    "Idle",
    "ImageAccessDenied",
    "ImageDeleted",
    "InsufficientRolePermissions",
    "InternalError",
    "InvalidConfiguration",
    "InvalidImage",
    "InvalidSecurityGroup",
    "InvalidSubnet",
    "Restoring",
    "SubnetOutOfIPAddresses",
]
TracingMode = Literal["Active", "PassThrough"]
