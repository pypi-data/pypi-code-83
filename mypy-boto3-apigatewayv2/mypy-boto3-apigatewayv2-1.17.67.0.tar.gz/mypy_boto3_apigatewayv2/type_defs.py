"""
Type annotations for apigatewayv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_apigatewayv2.literals import (
    AuthorizationType,
    AuthorizerType,
    ConnectionType,
    ContentHandlingStrategy,
    DeploymentStatus,
    DomainNameStatus,
    EndpointType,
    IntegrationType,
    LoggingLevel,
    PassthroughBehavior,
    ProtocolType,
    SecurityPolicy,
    VpcLinkStatus,
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
    "AccessLogSettingsTypeDef",
    "ApiMappingTypeDef",
    "ApiTypeDef",
    "AuthorizerTypeDef",
    "CorsTypeDef",
    "CreateApiMappingResponseTypeDef",
    "CreateApiResponseTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDomainNameResponseTypeDef",
    "CreateIntegrationResponseResponseTypeDef",
    "CreateIntegrationResultTypeDef",
    "CreateModelResponseTypeDef",
    "CreateRouteResponseResponseTypeDef",
    "CreateRouteResultTypeDef",
    "CreateStageResponseTypeDef",
    "CreateVpcLinkResponseTypeDef",
    "DeploymentTypeDef",
    "DomainNameConfigurationTypeDef",
    "DomainNameTypeDef",
    "ExportApiResponseTypeDef",
    "GetApiMappingResponseTypeDef",
    "GetApiMappingsResponseTypeDef",
    "GetApiResponseTypeDef",
    "GetApisResponseTypeDef",
    "GetAuthorizerResponseTypeDef",
    "GetAuthorizersResponseTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetDeploymentsResponseTypeDef",
    "GetDomainNameResponseTypeDef",
    "GetDomainNamesResponseTypeDef",
    "GetIntegrationResponseResponseTypeDef",
    "GetIntegrationResponsesResponseTypeDef",
    "GetIntegrationResultTypeDef",
    "GetIntegrationsResponseTypeDef",
    "GetModelResponseTypeDef",
    "GetModelTemplateResponseTypeDef",
    "GetModelsResponseTypeDef",
    "GetRouteResponseResponseTypeDef",
    "GetRouteResponsesResponseTypeDef",
    "GetRouteResultTypeDef",
    "GetRoutesResponseTypeDef",
    "GetStageResponseTypeDef",
    "GetStagesResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetVpcLinkResponseTypeDef",
    "GetVpcLinksResponseTypeDef",
    "ImportApiResponseTypeDef",
    "IntegrationResponseTypeDef",
    "IntegrationTypeDef",
    "JWTConfigurationTypeDef",
    "ModelTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ReimportApiResponseTypeDef",
    "RouteResponseTypeDef",
    "RouteSettingsTypeDef",
    "RouteTypeDef",
    "StageTypeDef",
    "TlsConfigInputTypeDef",
    "TlsConfigTypeDef",
    "UpdateApiMappingResponseTypeDef",
    "UpdateApiResponseTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateDeploymentResponseTypeDef",
    "UpdateDomainNameResponseTypeDef",
    "UpdateIntegrationResponseResponseTypeDef",
    "UpdateIntegrationResultTypeDef",
    "UpdateModelResponseTypeDef",
    "UpdateRouteResponseResponseTypeDef",
    "UpdateRouteResultTypeDef",
    "UpdateStageResponseTypeDef",
    "UpdateVpcLinkResponseTypeDef",
    "VpcLinkTypeDef",
)


class AccessLogSettingsTypeDef(TypedDict, total=False):
    DestinationArn: str
    Format: str


class _RequiredApiMappingTypeDef(TypedDict):
    ApiId: str
    Stage: str


class ApiMappingTypeDef(_RequiredApiMappingTypeDef, total=False):
    ApiMappingId: str
    ApiMappingKey: str


class _RequiredApiTypeDef(TypedDict):
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str


class ApiTypeDef(_RequiredApiTypeDef, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class _RequiredAuthorizerTypeDef(TypedDict):
    Name: str


class AuthorizerTypeDef(_RequiredAuthorizerTypeDef, total=False):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: "JWTConfigurationTypeDef"


class CorsTypeDef(TypedDict, total=False):
    AllowCredentials: bool
    AllowHeaders: List[str]
    AllowMethods: List[str]
    AllowOrigins: List[str]
    ExposeHeaders: List[str]
    MaxAge: int


class CreateApiMappingResponseTypeDef(TypedDict, total=False):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str


class CreateApiResponseTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class CreateAuthorizerResponseTypeDef(TypedDict, total=False):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: "JWTConfigurationTypeDef"
    Name: str


class CreateDeploymentResponseTypeDef(TypedDict, total=False):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatus
    DeploymentStatusMessage: str
    Description: str


class CreateDomainNameResponseTypeDef(TypedDict, total=False):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"]
    MutualTlsAuthentication: "MutualTlsAuthenticationTypeDef"
    Tags: Dict[str, str]


class CreateIntegrationResponseResponseTypeDef(TypedDict, total=False):
    ContentHandlingStrategy: ContentHandlingStrategy
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str


class CreateIntegrationResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionType
    ContentHandlingStrategy: ContentHandlingStrategy
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehavior
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: "TlsConfigTypeDef"


class CreateModelResponseTypeDef(TypedDict, total=False):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str


class CreateRouteResponseResponseTypeDef(TypedDict, total=False):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteResponseId: str
    RouteResponseKey: str


class CreateRouteResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str


class CreateStageResponseTypeDef(TypedDict, total=False):
    AccessLogSettings: "AccessLogSettingsTypeDef"
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: "RouteSettingsTypeDef"
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, "RouteSettingsTypeDef"]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]


class CreateVpcLinkResponseTypeDef(TypedDict, total=False):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatus
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]


class DeploymentTypeDef(TypedDict, total=False):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatus
    DeploymentStatusMessage: str
    Description: str


class DomainNameConfigurationTypeDef(TypedDict, total=False):
    ApiGatewayDomainName: str
    CertificateArn: str
    CertificateName: str
    CertificateUploadDate: datetime
    DomainNameStatus: DomainNameStatus
    DomainNameStatusMessage: str
    EndpointType: EndpointType
    HostedZoneId: str
    SecurityPolicy: SecurityPolicy


class _RequiredDomainNameTypeDef(TypedDict):
    DomainName: str


class DomainNameTypeDef(_RequiredDomainNameTypeDef, total=False):
    ApiMappingSelectionExpression: str
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"]
    MutualTlsAuthentication: "MutualTlsAuthenticationTypeDef"
    Tags: Dict[str, str]


class ExportApiResponseTypeDef(TypedDict, total=False):
    body: Union[bytes, IO[bytes]]


class GetApiMappingResponseTypeDef(TypedDict, total=False):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str


class GetApiMappingsResponseTypeDef(TypedDict, total=False):
    Items: List["ApiMappingTypeDef"]
    NextToken: str


class GetApiResponseTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class GetApisResponseTypeDef(TypedDict, total=False):
    Items: List["ApiTypeDef"]
    NextToken: str


class GetAuthorizerResponseTypeDef(TypedDict, total=False):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: "JWTConfigurationTypeDef"
    Name: str


class GetAuthorizersResponseTypeDef(TypedDict, total=False):
    Items: List["AuthorizerTypeDef"]
    NextToken: str


class GetDeploymentResponseTypeDef(TypedDict, total=False):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatus
    DeploymentStatusMessage: str
    Description: str


class GetDeploymentsResponseTypeDef(TypedDict, total=False):
    Items: List["DeploymentTypeDef"]
    NextToken: str


class GetDomainNameResponseTypeDef(TypedDict, total=False):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"]
    MutualTlsAuthentication: "MutualTlsAuthenticationTypeDef"
    Tags: Dict[str, str]


class GetDomainNamesResponseTypeDef(TypedDict, total=False):
    Items: List["DomainNameTypeDef"]
    NextToken: str


class GetIntegrationResponseResponseTypeDef(TypedDict, total=False):
    ContentHandlingStrategy: ContentHandlingStrategy
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str


class GetIntegrationResponsesResponseTypeDef(TypedDict, total=False):
    Items: List["IntegrationResponseTypeDef"]
    NextToken: str


class GetIntegrationResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionType
    ContentHandlingStrategy: ContentHandlingStrategy
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehavior
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: "TlsConfigTypeDef"


class GetIntegrationsResponseTypeDef(TypedDict, total=False):
    Items: List["IntegrationTypeDef"]
    NextToken: str


class GetModelResponseTypeDef(TypedDict, total=False):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str


class GetModelTemplateResponseTypeDef(TypedDict, total=False):
    Value: str


class GetModelsResponseTypeDef(TypedDict, total=False):
    Items: List["ModelTypeDef"]
    NextToken: str


class GetRouteResponseResponseTypeDef(TypedDict, total=False):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteResponseId: str
    RouteResponseKey: str


class GetRouteResponsesResponseTypeDef(TypedDict, total=False):
    Items: List["RouteResponseTypeDef"]
    NextToken: str


class GetRouteResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str


class GetRoutesResponseTypeDef(TypedDict, total=False):
    Items: List["RouteTypeDef"]
    NextToken: str


class GetStageResponseTypeDef(TypedDict, total=False):
    AccessLogSettings: "AccessLogSettingsTypeDef"
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: "RouteSettingsTypeDef"
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, "RouteSettingsTypeDef"]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]


class GetStagesResponseTypeDef(TypedDict, total=False):
    Items: List["StageTypeDef"]
    NextToken: str


class GetTagsResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class GetVpcLinkResponseTypeDef(TypedDict, total=False):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatus
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]


class GetVpcLinksResponseTypeDef(TypedDict, total=False):
    Items: List["VpcLinkTypeDef"]
    NextToken: str


class ImportApiResponseTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class _RequiredIntegrationResponseTypeDef(TypedDict):
    IntegrationResponseKey: str


class IntegrationResponseTypeDef(_RequiredIntegrationResponseTypeDef, total=False):
    ContentHandlingStrategy: ContentHandlingStrategy
    IntegrationResponseId: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str


class IntegrationTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionType
    ContentHandlingStrategy: ContentHandlingStrategy
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehavior
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: "TlsConfigTypeDef"


class JWTConfigurationTypeDef(TypedDict, total=False):
    Audience: List[str]
    Issuer: str


class _RequiredModelTypeDef(TypedDict):
    Name: str


class ModelTypeDef(_RequiredModelTypeDef, total=False):
    ContentType: str
    Description: str
    ModelId: str
    Schema: str


class MutualTlsAuthenticationInputTypeDef(TypedDict, total=False):
    TruststoreUri: str
    TruststoreVersion: str


class MutualTlsAuthenticationTypeDef(TypedDict, total=False):
    TruststoreUri: str
    TruststoreVersion: str
    TruststoreWarnings: List[str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterConstraintsTypeDef(TypedDict, total=False):
    Required: bool


class ReimportApiResponseTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class _RequiredRouteResponseTypeDef(TypedDict):
    RouteResponseKey: str


class RouteResponseTypeDef(_RequiredRouteResponseTypeDef, total=False):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteResponseId: str


class RouteSettingsTypeDef(TypedDict, total=False):
    DataTraceEnabled: bool
    DetailedMetricsEnabled: bool
    LoggingLevel: LoggingLevel
    ThrottlingBurstLimit: int
    ThrottlingRateLimit: float


class _RequiredRouteTypeDef(TypedDict):
    RouteKey: str


class RouteTypeDef(_RequiredRouteTypeDef, total=False):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteId: str
    RouteResponseSelectionExpression: str
    Target: str


class _RequiredStageTypeDef(TypedDict):
    StageName: str


class StageTypeDef(_RequiredStageTypeDef, total=False):
    AccessLogSettings: "AccessLogSettingsTypeDef"
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: "RouteSettingsTypeDef"
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, "RouteSettingsTypeDef"]
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]


class TlsConfigInputTypeDef(TypedDict, total=False):
    ServerNameToVerify: str


class TlsConfigTypeDef(TypedDict, total=False):
    ServerNameToVerify: str


class UpdateApiMappingResponseTypeDef(TypedDict, total=False):
    ApiId: str
    ApiMappingId: str
    ApiMappingKey: str
    Stage: str


class UpdateApiResponseTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiGatewayManaged: bool
    ApiId: str
    ApiKeySelectionExpression: str
    CorsConfiguration: "CorsTypeDef"
    CreatedDate: datetime
    Description: str
    DisableSchemaValidation: bool
    DisableExecuteApiEndpoint: bool
    ImportInfo: List[str]
    Name: str
    ProtocolType: ProtocolType
    RouteSelectionExpression: str
    Tags: Dict[str, str]
    Version: str
    Warnings: List[str]


class UpdateAuthorizerResponseTypeDef(TypedDict, total=False):
    AuthorizerCredentialsArn: str
    AuthorizerId: str
    AuthorizerPayloadFormatVersion: str
    AuthorizerResultTtlInSeconds: int
    AuthorizerType: AuthorizerType
    AuthorizerUri: str
    EnableSimpleResponses: bool
    IdentitySource: List[str]
    IdentityValidationExpression: str
    JwtConfiguration: "JWTConfigurationTypeDef"
    Name: str


class UpdateDeploymentResponseTypeDef(TypedDict, total=False):
    AutoDeployed: bool
    CreatedDate: datetime
    DeploymentId: str
    DeploymentStatus: DeploymentStatus
    DeploymentStatusMessage: str
    Description: str


class UpdateDomainNameResponseTypeDef(TypedDict, total=False):
    ApiMappingSelectionExpression: str
    DomainName: str
    DomainNameConfigurations: List["DomainNameConfigurationTypeDef"]
    MutualTlsAuthentication: "MutualTlsAuthenticationTypeDef"
    Tags: Dict[str, str]


class UpdateIntegrationResponseResponseTypeDef(TypedDict, total=False):
    ContentHandlingStrategy: ContentHandlingStrategy
    IntegrationResponseId: str
    IntegrationResponseKey: str
    ResponseParameters: Dict[str, str]
    ResponseTemplates: Dict[str, str]
    TemplateSelectionExpression: str


class UpdateIntegrationResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ConnectionId: str
    ConnectionType: ConnectionType
    ContentHandlingStrategy: ContentHandlingStrategy
    CredentialsArn: str
    Description: str
    IntegrationId: str
    IntegrationMethod: str
    IntegrationResponseSelectionExpression: str
    IntegrationSubtype: str
    IntegrationType: IntegrationType
    IntegrationUri: str
    PassthroughBehavior: PassthroughBehavior
    PayloadFormatVersion: str
    RequestParameters: Dict[str, str]
    RequestTemplates: Dict[str, str]
    ResponseParameters: Dict[str, Dict[str, str]]
    TemplateSelectionExpression: str
    TimeoutInMillis: int
    TlsConfig: "TlsConfigTypeDef"


class UpdateModelResponseTypeDef(TypedDict, total=False):
    ContentType: str
    Description: str
    ModelId: str
    Name: str
    Schema: str


class UpdateRouteResponseResponseTypeDef(TypedDict, total=False):
    ModelSelectionExpression: str
    ResponseModels: Dict[str, str]
    ResponseParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteResponseId: str
    RouteResponseKey: str


class UpdateRouteResultTypeDef(TypedDict, total=False):
    ApiGatewayManaged: bool
    ApiKeyRequired: bool
    AuthorizationScopes: List[str]
    AuthorizationType: AuthorizationType
    AuthorizerId: str
    ModelSelectionExpression: str
    OperationName: str
    RequestModels: Dict[str, str]
    RequestParameters: Dict[str, "ParameterConstraintsTypeDef"]
    RouteId: str
    RouteKey: str
    RouteResponseSelectionExpression: str
    Target: str


class UpdateStageResponseTypeDef(TypedDict, total=False):
    AccessLogSettings: "AccessLogSettingsTypeDef"
    ApiGatewayManaged: bool
    AutoDeploy: bool
    ClientCertificateId: str
    CreatedDate: datetime
    DefaultRouteSettings: "RouteSettingsTypeDef"
    DeploymentId: str
    Description: str
    LastDeploymentStatusMessage: str
    LastUpdatedDate: datetime
    RouteSettings: Dict[str, "RouteSettingsTypeDef"]
    StageName: str
    StageVariables: Dict[str, str]
    Tags: Dict[str, str]


class UpdateVpcLinkResponseTypeDef(TypedDict, total=False):
    CreatedDate: datetime
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    Tags: Dict[str, str]
    VpcLinkId: str
    VpcLinkStatus: VpcLinkStatus
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]


class _RequiredVpcLinkTypeDef(TypedDict):
    Name: str
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcLinkId: str


class VpcLinkTypeDef(_RequiredVpcLinkTypeDef, total=False):
    CreatedDate: datetime
    Tags: Dict[str, str]
    VpcLinkStatus: VpcLinkStatus
    VpcLinkStatusMessage: str
    VpcLinkVersion: Literal["V2"]
