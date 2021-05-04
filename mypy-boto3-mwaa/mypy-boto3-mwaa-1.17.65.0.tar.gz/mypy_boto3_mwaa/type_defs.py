"""
Type annotations for mwaa service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mwaa.type_defs import CreateCliTokenResponseTypeDef

    data: CreateCliTokenResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_mwaa.literals import (
    EnvironmentStatus,
    LoggingLevel,
    Unit,
    UpdateStatus,
    WebserverAccessMode,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateCliTokenResponseTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateWebLoginTokenResponseTypeDef",
    "DimensionTypeDef",
    "EnvironmentTypeDef",
    "GetEnvironmentOutputTypeDef",
    "LastUpdateTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LoggingConfigurationInputTypeDef",
    "LoggingConfigurationTypeDef",
    "MetricDatumTypeDef",
    "ModuleLoggingConfigurationInputTypeDef",
    "ModuleLoggingConfigurationTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "StatisticSetTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateErrorTypeDef",
    "UpdateNetworkConfigurationInputTypeDef",
)


class CreateCliTokenResponseTypeDef(TypedDict, total=False):
    CliToken: str
    WebServerHostname: str


class CreateEnvironmentOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: "ResponseMetadata"


class CreateWebLoginTokenResponseTypeDef(TypedDict, total=False):
    WebServerHostname: str
    WebToken: str


class DimensionTypeDef(TypedDict):
    Name: str
    Value: str


class EnvironmentTypeDef(TypedDict, total=False):
    AirflowConfigurationOptions: Dict[str, str]
    AirflowVersion: str
    Arn: str
    CreatedAt: datetime
    DagS3Path: str
    EnvironmentClass: str
    ExecutionRoleArn: str
    KmsKey: str
    LastUpdate: "LastUpdateTypeDef"
    LoggingConfiguration: "LoggingConfigurationTypeDef"
    MaxWorkers: int
    MinWorkers: int
    Name: str
    NetworkConfiguration: "NetworkConfigurationTypeDef"
    PluginsS3ObjectVersion: str
    PluginsS3Path: str
    RequirementsS3ObjectVersion: str
    RequirementsS3Path: str
    ServiceRoleArn: str
    SourceBucketArn: str
    Status: EnvironmentStatus
    Tags: Dict[str, str]
    WebserverAccessMode: WebserverAccessMode
    WebserverUrl: str
    WeeklyMaintenanceWindowStart: str


class GetEnvironmentOutputTypeDef(TypedDict):
    Environment: "EnvironmentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class LastUpdateTypeDef(TypedDict, total=False):
    CreatedAt: datetime
    Error: "UpdateErrorTypeDef"
    Status: UpdateStatus


class ListEnvironmentsOutputTypeDef(TypedDict):
    Environments: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class LoggingConfigurationInputTypeDef(TypedDict, total=False):
    DagProcessingLogs: "ModuleLoggingConfigurationInputTypeDef"
    SchedulerLogs: "ModuleLoggingConfigurationInputTypeDef"
    TaskLogs: "ModuleLoggingConfigurationInputTypeDef"
    WebserverLogs: "ModuleLoggingConfigurationInputTypeDef"
    WorkerLogs: "ModuleLoggingConfigurationInputTypeDef"


class LoggingConfigurationTypeDef(TypedDict, total=False):
    DagProcessingLogs: "ModuleLoggingConfigurationTypeDef"
    SchedulerLogs: "ModuleLoggingConfigurationTypeDef"
    TaskLogs: "ModuleLoggingConfigurationTypeDef"
    WebserverLogs: "ModuleLoggingConfigurationTypeDef"
    WorkerLogs: "ModuleLoggingConfigurationTypeDef"


class _RequiredMetricDatumTypeDef(TypedDict):
    MetricName: str
    Timestamp: datetime


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, total=False):
    Dimensions: List["DimensionTypeDef"]
    StatisticValues: "StatisticSetTypeDef"
    Unit: Unit
    Value: float


class ModuleLoggingConfigurationInputTypeDef(TypedDict):
    Enabled: bool
    LogLevel: LoggingLevel


class ModuleLoggingConfigurationTypeDef(TypedDict, total=False):
    CloudWatchLogGroupArn: str
    Enabled: bool
    LogLevel: LoggingLevel


class NetworkConfigurationTypeDef(TypedDict, total=False):
    SecurityGroupIds: List[str]
    SubnetIds: List[str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class StatisticSetTypeDef(TypedDict, total=False):
    Maximum: float
    Minimum: float
    SampleCount: int
    Sum: float


class UpdateEnvironmentOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: "ResponseMetadata"


class UpdateErrorTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str


class UpdateNetworkConfigurationInputTypeDef(TypedDict):
    SecurityGroupIds: List[str]
