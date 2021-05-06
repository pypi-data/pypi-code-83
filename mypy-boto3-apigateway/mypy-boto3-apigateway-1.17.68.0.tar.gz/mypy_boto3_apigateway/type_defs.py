"""
Type annotations for apigateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_apigateway.literals import (
    ApiKeySourceType,
    AuthorizerType,
    CacheClusterSize,
    CacheClusterStatus,
    ConnectionType,
    ContentHandlingStrategy,
    DocumentationPartType,
    DomainNameStatus,
    EndpointType,
    GatewayResponseType,
    IntegrationType,
    Op,
    QuotaPeriodType,
    SecurityPolicy,
    UnauthorizedCacheControlHeaderStrategy,
    VpcLinkStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessLogSettingsTypeDef",
    "AccountTypeDef",
    "ApiKeyIdsTypeDef",
    "ApiKeyTypeDef",
    "ApiKeysTypeDef",
    "ApiStageTypeDef",
    "AuthorizerTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingTypeDef",
    "BasePathMappingsTypeDef",
    "CanarySettingsTypeDef",
    "ClientCertificateTypeDef",
    "ClientCertificatesTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "DocumentationPartIdsTypeDef",
    "DocumentationPartLocationTypeDef",
    "DocumentationPartTypeDef",
    "DocumentationPartsTypeDef",
    "DocumentationVersionTypeDef",
    "DocumentationVersionsTypeDef",
    "DomainNameTypeDef",
    "DomainNamesTypeDef",
    "EndpointConfigurationTypeDef",
    "ExportResponseTypeDef",
    "GatewayResponseTypeDef",
    "GatewayResponsesTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "MethodSnapshotTypeDef",
    "MethodTypeDef",
    "ModelTypeDef",
    "ModelsTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "PatchOperationTypeDef",
    "QuotaSettingsTypeDef",
    "RequestValidatorTypeDef",
    "RequestValidatorsTypeDef",
    "ResourceTypeDef",
    "ResourcesTypeDef",
    "RestApiTypeDef",
    "RestApisTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "SdkResponseTypeDef",
    "SdkTypeTypeDef",
    "SdkTypesTypeDef",
    "StageKeyTypeDef",
    "StageTypeDef",
    "StagesTypeDef",
    "TagsTypeDef",
    "TemplateTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "TestInvokeMethodResponseTypeDef",
    "ThrottleSettingsTypeDef",
    "TlsConfigTypeDef",
    "UsagePlanKeyTypeDef",
    "UsagePlanKeysTypeDef",
    "UsagePlanTypeDef",
    "UsagePlansTypeDef",
    "UsageTypeDef",
    "VpcLinkTypeDef",
    "VpcLinksTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef", {"format": str, "destinationArn": str}, total=False
)


class AccountTypeDef(TypedDict, total=False):
    cloudwatchRoleArn: str
    throttleSettings: "ThrottleSettingsTypeDef"
    features: List[str]
    apiKeyVersion: str


class ApiKeyIdsTypeDef(TypedDict, total=False):
    ids: List[str]
    warnings: List[str]


ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class ApiKeysTypeDef(TypedDict, total=False):
    warnings: List[str]
    position: str
    items: List["ApiKeyTypeDef"]


class ApiStageTypeDef(TypedDict, total=False):
    apiId: str
    stage: str
    throttle: Dict[str, "ThrottleSettingsTypeDef"]


AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "id": str,
        "name": str,
        "type": AuthorizerType,
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
    },
    total=False,
)


class AuthorizersTypeDef(TypedDict, total=False):
    position: str
    items: List["AuthorizerTypeDef"]


class BasePathMappingTypeDef(TypedDict, total=False):
    basePath: str
    restApiId: str
    stage: str


class BasePathMappingsTypeDef(TypedDict, total=False):
    position: str
    items: List["BasePathMappingTypeDef"]


class CanarySettingsTypeDef(TypedDict, total=False):
    percentTraffic: float
    deploymentId: str
    stageVariableOverrides: Dict[str, str]
    useStageCache: bool


class ClientCertificateTypeDef(TypedDict, total=False):
    clientCertificateId: str
    description: str
    pemEncodedCertificate: str
    createdDate: datetime
    expirationDate: datetime
    tags: Dict[str, str]


class ClientCertificatesTypeDef(TypedDict, total=False):
    position: str
    items: List["ClientCertificateTypeDef"]


class DeploymentCanarySettingsTypeDef(TypedDict, total=False):
    percentTraffic: float
    stageVariableOverrides: Dict[str, str]
    useStageCache: bool


DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, "MethodSnapshotTypeDef"]],
    },
    total=False,
)


class DeploymentsTypeDef(TypedDict, total=False):
    position: str
    items: List["DeploymentTypeDef"]


class DocumentationPartIdsTypeDef(TypedDict, total=False):
    ids: List[str]
    warnings: List[str]


_RequiredDocumentationPartLocationTypeDef = TypedDict(
    "_RequiredDocumentationPartLocationTypeDef", {"type": DocumentationPartType}
)
_OptionalDocumentationPartLocationTypeDef = TypedDict(
    "_OptionalDocumentationPartLocationTypeDef",
    {"path": str, "method": str, "statusCode": str, "name": str},
    total=False,
)


class DocumentationPartLocationTypeDef(
    _RequiredDocumentationPartLocationTypeDef, _OptionalDocumentationPartLocationTypeDef
):
    pass


DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {"id": str, "location": "DocumentationPartLocationTypeDef", "properties": str},
    total=False,
)


class DocumentationPartsTypeDef(TypedDict, total=False):
    position: str
    items: List["DocumentationPartTypeDef"]


class DocumentationVersionTypeDef(TypedDict, total=False):
    version: str
    createdDate: datetime
    description: str


class DocumentationVersionsTypeDef(TypedDict, total=False):
    position: str
    items: List["DocumentationVersionTypeDef"]


class DomainNameTypeDef(TypedDict, total=False):
    domainName: str
    certificateName: str
    certificateArn: str
    certificateUploadDate: datetime
    regionalDomainName: str
    regionalHostedZoneId: str
    regionalCertificateName: str
    regionalCertificateArn: str
    distributionDomainName: str
    distributionHostedZoneId: str
    endpointConfiguration: "EndpointConfigurationTypeDef"
    domainNameStatus: DomainNameStatus
    domainNameStatusMessage: str
    securityPolicy: SecurityPolicy
    tags: Dict[str, str]
    mutualTlsAuthentication: "MutualTlsAuthenticationTypeDef"


class DomainNamesTypeDef(TypedDict, total=False):
    position: str
    items: List["DomainNameTypeDef"]


EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {"types": List[EndpointType], "vpcEndpointIds": List[str]},
    total=False,
)


class ExportResponseTypeDef(TypedDict, total=False):
    contentType: str
    contentDisposition: str
    body: Union[bytes, IO[bytes]]


class GatewayResponseTypeDef(TypedDict, total=False):
    responseType: GatewayResponseType
    statusCode: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    defaultResponse: bool


class GatewayResponsesTypeDef(TypedDict, total=False):
    position: str
    items: List["GatewayResponseTypeDef"]


class IntegrationResponseTypeDef(TypedDict, total=False):
    statusCode: str
    selectionPattern: str
    responseParameters: Dict[str, str]
    responseTemplates: Dict[str, str]
    contentHandling: ContentHandlingStrategy


IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": IntegrationType,
        "httpMethod": str,
        "uri": str,
        "connectionType": ConnectionType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": ContentHandlingStrategy,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, "IntegrationResponseTypeDef"],
        "tlsConfig": "TlsConfigTypeDef",
    },
    total=False,
)


class MethodResponseTypeDef(TypedDict, total=False):
    statusCode: str
    responseParameters: Dict[str, bool]
    responseModels: Dict[str, str]


class MethodSettingTypeDef(TypedDict, total=False):
    metricsEnabled: bool
    loggingLevel: str
    dataTraceEnabled: bool
    throttlingBurstLimit: int
    throttlingRateLimit: float
    cachingEnabled: bool
    cacheTtlInSeconds: int
    cacheDataEncrypted: bool
    requireAuthorizationForCacheControl: bool
    unauthorizedCacheControlHeaderStrategy: UnauthorizedCacheControlHeaderStrategy


class MethodSnapshotTypeDef(TypedDict, total=False):
    authorizationType: str
    apiKeyRequired: bool


class MethodTypeDef(TypedDict, total=False):
    httpMethod: str
    authorizationType: str
    authorizerId: str
    apiKeyRequired: bool
    requestValidatorId: str
    operationName: str
    requestParameters: Dict[str, bool]
    requestModels: Dict[str, str]
    methodResponses: Dict[str, "MethodResponseTypeDef"]
    methodIntegration: "IntegrationTypeDef"
    authorizationScopes: List[str]


ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {"id": str, "name": str, "description": str, "schema": str, "contentType": str},
    total=False,
)


class ModelsTypeDef(TypedDict, total=False):
    position: str
    items: List["ModelTypeDef"]


class MutualTlsAuthenticationInputTypeDef(TypedDict, total=False):
    truststoreUri: str
    truststoreVersion: str


class MutualTlsAuthenticationTypeDef(TypedDict, total=False):
    truststoreUri: str
    truststoreVersion: str
    truststoreWarnings: List[str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef", {"op": Op, "path": str, "value": str, "from": str}, total=False
)


class QuotaSettingsTypeDef(TypedDict, total=False):
    limit: int
    offset: int
    period: QuotaPeriodType


RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {"id": str, "name": str, "validateRequestBody": bool, "validateRequestParameters": bool},
    total=False,
)


class RequestValidatorsTypeDef(TypedDict, total=False):
    position: str
    items: List["RequestValidatorTypeDef"]


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, "MethodTypeDef"],
    },
    total=False,
)


class ResourcesTypeDef(TypedDict, total=False):
    position: str
    items: List["ResourceTypeDef"]


RestApiTypeDef = TypedDict(
    "RestApiTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceType,
        "endpointConfiguration": "EndpointConfigurationTypeDef",
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
    },
    total=False,
)


class RestApisTypeDef(TypedDict, total=False):
    position: str
    items: List["RestApiTypeDef"]


class SdkConfigurationPropertyTypeDef(TypedDict, total=False):
    name: str
    friendlyName: str
    description: str
    required: bool
    defaultValue: str


class SdkResponseTypeDef(TypedDict, total=False):
    contentType: str
    contentDisposition: str
    body: Union[bytes, IO[bytes]]


SdkTypeTypeDef = TypedDict(
    "SdkTypeTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List["SdkConfigurationPropertyTypeDef"],
    },
    total=False,
)


class SdkTypesTypeDef(TypedDict, total=False):
    position: str
    items: List["SdkTypeTypeDef"]


class StageKeyTypeDef(TypedDict, total=False):
    restApiId: str
    stageName: str


class StageTypeDef(TypedDict, total=False):
    deploymentId: str
    clientCertificateId: str
    stageName: str
    description: str
    cacheClusterEnabled: bool
    cacheClusterSize: CacheClusterSize
    cacheClusterStatus: CacheClusterStatus
    methodSettings: Dict[str, "MethodSettingTypeDef"]
    variables: Dict[str, str]
    documentationVersion: str
    accessLogSettings: "AccessLogSettingsTypeDef"
    canarySettings: "CanarySettingsTypeDef"
    tracingEnabled: bool
    webAclArn: str
    tags: Dict[str, str]
    createdDate: datetime
    lastUpdatedDate: datetime


class StagesTypeDef(TypedDict, total=False):
    item: List["StageTypeDef"]


class TagsTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class TemplateTypeDef(TypedDict, total=False):
    value: str


class TestInvokeAuthorizerResponseTypeDef(TypedDict, total=False):
    clientStatus: int
    log: str
    latency: int
    principalId: str
    policy: str
    authorization: Dict[str, List[str]]
    claims: Dict[str, str]


class TestInvokeMethodResponseTypeDef(TypedDict, total=False):
    status: int
    body: str
    headers: Dict[str, str]
    multiValueHeaders: Dict[str, List[str]]
    log: str
    latency: int


class ThrottleSettingsTypeDef(TypedDict, total=False):
    burstLimit: int
    rateLimit: float


class TlsConfigTypeDef(TypedDict, total=False):
    insecureSkipVerification: bool


UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef", {"id": str, "type": str, "value": str, "name": str}, total=False
)


class UsagePlanKeysTypeDef(TypedDict, total=False):
    position: str
    items: List["UsagePlanKeyTypeDef"]


UsagePlanTypeDef = TypedDict(
    "UsagePlanTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List["ApiStageTypeDef"],
        "throttle": "ThrottleSettingsTypeDef",
        "quota": "QuotaSettingsTypeDef",
        "productCode": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class UsagePlansTypeDef(TypedDict, total=False):
    position: str
    items: List["UsagePlanTypeDef"]


class UsageTypeDef(TypedDict, total=False):
    usagePlanId: str
    startDate: str
    endDate: str
    position: str
    items: Dict[str, List[List[int]]]


VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatus,
        "statusMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class VpcLinksTypeDef(TypedDict, total=False):
    position: str
    items: List["VpcLinkTypeDef"]
