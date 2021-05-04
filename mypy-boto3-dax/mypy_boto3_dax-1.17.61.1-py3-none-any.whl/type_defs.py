"""
Type annotations for dax service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dax.type_defs import ClusterTypeDef

    data: ClusterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_dax.literals import ChangeType, IsModifiable, ParameterType, SourceType, SSEStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClusterTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateParameterGroupResponseTypeDef",
    "CreateSubnetGroupResponseTypeDef",
    "DecreaseReplicationFactorResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteParameterGroupResponseTypeDef",
    "DeleteSubnetGroupResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeDefaultParametersResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeParameterGroupsResponseTypeDef",
    "DescribeParametersResponseTypeDef",
    "DescribeSubnetGroupsResponseTypeDef",
    "EndpointTypeDef",
    "EventTypeDef",
    "IncreaseReplicationFactorResponseTypeDef",
    "ListTagsResponseTypeDef",
    "NodeTypeDef",
    "NodeTypeSpecificValueTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterGroupStatusTypeDef",
    "ParameterGroupTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "RebootNodeResponseTypeDef",
    "SSEDescriptionTypeDef",
    "SSESpecificationTypeDef",
    "SecurityGroupMembershipTypeDef",
    "SubnetGroupTypeDef",
    "SubnetTypeDef",
    "TagResourceResponseTypeDef",
    "TagTypeDef",
    "UntagResourceResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateParameterGroupResponseTypeDef",
    "UpdateSubnetGroupResponseTypeDef",
)


class ClusterTypeDef(TypedDict, total=False):
    ClusterName: str
    Description: str
    ClusterArn: str
    TotalNodes: int
    ActiveNodes: int
    NodeType: str
    Status: str
    ClusterDiscoveryEndpoint: "EndpointTypeDef"
    NodeIdsToRemove: List[str]
    Nodes: List["NodeTypeDef"]
    PreferredMaintenanceWindow: str
    NotificationConfiguration: "NotificationConfigurationTypeDef"
    SubnetGroup: str
    SecurityGroups: List["SecurityGroupMembershipTypeDef"]
    IamRoleArn: str
    ParameterGroup: "ParameterGroupStatusTypeDef"
    SSEDescription: "SSEDescriptionTypeDef"


class CreateClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class CreateParameterGroupResponseTypeDef(TypedDict, total=False):
    ParameterGroup: "ParameterGroupTypeDef"


class CreateSubnetGroupResponseTypeDef(TypedDict, total=False):
    SubnetGroup: "SubnetGroupTypeDef"


class DecreaseReplicationFactorResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class DeleteClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class DeleteParameterGroupResponseTypeDef(TypedDict, total=False):
    DeletionMessage: str


class DeleteSubnetGroupResponseTypeDef(TypedDict, total=False):
    DeletionMessage: str


class DescribeClustersResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Clusters: List["ClusterTypeDef"]


class DescribeDefaultParametersResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Parameters: List["ParameterTypeDef"]


class DescribeEventsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Events: List["EventTypeDef"]


class DescribeParameterGroupsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ParameterGroups: List["ParameterGroupTypeDef"]


class DescribeParametersResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Parameters: List["ParameterTypeDef"]


class DescribeSubnetGroupsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    SubnetGroups: List["SubnetGroupTypeDef"]


class EndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int


class EventTypeDef(TypedDict, total=False):
    SourceName: str
    SourceType: SourceType
    Message: str
    Date: datetime


class IncreaseReplicationFactorResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ListTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class NodeTypeDef(TypedDict, total=False):
    NodeId: str
    Endpoint: "EndpointTypeDef"
    NodeCreateTime: datetime
    AvailabilityZone: str
    NodeStatus: str
    ParameterGroupStatus: str


class NodeTypeSpecificValueTypeDef(TypedDict, total=False):
    NodeType: str
    Value: str


class NotificationConfigurationTypeDef(TypedDict, total=False):
    TopicArn: str
    TopicStatus: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterGroupStatusTypeDef(TypedDict, total=False):
    ParameterGroupName: str
    ParameterApplyStatus: str
    NodeIdsToReboot: List[str]


class ParameterGroupTypeDef(TypedDict, total=False):
    ParameterGroupName: str
    Description: str


class ParameterNameValueTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterValue: str


class ParameterTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterType: ParameterType
    ParameterValue: str
    NodeTypeSpecificValues: List["NodeTypeSpecificValueTypeDef"]
    Description: str
    Source: str
    DataType: str
    AllowedValues: str
    IsModifiable: IsModifiable
    ChangeType: ChangeType


class RebootNodeResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class SSEDescriptionTypeDef(TypedDict, total=False):
    Status: SSEStatus


class SSESpecificationTypeDef(TypedDict):
    Enabled: bool


class SecurityGroupMembershipTypeDef(TypedDict, total=False):
    SecurityGroupIdentifier: str
    Status: str


class SubnetGroupTypeDef(TypedDict, total=False):
    SubnetGroupName: str
    Description: str
    VpcId: str
    Subnets: List["SubnetTypeDef"]


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: str


class TagResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UntagResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class UpdateClusterResponseTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class UpdateParameterGroupResponseTypeDef(TypedDict, total=False):
    ParameterGroup: "ParameterGroupTypeDef"


class UpdateSubnetGroupResponseTypeDef(TypedDict, total=False):
    SubnetGroup: "SubnetGroupTypeDef"
