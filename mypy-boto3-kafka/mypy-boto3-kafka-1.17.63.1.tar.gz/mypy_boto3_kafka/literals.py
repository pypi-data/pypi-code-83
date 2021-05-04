"""
Type annotations for kafka service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafka/literals.html)

Usage::

    ```python
    from mypy_boto3_kafka.literals import BrokerAZDistribution

    data: BrokerAZDistribution = "DEFAULT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BrokerAZDistribution",
    "ClientBroker",
    "ClusterState",
    "ConfigurationState",
    "EnhancedMonitoring",
    "KafkaVersionStatus",
    "ListClusterOperationsPaginatorName",
    "ListClustersPaginatorName",
    "ListConfigurationRevisionsPaginatorName",
    "ListConfigurationsPaginatorName",
    "ListKafkaVersionsPaginatorName",
    "ListNodesPaginatorName",
    "ListScramSecretsPaginatorName",
    "NodeType",
)


BrokerAZDistribution = Literal["DEFAULT"]
ClientBroker = Literal["PLAINTEXT", "TLS", "TLS_PLAINTEXT"]
ClusterState = Literal[
    "ACTIVE",
    "CREATING",
    "DELETING",
    "FAILED",
    "HEALING",
    "MAINTENANCE",
    "REBOOTING_BROKER",
    "UPDATING",
]
ConfigurationState = Literal["ACTIVE", "DELETE_FAILED", "DELETING"]
EnhancedMonitoring = Literal[
    "DEFAULT", "PER_BROKER", "PER_TOPIC_PER_BROKER", "PER_TOPIC_PER_PARTITION"
]
KafkaVersionStatus = Literal["ACTIVE", "DEPRECATED"]
ListClusterOperationsPaginatorName = Literal["list_cluster_operations"]
ListClustersPaginatorName = Literal["list_clusters"]
ListConfigurationRevisionsPaginatorName = Literal["list_configuration_revisions"]
ListConfigurationsPaginatorName = Literal["list_configurations"]
ListKafkaVersionsPaginatorName = Literal["list_kafka_versions"]
ListNodesPaginatorName = Literal["list_nodes"]
ListScramSecretsPaginatorName = Literal["list_scram_secrets"]
NodeType = Literal["BROKER"]
