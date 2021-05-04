"""
Type annotations for schemas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import CreateDiscovererResponseTypeDef

    data: CreateDiscovererResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_schemas.literals import CodeGenerationStatus, DiscovererState, TypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "ExportSchemaResponseTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegistrySummaryTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasResponseTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererResponseTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "WaiterConfigTypeDef",
)


class CreateDiscovererResponseTypeDef(TypedDict, total=False):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererState
    Tags: Dict[str, str]


class CreateRegistryResponseTypeDef(TypedDict, total=False):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]


CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)


class DescribeCodeBindingResponseTypeDef(TypedDict, total=False):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatus


class DescribeDiscovererResponseTypeDef(TypedDict, total=False):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererState
    Tags: Dict[str, str]


class DescribeRegistryResponseTypeDef(TypedDict, total=False):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]


DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)


class DiscovererSummaryTypeDef(TypedDict, total=False):
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererState
    Tags: Dict[str, str]


ExportSchemaResponseTypeDef = TypedDict(
    "ExportSchemaResponseTypeDef",
    {"Content": str, "SchemaArn": str, "SchemaName": str, "SchemaVersion": str, "Type": str},
    total=False,
)


class GetCodeBindingSourceResponseTypeDef(TypedDict, total=False):
    Body: Union[bytes, IO[bytes]]


class GetDiscoveredSchemaResponseTypeDef(TypedDict, total=False):
    Content: str


class GetResourcePolicyResponseTypeDef(TypedDict, total=False):
    Policy: str
    RevisionId: str


class ListDiscoverersResponseTypeDef(TypedDict, total=False):
    Discoverers: List["DiscovererSummaryTypeDef"]
    NextToken: str


class ListRegistriesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Registries: List["RegistrySummaryTypeDef"]


class ListSchemaVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    SchemaVersions: List["SchemaVersionSummaryTypeDef"]


class ListSchemasResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Schemas: List["SchemaSummaryTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutCodeBindingResponseTypeDef(TypedDict, total=False):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatus


class PutResourcePolicyResponseTypeDef(TypedDict, total=False):
    Policy: str
    RevisionId: str


class RegistrySummaryTypeDef(TypedDict, total=False):
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]


class SchemaSummaryTypeDef(TypedDict, total=False):
    LastModified: datetime
    SchemaArn: str
    SchemaName: str
    Tags: Dict[str, str]
    VersionCount: int


SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {"SchemaArn": str, "SchemaName": str, "SchemaVersion": str, "Type": TypeType},
    total=False,
)


class SearchSchemaSummaryTypeDef(TypedDict, total=False):
    RegistryName: str
    SchemaArn: str
    SchemaName: str
    SchemaVersions: List["SearchSchemaVersionSummaryTypeDef"]


SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {"CreatedDate": datetime, "SchemaVersion": str, "Type": TypeType},
    total=False,
)


class SearchSchemasResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Schemas: List["SearchSchemaSummaryTypeDef"]


class StartDiscovererResponseTypeDef(TypedDict, total=False):
    DiscovererId: str
    State: DiscovererState


class StopDiscovererResponseTypeDef(TypedDict, total=False):
    DiscovererId: str
    State: DiscovererState


class UpdateDiscovererResponseTypeDef(TypedDict, total=False):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererState
    Tags: Dict[str, str]


class UpdateRegistryResponseTypeDef(TypedDict, total=False):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]


UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
    },
    total=False,
)


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
