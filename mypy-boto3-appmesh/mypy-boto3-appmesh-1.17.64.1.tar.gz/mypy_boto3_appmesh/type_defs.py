"""
Type annotations for appmesh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_appmesh.literals import (
    DurationUnit,
    EgressFilterType,
    GatewayRouteStatusCode,
    GrpcRetryPolicyEvent,
    HttpMethod,
    HttpScheme,
    ListenerTlsMode,
    MeshStatusCode,
    PortProtocol,
    RouteStatusCode,
    VirtualGatewayListenerTlsMode,
    VirtualGatewayPortProtocol,
    VirtualGatewayStatusCode,
    VirtualNodeStatusCode,
    VirtualRouterStatusCode,
    VirtualServiceStatusCode,
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
    "AccessLogTypeDef",
    "AwsCloudMapInstanceAttributeTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "BackendDefaultsTypeDef",
    "BackendTypeDef",
    "ClientPolicyTlsTypeDef",
    "ClientPolicyTypeDef",
    "ClientTlsCertificateTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "CreateMeshOutputTypeDef",
    "CreateRouteOutputTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DeleteMeshOutputTypeDef",
    "DeleteRouteOutputTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "DescribeMeshOutputTypeDef",
    "DescribeRouteOutputTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcRouteActionTypeDef",
    "GrpcRouteMatchTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataTypeDef",
    "GrpcRouteTypeDef",
    "GrpcTimeoutTypeDef",
    "HeaderMatchMethodTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "ListenerTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
    "MeshSpecTypeDef",
    "MeshStatusTypeDef",
    "OutlierDetectionTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "ResourceMetadataTypeDef",
    "ResponseMetadata",
    "RouteDataTypeDef",
    "RouteRefTypeDef",
    "RouteSpecTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TagRefTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "UpdateMeshOutputTypeDef",
    "UpdateRouteOutputTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualNodeDataTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeRefTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualRouterDataTypeDef",
    "VirtualRouterListenerTypeDef",
    "VirtualRouterRefTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualRouterSpecTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualServiceDataTypeDef",
    "VirtualServiceProviderTypeDef",
    "VirtualServiceRefTypeDef",
    "VirtualServiceSpecTypeDef",
    "VirtualServiceStatusTypeDef",
    "WeightedTargetTypeDef",
)


class AccessLogTypeDef(TypedDict, total=False):
    file: "FileAccessLogTypeDef"


class AwsCloudMapInstanceAttributeTypeDef(TypedDict):
    key: str
    value: str


class _RequiredAwsCloudMapServiceDiscoveryTypeDef(TypedDict):
    namespaceName: str
    serviceName: str


class AwsCloudMapServiceDiscoveryTypeDef(_RequiredAwsCloudMapServiceDiscoveryTypeDef, total=False):
    attributes: List["AwsCloudMapInstanceAttributeTypeDef"]


class BackendDefaultsTypeDef(TypedDict, total=False):
    clientPolicy: "ClientPolicyTypeDef"


class BackendTypeDef(TypedDict, total=False):
    virtualService: "VirtualServiceBackendTypeDef"


class _RequiredClientPolicyTlsTypeDef(TypedDict):
    validation: "TlsValidationContextTypeDef"


class ClientPolicyTlsTypeDef(_RequiredClientPolicyTlsTypeDef, total=False):
    certificate: "ClientTlsCertificateTypeDef"
    enforce: bool
    ports: List[int]


class ClientPolicyTypeDef(TypedDict, total=False):
    tls: "ClientPolicyTlsTypeDef"


class ClientTlsCertificateTypeDef(TypedDict, total=False):
    file: "ListenerTlsFileCertificateTypeDef"
    sds: "ListenerTlsSdsCertificateTypeDef"


class CreateGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: "GatewayRouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateMeshOutputTypeDef(TypedDict):
    mesh: "MeshDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateRouteOutputTypeDef(TypedDict):
    route: "RouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: "VirtualGatewayDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: "VirtualNodeDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: "VirtualRouterDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateVirtualServiceOutputTypeDef(TypedDict):
    virtualService: "VirtualServiceDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: "GatewayRouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteMeshOutputTypeDef(TypedDict):
    mesh: "MeshDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteRouteOutputTypeDef(TypedDict):
    route: "RouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: "VirtualGatewayDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: "VirtualNodeDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: "VirtualRouterDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteVirtualServiceOutputTypeDef(TypedDict):
    virtualService: "VirtualServiceDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: "GatewayRouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeMeshOutputTypeDef(TypedDict):
    mesh: "MeshDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeRouteOutputTypeDef(TypedDict):
    route: "RouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: "VirtualGatewayDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: "VirtualNodeDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: "VirtualRouterDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeVirtualServiceOutputTypeDef(TypedDict):
    virtualService: "VirtualServiceDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DnsServiceDiscoveryTypeDef(TypedDict):
    hostname: str


class DurationTypeDef(TypedDict, total=False):
    unit: DurationUnit
    value: int


EgressFilterTypeDef = TypedDict("EgressFilterTypeDef", {"type": EgressFilterType})


class FileAccessLogTypeDef(TypedDict):
    path: str


class GatewayRouteDataTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "GatewayRouteSpecTypeDef"
    status: "GatewayRouteStatusTypeDef"
    virtualGatewayName: str


class GatewayRouteRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    gatewayRouteName: str
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str


class GatewayRouteSpecTypeDef(TypedDict, total=False):
    grpcRoute: "GrpcGatewayRouteTypeDef"
    http2Route: "HttpGatewayRouteTypeDef"
    httpRoute: "HttpGatewayRouteTypeDef"


class GatewayRouteStatusTypeDef(TypedDict):
    status: GatewayRouteStatusCode


class GatewayRouteTargetTypeDef(TypedDict):
    virtualService: "GatewayRouteVirtualServiceTypeDef"


class GatewayRouteVirtualServiceTypeDef(TypedDict):
    virtualServiceName: str


class GrpcGatewayRouteActionTypeDef(TypedDict):
    target: "GatewayRouteTargetTypeDef"


class GrpcGatewayRouteMatchTypeDef(TypedDict, total=False):
    serviceName: str


class GrpcGatewayRouteTypeDef(TypedDict):
    action: "GrpcGatewayRouteActionTypeDef"
    match: "GrpcGatewayRouteMatchTypeDef"


class _RequiredGrpcRetryPolicyTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: "DurationTypeDef"


class GrpcRetryPolicyTypeDef(_RequiredGrpcRetryPolicyTypeDef, total=False):
    grpcRetryEvents: List[GrpcRetryPolicyEvent]
    httpRetryEvents: List[str]
    tcpRetryEvents: List[Literal["connection-error"]]


class GrpcRouteActionTypeDef(TypedDict):
    weightedTargets: List["WeightedTargetTypeDef"]


class GrpcRouteMatchTypeDef(TypedDict, total=False):
    metadata: List["GrpcRouteMetadataTypeDef"]
    methodName: str
    serviceName: str


GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {"exact": str, "prefix": str, "range": "MatchRangeTypeDef", "regex": str, "suffix": str},
    total=False,
)


class _RequiredGrpcRouteMetadataTypeDef(TypedDict):
    name: str


class GrpcRouteMetadataTypeDef(_RequiredGrpcRouteMetadataTypeDef, total=False):
    invert: bool
    match: "GrpcRouteMetadataMatchMethodTypeDef"


class _RequiredGrpcRouteTypeDef(TypedDict):
    action: "GrpcRouteActionTypeDef"
    match: "GrpcRouteMatchTypeDef"


class GrpcRouteTypeDef(_RequiredGrpcRouteTypeDef, total=False):
    retryPolicy: "GrpcRetryPolicyTypeDef"
    timeout: "GrpcTimeoutTypeDef"


class GrpcTimeoutTypeDef(TypedDict, total=False):
    idle: "DurationTypeDef"
    perRequest: "DurationTypeDef"


HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {"exact": str, "prefix": str, "range": "MatchRangeTypeDef", "regex": str, "suffix": str},
    total=False,
)


class _RequiredHealthCheckPolicyTypeDef(TypedDict):
    healthyThreshold: int
    intervalMillis: int
    protocol: PortProtocol
    timeoutMillis: int
    unhealthyThreshold: int


class HealthCheckPolicyTypeDef(_RequiredHealthCheckPolicyTypeDef, total=False):
    path: str
    port: int


class HttpGatewayRouteActionTypeDef(TypedDict):
    target: "GatewayRouteTargetTypeDef"


class HttpGatewayRouteMatchTypeDef(TypedDict):
    prefix: str


class HttpGatewayRouteTypeDef(TypedDict):
    action: "HttpGatewayRouteActionTypeDef"
    match: "HttpGatewayRouteMatchTypeDef"


class _RequiredHttpRetryPolicyTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: "DurationTypeDef"


class HttpRetryPolicyTypeDef(_RequiredHttpRetryPolicyTypeDef, total=False):
    httpRetryEvents: List[str]
    tcpRetryEvents: List[Literal["connection-error"]]


class HttpRouteActionTypeDef(TypedDict):
    weightedTargets: List["WeightedTargetTypeDef"]


class _RequiredHttpRouteHeaderTypeDef(TypedDict):
    name: str


class HttpRouteHeaderTypeDef(_RequiredHttpRouteHeaderTypeDef, total=False):
    invert: bool
    match: "HeaderMatchMethodTypeDef"


class _RequiredHttpRouteMatchTypeDef(TypedDict):
    prefix: str


class HttpRouteMatchTypeDef(_RequiredHttpRouteMatchTypeDef, total=False):
    headers: List["HttpRouteHeaderTypeDef"]
    method: HttpMethod
    scheme: HttpScheme


class _RequiredHttpRouteTypeDef(TypedDict):
    action: "HttpRouteActionTypeDef"
    match: "HttpRouteMatchTypeDef"


class HttpRouteTypeDef(_RequiredHttpRouteTypeDef, total=False):
    retryPolicy: "HttpRetryPolicyTypeDef"
    timeout: "HttpTimeoutTypeDef"


class HttpTimeoutTypeDef(TypedDict, total=False):
    idle: "DurationTypeDef"
    perRequest: "DurationTypeDef"


class ListGatewayRoutesOutputTypeDef(TypedDict):
    gatewayRoutes: List["GatewayRouteRefTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListMeshesOutputTypeDef(TypedDict):
    meshes: List["MeshRefTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRoutesOutputTypeDef(TypedDict):
    nextToken: str
    routes: List["RouteRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    nextToken: str
    tags: List["TagRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListVirtualGatewaysOutputTypeDef(TypedDict):
    nextToken: str
    virtualGateways: List["VirtualGatewayRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListVirtualNodesOutputTypeDef(TypedDict):
    nextToken: str
    virtualNodes: List["VirtualNodeRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListVirtualRoutersOutputTypeDef(TypedDict):
    nextToken: str
    virtualRouters: List["VirtualRouterRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListVirtualServicesOutputTypeDef(TypedDict):
    nextToken: str
    virtualServices: List["VirtualServiceRefTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListenerTimeoutTypeDef(TypedDict, total=False):
    grpc: "GrpcTimeoutTypeDef"
    http: "HttpTimeoutTypeDef"
    http2: "HttpTimeoutTypeDef"
    tcp: "TcpTimeoutTypeDef"


class ListenerTlsAcmCertificateTypeDef(TypedDict):
    certificateArn: str


class ListenerTlsCertificateTypeDef(TypedDict, total=False):
    acm: "ListenerTlsAcmCertificateTypeDef"
    file: "ListenerTlsFileCertificateTypeDef"
    sds: "ListenerTlsSdsCertificateTypeDef"


class ListenerTlsFileCertificateTypeDef(TypedDict):
    certificateChain: str
    privateKey: str


class ListenerTlsSdsCertificateTypeDef(TypedDict):
    secretName: str


class _RequiredListenerTlsTypeDef(TypedDict):
    certificate: "ListenerTlsCertificateTypeDef"
    mode: ListenerTlsMode


class ListenerTlsTypeDef(_RequiredListenerTlsTypeDef, total=False):
    validation: "ListenerTlsValidationContextTypeDef"


class ListenerTlsValidationContextTrustTypeDef(TypedDict, total=False):
    file: "TlsValidationContextFileTrustTypeDef"
    sds: "TlsValidationContextSdsTrustTypeDef"


class _RequiredListenerTlsValidationContextTypeDef(TypedDict):
    trust: "ListenerTlsValidationContextTrustTypeDef"


class ListenerTlsValidationContextTypeDef(
    _RequiredListenerTlsValidationContextTypeDef, total=False
):
    subjectAlternativeNames: "SubjectAlternativeNamesTypeDef"


class _RequiredListenerTypeDef(TypedDict):
    portMapping: "PortMappingTypeDef"


class ListenerTypeDef(_RequiredListenerTypeDef, total=False):
    connectionPool: "VirtualNodeConnectionPoolTypeDef"
    healthCheck: "HealthCheckPolicyTypeDef"
    outlierDetection: "OutlierDetectionTypeDef"
    timeout: "ListenerTimeoutTypeDef"
    tls: "ListenerTlsTypeDef"


class LoggingTypeDef(TypedDict, total=False):
    accessLog: "AccessLogTypeDef"


class MatchRangeTypeDef(TypedDict):
    end: int
    start: int


class MeshDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "MeshSpecTypeDef"
    status: "MeshStatusTypeDef"


class MeshRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int


class MeshSpecTypeDef(TypedDict, total=False):
    egressFilter: "EgressFilterTypeDef"


class MeshStatusTypeDef(TypedDict, total=False):
    status: MeshStatusCode


class OutlierDetectionTypeDef(TypedDict):
    baseEjectionDuration: "DurationTypeDef"
    interval: "DurationTypeDef"
    maxEjectionPercent: int
    maxServerErrors: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PortMappingTypeDef(TypedDict):
    port: int
    protocol: PortProtocol


class ResourceMetadataTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshOwner: str
    resourceOwner: str
    uid: str
    version: int


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RouteDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    routeName: str
    spec: "RouteSpecTypeDef"
    status: "RouteStatusTypeDef"
    virtualRouterName: str


class RouteRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    routeName: str
    version: int
    virtualRouterName: str


class RouteSpecTypeDef(TypedDict, total=False):
    grpcRoute: "GrpcRouteTypeDef"
    http2Route: "HttpRouteTypeDef"
    httpRoute: "HttpRouteTypeDef"
    priority: int
    tcpRoute: "TcpRouteTypeDef"


class RouteStatusTypeDef(TypedDict):
    status: RouteStatusCode


class ServiceDiscoveryTypeDef(TypedDict, total=False):
    awsCloudMap: "AwsCloudMapServiceDiscoveryTypeDef"
    dns: "DnsServiceDiscoveryTypeDef"


class SubjectAlternativeNameMatchersTypeDef(TypedDict):
    exact: List[str]


class SubjectAlternativeNamesTypeDef(TypedDict):
    match: "SubjectAlternativeNameMatchersTypeDef"


class TagRefTypeDef(TypedDict):
    key: str
    value: str


class TcpRouteActionTypeDef(TypedDict):
    weightedTargets: List["WeightedTargetTypeDef"]


class _RequiredTcpRouteTypeDef(TypedDict):
    action: "TcpRouteActionTypeDef"


class TcpRouteTypeDef(_RequiredTcpRouteTypeDef, total=False):
    timeout: "TcpTimeoutTypeDef"


class TcpTimeoutTypeDef(TypedDict, total=False):
    idle: "DurationTypeDef"


class TlsValidationContextAcmTrustTypeDef(TypedDict):
    certificateAuthorityArns: List[str]


class TlsValidationContextFileTrustTypeDef(TypedDict):
    certificateChain: str


class TlsValidationContextSdsTrustTypeDef(TypedDict):
    secretName: str


class TlsValidationContextTrustTypeDef(TypedDict, total=False):
    acm: "TlsValidationContextAcmTrustTypeDef"
    file: "TlsValidationContextFileTrustTypeDef"
    sds: "TlsValidationContextSdsTrustTypeDef"


class _RequiredTlsValidationContextTypeDef(TypedDict):
    trust: "TlsValidationContextTrustTypeDef"


class TlsValidationContextTypeDef(_RequiredTlsValidationContextTypeDef, total=False):
    subjectAlternativeNames: "SubjectAlternativeNamesTypeDef"


class UpdateGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: "GatewayRouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateMeshOutputTypeDef(TypedDict):
    mesh: "MeshDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateRouteOutputTypeDef(TypedDict):
    route: "RouteDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: "VirtualGatewayDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: "VirtualNodeDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: "VirtualRouterDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateVirtualServiceOutputTypeDef(TypedDict):
    virtualService: "VirtualServiceDataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class VirtualGatewayAccessLogTypeDef(TypedDict, total=False):
    file: "VirtualGatewayFileAccessLogTypeDef"


class VirtualGatewayBackendDefaultsTypeDef(TypedDict, total=False):
    clientPolicy: "VirtualGatewayClientPolicyTypeDef"


class _RequiredVirtualGatewayClientPolicyTlsTypeDef(TypedDict):
    validation: "VirtualGatewayTlsValidationContextTypeDef"


class VirtualGatewayClientPolicyTlsTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsTypeDef, total=False
):
    certificate: "VirtualGatewayClientTlsCertificateTypeDef"
    enforce: bool
    ports: List[int]


class VirtualGatewayClientPolicyTypeDef(TypedDict, total=False):
    tls: "VirtualGatewayClientPolicyTlsTypeDef"


class VirtualGatewayClientTlsCertificateTypeDef(TypedDict, total=False):
    file: "VirtualGatewayListenerTlsFileCertificateTypeDef"
    sds: "VirtualGatewayListenerTlsSdsCertificateTypeDef"


class VirtualGatewayConnectionPoolTypeDef(TypedDict, total=False):
    grpc: "VirtualGatewayGrpcConnectionPoolTypeDef"
    http: "VirtualGatewayHttpConnectionPoolTypeDef"
    http2: "VirtualGatewayHttp2ConnectionPoolTypeDef"


class VirtualGatewayDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "VirtualGatewaySpecTypeDef"
    status: "VirtualGatewayStatusTypeDef"
    virtualGatewayName: str


class VirtualGatewayFileAccessLogTypeDef(TypedDict):
    path: str


class VirtualGatewayGrpcConnectionPoolTypeDef(TypedDict):
    maxRequests: int


class _RequiredVirtualGatewayHealthCheckPolicyTypeDef(TypedDict):
    healthyThreshold: int
    intervalMillis: int
    protocol: VirtualGatewayPortProtocol
    timeoutMillis: int
    unhealthyThreshold: int


class VirtualGatewayHealthCheckPolicyTypeDef(
    _RequiredVirtualGatewayHealthCheckPolicyTypeDef, total=False
):
    path: str
    port: int


class VirtualGatewayHttp2ConnectionPoolTypeDef(TypedDict):
    maxRequests: int


class _RequiredVirtualGatewayHttpConnectionPoolTypeDef(TypedDict):
    maxConnections: int


class VirtualGatewayHttpConnectionPoolTypeDef(
    _RequiredVirtualGatewayHttpConnectionPoolTypeDef, total=False
):
    maxPendingRequests: int


class VirtualGatewayListenerTlsAcmCertificateTypeDef(TypedDict):
    certificateArn: str


class VirtualGatewayListenerTlsCertificateTypeDef(TypedDict, total=False):
    acm: "VirtualGatewayListenerTlsAcmCertificateTypeDef"
    file: "VirtualGatewayListenerTlsFileCertificateTypeDef"
    sds: "VirtualGatewayListenerTlsSdsCertificateTypeDef"


class VirtualGatewayListenerTlsFileCertificateTypeDef(TypedDict):
    certificateChain: str
    privateKey: str


class VirtualGatewayListenerTlsSdsCertificateTypeDef(TypedDict):
    secretName: str


class _RequiredVirtualGatewayListenerTlsTypeDef(TypedDict):
    certificate: "VirtualGatewayListenerTlsCertificateTypeDef"
    mode: VirtualGatewayListenerTlsMode


class VirtualGatewayListenerTlsTypeDef(_RequiredVirtualGatewayListenerTlsTypeDef, total=False):
    validation: "VirtualGatewayListenerTlsValidationContextTypeDef"


class VirtualGatewayListenerTlsValidationContextTrustTypeDef(TypedDict, total=False):
    file: "VirtualGatewayTlsValidationContextFileTrustTypeDef"
    sds: "VirtualGatewayTlsValidationContextSdsTrustTypeDef"


class _RequiredVirtualGatewayListenerTlsValidationContextTypeDef(TypedDict):
    trust: "VirtualGatewayListenerTlsValidationContextTrustTypeDef"


class VirtualGatewayListenerTlsValidationContextTypeDef(
    _RequiredVirtualGatewayListenerTlsValidationContextTypeDef, total=False
):
    subjectAlternativeNames: "SubjectAlternativeNamesTypeDef"


class _RequiredVirtualGatewayListenerTypeDef(TypedDict):
    portMapping: "VirtualGatewayPortMappingTypeDef"


class VirtualGatewayListenerTypeDef(_RequiredVirtualGatewayListenerTypeDef, total=False):
    connectionPool: "VirtualGatewayConnectionPoolTypeDef"
    healthCheck: "VirtualGatewayHealthCheckPolicyTypeDef"
    tls: "VirtualGatewayListenerTlsTypeDef"


class VirtualGatewayLoggingTypeDef(TypedDict, total=False):
    accessLog: "VirtualGatewayAccessLogTypeDef"


class VirtualGatewayPortMappingTypeDef(TypedDict):
    port: int
    protocol: VirtualGatewayPortProtocol


class VirtualGatewayRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str


class _RequiredVirtualGatewaySpecTypeDef(TypedDict):
    listeners: List["VirtualGatewayListenerTypeDef"]


class VirtualGatewaySpecTypeDef(_RequiredVirtualGatewaySpecTypeDef, total=False):
    backendDefaults: "VirtualGatewayBackendDefaultsTypeDef"
    logging: "VirtualGatewayLoggingTypeDef"


class VirtualGatewayStatusTypeDef(TypedDict):
    status: VirtualGatewayStatusCode


class VirtualGatewayTlsValidationContextAcmTrustTypeDef(TypedDict):
    certificateAuthorityArns: List[str]


class VirtualGatewayTlsValidationContextFileTrustTypeDef(TypedDict):
    certificateChain: str


class VirtualGatewayTlsValidationContextSdsTrustTypeDef(TypedDict):
    secretName: str


class VirtualGatewayTlsValidationContextTrustTypeDef(TypedDict, total=False):
    acm: "VirtualGatewayTlsValidationContextAcmTrustTypeDef"
    file: "VirtualGatewayTlsValidationContextFileTrustTypeDef"
    sds: "VirtualGatewayTlsValidationContextSdsTrustTypeDef"


class _RequiredVirtualGatewayTlsValidationContextTypeDef(TypedDict):
    trust: "VirtualGatewayTlsValidationContextTrustTypeDef"


class VirtualGatewayTlsValidationContextTypeDef(
    _RequiredVirtualGatewayTlsValidationContextTypeDef, total=False
):
    subjectAlternativeNames: "SubjectAlternativeNamesTypeDef"


class VirtualNodeConnectionPoolTypeDef(TypedDict, total=False):
    grpc: "VirtualNodeGrpcConnectionPoolTypeDef"
    http: "VirtualNodeHttpConnectionPoolTypeDef"
    http2: "VirtualNodeHttp2ConnectionPoolTypeDef"
    tcp: "VirtualNodeTcpConnectionPoolTypeDef"


class VirtualNodeDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "VirtualNodeSpecTypeDef"
    status: "VirtualNodeStatusTypeDef"
    virtualNodeName: str


class VirtualNodeGrpcConnectionPoolTypeDef(TypedDict):
    maxRequests: int


class VirtualNodeHttp2ConnectionPoolTypeDef(TypedDict):
    maxRequests: int


class _RequiredVirtualNodeHttpConnectionPoolTypeDef(TypedDict):
    maxConnections: int


class VirtualNodeHttpConnectionPoolTypeDef(
    _RequiredVirtualNodeHttpConnectionPoolTypeDef, total=False
):
    maxPendingRequests: int


class VirtualNodeRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualNodeName: str


class VirtualNodeServiceProviderTypeDef(TypedDict):
    virtualNodeName: str


class VirtualNodeSpecTypeDef(TypedDict, total=False):
    backendDefaults: "BackendDefaultsTypeDef"
    backends: List["BackendTypeDef"]
    listeners: List["ListenerTypeDef"]
    logging: "LoggingTypeDef"
    serviceDiscovery: "ServiceDiscoveryTypeDef"


class VirtualNodeStatusTypeDef(TypedDict):
    status: VirtualNodeStatusCode


class VirtualNodeTcpConnectionPoolTypeDef(TypedDict):
    maxConnections: int


class VirtualRouterDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "VirtualRouterSpecTypeDef"
    status: "VirtualRouterStatusTypeDef"
    virtualRouterName: str


class VirtualRouterListenerTypeDef(TypedDict):
    portMapping: "PortMappingTypeDef"


class VirtualRouterRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualRouterName: str


class VirtualRouterServiceProviderTypeDef(TypedDict):
    virtualRouterName: str


class VirtualRouterSpecTypeDef(TypedDict, total=False):
    listeners: List["VirtualRouterListenerTypeDef"]


class VirtualRouterStatusTypeDef(TypedDict):
    status: VirtualRouterStatusCode


class _RequiredVirtualServiceBackendTypeDef(TypedDict):
    virtualServiceName: str


class VirtualServiceBackendTypeDef(_RequiredVirtualServiceBackendTypeDef, total=False):
    clientPolicy: "ClientPolicyTypeDef"


class VirtualServiceDataTypeDef(TypedDict):
    meshName: str
    metadata: "ResourceMetadataTypeDef"
    spec: "VirtualServiceSpecTypeDef"
    status: "VirtualServiceStatusTypeDef"
    virtualServiceName: str


class VirtualServiceProviderTypeDef(TypedDict, total=False):
    virtualNode: "VirtualNodeServiceProviderTypeDef"
    virtualRouter: "VirtualRouterServiceProviderTypeDef"


class VirtualServiceRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualServiceName: str


class VirtualServiceSpecTypeDef(TypedDict, total=False):
    provider: "VirtualServiceProviderTypeDef"


class VirtualServiceStatusTypeDef(TypedDict):
    status: VirtualServiceStatusCode


class WeightedTargetTypeDef(TypedDict):
    virtualNode: str
    weight: int
