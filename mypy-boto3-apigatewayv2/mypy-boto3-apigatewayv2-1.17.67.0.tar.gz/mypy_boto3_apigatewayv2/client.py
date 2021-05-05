"""
Type annotations for apigatewayv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apigatewayv2 import ApiGatewayV2Client

    client: ApiGatewayV2Client = boto3.client("apigatewayv2")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_apigatewayv2.literals import (
    AuthorizationType,
    AuthorizerType,
    ConnectionType,
    ContentHandlingStrategy,
    IntegrationType,
    JSONYAMLType,
    PassthroughBehavior,
    ProtocolType,
)
from mypy_boto3_apigatewayv2.paginator import (
    GetApisPaginator,
    GetAuthorizersPaginator,
    GetDeploymentsPaginator,
    GetDomainNamesPaginator,
    GetIntegrationResponsesPaginator,
    GetIntegrationsPaginator,
    GetModelsPaginator,
    GetRouteResponsesPaginator,
    GetRoutesPaginator,
    GetStagesPaginator,
)
from mypy_boto3_apigatewayv2.type_defs import (
    AccessLogSettingsTypeDef,
    CorsTypeDef,
    CreateApiMappingResponseTypeDef,
    CreateApiResponseTypeDef,
    CreateAuthorizerResponseTypeDef,
    CreateDeploymentResponseTypeDef,
    CreateDomainNameResponseTypeDef,
    CreateIntegrationResponseResponseTypeDef,
    CreateIntegrationResultTypeDef,
    CreateModelResponseTypeDef,
    CreateRouteResponseResponseTypeDef,
    CreateRouteResultTypeDef,
    CreateStageResponseTypeDef,
    CreateVpcLinkResponseTypeDef,
    DomainNameConfigurationTypeDef,
    ExportApiResponseTypeDef,
    GetApiMappingResponseTypeDef,
    GetApiMappingsResponseTypeDef,
    GetApiResponseTypeDef,
    GetApisResponseTypeDef,
    GetAuthorizerResponseTypeDef,
    GetAuthorizersResponseTypeDef,
    GetDeploymentResponseTypeDef,
    GetDeploymentsResponseTypeDef,
    GetDomainNameResponseTypeDef,
    GetDomainNamesResponseTypeDef,
    GetIntegrationResponseResponseTypeDef,
    GetIntegrationResponsesResponseTypeDef,
    GetIntegrationResultTypeDef,
    GetIntegrationsResponseTypeDef,
    GetModelResponseTypeDef,
    GetModelsResponseTypeDef,
    GetModelTemplateResponseTypeDef,
    GetRouteResponseResponseTypeDef,
    GetRouteResponsesResponseTypeDef,
    GetRouteResultTypeDef,
    GetRoutesResponseTypeDef,
    GetStageResponseTypeDef,
    GetStagesResponseTypeDef,
    GetTagsResponseTypeDef,
    GetVpcLinkResponseTypeDef,
    GetVpcLinksResponseTypeDef,
    ImportApiResponseTypeDef,
    JWTConfigurationTypeDef,
    MutualTlsAuthenticationInputTypeDef,
    ParameterConstraintsTypeDef,
    ReimportApiResponseTypeDef,
    RouteSettingsTypeDef,
    TlsConfigInputTypeDef,
    UpdateApiMappingResponseTypeDef,
    UpdateApiResponseTypeDef,
    UpdateAuthorizerResponseTypeDef,
    UpdateDeploymentResponseTypeDef,
    UpdateDomainNameResponseTypeDef,
    UpdateIntegrationResponseResponseTypeDef,
    UpdateIntegrationResultTypeDef,
    UpdateModelResponseTypeDef,
    UpdateRouteResponseResponseTypeDef,
    UpdateRouteResultTypeDef,
    UpdateStageResponseTypeDef,
    UpdateVpcLinkResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApiGatewayV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class ApiGatewayV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#can-paginate)
        """

    def create_api(
        self,
        Name: str,
        ProtocolType: ProtocolType,
        ApiKeySelectionExpression: str = None,
        CorsConfiguration: "CorsTypeDef" = None,
        CredentialsArn: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        DisableExecuteApiEndpoint: bool = None,
        RouteKey: str = None,
        RouteSelectionExpression: str = None,
        Tags: Dict[str, str] = None,
        Target: str = None,
        Version: str = None,
    ) -> CreateApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-api)
        """

    def create_api_mapping(
        self, ApiId: str, DomainName: str, Stage: str, ApiMappingKey: str = None
    ) -> CreateApiMappingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_api_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-api-mapping)
        """

    def create_authorizer(
        self,
        ApiId: str,
        AuthorizerType: AuthorizerType,
        IdentitySource: List[str],
        Name: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerPayloadFormatVersion: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        AuthorizerUri: str = None,
        EnableSimpleResponses: bool = None,
        IdentityValidationExpression: str = None,
        JwtConfiguration: "JWTConfigurationTypeDef" = None,
    ) -> CreateAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-authorizer)
        """

    def create_deployment(
        self, ApiId: str, Description: str = None, StageName: str = None
    ) -> CreateDeploymentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-deployment)
        """

    def create_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: List["DomainNameConfigurationTypeDef"] = None,
        MutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDomainNameResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-domain-name)
        """

    def create_integration(
        self,
        ApiId: str,
        IntegrationType: IntegrationType,
        ConnectionId: str = None,
        ConnectionType: ConnectionType = None,
        ContentHandlingStrategy: ContentHandlingStrategy = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationSubtype: str = None,
        IntegrationUri: str = None,
        PassthroughBehavior: PassthroughBehavior = None,
        PayloadFormatVersion: str = None,
        RequestParameters: Dict[str, str] = None,
        RequestTemplates: Dict[str, str] = None,
        ResponseParameters: Dict[str, Dict[str, str]] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
        TlsConfig: TlsConfigInputTypeDef = None,
    ) -> CreateIntegrationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-integration)
        """

    def create_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: ContentHandlingStrategy = None,
        ResponseParameters: Dict[str, str] = None,
        ResponseTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
    ) -> CreateIntegrationResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-integration-response)
        """

    def create_model(
        self, ApiId: str, Name: str, Schema: str, ContentType: str = None, Description: str = None
    ) -> CreateModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-model)
        """

    def create_route(
        self,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[str] = None,
        AuthorizationType: AuthorizationType = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, str] = None,
        RequestParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> CreateRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-route)
        """

    def create_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, str] = None,
        ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
    ) -> CreateRouteResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_route_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-route-response)
        """

    def create_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: "AccessLogSettingsTypeDef" = None,
        AutoDeploy: bool = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: "RouteSettingsTypeDef" = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, "RouteSettingsTypeDef"] = None,
        StageVariables: Dict[str, str] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateStageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-stage)
        """

    def create_vpc_link(
        self,
        Name: str,
        SubnetIds: List[str],
        SecurityGroupIds: List[str] = None,
        Tags: Dict[str, str] = None,
    ) -> CreateVpcLinkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.create_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#create-vpc-link)
        """

    def delete_access_log_settings(self, ApiId: str, StageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_access_log_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-access-log-settings)
        """

    def delete_api(self, ApiId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-api)
        """

    def delete_api_mapping(self, ApiMappingId: str, DomainName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_api_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-api-mapping)
        """

    def delete_authorizer(self, ApiId: str, AuthorizerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-authorizer)
        """

    def delete_cors_configuration(self, ApiId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_cors_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-cors-configuration)
        """

    def delete_deployment(self, ApiId: str, DeploymentId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-deployment)
        """

    def delete_domain_name(self, DomainName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-domain-name)
        """

    def delete_integration(self, ApiId: str, IntegrationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-integration)
        """

    def delete_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-integration-response)
        """

    def delete_model(self, ApiId: str, ModelId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-model)
        """

    def delete_route(self, ApiId: str, RouteId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-route)
        """

    def delete_route_request_parameter(
        self, ApiId: str, RequestParameterKey: str, RouteId: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_request_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-route-request-parameter)
        """

    def delete_route_response(self, ApiId: str, RouteId: str, RouteResponseId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-route-response)
        """

    def delete_route_settings(self, ApiId: str, RouteKey: str, StageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_route_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-route-settings)
        """

    def delete_stage(self, ApiId: str, StageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-stage)
        """

    def delete_vpc_link(self, VpcLinkId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.delete_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#delete-vpc-link)
        """

    def export_api(
        self,
        ApiId: str,
        OutputType: JSONYAMLType,
        Specification: Literal["OAS30"],
        ExportVersion: str = None,
        IncludeExtensions: bool = None,
        StageName: str = None,
    ) -> ExportApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.export_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#export-api)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#generate-presigned-url)
        """

    def get_api(self, ApiId: str) -> GetApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-api)
        """

    def get_api_mapping(self, ApiMappingId: str, DomainName: str) -> GetApiMappingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-api-mapping)
        """

    def get_api_mappings(
        self, DomainName: str, MaxResults: str = None, NextToken: str = None
    ) -> GetApiMappingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_api_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-api-mappings)
        """

    def get_apis(self, MaxResults: str = None, NextToken: str = None) -> GetApisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_apis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-apis)
        """

    def get_authorizer(self, ApiId: str, AuthorizerId: str) -> GetAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-authorizer)
        """

    def get_authorizers(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetAuthorizersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_authorizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-authorizers)
        """

    def get_deployment(self, ApiId: str, DeploymentId: str) -> GetDeploymentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-deployment)
        """

    def get_deployments(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetDeploymentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-deployments)
        """

    def get_domain_name(self, DomainName: str) -> GetDomainNameResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-domain-name)
        """

    def get_domain_names(
        self, MaxResults: str = None, NextToken: str = None
    ) -> GetDomainNamesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-domain-names)
        """

    def get_integration(self, ApiId: str, IntegrationId: str) -> GetIntegrationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-integration)
        """

    def get_integration_response(
        self, ApiId: str, IntegrationId: str, IntegrationResponseId: str
    ) -> GetIntegrationResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-integration-response)
        """

    def get_integration_responses(
        self, ApiId: str, IntegrationId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetIntegrationResponsesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integration_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-integration-responses)
        """

    def get_integrations(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetIntegrationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_integrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-integrations)
        """

    def get_model(self, ApiId: str, ModelId: str) -> GetModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-model)
        """

    def get_model_template(self, ApiId: str, ModelId: str) -> GetModelTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_model_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-model-template)
        """

    def get_models(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-models)
        """

    def get_route(self, ApiId: str, RouteId: str) -> GetRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-route)
        """

    def get_route_response(
        self, ApiId: str, RouteId: str, RouteResponseId: str
    ) -> GetRouteResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-route-response)
        """

    def get_route_responses(
        self, ApiId: str, RouteId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetRouteResponsesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_route_responses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-route-responses)
        """

    def get_routes(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetRoutesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-routes)
        """

    def get_stage(self, ApiId: str, StageName: str) -> GetStageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-stage)
        """

    def get_stages(
        self, ApiId: str, MaxResults: str = None, NextToken: str = None
    ) -> GetStagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_stages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-stages)
        """

    def get_tags(self, ResourceArn: str) -> GetTagsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-tags)
        """

    def get_vpc_link(self, VpcLinkId: str) -> GetVpcLinkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-vpc-link)
        """

    def get_vpc_links(
        self, MaxResults: str = None, NextToken: str = None
    ) -> GetVpcLinksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.get_vpc_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#get-vpc-links)
        """

    def import_api(
        self, Body: str, Basepath: str = None, FailOnWarnings: bool = None
    ) -> ImportApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.import_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#import-api)
        """

    def reimport_api(
        self, ApiId: str, Body: str, Basepath: str = None, FailOnWarnings: bool = None
    ) -> ReimportApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.reimport_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#reimport-api)
        """

    def reset_authorizers_cache(self, ApiId: str, StageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.reset_authorizers_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#reset-authorizers-cache)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#untag-resource)
        """

    def update_api(
        self,
        ApiId: str,
        ApiKeySelectionExpression: str = None,
        CorsConfiguration: "CorsTypeDef" = None,
        CredentialsArn: str = None,
        Description: str = None,
        DisableSchemaValidation: bool = None,
        DisableExecuteApiEndpoint: bool = None,
        Name: str = None,
        RouteKey: str = None,
        RouteSelectionExpression: str = None,
        Target: str = None,
        Version: str = None,
    ) -> UpdateApiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-api)
        """

    def update_api_mapping(
        self,
        ApiId: str,
        ApiMappingId: str,
        DomainName: str,
        ApiMappingKey: str = None,
        Stage: str = None,
    ) -> UpdateApiMappingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_api_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-api-mapping)
        """

    def update_authorizer(
        self,
        ApiId: str,
        AuthorizerId: str,
        AuthorizerCredentialsArn: str = None,
        AuthorizerPayloadFormatVersion: str = None,
        AuthorizerResultTtlInSeconds: int = None,
        AuthorizerType: AuthorizerType = None,
        AuthorizerUri: str = None,
        EnableSimpleResponses: bool = None,
        IdentitySource: List[str] = None,
        IdentityValidationExpression: str = None,
        JwtConfiguration: "JWTConfigurationTypeDef" = None,
        Name: str = None,
    ) -> UpdateAuthorizerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_authorizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-authorizer)
        """

    def update_deployment(
        self, ApiId: str, DeploymentId: str, Description: str = None
    ) -> UpdateDeploymentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-deployment)
        """

    def update_domain_name(
        self,
        DomainName: str,
        DomainNameConfigurations: List["DomainNameConfigurationTypeDef"] = None,
        MutualTlsAuthentication: MutualTlsAuthenticationInputTypeDef = None,
    ) -> UpdateDomainNameResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_domain_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-domain-name)
        """

    def update_integration(
        self,
        ApiId: str,
        IntegrationId: str,
        ConnectionId: str = None,
        ConnectionType: ConnectionType = None,
        ContentHandlingStrategy: ContentHandlingStrategy = None,
        CredentialsArn: str = None,
        Description: str = None,
        IntegrationMethod: str = None,
        IntegrationSubtype: str = None,
        IntegrationType: IntegrationType = None,
        IntegrationUri: str = None,
        PassthroughBehavior: PassthroughBehavior = None,
        PayloadFormatVersion: str = None,
        RequestParameters: Dict[str, str] = None,
        RequestTemplates: Dict[str, str] = None,
        ResponseParameters: Dict[str, Dict[str, str]] = None,
        TemplateSelectionExpression: str = None,
        TimeoutInMillis: int = None,
        TlsConfig: TlsConfigInputTypeDef = None,
    ) -> UpdateIntegrationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-integration)
        """

    def update_integration_response(
        self,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseId: str,
        ContentHandlingStrategy: ContentHandlingStrategy = None,
        IntegrationResponseKey: str = None,
        ResponseParameters: Dict[str, str] = None,
        ResponseTemplates: Dict[str, str] = None,
        TemplateSelectionExpression: str = None,
    ) -> UpdateIntegrationResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_integration_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-integration-response)
        """

    def update_model(
        self,
        ApiId: str,
        ModelId: str,
        ContentType: str = None,
        Description: str = None,
        Name: str = None,
        Schema: str = None,
    ) -> UpdateModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-model)
        """

    def update_route(
        self,
        ApiId: str,
        RouteId: str,
        ApiKeyRequired: bool = None,
        AuthorizationScopes: List[str] = None,
        AuthorizationType: AuthorizationType = None,
        AuthorizerId: str = None,
        ModelSelectionExpression: str = None,
        OperationName: str = None,
        RequestModels: Dict[str, str] = None,
        RequestParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
        RouteKey: str = None,
        RouteResponseSelectionExpression: str = None,
        Target: str = None,
    ) -> UpdateRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-route)
        """

    def update_route_response(
        self,
        ApiId: str,
        RouteId: str,
        RouteResponseId: str,
        ModelSelectionExpression: str = None,
        ResponseModels: Dict[str, str] = None,
        ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"] = None,
        RouteResponseKey: str = None,
    ) -> UpdateRouteResponseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_route_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-route-response)
        """

    def update_stage(
        self,
        ApiId: str,
        StageName: str,
        AccessLogSettings: "AccessLogSettingsTypeDef" = None,
        AutoDeploy: bool = None,
        ClientCertificateId: str = None,
        DefaultRouteSettings: "RouteSettingsTypeDef" = None,
        DeploymentId: str = None,
        Description: str = None,
        RouteSettings: Dict[str, "RouteSettingsTypeDef"] = None,
        StageVariables: Dict[str, str] = None,
    ) -> UpdateStageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-stage)
        """

    def update_vpc_link(self, VpcLinkId: str, Name: str = None) -> UpdateVpcLinkResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Client.update_vpc_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/client.html#update-vpc-link)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_apis"]) -> GetApisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetApis)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getapispaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_authorizers"]) -> GetAuthorizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetAuthorizers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getauthorizerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_deployments"]) -> GetDeploymentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDeployments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdeploymentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_domain_names"]) -> GetDomainNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetDomainNames)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getdomainnamespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_integration_responses"]
    ) -> GetIntegrationResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrationResponses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationresponsespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_integrations"]
    ) -> GetIntegrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetIntegrations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getintegrationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_models"]) -> GetModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetModels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getmodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_route_responses"]
    ) -> GetRouteResponsesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRouteResponses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getrouteresponsespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_routes"]) -> GetRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetRoutes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getroutespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_stages"]) -> GetStagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/apigatewayv2.html#ApiGatewayV2.Paginator.GetStages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/paginators.html#getstagespaginator)
        """
