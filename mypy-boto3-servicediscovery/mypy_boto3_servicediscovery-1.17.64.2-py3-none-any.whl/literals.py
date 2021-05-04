"""
Type annotations for servicediscovery service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/literals.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.literals import CustomHealthStatus

    data: CustomHealthStatus = "HEALTHY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CustomHealthStatus",
    "FilterCondition",
    "HealthCheckType",
    "HealthStatus",
    "HealthStatusFilter",
    "ListInstancesPaginatorName",
    "ListNamespacesPaginatorName",
    "ListOperationsPaginatorName",
    "ListServicesPaginatorName",
    "NamespaceFilterName",
    "NamespaceType",
    "OperationFilterName",
    "OperationStatus",
    "OperationTargetType",
    "OperationType",
    "RecordType",
    "RoutingPolicy",
    "ServiceFilterName",
    "ServiceType",
    "ServiceTypeOption",
)


CustomHealthStatus = Literal["HEALTHY", "UNHEALTHY"]
FilterCondition = Literal["BETWEEN", "EQ", "IN"]
HealthCheckType = Literal["HTTP", "HTTPS", "TCP"]
HealthStatus = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
HealthStatusFilter = Literal["ALL", "HEALTHY", "UNHEALTHY"]
ListInstancesPaginatorName = Literal["list_instances"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListOperationsPaginatorName = Literal["list_operations"]
ListServicesPaginatorName = Literal["list_services"]
NamespaceFilterName = Literal["TYPE"]
NamespaceType = Literal["DNS_PRIVATE", "DNS_PUBLIC", "HTTP"]
OperationFilterName = Literal["NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"]
OperationStatus = Literal["FAIL", "PENDING", "SUBMITTED", "SUCCESS"]
OperationTargetType = Literal["INSTANCE", "NAMESPACE", "SERVICE"]
OperationType = Literal[
    "CREATE_NAMESPACE",
    "DELETE_NAMESPACE",
    "DEREGISTER_INSTANCE",
    "REGISTER_INSTANCE",
    "UPDATE_SERVICE",
]
RecordType = Literal["A", "AAAA", "CNAME", "SRV"]
RoutingPolicy = Literal["MULTIVALUE", "WEIGHTED"]
ServiceFilterName = Literal["NAMESPACE_ID"]
ServiceType = Literal["DNS", "DNS_HTTP", "HTTP"]
ServiceTypeOption = Literal["HTTP"]
