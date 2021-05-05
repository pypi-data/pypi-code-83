"""
Type annotations for appsync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appsync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef

    data: AdditionalAuthenticationProviderTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from mypy_boto3_appsync.literals import (
    ApiCacheStatus,
    ApiCacheType,
    ApiCachingBehavior,
    AuthenticationType,
    ConflictDetectionType,
    ConflictHandlerType,
    DataSourceType,
    DefaultAction,
    FieldLogLevel,
    ResolverKind,
    SchemaStatus,
    TypeDefinitionFormat,
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
    "AdditionalAuthenticationProviderTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeResponseTypeDef",
    "DataSourceTypeDef",
    "DeltaSyncConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "FunctionConfigurationTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetTypeResponseTypeDef",
    "GraphqlApiTypeDef",
    "HttpDataSourceConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "ListApiKeysResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesResponseTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "SyncConfigTypeDef",
    "TypeTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateTypeResponseTypeDef",
    "UserPoolConfigTypeDef",
)


class AdditionalAuthenticationProviderTypeDef(TypedDict, total=False):
    authenticationType: AuthenticationType
    openIDConnectConfig: "OpenIDConnectConfigTypeDef"
    userPoolConfig: "CognitoUserPoolConfigTypeDef"


ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehavior,
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": ApiCacheType,
        "status": ApiCacheStatus,
    },
    total=False,
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef", {"id": str, "description": str, "expires": int, "deletes": int}, total=False
)


class _RequiredAuthorizationConfigTypeDef(TypedDict):
    authorizationType: Literal["AWS_IAM"]


class AuthorizationConfigTypeDef(_RequiredAuthorizationConfigTypeDef, total=False):
    awsIamConfig: "AwsIamConfigTypeDef"


class AwsIamConfigTypeDef(TypedDict, total=False):
    signingRegion: str
    signingServiceName: str


class CachingConfigTypeDef(TypedDict, total=False):
    ttl: int
    cachingKeys: List[str]


class _RequiredCognitoUserPoolConfigTypeDef(TypedDict):
    userPoolId: str
    awsRegion: str


class CognitoUserPoolConfigTypeDef(_RequiredCognitoUserPoolConfigTypeDef, total=False):
    appIdClientRegex: str


class CreateApiCacheResponseTypeDef(TypedDict, total=False):
    apiCache: "ApiCacheTypeDef"


class CreateApiKeyResponseTypeDef(TypedDict, total=False):
    apiKey: "ApiKeyTypeDef"


class CreateDataSourceResponseTypeDef(TypedDict, total=False):
    dataSource: "DataSourceTypeDef"


class CreateFunctionResponseTypeDef(TypedDict, total=False):
    functionConfiguration: "FunctionConfigurationTypeDef"


class CreateGraphqlApiResponseTypeDef(TypedDict, total=False):
    graphqlApi: "GraphqlApiTypeDef"


class CreateResolverResponseTypeDef(TypedDict, total=False):
    resolver: "ResolverTypeDef"


CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": DataSourceType,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)


class DeltaSyncConfigTypeDef(TypedDict, total=False):
    baseTableTTL: int
    deltaSyncTableName: str
    deltaSyncTableTTL: int


class _RequiredDynamodbDataSourceConfigTypeDef(TypedDict):
    tableName: str
    awsRegion: str


class DynamodbDataSourceConfigTypeDef(_RequiredDynamodbDataSourceConfigTypeDef, total=False):
    useCallerCredentials: bool
    deltaSyncConfig: "DeltaSyncConfigTypeDef"
    versioned: bool


class ElasticsearchDataSourceConfigTypeDef(TypedDict):
    endpoint: str
    awsRegion: str


class FunctionConfigurationTypeDef(TypedDict, total=False):
    functionId: str
    functionArn: str
    name: str
    description: str
    dataSourceName: str
    requestMappingTemplate: str
    responseMappingTemplate: str
    functionVersion: str
    syncConfig: "SyncConfigTypeDef"


class GetApiCacheResponseTypeDef(TypedDict, total=False):
    apiCache: "ApiCacheTypeDef"


class GetDataSourceResponseTypeDef(TypedDict, total=False):
    dataSource: "DataSourceTypeDef"


class GetFunctionResponseTypeDef(TypedDict, total=False):
    functionConfiguration: "FunctionConfigurationTypeDef"


class GetGraphqlApiResponseTypeDef(TypedDict, total=False):
    graphqlApi: "GraphqlApiTypeDef"


class GetIntrospectionSchemaResponseTypeDef(TypedDict, total=False):
    schema: Union[bytes, IO[bytes]]


class GetResolverResponseTypeDef(TypedDict, total=False):
    resolver: "ResolverTypeDef"


class GetSchemaCreationStatusResponseTypeDef(TypedDict, total=False):
    status: SchemaStatus
    details: str


GetTypeResponseTypeDef = TypedDict("GetTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False)


class GraphqlApiTypeDef(TypedDict, total=False):
    name: str
    apiId: str
    authenticationType: AuthenticationType
    logConfig: "LogConfigTypeDef"
    userPoolConfig: "UserPoolConfigTypeDef"
    openIDConnectConfig: "OpenIDConnectConfigTypeDef"
    arn: str
    uris: Dict[str, str]
    tags: Dict[str, str]
    additionalAuthenticationProviders: List["AdditionalAuthenticationProviderTypeDef"]
    xrayEnabled: bool
    wafWebAclArn: str


class HttpDataSourceConfigTypeDef(TypedDict, total=False):
    endpoint: str
    authorizationConfig: "AuthorizationConfigTypeDef"


class LambdaConflictHandlerConfigTypeDef(TypedDict, total=False):
    lambdaConflictHandlerArn: str


class LambdaDataSourceConfigTypeDef(TypedDict):
    lambdaFunctionArn: str


class ListApiKeysResponseTypeDef(TypedDict, total=False):
    apiKeys: List["ApiKeyTypeDef"]
    nextToken: str


class ListDataSourcesResponseTypeDef(TypedDict, total=False):
    dataSources: List["DataSourceTypeDef"]
    nextToken: str


class ListFunctionsResponseTypeDef(TypedDict, total=False):
    functions: List["FunctionConfigurationTypeDef"]
    nextToken: str


class ListGraphqlApisResponseTypeDef(TypedDict, total=False):
    graphqlApis: List["GraphqlApiTypeDef"]
    nextToken: str


class ListResolversByFunctionResponseTypeDef(TypedDict, total=False):
    resolvers: List["ResolverTypeDef"]
    nextToken: str


class ListResolversResponseTypeDef(TypedDict, total=False):
    resolvers: List["ResolverTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef", {"types": List["TypeTypeDef"], "nextToken": str}, total=False
)


class _RequiredLogConfigTypeDef(TypedDict):
    fieldLogLevel: FieldLogLevel
    cloudWatchLogsRoleArn: str


class LogConfigTypeDef(_RequiredLogConfigTypeDef, total=False):
    excludeVerboseContent: bool


class _RequiredOpenIDConnectConfigTypeDef(TypedDict):
    issuer: str


class OpenIDConnectConfigTypeDef(_RequiredOpenIDConnectConfigTypeDef, total=False):
    clientId: str
    iatTTL: int
    authTTL: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PipelineConfigTypeDef(TypedDict, total=False):
    functions: List[str]


class RdsHttpEndpointConfigTypeDef(TypedDict, total=False):
    awsRegion: str
    dbClusterIdentifier: str
    databaseName: str
    schema: str
    awsSecretStoreArn: str


class RelationalDatabaseDataSourceConfigTypeDef(TypedDict, total=False):
    relationalDatabaseSourceType: Literal["RDS_HTTP_ENDPOINT"]
    rdsHttpEndpointConfig: "RdsHttpEndpointConfigTypeDef"


class ResolverTypeDef(TypedDict, total=False):
    typeName: str
    fieldName: str
    dataSourceName: str
    resolverArn: str
    requestMappingTemplate: str
    responseMappingTemplate: str
    kind: ResolverKind
    pipelineConfig: "PipelineConfigTypeDef"
    syncConfig: "SyncConfigTypeDef"
    cachingConfig: "CachingConfigTypeDef"


class StartSchemaCreationResponseTypeDef(TypedDict, total=False):
    status: SchemaStatus


class SyncConfigTypeDef(TypedDict, total=False):
    conflictHandler: ConflictHandlerType
    conflictDetection: ConflictDetectionType
    lambdaConflictHandlerConfig: "LambdaConflictHandlerConfigTypeDef"


TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": TypeDefinitionFormat,
    },
    total=False,
)


class UpdateApiCacheResponseTypeDef(TypedDict, total=False):
    apiCache: "ApiCacheTypeDef"


class UpdateApiKeyResponseTypeDef(TypedDict, total=False):
    apiKey: "ApiKeyTypeDef"


class UpdateDataSourceResponseTypeDef(TypedDict, total=False):
    dataSource: "DataSourceTypeDef"


class UpdateFunctionResponseTypeDef(TypedDict, total=False):
    functionConfiguration: "FunctionConfigurationTypeDef"


class UpdateGraphqlApiResponseTypeDef(TypedDict, total=False):
    graphqlApi: "GraphqlApiTypeDef"


class UpdateResolverResponseTypeDef(TypedDict, total=False):
    resolver: "ResolverTypeDef"


UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False
)


class _RequiredUserPoolConfigTypeDef(TypedDict):
    userPoolId: str
    awsRegion: str
    defaultAction: DefaultAction


class UserPoolConfigTypeDef(_RequiredUserPoolConfigTypeDef, total=False):
    appIdClientRegex: str
