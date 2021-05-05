"""
Type annotations for apigateway service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apigateway import APIGatewayClient

    client: APIGatewayClient = boto3.client("apigateway")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_apigateway.literals import (
    ApiKeySourceType,
    AuthorizerType,
    CacheClusterSize,
    ConnectionType,
    ContentHandlingStrategy,
    DocumentationPartType,
    GatewayResponseType,
    IntegrationType,
    LocationStatusType,
    PutMode,
    SecurityPolicy,
)
from mypy_boto3_apigateway.paginator import (
    GetApiKeysPaginator,
    GetAuthorizersPaginator,
    GetBasePathMappingsPaginator,
    GetClientCertificatesPaginator,
    GetDeploymentsPaginator,
    GetDocumentationPartsPaginator,
    GetDocumentationVersionsPaginator,
    GetDomainNamesPaginator,
    GetGatewayResponsesPaginator,
    GetModelsPaginator,
    GetRequestValidatorsPaginator,
    GetResourcesPaginator,
    GetRestApisPaginator,
    GetSdkTypesPaginator,
    GetUsagePaginator,
    GetUsagePlanKeysPaginator,
    GetUsagePlansPaginator,
    GetVpcLinksPaginator,
)
from mypy_boto3_apigateway.type_defs import (
    AccountTypeDef,
    ApiKeyIdsTypeDef,
    ApiKeysTypeDef,
    ApiKeyTypeDef,
    ApiStageTypeDef,
    AuthorizersTypeDef,
    AuthorizerTypeDef,
    BasePathMappingsTypeDef,
    BasePathMappingTypeDef,
    CanarySettingsTypeDef,
    ClientCertificatesTypeDef,
    ClientCertificateTypeDef,
    DeploymentCanarySettingsTypeDef,
    DeploymentsTypeDef,
    DeploymentTypeDef,
    DocumentationPartIdsTypeDef,
    DocumentationPartLocationTypeDef,
    DocumentationPartsTypeDef,
    DocumentationPartTypeDef,
    DocumentationVersionsTypeDef,
    DocumentationVersionTypeDef,
    DomainNamesTypeDef,
    DomainNameTypeDef,
    EndpointConfigurationTypeDef,
    ExportResponseTypeDef,
    GatewayResponsesTypeDef,
    GatewayResponseTypeDef,
    IntegrationResponseTypeDef,
    IntegrationTypeDef,
    MethodResponseTypeDef,
    MethodTypeDef,
    ModelsTypeDef,
    ModelTypeDef,
    MutualTlsAuthenticationInputTypeDef,
    PatchOperationTypeDef,
    QuotaSettingsTypeDef,
    RequestValidatorsTypeDef,
    RequestValidatorTypeDef,
    ResourcesTypeDef,
    ResourceTypeDef,
    RestApisTypeDef,
    RestApiTypeDef,
    SdkResponseTypeDef,
    SdkTypesTypeDef,
    SdkTypeTypeDef,
    StageKeyTypeDef,
    StagesTypeDef,
    StageTypeDef,
    TagsTypeDef,
    TemplateTypeDef,
    TestInvokeAuthorizerResponseTypeDef,
    TestInvokeMethodResponseTypeDef,
    ThrottleSettingsTypeDef,
    TlsConfigTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlanKeyTypeDef,
    UsagePlansTypeDef,
    UsagePlanTypeDef,
    UsageTypeDef,
    VpcLinksTypeDef,
    VpcLinkTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("APIGatewayClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class APIGatewayClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#can-paginate)
        """

    def create_api_key(
        self,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        generateDistinctId: bool = None,
        value: str = None,
        stageKeys: List[StageKeyTypeDef] = None,
        customerId: str = None,
        tags: Dict[str, str] = None,
    ) -> "ApiKeyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-api-key)
        """

    def create_authorizer(
        self,
        restApiId: str,
        name: str,
        type: AuthorizerType,
        providerARNs: List[str] = None,
        authType: str = None,
        authorizerUri: str = None,
        authorizerCredentials: str = None,
        identitySource: str = None,
        identityValidationExpression: str = None,
        authorizerResultTtlInSeconds: int = None,
    ) -> "AuthorizerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-authorizer)
        """

    def create_base_path_mapping(
        self, domainName: str, restApiId: str, basePath: str = None, stage: str = None
    ) -> "BasePathMappingTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-base-path-mapping)
        """

    def create_deployment(
        self,
        restApiId: str,
        stageName: str = None,
        stageDescription: str = None,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: CacheClusterSize = None,
        variables: Dict[str, str] = None,
        canarySettings: DeploymentCanarySettingsTypeDef = None,
        tracingEnabled: bool = None,
    ) -> "DeploymentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-deployment)
        """

    def create_documentation_part(
        self, restApiId: str, location: "DocumentationPartLocationTypeDef", properties: str
    ) -> "DocumentationPartTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-documentation-part)
        """

    def create_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        stageName: str = None,
        description: str = None,
    ) -> "DocumentationVersionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-documentation-version)
        """

    def create_domain_name(
        self,
        domainName: str,
        certificateName: str = None,
        certificateBody: str = None,
        certificatePrivateKey: str = None,
        certificateChain: str = None,
        certificateArn: str = None,
        regionalCertificateName: str = None,
        regionalCertificateArn: str = None,
        endpointConfiguration: "EndpointConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
        securityPolicy: SecurityPolicy = None,
        mutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None,
    ) -> "DomainNameTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-domain-name)
        """

    def create_model(
        self,
        restApiId: str,
        name: str,
        contentType: str,
        description: str = None,
        schema: str = None,
    ) -> "ModelTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-model)
        """

    def create_request_validator(
        self,
        restApiId: str,
        name: str = None,
        validateRequestBody: bool = None,
        validateRequestParameters: bool = None,
    ) -> "RequestValidatorTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-request-validator)
        """

    def create_resource(self, restApiId: str, parentId: str, pathPart: str) -> "ResourceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-resource)
        """

    def create_rest_api(
        self,
        name: str,
        description: str = None,
        version: str = None,
        cloneFrom: str = None,
        binaryMediaTypes: List[str] = None,
        minimumCompressionSize: int = None,
        apiKeySource: ApiKeySourceType = None,
        endpointConfiguration: "EndpointConfigurationTypeDef" = None,
        policy: str = None,
        tags: Dict[str, str] = None,
        disableExecuteApiEndpoint: bool = None,
    ) -> "RestApiTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-rest-api)
        """

    def create_stage(
        self,
        restApiId: str,
        stageName: str,
        deploymentId: str,
        description: str = None,
        cacheClusterEnabled: bool = None,
        cacheClusterSize: CacheClusterSize = None,
        variables: Dict[str, str] = None,
        documentationVersion: str = None,
        canarySettings: "CanarySettingsTypeDef" = None,
        tracingEnabled: bool = None,
        tags: Dict[str, str] = None,
    ) -> "StageTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-stage)
        """

    def create_usage_plan(
        self,
        name: str,
        description: str = None,
        apiStages: List["ApiStageTypeDef"] = None,
        throttle: "ThrottleSettingsTypeDef" = None,
        quota: "QuotaSettingsTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> "UsagePlanTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-usage-plan)
        """

    def create_usage_plan_key(
        self, usagePlanId: str, keyId: str, keyType: str
    ) -> "UsagePlanKeyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-usage-plan-key)
        """

    def create_vpc_link(
        self, name: str, targetArns: List[str], description: str = None, tags: Dict[str, str] = None
    ) -> "VpcLinkTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.create_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#create-vpc-link)
        """

    def delete_api_key(self, apiKey: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-api-key)
        """

    def delete_authorizer(self, restApiId: str, authorizerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-authorizer)
        """

    def delete_base_path_mapping(self, domainName: str, basePath: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-base-path-mapping)
        """

    def delete_client_certificate(self, clientCertificateId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-client-certificate)
        """

    def delete_deployment(self, restApiId: str, deploymentId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-deployment)
        """

    def delete_documentation_part(self, restApiId: str, documentationPartId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-documentation-part)
        """

    def delete_documentation_version(self, restApiId: str, documentationVersion: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-documentation-version)
        """

    def delete_domain_name(self, domainName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-domain-name)
        """

    def delete_gateway_response(self, restApiId: str, responseType: GatewayResponseType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-gateway-response)
        """

    def delete_integration(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-integration)
        """

    def delete_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-integration-response)
        """

    def delete_method(self, restApiId: str, resourceId: str, httpMethod: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-method)
        """

    def delete_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-method-response)
        """

    def delete_model(self, restApiId: str, modelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-model)
        """

    def delete_request_validator(self, restApiId: str, requestValidatorId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-request-validator)
        """

    def delete_resource(self, restApiId: str, resourceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-resource)
        """

    def delete_rest_api(self, restApiId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-rest-api)
        """

    def delete_stage(self, restApiId: str, stageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-stage)
        """

    def delete_usage_plan(self, usagePlanId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-usage-plan)
        """

    def delete_usage_plan_key(self, usagePlanId: str, keyId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-usage-plan-key)
        """

    def delete_vpc_link(self, vpcLinkId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.delete_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#delete-vpc-link)
        """

    def flush_stage_authorizers_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.flush_stage_authorizers_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#flush-stage-authorizers-cache)
        """

    def flush_stage_cache(self, restApiId: str, stageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.flush_stage_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#flush-stage-cache)
        """

    def generate_client_certificate(
        self, description: str = None, tags: Dict[str, str] = None
    ) -> "ClientCertificateTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.generate_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#generate-client-certificate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#generate-presigned-url)
        """

    def get_account(self) -> AccountTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-account)
        """

    def get_api_key(self, apiKey: str, includeValue: bool = None) -> "ApiKeyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-api-key)
        """

    def get_api_keys(
        self,
        position: str = None,
        limit: int = None,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
    ) -> ApiKeysTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-api-keys)
        """

    def get_authorizer(self, restApiId: str, authorizerId: str) -> "AuthorizerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-authorizer)
        """

    def get_authorizers(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> AuthorizersTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_authorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-authorizers)
        """

    def get_base_path_mapping(self, domainName: str, basePath: str) -> "BasePathMappingTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-base-path-mapping)
        """

    def get_base_path_mappings(
        self, domainName: str, position: str = None, limit: int = None
    ) -> BasePathMappingsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_base_path_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-base-path-mappings)
        """

    def get_client_certificate(self, clientCertificateId: str) -> "ClientCertificateTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-client-certificate)
        """

    def get_client_certificates(
        self, position: str = None, limit: int = None
    ) -> ClientCertificatesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_client_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-client-certificates)
        """

    def get_deployment(
        self, restApiId: str, deploymentId: str, embed: List[str] = None
    ) -> "DeploymentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-deployment)
        """

    def get_deployments(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> DeploymentsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-deployments)
        """

    def get_documentation_part(
        self, restApiId: str, documentationPartId: str
    ) -> "DocumentationPartTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-documentation-part)
        """

    def get_documentation_parts(
        self,
        restApiId: str,
        type: DocumentationPartType = None,
        nameQuery: str = None,
        path: str = None,
        position: str = None,
        limit: int = None,
        locationStatus: LocationStatusType = None,
    ) -> DocumentationPartsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_documentation_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-documentation-parts)
        """

    def get_documentation_version(
        self, restApiId: str, documentationVersion: str
    ) -> "DocumentationVersionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-documentation-version)
        """

    def get_documentation_versions(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> DocumentationVersionsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_documentation_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-documentation-versions)
        """

    def get_domain_name(self, domainName: str) -> "DomainNameTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-domain-name)
        """

    def get_domain_names(self, position: str = None, limit: int = None) -> DomainNamesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-domain-names)
        """

    def get_export(
        self,
        restApiId: str,
        stageName: str,
        exportType: str,
        parameters: Dict[str, str] = None,
        accepts: str = None,
    ) -> ExportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-export)
        """

    def get_gateway_response(
        self, restApiId: str, responseType: GatewayResponseType
    ) -> "GatewayResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-gateway-response)
        """

    def get_gateway_responses(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> GatewayResponsesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_gateway_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-gateway-responses)
        """

    def get_integration(
        self, restApiId: str, resourceId: str, httpMethod: str
    ) -> "IntegrationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-integration)
        """

    def get_integration_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> "IntegrationResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-integration-response)
        """

    def get_method(self, restApiId: str, resourceId: str, httpMethod: str) -> "MethodTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-method)
        """

    def get_method_response(
        self, restApiId: str, resourceId: str, httpMethod: str, statusCode: str
    ) -> "MethodResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-method-response)
        """

    def get_model(self, restApiId: str, modelName: str, flatten: bool = None) -> "ModelTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-model)
        """

    def get_model_template(self, restApiId: str, modelName: str) -> TemplateTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_model_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-model-template)
        """

    def get_models(self, restApiId: str, position: str = None, limit: int = None) -> ModelsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-models)
        """

    def get_request_validator(
        self, restApiId: str, requestValidatorId: str
    ) -> "RequestValidatorTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-request-validator)
        """

    def get_request_validators(
        self, restApiId: str, position: str = None, limit: int = None
    ) -> RequestValidatorsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_request_validators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-request-validators)
        """

    def get_resource(
        self, restApiId: str, resourceId: str, embed: List[str] = None
    ) -> "ResourceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-resource)
        """

    def get_resources(
        self, restApiId: str, position: str = None, limit: int = None, embed: List[str] = None
    ) -> ResourcesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-resources)
        """

    def get_rest_api(self, restApiId: str) -> "RestApiTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-rest-api)
        """

    def get_rest_apis(self, position: str = None, limit: int = None) -> RestApisTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_rest_apis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-rest-apis)
        """

    def get_sdk(
        self, restApiId: str, stageName: str, sdkType: str, parameters: Dict[str, str] = None
    ) -> SdkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_sdk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-sdk)
        """

    def get_sdk_type(self, id: str) -> "SdkTypeTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_sdk_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-sdk-type)
        """

    def get_sdk_types(self, position: str = None, limit: int = None) -> SdkTypesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_sdk_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-sdk-types)
        """

    def get_stage(self, restApiId: str, stageName: str) -> "StageTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-stage)
        """

    def get_stages(self, restApiId: str, deploymentId: str = None) -> StagesTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-stages)
        """

    def get_tags(self, resourceArn: str, position: str = None, limit: int = None) -> TagsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-tags)
        """

    def get_usage(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        position: str = None,
        limit: int = None,
    ) -> UsageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-usage)
        """

    def get_usage_plan(self, usagePlanId: str) -> "UsagePlanTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-usage-plan)
        """

    def get_usage_plan_key(self, usagePlanId: str, keyId: str) -> "UsagePlanKeyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-usage-plan-key)
        """

    def get_usage_plan_keys(
        self, usagePlanId: str, position: str = None, limit: int = None, nameQuery: str = None
    ) -> UsagePlanKeysTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_usage_plan_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-usage-plan-keys)
        """

    def get_usage_plans(
        self, position: str = None, keyId: str = None, limit: int = None
    ) -> UsagePlansTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_usage_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-usage-plans)
        """

    def get_vpc_link(self, vpcLinkId: str) -> "VpcLinkTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-vpc-link)
        """

    def get_vpc_links(self, position: str = None, limit: int = None) -> VpcLinksTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.get_vpc_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#get-vpc-links)
        """

    def import_api_keys(
        self, body: Union[bytes, IO[bytes]], format: Literal["csv"], failOnWarnings: bool = None
    ) -> ApiKeyIdsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.import_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import-api-keys)
        """

    def import_documentation_parts(
        self,
        restApiId: str,
        body: Union[bytes, IO[bytes]],
        mode: PutMode = None,
        failOnWarnings: bool = None,
    ) -> DocumentationPartIdsTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.import_documentation_parts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import-documentation-parts)
        """

    def import_rest_api(
        self,
        body: Union[bytes, IO[bytes]],
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None,
    ) -> "RestApiTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.import_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#import-rest-api)
        """

    def put_gateway_response(
        self,
        restApiId: str,
        responseType: GatewayResponseType,
        statusCode: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
    ) -> "GatewayResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-gateway-response)
        """

    def put_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        type: IntegrationType,
        integrationHttpMethod: str = None,
        uri: str = None,
        connectionType: ConnectionType = None,
        connectionId: str = None,
        credentials: str = None,
        requestParameters: Dict[str, str] = None,
        requestTemplates: Dict[str, str] = None,
        passthroughBehavior: str = None,
        cacheNamespace: str = None,
        cacheKeyParameters: List[str] = None,
        contentHandling: ContentHandlingStrategy = None,
        timeoutInMillis: int = None,
        tlsConfig: "TlsConfigTypeDef" = None,
    ) -> "IntegrationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-integration)
        """

    def put_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        selectionPattern: str = None,
        responseParameters: Dict[str, str] = None,
        responseTemplates: Dict[str, str] = None,
        contentHandling: ContentHandlingStrategy = None,
    ) -> "IntegrationResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-integration-response)
        """

    def put_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        authorizationType: str,
        authorizerId: str = None,
        apiKeyRequired: bool = None,
        operationName: str = None,
        requestParameters: Dict[str, bool] = None,
        requestModels: Dict[str, str] = None,
        requestValidatorId: str = None,
        authorizationScopes: List[str] = None,
    ) -> "MethodTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-method)
        """

    def put_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        responseParameters: Dict[str, bool] = None,
        responseModels: Dict[str, str] = None,
    ) -> "MethodResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-method-response)
        """

    def put_rest_api(
        self,
        restApiId: str,
        body: Union[bytes, IO[bytes]],
        mode: PutMode = None,
        failOnWarnings: bool = None,
        parameters: Dict[str, str] = None,
    ) -> "RestApiTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.put_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#put-rest-api)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#tag-resource)
        """

    def test_invoke_authorizer(
        self,
        restApiId: str,
        authorizerId: str,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        pathWithQueryString: str = None,
        body: str = None,
        stageVariables: Dict[str, str] = None,
        additionalContext: Dict[str, str] = None,
    ) -> TestInvokeAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.test_invoke_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#test-invoke-authorizer)
        """

    def test_invoke_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        pathWithQueryString: str = None,
        body: str = None,
        headers: Dict[str, str] = None,
        multiValueHeaders: Dict[str, List[str]] = None,
        clientCertificateId: str = None,
        stageVariables: Dict[str, str] = None,
    ) -> TestInvokeMethodResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.test_invoke_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#test-invoke-method)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#untag-resource)
        """

    def update_account(self, patchOperations: List[PatchOperationTypeDef] = None) -> AccountTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-account)
        """

    def update_api_key(
        self, apiKey: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ApiKeyTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-api-key)
        """

    def update_authorizer(
        self, restApiId: str, authorizerId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "AuthorizerTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-authorizer)
        """

    def update_base_path_mapping(
        self, domainName: str, basePath: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "BasePathMappingTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_base_path_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-base-path-mapping)
        """

    def update_client_certificate(
        self, clientCertificateId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ClientCertificateTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_client_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-client-certificate)
        """

    def update_deployment(
        self, restApiId: str, deploymentId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "DeploymentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-deployment)
        """

    def update_documentation_part(
        self,
        restApiId: str,
        documentationPartId: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "DocumentationPartTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_documentation_part)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-documentation-part)
        """

    def update_documentation_version(
        self,
        restApiId: str,
        documentationVersion: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "DocumentationVersionTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_documentation_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-documentation-version)
        """

    def update_domain_name(
        self, domainName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "DomainNameTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-domain-name)
        """

    def update_gateway_response(
        self,
        restApiId: str,
        responseType: GatewayResponseType,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "GatewayResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_gateway_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-gateway-response)
        """

    def update_integration(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "IntegrationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-integration)
        """

    def update_integration_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "IntegrationResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-integration-response)
        """

    def update_method(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "MethodTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-method)
        """

    def update_method_response(
        self,
        restApiId: str,
        resourceId: str,
        httpMethod: str,
        statusCode: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "MethodResponseTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_method_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-method-response)
        """

    def update_model(
        self, restApiId: str, modelName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ModelTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-model)
        """

    def update_request_validator(
        self,
        restApiId: str,
        requestValidatorId: str,
        patchOperations: List[PatchOperationTypeDef] = None,
    ) -> "RequestValidatorTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_request_validator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-request-validator)
        """

    def update_resource(
        self, restApiId: str, resourceId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "ResourceTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-resource)
        """

    def update_rest_api(
        self, restApiId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "RestApiTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_rest_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-rest-api)
        """

    def update_stage(
        self, restApiId: str, stageName: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "StageTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-stage)
        """

    def update_usage(
        self, usagePlanId: str, keyId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> UsageTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-usage)
        """

    def update_usage_plan(
        self, usagePlanId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "UsagePlanTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_usage_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-usage-plan)
        """

    def update_vpc_link(
        self, vpcLinkId: str, patchOperations: List[PatchOperationTypeDef] = None
    ) -> "VpcLinkTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Client.update_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/client.html#update-vpc-link)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_api_keys"]) -> GetApiKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getapikeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_authorizers"]) -> GetAuthorizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getauthorizerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_base_path_mappings"]
    ) -> GetBasePathMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getbasepathmappingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_client_certificates"]
    ) -> GetClientCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getclientcertificatespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_deployments"]) -> GetDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdeploymentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_parts"]
    ) -> GetDocumentationPartsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdocumentationpartspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_documentation_versions"]
    ) -> GetDocumentationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdocumentationversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_domain_names"]) -> GetDomainNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getdomainnamespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_gateway_responses"]
    ) -> GetGatewayResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getgatewayresponsespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_models"]) -> GetModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetModels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getmodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_request_validators"]
    ) -> GetRequestValidatorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getrequestvalidatorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_resources"]) -> GetResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetResources)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getresourcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_rest_apis"]) -> GetRestApisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getrestapispaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_sdk_types"]) -> GetSdkTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getsdktypespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_usage"]) -> GetUsagePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusagepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_usage_plan_keys"]
    ) -> GetUsagePlanKeysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusageplankeyspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_usage_plans"]) -> GetUsagePlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getusageplanspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_vpc_links"]) -> GetVpcLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigateway/paginators.html#getvpclinkspaginator)
        """
