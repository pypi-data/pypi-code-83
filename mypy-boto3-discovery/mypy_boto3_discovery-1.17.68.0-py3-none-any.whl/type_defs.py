"""
Type annotations for discovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_discovery.literals import (
    AgentStatus,
    BatchDeleteImportDataErrorCode,
    ConfigurationItemType,
    ContinuousExportStatus,
    ExportStatus,
    ImportStatus,
    ImportTaskFilterName,
    orderString,
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
    "AgentConfigurationStatusTypeDef",
    "AgentInfoTypeDef",
    "AgentNetworkInfoTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "BatchDeleteImportDataResponseTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CreateApplicationResponseTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "DescribeAgentsResponseTypeDef",
    "DescribeConfigurationsResponseTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeImportTasksResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "ExportConfigurationsResponseTypeDef",
    "ExportFilterTypeDef",
    "ExportInfoTypeDef",
    "FilterTypeDef",
    "GetDiscoverySummaryResponseTypeDef",
    "ImportTaskFilterTypeDef",
    "ImportTaskTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListServerNeighborsResponseTypeDef",
    "NeighborConnectionDetailTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "StartContinuousExportResponseTypeDef",
    "StartDataCollectionByAgentIdsResponseTypeDef",
    "StartExportTaskResponseTypeDef",
    "StartImportTaskResponseTypeDef",
    "StopContinuousExportResponseTypeDef",
    "StopDataCollectionByAgentIdsResponseTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
)


class AgentConfigurationStatusTypeDef(TypedDict, total=False):
    agentId: str
    operationSucceeded: bool
    description: str


class AgentInfoTypeDef(TypedDict, total=False):
    agentId: str
    hostName: str
    agentNetworkInfoList: List["AgentNetworkInfoTypeDef"]
    connectorId: str
    version: str
    health: AgentStatus
    lastHealthPingTime: str
    collectionStatus: str
    agentType: str
    registeredTime: str


class AgentNetworkInfoTypeDef(TypedDict, total=False):
    ipAddress: str
    macAddress: str


class BatchDeleteImportDataErrorTypeDef(TypedDict, total=False):
    importTaskId: str
    errorCode: BatchDeleteImportDataErrorCode
    errorDescription: str


class BatchDeleteImportDataResponseTypeDef(TypedDict, total=False):
    errors: List["BatchDeleteImportDataErrorTypeDef"]


class ConfigurationTagTypeDef(TypedDict, total=False):
    configurationType: ConfigurationItemType
    configurationId: str
    key: str
    value: str
    timeOfCreation: datetime


class ContinuousExportDescriptionTypeDef(TypedDict, total=False):
    exportId: str
    status: ContinuousExportStatus
    statusDetail: str
    s3Bucket: str
    startTime: datetime
    stopTime: datetime
    dataSource: Literal["AGENT"]
    schemaStorageConfig: Dict[str, str]


class CreateApplicationResponseTypeDef(TypedDict, total=False):
    configurationId: str


class CustomerAgentInfoTypeDef(TypedDict):
    activeAgents: int
    healthyAgents: int
    blackListedAgents: int
    shutdownAgents: int
    unhealthyAgents: int
    totalAgents: int
    unknownAgents: int


class CustomerConnectorInfoTypeDef(TypedDict):
    activeConnectors: int
    healthyConnectors: int
    blackListedConnectors: int
    shutdownConnectors: int
    unhealthyConnectors: int
    totalConnectors: int
    unknownConnectors: int


class DescribeAgentsResponseTypeDef(TypedDict, total=False):
    agentsInfo: List["AgentInfoTypeDef"]
    nextToken: str


class DescribeConfigurationsResponseTypeDef(TypedDict, total=False):
    configurations: List[Dict[str, str]]


class DescribeContinuousExportsResponseTypeDef(TypedDict, total=False):
    descriptions: List["ContinuousExportDescriptionTypeDef"]
    nextToken: str


class DescribeExportConfigurationsResponseTypeDef(TypedDict, total=False):
    exportsInfo: List["ExportInfoTypeDef"]
    nextToken: str


class DescribeExportTasksResponseTypeDef(TypedDict, total=False):
    exportsInfo: List["ExportInfoTypeDef"]
    nextToken: str


class DescribeImportTasksResponseTypeDef(TypedDict, total=False):
    nextToken: str
    tasks: List["ImportTaskTypeDef"]


class DescribeTagsResponseTypeDef(TypedDict, total=False):
    tags: List["ConfigurationTagTypeDef"]
    nextToken: str


class ExportConfigurationsResponseTypeDef(TypedDict, total=False):
    exportId: str


class ExportFilterTypeDef(TypedDict):
    name: str
    values: List[str]
    condition: str


class _RequiredExportInfoTypeDef(TypedDict):
    exportId: str
    exportStatus: ExportStatus
    statusMessage: str
    exportRequestTime: datetime


class ExportInfoTypeDef(_RequiredExportInfoTypeDef, total=False):
    configurationsDownloadUrl: str
    isTruncated: bool
    requestedStartTime: datetime
    requestedEndTime: datetime


class FilterTypeDef(TypedDict):
    name: str
    values: List[str]
    condition: str


class GetDiscoverySummaryResponseTypeDef(TypedDict, total=False):
    servers: int
    applications: int
    serversMappedToApplications: int
    serversMappedtoTags: int
    agentSummary: "CustomerAgentInfoTypeDef"
    connectorSummary: "CustomerConnectorInfoTypeDef"


class ImportTaskFilterTypeDef(TypedDict, total=False):
    name: ImportTaskFilterName
    values: List[str]


class ImportTaskTypeDef(TypedDict, total=False):
    importTaskId: str
    clientRequestToken: str
    name: str
    importUrl: str
    status: ImportStatus
    importRequestTime: datetime
    importCompletionTime: datetime
    importDeletedTime: datetime
    serverImportSuccess: int
    serverImportFailure: int
    applicationImportSuccess: int
    applicationImportFailure: int
    errorsAndFailedEntriesZip: str


class ListConfigurationsResponseTypeDef(TypedDict, total=False):
    configurations: List[Dict[str, str]]
    nextToken: str


class _RequiredListServerNeighborsResponseTypeDef(TypedDict):
    neighbors: List["NeighborConnectionDetailTypeDef"]


class ListServerNeighborsResponseTypeDef(_RequiredListServerNeighborsResponseTypeDef, total=False):
    nextToken: str
    knownDependencyCount: int


class _RequiredNeighborConnectionDetailTypeDef(TypedDict):
    sourceServerId: str
    destinationServerId: str
    connectionsCount: int


class NeighborConnectionDetailTypeDef(_RequiredNeighborConnectionDetailTypeDef, total=False):
    destinationPort: int
    transportProtocol: str


class _RequiredOrderByElementTypeDef(TypedDict):
    fieldName: str


class OrderByElementTypeDef(_RequiredOrderByElementTypeDef, total=False):
    sortOrder: orderString


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class StartContinuousExportResponseTypeDef(TypedDict, total=False):
    exportId: str
    s3Bucket: str
    startTime: datetime
    dataSource: Literal["AGENT"]
    schemaStorageConfig: Dict[str, str]


class StartDataCollectionByAgentIdsResponseTypeDef(TypedDict, total=False):
    agentsConfigurationStatus: List["AgentConfigurationStatusTypeDef"]


class StartExportTaskResponseTypeDef(TypedDict, total=False):
    exportId: str


class StartImportTaskResponseTypeDef(TypedDict, total=False):
    task: "ImportTaskTypeDef"


class StopContinuousExportResponseTypeDef(TypedDict, total=False):
    startTime: datetime
    stopTime: datetime


class StopDataCollectionByAgentIdsResponseTypeDef(TypedDict, total=False):
    agentsConfigurationStatus: List["AgentConfigurationStatusTypeDef"]


class TagFilterTypeDef(TypedDict):
    name: str
    values: List[str]


class TagTypeDef(TypedDict):
    key: str
    value: str
