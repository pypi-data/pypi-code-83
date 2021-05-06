"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import CreateHttpNamespaceResponseTypeDef

    data: CreateHttpNamespaceResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_servicediscovery.literals import (
    FilterCondition,
    HealthCheckType,
    HealthStatus,
    NamespaceType,
    OperationFilterName,
    OperationStatus,
    OperationTargetType,
    OperationType,
    RecordType,
    RoutingPolicy,
    ServiceType,
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
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NamespaceFilterTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagTypeDef",
    "UpdateServiceResponseTypeDef",
)


class CreateHttpNamespaceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class CreatePrivateDnsNamespaceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class CreatePublicDnsNamespaceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class CreateServiceResponseTypeDef(TypedDict, total=False):
    Service: "ServiceTypeDef"


class DeleteNamespaceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class DeregisterInstanceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class DiscoverInstancesResponseTypeDef(TypedDict, total=False):
    Instances: List["HttpInstanceSummaryTypeDef"]


class DnsConfigChangeTypeDef(TypedDict):
    DnsRecords: List["DnsRecordTypeDef"]


class _RequiredDnsConfigTypeDef(TypedDict):
    DnsRecords: List["DnsRecordTypeDef"]


class DnsConfigTypeDef(_RequiredDnsConfigTypeDef, total=False):
    NamespaceId: str
    RoutingPolicy: RoutingPolicy


class DnsPropertiesTypeDef(TypedDict, total=False):
    HostedZoneId: str


DnsRecordTypeDef = TypedDict("DnsRecordTypeDef", {"Type": RecordType, "TTL": int})


class GetInstanceResponseTypeDef(TypedDict, total=False):
    Instance: "InstanceTypeDef"


class GetInstancesHealthStatusResponseTypeDef(TypedDict, total=False):
    Status: Dict[str, HealthStatus]
    NextToken: str


class GetNamespaceResponseTypeDef(TypedDict, total=False):
    Namespace: "NamespaceTypeDef"


class GetOperationResponseTypeDef(TypedDict, total=False):
    Operation: "OperationTypeDef"


class GetServiceResponseTypeDef(TypedDict, total=False):
    Service: "ServiceTypeDef"


_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef", {"Type": HealthCheckType}
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef", {"ResourcePath": str, "FailureThreshold": int}, total=False
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


class HealthCheckCustomConfigTypeDef(TypedDict, total=False):
    FailureThreshold: int


class HttpInstanceSummaryTypeDef(TypedDict, total=False):
    InstanceId: str
    NamespaceName: str
    ServiceName: str
    HealthStatus: HealthStatus
    Attributes: Dict[str, str]


class HttpPropertiesTypeDef(TypedDict, total=False):
    HttpName: str


class InstanceSummaryTypeDef(TypedDict, total=False):
    Id: str
    Attributes: Dict[str, str]


class _RequiredInstanceTypeDef(TypedDict):
    Id: str


class InstanceTypeDef(_RequiredInstanceTypeDef, total=False):
    CreatorRequestId: str
    Attributes: Dict[str, str]


class ListInstancesResponseTypeDef(TypedDict, total=False):
    Instances: List["InstanceSummaryTypeDef"]
    NextToken: str


class ListNamespacesResponseTypeDef(TypedDict, total=False):
    Namespaces: List["NamespaceSummaryTypeDef"]
    NextToken: str


class ListOperationsResponseTypeDef(TypedDict, total=False):
    Operations: List["OperationSummaryTypeDef"]
    NextToken: str


class ListServicesResponseTypeDef(TypedDict, total=False):
    Services: List["ServiceSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class _RequiredNamespaceFilterTypeDef(TypedDict):
    Name: Literal["TYPE"]
    Values: List[str]


class NamespaceFilterTypeDef(_RequiredNamespaceFilterTypeDef, total=False):
    Condition: FilterCondition


class NamespacePropertiesTypeDef(TypedDict, total=False):
    DnsProperties: "DnsPropertiesTypeDef"
    HttpProperties: "HttpPropertiesTypeDef"


NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class _RequiredOperationFilterTypeDef(TypedDict):
    Name: OperationFilterName
    Values: List[str]


class OperationFilterTypeDef(_RequiredOperationFilterTypeDef, total=False):
    Condition: FilterCondition


class OperationSummaryTypeDef(TypedDict, total=False):
    Id: str
    Status: OperationStatus


OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": OperationType,
        "Status": OperationStatus,
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[OperationTargetType, str],
    },
    total=False,
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RegisterInstanceResponseTypeDef(TypedDict, total=False):
    OperationId: str


class ServiceChangeTypeDef(TypedDict, total=False):
    Description: str
    DnsConfig: "DnsConfigChangeTypeDef"
    HealthCheckConfig: "HealthCheckConfigTypeDef"


class _RequiredServiceFilterTypeDef(TypedDict):
    Name: Literal["NAMESPACE_ID"]
    Values: List[str]


class ServiceFilterTypeDef(_RequiredServiceFilterTypeDef, total=False):
    Condition: FilterCondition


ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": ServiceType,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "Type": ServiceType,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateServiceResponseTypeDef(TypedDict, total=False):
    OperationId: str
