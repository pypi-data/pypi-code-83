"""
Type annotations for appsync service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/literals.html)

Usage::

    ```python
    from mypy_boto3_appsync.literals import ApiCacheStatus

    data: ApiCacheStatus = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApiCacheStatus",
    "ApiCacheType",
    "ApiCachingBehavior",
    "AuthenticationType",
    "AuthorizationType",
    "ConflictDetectionType",
    "ConflictHandlerType",
    "DataSourceType",
    "DefaultAction",
    "FieldLogLevel",
    "ListApiKeysPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListFunctionsPaginatorName",
    "ListGraphqlApisPaginatorName",
    "ListResolversByFunctionPaginatorName",
    "ListResolversPaginatorName",
    "ListTypesPaginatorName",
    "OutputType",
    "RelationalDatabaseSourceType",
    "ResolverKind",
    "SchemaStatus",
    "TypeDefinitionFormat",
)


ApiCacheStatus = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED", "MODIFYING"]
ApiCacheType = Literal[
    "LARGE",
    "LARGE_12X",
    "LARGE_2X",
    "LARGE_4X",
    "LARGE_8X",
    "MEDIUM",
    "R4_2XLARGE",
    "R4_4XLARGE",
    "R4_8XLARGE",
    "R4_LARGE",
    "R4_XLARGE",
    "SMALL",
    "T2_MEDIUM",
    "T2_SMALL",
    "XLARGE",
]
ApiCachingBehavior = Literal["FULL_REQUEST_CACHING", "PER_RESOLVER_CACHING"]
AuthenticationType = Literal["AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "OPENID_CONNECT"]
AuthorizationType = Literal["AWS_IAM"]
ConflictDetectionType = Literal["NONE", "VERSION"]
ConflictHandlerType = Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
DataSourceType = Literal[
    "AMAZON_DYNAMODB", "AMAZON_ELASTICSEARCH", "AWS_LAMBDA", "HTTP", "NONE", "RELATIONAL_DATABASE"
]
DefaultAction = Literal["ALLOW", "DENY"]
FieldLogLevel = Literal["ALL", "ERROR", "NONE"]
ListApiKeysPaginatorName = Literal["list_api_keys"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListFunctionsPaginatorName = Literal["list_functions"]
ListGraphqlApisPaginatorName = Literal["list_graphql_apis"]
ListResolversByFunctionPaginatorName = Literal["list_resolvers_by_function"]
ListResolversPaginatorName = Literal["list_resolvers"]
ListTypesPaginatorName = Literal["list_types"]
OutputType = Literal["JSON", "SDL"]
RelationalDatabaseSourceType = Literal["RDS_HTTP_ENDPOINT"]
ResolverKind = Literal["PIPELINE", "UNIT"]
SchemaStatus = Literal["ACTIVE", "DELETING", "FAILED", "NOT_APPLICABLE", "PROCESSING", "SUCCESS"]
TypeDefinitionFormat = Literal["JSON", "SDL"]
