"""
Type annotations for apigateway service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/literals.html)

Usage::

    ```python
    from mypy_boto3_apigateway.literals import ApiKeySourceType

    data: ApiKeySourceType = "AUTHORIZER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApiKeySourceType",
    "ApiKeysFormat",
    "AuthorizerType",
    "CacheClusterSize",
    "CacheClusterStatus",
    "ConnectionType",
    "ContentHandlingStrategy",
    "DocumentationPartType",
    "DomainNameStatus",
    "EndpointType",
    "GatewayResponseType",
    "GetApiKeysPaginatorName",
    "GetAuthorizersPaginatorName",
    "GetBasePathMappingsPaginatorName",
    "GetClientCertificatesPaginatorName",
    "GetDeploymentsPaginatorName",
    "GetDocumentationPartsPaginatorName",
    "GetDocumentationVersionsPaginatorName",
    "GetDomainNamesPaginatorName",
    "GetGatewayResponsesPaginatorName",
    "GetModelsPaginatorName",
    "GetRequestValidatorsPaginatorName",
    "GetResourcesPaginatorName",
    "GetRestApisPaginatorName",
    "GetSdkTypesPaginatorName",
    "GetUsagePaginatorName",
    "GetUsagePlanKeysPaginatorName",
    "GetUsagePlansPaginatorName",
    "GetVpcLinksPaginatorName",
    "IntegrationType",
    "LocationStatusType",
    "Op",
    "PutMode",
    "QuotaPeriodType",
    "SecurityPolicy",
    "UnauthorizedCacheControlHeaderStrategy",
    "VpcLinkStatus",
)


ApiKeySourceType = Literal["AUTHORIZER", "HEADER"]
ApiKeysFormat = Literal["csv"]
AuthorizerType = Literal["COGNITO_USER_POOLS", "REQUEST", "TOKEN"]
CacheClusterSize = Literal["0.5", "1.6", "118", "13.5", "237", "28.4", "58.2", "6.1"]
CacheClusterStatus = Literal[
    "AVAILABLE", "CREATE_IN_PROGRESS", "DELETE_IN_PROGRESS", "FLUSH_IN_PROGRESS", "NOT_AVAILABLE"
]
ConnectionType = Literal["INTERNET", "VPC_LINK"]
ContentHandlingStrategy = Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
DocumentationPartType = Literal[
    "API",
    "AUTHORIZER",
    "METHOD",
    "MODEL",
    "PATH_PARAMETER",
    "QUERY_PARAMETER",
    "REQUEST_BODY",
    "REQUEST_HEADER",
    "RESOURCE",
    "RESPONSE",
    "RESPONSE_BODY",
    "RESPONSE_HEADER",
]
DomainNameStatus = Literal["AVAILABLE", "PENDING", "UPDATING"]
EndpointType = Literal["EDGE", "PRIVATE", "REGIONAL"]
GatewayResponseType = Literal[
    "ACCESS_DENIED",
    "API_CONFIGURATION_ERROR",
    "AUTHORIZER_CONFIGURATION_ERROR",
    "AUTHORIZER_FAILURE",
    "BAD_REQUEST_BODY",
    "BAD_REQUEST_PARAMETERS",
    "DEFAULT_4XX",
    "DEFAULT_5XX",
    "EXPIRED_TOKEN",
    "INTEGRATION_FAILURE",
    "INTEGRATION_TIMEOUT",
    "INVALID_API_KEY",
    "INVALID_SIGNATURE",
    "MISSING_AUTHENTICATION_TOKEN",
    "QUOTA_EXCEEDED",
    "REQUEST_TOO_LARGE",
    "RESOURCE_NOT_FOUND",
    "THROTTLED",
    "UNAUTHORIZED",
    "UNSUPPORTED_MEDIA_TYPE",
]
GetApiKeysPaginatorName = Literal["get_api_keys"]
GetAuthorizersPaginatorName = Literal["get_authorizers"]
GetBasePathMappingsPaginatorName = Literal["get_base_path_mappings"]
GetClientCertificatesPaginatorName = Literal["get_client_certificates"]
GetDeploymentsPaginatorName = Literal["get_deployments"]
GetDocumentationPartsPaginatorName = Literal["get_documentation_parts"]
GetDocumentationVersionsPaginatorName = Literal["get_documentation_versions"]
GetDomainNamesPaginatorName = Literal["get_domain_names"]
GetGatewayResponsesPaginatorName = Literal["get_gateway_responses"]
GetModelsPaginatorName = Literal["get_models"]
GetRequestValidatorsPaginatorName = Literal["get_request_validators"]
GetResourcesPaginatorName = Literal["get_resources"]
GetRestApisPaginatorName = Literal["get_rest_apis"]
GetSdkTypesPaginatorName = Literal["get_sdk_types"]
GetUsagePaginatorName = Literal["get_usage"]
GetUsagePlanKeysPaginatorName = Literal["get_usage_plan_keys"]
GetUsagePlansPaginatorName = Literal["get_usage_plans"]
GetVpcLinksPaginatorName = Literal["get_vpc_links"]
IntegrationType = Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
LocationStatusType = Literal["DOCUMENTED", "UNDOCUMENTED"]
Op = Literal["add", "copy", "move", "remove", "replace", "test"]
PutMode = Literal["merge", "overwrite"]
QuotaPeriodType = Literal["DAY", "MONTH", "WEEK"]
SecurityPolicy = Literal["TLS_1_0", "TLS_1_2"]
UnauthorizedCacheControlHeaderStrategy = Literal[
    "FAIL_WITH_403", "SUCCEED_WITHOUT_RESPONSE_HEADER", "SUCCEED_WITH_RESPONSE_HEADER"
]
VpcLinkStatus = Literal["AVAILABLE", "DELETING", "FAILED", "PENDING"]
