"""
Type annotations for emr-containers service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr_containers.type_defs import CancelJobRunResponseTypeDef

    data: CancelJobRunResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_emr_containers.literals import (
    EndpointState,
    FailureReason,
    JobRunState,
    PersistentAppUI,
    VirtualClusterState,
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
    "CancelJobRunResponseTypeDef",
    "CloudWatchMonitoringConfigurationTypeDef",
    "ConfigurationOverridesTypeDef",
    "ConfigurationTypeDef",
    "ContainerInfoTypeDef",
    "ContainerProviderTypeDef",
    "CreateManagedEndpointResponseTypeDef",
    "CreateVirtualClusterResponseTypeDef",
    "DeleteManagedEndpointResponseTypeDef",
    "DeleteVirtualClusterResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeManagedEndpointResponseTypeDef",
    "DescribeVirtualClusterResponseTypeDef",
    "EksInfoTypeDef",
    "EndpointTypeDef",
    "JobDriverTypeDef",
    "JobRunTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListManagedEndpointsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVirtualClustersResponseTypeDef",
    "MonitoringConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "S3MonitoringConfigurationTypeDef",
    "SparkSubmitJobDriverTypeDef",
    "StartJobRunResponseTypeDef",
    "VirtualClusterTypeDef",
)

CancelJobRunResponseTypeDef = TypedDict(
    "CancelJobRunResponseTypeDef", {"id": str, "virtualClusterId": str}, total=False
)


class _RequiredCloudWatchMonitoringConfigurationTypeDef(TypedDict):
    logGroupName: str


class CloudWatchMonitoringConfigurationTypeDef(
    _RequiredCloudWatchMonitoringConfigurationTypeDef, total=False
):
    logStreamNamePrefix: str


class ConfigurationOverridesTypeDef(TypedDict, total=False):
    applicationConfiguration: List["ConfigurationTypeDef"]
    monitoringConfiguration: "MonitoringConfigurationTypeDef"


class _RequiredConfigurationTypeDef(TypedDict):
    classification: str


class ConfigurationTypeDef(_RequiredConfigurationTypeDef, total=False):
    properties: Dict[str, str]
    configurations: List[Dict[str, Any]]


class ContainerInfoTypeDef(TypedDict, total=False):
    eksInfo: "EksInfoTypeDef"


_RequiredContainerProviderTypeDef = TypedDict(
    "_RequiredContainerProviderTypeDef", {"type": Literal["EKS"], "id": str}
)
_OptionalContainerProviderTypeDef = TypedDict(
    "_OptionalContainerProviderTypeDef", {"info": "ContainerInfoTypeDef"}, total=False
)


class ContainerProviderTypeDef(
    _RequiredContainerProviderTypeDef, _OptionalContainerProviderTypeDef
):
    pass


CreateManagedEndpointResponseTypeDef = TypedDict(
    "CreateManagedEndpointResponseTypeDef",
    {"id": str, "name": str, "arn": str, "virtualClusterId": str},
    total=False,
)

CreateVirtualClusterResponseTypeDef = TypedDict(
    "CreateVirtualClusterResponseTypeDef", {"id": str, "name": str, "arn": str}, total=False
)

DeleteManagedEndpointResponseTypeDef = TypedDict(
    "DeleteManagedEndpointResponseTypeDef", {"id": str, "virtualClusterId": str}, total=False
)

DeleteVirtualClusterResponseTypeDef = TypedDict(
    "DeleteVirtualClusterResponseTypeDef", {"id": str}, total=False
)


class DescribeJobRunResponseTypeDef(TypedDict, total=False):
    jobRun: "JobRunTypeDef"


class DescribeManagedEndpointResponseTypeDef(TypedDict, total=False):
    endpoint: "EndpointTypeDef"


class DescribeVirtualClusterResponseTypeDef(TypedDict, total=False):
    virtualCluster: "VirtualClusterTypeDef"


class EksInfoTypeDef(TypedDict, total=False):
    namespace: str


EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "virtualClusterId": str,
        "type": str,
        "state": EndpointState,
        "releaseLabel": str,
        "executionRoleArn": str,
        "certificateArn": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "serverUrl": str,
        "createdAt": datetime,
        "securityGroup": str,
        "subnetIds": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)


class JobDriverTypeDef(TypedDict, total=False):
    sparkSubmitJobDriver: "SparkSubmitJobDriverTypeDef"


JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "id": str,
        "name": str,
        "virtualClusterId": str,
        "arn": str,
        "state": JobRunState,
        "clientToken": str,
        "executionRoleArn": str,
        "releaseLabel": str,
        "configurationOverrides": "ConfigurationOverridesTypeDef",
        "jobDriver": "JobDriverTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "finishedAt": datetime,
        "stateDetails": str,
        "failureReason": FailureReason,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListJobRunsResponseTypeDef(TypedDict, total=False):
    jobRuns: List["JobRunTypeDef"]
    nextToken: str


class ListManagedEndpointsResponseTypeDef(TypedDict, total=False):
    endpoints: List["EndpointTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ListVirtualClustersResponseTypeDef(TypedDict, total=False):
    virtualClusters: List["VirtualClusterTypeDef"]
    nextToken: str


class MonitoringConfigurationTypeDef(TypedDict, total=False):
    persistentAppUI: PersistentAppUI
    cloudWatchMonitoringConfiguration: "CloudWatchMonitoringConfigurationTypeDef"
    s3MonitoringConfiguration: "S3MonitoringConfigurationTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class S3MonitoringConfigurationTypeDef(TypedDict):
    logUri: str


class _RequiredSparkSubmitJobDriverTypeDef(TypedDict):
    entryPoint: str


class SparkSubmitJobDriverTypeDef(_RequiredSparkSubmitJobDriverTypeDef, total=False):
    entryPointArguments: List[str]
    sparkSubmitParameters: str


StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {"id": str, "name": str, "arn": str, "virtualClusterId": str},
    total=False,
)

VirtualClusterTypeDef = TypedDict(
    "VirtualClusterTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "state": VirtualClusterState,
        "containerProvider": "ContainerProviderTypeDef",
        "createdAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)
