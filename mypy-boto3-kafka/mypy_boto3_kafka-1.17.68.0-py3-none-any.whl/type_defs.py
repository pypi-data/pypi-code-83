"""
Type annotations for kafka service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kafka.type_defs import BatchAssociateScramSecretResponseTypeDef

    data: BatchAssociateScramSecretResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_kafka.literals import (
    ClientBroker,
    ClusterState,
    ConfigurationState,
    EnhancedMonitoring,
    KafkaVersionStatus,
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
    "BatchAssociateScramSecretResponseTypeDef",
    "BatchDisassociateScramSecretResponseTypeDef",
    "BrokerEBSVolumeInfoTypeDef",
    "BrokerLogsTypeDef",
    "BrokerNodeGroupInfoTypeDef",
    "BrokerNodeInfoTypeDef",
    "BrokerSoftwareInfoTypeDef",
    "ClientAuthenticationTypeDef",
    "CloudWatchLogsTypeDef",
    "ClusterInfoTypeDef",
    "ClusterOperationInfoTypeDef",
    "ClusterOperationStepInfoTypeDef",
    "ClusterOperationStepTypeDef",
    "CompatibleKafkaVersionTypeDef",
    "ConfigurationInfoTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteConfigurationResponseTypeDef",
    "DescribeClusterOperationResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "EBSStorageInfoTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionInTransitTypeDef",
    "EncryptionInfoTypeDef",
    "ErrorInfoTypeDef",
    "FirehoseTypeDef",
    "GetBootstrapBrokersResponseTypeDef",
    "GetCompatibleKafkaVersionsResponseTypeDef",
    "IamTypeDef",
    "JmxExporterInfoTypeDef",
    "JmxExporterTypeDef",
    "KafkaVersionTypeDef",
    "ListClusterOperationsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListKafkaVersionsResponseTypeDef",
    "ListNodesResponseTypeDef",
    "ListScramSecretsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingInfoTypeDef",
    "MutableClusterInfoTypeDef",
    "NodeExporterInfoTypeDef",
    "NodeExporterTypeDef",
    "NodeInfoTypeDef",
    "OpenMonitoringInfoTypeDef",
    "OpenMonitoringTypeDef",
    "PaginatorConfigTypeDef",
    "PrometheusInfoTypeDef",
    "PrometheusTypeDef",
    "RebootBrokerResponseTypeDef",
    "S3TypeDef",
    "SaslTypeDef",
    "ScramTypeDef",
    "StateInfoTypeDef",
    "StorageInfoTypeDef",
    "TlsTypeDef",
    "UnprocessedScramSecretTypeDef",
    "UpdateBrokerCountResponseTypeDef",
    "UpdateBrokerStorageResponseTypeDef",
    "UpdateBrokerTypeResponseTypeDef",
    "UpdateClusterConfigurationResponseTypeDef",
    "UpdateClusterKafkaVersionResponseTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateMonitoringResponseTypeDef",
    "ZookeeperNodeInfoTypeDef",
)


class BatchAssociateScramSecretResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    UnprocessedScramSecrets: List["UnprocessedScramSecretTypeDef"]


class BatchDisassociateScramSecretResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    UnprocessedScramSecrets: List["UnprocessedScramSecretTypeDef"]


class BrokerEBSVolumeInfoTypeDef(TypedDict):
    KafkaBrokerNodeId: str
    VolumeSizeGB: int


class BrokerLogsTypeDef(TypedDict, total=False):
    CloudWatchLogs: "CloudWatchLogsTypeDef"
    Firehose: "FirehoseTypeDef"
    S3: "S3TypeDef"


class _RequiredBrokerNodeGroupInfoTypeDef(TypedDict):
    ClientSubnets: List[str]
    InstanceType: str


class BrokerNodeGroupInfoTypeDef(_RequiredBrokerNodeGroupInfoTypeDef, total=False):
    BrokerAZDistribution: Literal["DEFAULT"]
    SecurityGroups: List[str]
    StorageInfo: "StorageInfoTypeDef"


class BrokerNodeInfoTypeDef(TypedDict, total=False):
    AttachedENIId: str
    BrokerId: float
    ClientSubnet: str
    ClientVpcIpAddress: str
    CurrentBrokerSoftwareInfo: "BrokerSoftwareInfoTypeDef"
    Endpoints: List[str]


class BrokerSoftwareInfoTypeDef(TypedDict, total=False):
    ConfigurationArn: str
    ConfigurationRevision: int
    KafkaVersion: str


class ClientAuthenticationTypeDef(TypedDict, total=False):
    Sasl: "SaslTypeDef"
    Tls: "TlsTypeDef"


class _RequiredCloudWatchLogsTypeDef(TypedDict):
    Enabled: bool


class CloudWatchLogsTypeDef(_RequiredCloudWatchLogsTypeDef, total=False):
    LogGroup: str


class ClusterInfoTypeDef(TypedDict, total=False):
    ActiveOperationArn: str
    BrokerNodeGroupInfo: "BrokerNodeGroupInfoTypeDef"
    ClientAuthentication: "ClientAuthenticationTypeDef"
    ClusterArn: str
    ClusterName: str
    CreationTime: datetime
    CurrentBrokerSoftwareInfo: "BrokerSoftwareInfoTypeDef"
    CurrentVersion: str
    EncryptionInfo: "EncryptionInfoTypeDef"
    EnhancedMonitoring: EnhancedMonitoring
    OpenMonitoring: "OpenMonitoringTypeDef"
    LoggingInfo: "LoggingInfoTypeDef"
    NumberOfBrokerNodes: int
    State: ClusterState
    StateInfo: "StateInfoTypeDef"
    Tags: Dict[str, str]
    ZookeeperConnectString: str
    ZookeeperConnectStringTls: str


class ClusterOperationInfoTypeDef(TypedDict, total=False):
    ClientRequestId: str
    ClusterArn: str
    CreationTime: datetime
    EndTime: datetime
    ErrorInfo: "ErrorInfoTypeDef"
    OperationArn: str
    OperationState: str
    OperationSteps: List["ClusterOperationStepTypeDef"]
    OperationType: str
    SourceClusterInfo: "MutableClusterInfoTypeDef"
    TargetClusterInfo: "MutableClusterInfoTypeDef"


class ClusterOperationStepInfoTypeDef(TypedDict, total=False):
    StepStatus: str


class ClusterOperationStepTypeDef(TypedDict, total=False):
    StepInfo: "ClusterOperationStepInfoTypeDef"
    StepName: str


class CompatibleKafkaVersionTypeDef(TypedDict, total=False):
    SourceVersion: str
    TargetVersions: List[str]


class ConfigurationInfoTypeDef(TypedDict):
    Arn: str
    Revision: int


class _RequiredConfigurationRevisionTypeDef(TypedDict):
    CreationTime: datetime
    Revision: int


class ConfigurationRevisionTypeDef(_RequiredConfigurationRevisionTypeDef, total=False):
    Description: str


class ConfigurationTypeDef(TypedDict):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    State: ConfigurationState


class CreateClusterResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterName: str
    State: ClusterState


class CreateConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    State: ConfigurationState


class DeleteClusterResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    State: ClusterState


class DeleteConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    State: ConfigurationState


class DescribeClusterOperationResponseTypeDef(TypedDict, total=False):
    ClusterOperationInfo: "ClusterOperationInfoTypeDef"


class DescribeClusterResponseTypeDef(TypedDict, total=False):
    ClusterInfo: "ClusterInfoTypeDef"


class DescribeConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    Description: str
    KafkaVersions: List[str]
    LatestRevision: "ConfigurationRevisionTypeDef"
    Name: str
    State: ConfigurationState


class DescribeConfigurationRevisionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    Description: str
    Revision: int
    ServerProperties: Union[bytes, IO[bytes]]


class EBSStorageInfoTypeDef(TypedDict, total=False):
    VolumeSize: int


class EncryptionAtRestTypeDef(TypedDict):
    DataVolumeKMSKeyId: str


class EncryptionInTransitTypeDef(TypedDict, total=False):
    ClientBroker: ClientBroker
    InCluster: bool


class EncryptionInfoTypeDef(TypedDict, total=False):
    EncryptionAtRest: "EncryptionAtRestTypeDef"
    EncryptionInTransit: "EncryptionInTransitTypeDef"


class ErrorInfoTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorString: str


class _RequiredFirehoseTypeDef(TypedDict):
    Enabled: bool


class FirehoseTypeDef(_RequiredFirehoseTypeDef, total=False):
    DeliveryStream: str


class GetBootstrapBrokersResponseTypeDef(TypedDict, total=False):
    BootstrapBrokerString: str
    BootstrapBrokerStringTls: str
    BootstrapBrokerStringSaslScram: str
    BootstrapBrokerStringSaslIam: str


class GetCompatibleKafkaVersionsResponseTypeDef(TypedDict, total=False):
    CompatibleKafkaVersions: List["CompatibleKafkaVersionTypeDef"]


class IamTypeDef(TypedDict, total=False):
    Enabled: bool


class JmxExporterInfoTypeDef(TypedDict):
    EnabledInBroker: bool


class JmxExporterTypeDef(TypedDict):
    EnabledInBroker: bool


class KafkaVersionTypeDef(TypedDict, total=False):
    Version: str
    Status: KafkaVersionStatus


class ListClusterOperationsResponseTypeDef(TypedDict, total=False):
    ClusterOperationInfoList: List["ClusterOperationInfoTypeDef"]
    NextToken: str


class ListClustersResponseTypeDef(TypedDict, total=False):
    ClusterInfoList: List["ClusterInfoTypeDef"]
    NextToken: str


class ListConfigurationRevisionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Revisions: List["ConfigurationRevisionTypeDef"]


class ListConfigurationsResponseTypeDef(TypedDict, total=False):
    Configurations: List["ConfigurationTypeDef"]
    NextToken: str


class ListKafkaVersionsResponseTypeDef(TypedDict, total=False):
    KafkaVersions: List["KafkaVersionTypeDef"]
    NextToken: str


class ListNodesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    NodeInfoList: List["NodeInfoTypeDef"]


class ListScramSecretsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    SecretArnList: List[str]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class LoggingInfoTypeDef(TypedDict):
    BrokerLogs: "BrokerLogsTypeDef"


class MutableClusterInfoTypeDef(TypedDict, total=False):
    BrokerEBSVolumeInfo: List["BrokerEBSVolumeInfoTypeDef"]
    ConfigurationInfo: "ConfigurationInfoTypeDef"
    NumberOfBrokerNodes: int
    EnhancedMonitoring: EnhancedMonitoring
    OpenMonitoring: "OpenMonitoringTypeDef"
    KafkaVersion: str
    LoggingInfo: "LoggingInfoTypeDef"
    InstanceType: str


class NodeExporterInfoTypeDef(TypedDict):
    EnabledInBroker: bool


class NodeExporterTypeDef(TypedDict):
    EnabledInBroker: bool


class NodeInfoTypeDef(TypedDict, total=False):
    AddedToClusterTime: str
    BrokerNodeInfo: "BrokerNodeInfoTypeDef"
    InstanceType: str
    NodeARN: str
    NodeType: Literal["BROKER"]
    ZookeeperNodeInfo: "ZookeeperNodeInfoTypeDef"


class OpenMonitoringInfoTypeDef(TypedDict):
    Prometheus: "PrometheusInfoTypeDef"


class OpenMonitoringTypeDef(TypedDict):
    Prometheus: "PrometheusTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PrometheusInfoTypeDef(TypedDict, total=False):
    JmxExporter: "JmxExporterInfoTypeDef"
    NodeExporter: "NodeExporterInfoTypeDef"


class PrometheusTypeDef(TypedDict, total=False):
    JmxExporter: "JmxExporterTypeDef"
    NodeExporter: "NodeExporterTypeDef"


class RebootBrokerResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class _RequiredS3TypeDef(TypedDict):
    Enabled: bool


class S3TypeDef(_RequiredS3TypeDef, total=False):
    Bucket: str
    Prefix: str


class SaslTypeDef(TypedDict, total=False):
    Scram: "ScramTypeDef"
    Iam: "IamTypeDef"


class ScramTypeDef(TypedDict, total=False):
    Enabled: bool


class StateInfoTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class StorageInfoTypeDef(TypedDict, total=False):
    EbsStorageInfo: "EBSStorageInfoTypeDef"


class TlsTypeDef(TypedDict, total=False):
    CertificateAuthorityArnList: List[str]


class UnprocessedScramSecretTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str
    SecretArn: str


class UpdateBrokerCountResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class UpdateBrokerStorageResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class UpdateBrokerTypeResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class UpdateClusterConfigurationResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class UpdateClusterKafkaVersionResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class UpdateConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    LatestRevision: "ConfigurationRevisionTypeDef"


class UpdateMonitoringResponseTypeDef(TypedDict, total=False):
    ClusterArn: str
    ClusterOperationArn: str


class ZookeeperNodeInfoTypeDef(TypedDict, total=False):
    AttachedENIId: str
    ClientVpcIpAddress: str
    Endpoints: List[str]
    ZookeeperId: float
    ZookeeperVersion: str
