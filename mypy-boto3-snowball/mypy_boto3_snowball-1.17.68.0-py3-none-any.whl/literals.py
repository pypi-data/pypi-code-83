"""
Type annotations for snowball service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/literals.html)

Usage::

    ```python
    from mypy_boto3_snowball.literals import ClusterState

    data: ClusterState = "AwaitingQuorum"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ClusterState",
    "DescribeAddressesPaginatorName",
    "JobState",
    "JobType",
    "ListClusterJobsPaginatorName",
    "ListClustersPaginatorName",
    "ListCompatibleImagesPaginatorName",
    "ListJobsPaginatorName",
    "LongTermPricingType",
    "ShipmentState",
    "ShippingLabelStatus",
    "ShippingOption",
    "SnowballCapacity",
    "SnowballType",
)


ClusterState = Literal["AwaitingQuorum", "Cancelled", "Complete", "InUse", "Pending"]
DescribeAddressesPaginatorName = Literal["describe_addresses"]
JobState = Literal[
    "Cancelled",
    "Complete",
    "InProgress",
    "InTransitToAWS",
    "InTransitToCustomer",
    "Listing",
    "New",
    "Pending",
    "PreparingAppliance",
    "PreparingShipment",
    "WithAWS",
    "WithAWSSortingFacility",
    "WithCustomer",
]
JobType = Literal["EXPORT", "IMPORT", "LOCAL_USE"]
ListClusterJobsPaginatorName = Literal["list_cluster_jobs"]
ListClustersPaginatorName = Literal["list_clusters"]
ListCompatibleImagesPaginatorName = Literal["list_compatible_images"]
ListJobsPaginatorName = Literal["list_jobs"]
LongTermPricingType = Literal["OneYear", "ThreeYear"]
ShipmentState = Literal["RECEIVED", "RETURNED"]
ShippingLabelStatus = Literal["Failed", "InProgress", "Succeeded", "TimedOut"]
ShippingOption = Literal["EXPRESS", "NEXT_DAY", "SECOND_DAY", "STANDARD"]
SnowballCapacity = Literal["NoPreference", "T100", "T14", "T42", "T50", "T8", "T80", "T98"]
SnowballType = Literal["EDGE", "EDGE_C", "EDGE_CG", "EDGE_S", "SNC1_HDD", "SNC1_SSD", "STANDARD"]
