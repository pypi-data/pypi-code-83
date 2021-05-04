"""
Type annotations for appconfig service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appconfig.type_defs import ApplicationTypeDef

    data: ApplicationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_appconfig.literals import (
    DeploymentEventType,
    DeploymentState,
    EnvironmentState,
    GrowthType,
    ReplicateTo,
    TriggeredBy,
    ValidatorType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationTypeDef",
    "ApplicationsTypeDef",
    "ConfigurationProfileSummaryTypeDef",
    "ConfigurationProfileTypeDef",
    "ConfigurationProfilesTypeDef",
    "ConfigurationTypeDef",
    "DeploymentEventTypeDef",
    "DeploymentStrategiesTypeDef",
    "DeploymentStrategyTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "DeploymentsTypeDef",
    "EnvironmentTypeDef",
    "EnvironmentsTypeDef",
    "HostedConfigurationVersionSummaryTypeDef",
    "HostedConfigurationVersionTypeDef",
    "HostedConfigurationVersionsTypeDef",
    "MonitorTypeDef",
    "ResourceTagsTypeDef",
    "ValidatorTypeDef",
)


class ApplicationTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str


class ApplicationsTypeDef(TypedDict, total=False):
    Items: List["ApplicationTypeDef"]
    NextToken: str


class ConfigurationProfileSummaryTypeDef(TypedDict, total=False):
    ApplicationId: str
    Id: str
    Name: str
    LocationUri: str
    ValidatorTypes: List[ValidatorType]


class ConfigurationProfileTypeDef(TypedDict, total=False):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    LocationUri: str
    RetrievalRoleArn: str
    Validators: List["ValidatorTypeDef"]


class ConfigurationProfilesTypeDef(TypedDict, total=False):
    Items: List["ConfigurationProfileSummaryTypeDef"]
    NextToken: str


class ConfigurationTypeDef(TypedDict, total=False):
    Content: Union[bytes, IO[bytes]]
    ConfigurationVersion: str
    ContentType: str


class DeploymentEventTypeDef(TypedDict, total=False):
    EventType: DeploymentEventType
    TriggeredBy: TriggeredBy
    Description: str
    OccurredAt: datetime


class DeploymentStrategiesTypeDef(TypedDict, total=False):
    Items: List["DeploymentStrategyTypeDef"]
    NextToken: str


class DeploymentStrategyTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    ReplicateTo: ReplicateTo


class DeploymentSummaryTypeDef(TypedDict, total=False):
    DeploymentNumber: int
    ConfigurationName: str
    ConfigurationVersion: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    State: DeploymentState
    PercentageComplete: float
    StartedAt: datetime
    CompletedAt: datetime


class DeploymentTypeDef(TypedDict, total=False):
    ApplicationId: str
    EnvironmentId: str
    DeploymentStrategyId: str
    ConfigurationProfileId: str
    DeploymentNumber: int
    ConfigurationName: str
    ConfigurationLocationUri: str
    ConfigurationVersion: str
    Description: str
    DeploymentDurationInMinutes: int
    GrowthType: GrowthType
    GrowthFactor: float
    FinalBakeTimeInMinutes: int
    State: DeploymentState
    EventLog: List["DeploymentEventTypeDef"]
    PercentageComplete: float
    StartedAt: datetime
    CompletedAt: datetime


class DeploymentsTypeDef(TypedDict, total=False):
    Items: List["DeploymentSummaryTypeDef"]
    NextToken: str


class EnvironmentTypeDef(TypedDict, total=False):
    ApplicationId: str
    Id: str
    Name: str
    Description: str
    State: EnvironmentState
    Monitors: List["MonitorTypeDef"]


class EnvironmentsTypeDef(TypedDict, total=False):
    Items: List["EnvironmentTypeDef"]
    NextToken: str


class HostedConfigurationVersionSummaryTypeDef(TypedDict, total=False):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    ContentType: str


class HostedConfigurationVersionTypeDef(TypedDict, total=False):
    ApplicationId: str
    ConfigurationProfileId: str
    VersionNumber: int
    Description: str
    Content: Union[bytes, IO[bytes]]
    ContentType: str


class HostedConfigurationVersionsTypeDef(TypedDict, total=False):
    Items: List["HostedConfigurationVersionSummaryTypeDef"]
    NextToken: str


class MonitorTypeDef(TypedDict, total=False):
    AlarmArn: str
    AlarmRoleArn: str


class ResourceTagsTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


ValidatorTypeDef = TypedDict("ValidatorTypeDef", {"Type": ValidatorType, "Content": str})
