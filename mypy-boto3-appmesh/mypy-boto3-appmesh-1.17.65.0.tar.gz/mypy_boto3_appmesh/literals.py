"""
Type annotations for appmesh service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/literals.html)

Usage::

    ```python
    from mypy_boto3_appmesh.literals import DurationUnit

    data: DurationUnit = "ms"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DurationUnit",
    "EgressFilterType",
    "GatewayRouteStatusCode",
    "GrpcRetryPolicyEvent",
    "HttpMethod",
    "HttpScheme",
    "ListGatewayRoutesPaginatorName",
    "ListMeshesPaginatorName",
    "ListRoutesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListVirtualGatewaysPaginatorName",
    "ListVirtualNodesPaginatorName",
    "ListVirtualRoutersPaginatorName",
    "ListVirtualServicesPaginatorName",
    "ListenerTlsMode",
    "MeshStatusCode",
    "PortProtocol",
    "RouteStatusCode",
    "TcpRetryPolicyEvent",
    "VirtualGatewayListenerTlsMode",
    "VirtualGatewayPortProtocol",
    "VirtualGatewayStatusCode",
    "VirtualNodeStatusCode",
    "VirtualRouterStatusCode",
    "VirtualServiceStatusCode",
)


DurationUnit = Literal["ms", "s"]
EgressFilterType = Literal["ALLOW_ALL", "DROP_ALL"]
GatewayRouteStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
GrpcRetryPolicyEvent = Literal[
    "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
]
HttpMethod = Literal["CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT", "TRACE"]
HttpScheme = Literal["http", "https"]
ListGatewayRoutesPaginatorName = Literal["list_gateway_routes"]
ListMeshesPaginatorName = Literal["list_meshes"]
ListRoutesPaginatorName = Literal["list_routes"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListVirtualGatewaysPaginatorName = Literal["list_virtual_gateways"]
ListVirtualNodesPaginatorName = Literal["list_virtual_nodes"]
ListVirtualRoutersPaginatorName = Literal["list_virtual_routers"]
ListVirtualServicesPaginatorName = Literal["list_virtual_services"]
ListenerTlsMode = Literal["DISABLED", "PERMISSIVE", "STRICT"]
MeshStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
PortProtocol = Literal["grpc", "http", "http2", "tcp"]
RouteStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
TcpRetryPolicyEvent = Literal["connection-error"]
VirtualGatewayListenerTlsMode = Literal["DISABLED", "PERMISSIVE", "STRICT"]
VirtualGatewayPortProtocol = Literal["grpc", "http", "http2"]
VirtualGatewayStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
VirtualNodeStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
VirtualRouterStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
VirtualServiceStatusCode = Literal["ACTIVE", "DELETED", "INACTIVE"]
