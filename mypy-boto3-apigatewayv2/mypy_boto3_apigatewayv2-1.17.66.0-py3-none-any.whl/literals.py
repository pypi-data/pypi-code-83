"""
Type annotations for apigatewayv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/literals.html)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.literals import AuthorizationType

    data: AuthorizationType = "AWS_IAM"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AuthorizationType",
    "AuthorizerType",
    "ConnectionType",
    "ContentHandlingStrategy",
    "DeploymentStatus",
    "DomainNameStatus",
    "EndpointType",
    "GetApisPaginatorName",
    "GetAuthorizersPaginatorName",
    "GetDeploymentsPaginatorName",
    "GetDomainNamesPaginatorName",
    "GetIntegrationResponsesPaginatorName",
    "GetIntegrationsPaginatorName",
    "GetModelsPaginatorName",
    "GetRouteResponsesPaginatorName",
    "GetRoutesPaginatorName",
    "GetStagesPaginatorName",
    "IntegrationType",
    "JSONYAMLType",
    "LoggingLevel",
    "OAS30Type",
    "PassthroughBehavior",
    "ProtocolType",
    "SecurityPolicy",
    "VpcLinkStatus",
    "VpcLinkVersion",
)


AuthorizationType = Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"]
AuthorizerType = Literal["JWT", "REQUEST"]
ConnectionType = Literal["INTERNET", "VPC_LINK"]
ContentHandlingStrategy = Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
DeploymentStatus = Literal["DEPLOYED", "FAILED", "PENDING"]
DomainNameStatus = Literal["AVAILABLE", "UPDATING"]
EndpointType = Literal["EDGE", "REGIONAL"]
GetApisPaginatorName = Literal["get_apis"]
GetAuthorizersPaginatorName = Literal["get_authorizers"]
GetDeploymentsPaginatorName = Literal["get_deployments"]
GetDomainNamesPaginatorName = Literal["get_domain_names"]
GetIntegrationResponsesPaginatorName = Literal["get_integration_responses"]
GetIntegrationsPaginatorName = Literal["get_integrations"]
GetModelsPaginatorName = Literal["get_models"]
GetRouteResponsesPaginatorName = Literal["get_route_responses"]
GetRoutesPaginatorName = Literal["get_routes"]
GetStagesPaginatorName = Literal["get_stages"]
IntegrationType = Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
JSONYAMLType = Literal["JSON", "YAML"]
LoggingLevel = Literal["ERROR", "INFO", "OFF"]
OAS30Type = Literal["OAS30"]
PassthroughBehavior = Literal["NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"]
ProtocolType = Literal["HTTP", "WEBSOCKET"]
SecurityPolicy = Literal["TLS_1_0", "TLS_1_2"]
VpcLinkStatus = Literal["AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"]
VpcLinkVersion = Literal["V2"]
