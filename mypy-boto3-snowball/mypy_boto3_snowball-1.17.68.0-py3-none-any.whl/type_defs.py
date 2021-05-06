"""
Type annotations for snowball service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_snowball/type_defs.html)

Usage::

    ```python
    from mypy_boto3_snowball.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_snowball.literals import (
    ClusterState,
    JobState,
    JobType,
    LongTermPricingType,
    ShippingLabelStatus,
    ShippingOption,
    SnowballCapacity,
    SnowballType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddressTypeDef",
    "ClusterListEntryTypeDef",
    "ClusterMetadataTypeDef",
    "CompatibleImageTypeDef",
    "CreateAddressResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateLongTermPricingResultTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DataTransferTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsResultTypeDef",
    "ListLongTermPricingResultTypeDef",
    "LongTermPricingListEntryTypeDef",
    "NotificationTypeDef",
    "PaginatorConfigTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TaxDocumentsTypeDef",
    "WirelessConnectionTypeDef",
)


class AddressTypeDef(TypedDict, total=False):
    AddressId: str
    Name: str
    Company: str
    Street1: str
    Street2: str
    Street3: str
    City: str
    StateOrProvince: str
    PrefectureOrDistrict: str
    Landmark: str
    Country: str
    PostalCode: str
    PhoneNumber: str
    IsRestricted: bool


class ClusterListEntryTypeDef(TypedDict, total=False):
    ClusterId: str
    ClusterState: ClusterState
    CreationDate: datetime
    Description: str


class ClusterMetadataTypeDef(TypedDict, total=False):
    ClusterId: str
    Description: str
    KmsKeyARN: str
    RoleARN: str
    ClusterState: ClusterState
    JobType: JobType
    SnowballType: SnowballType
    CreationDate: datetime
    Resources: "JobResourceTypeDef"
    AddressId: str
    ShippingOption: ShippingOption
    Notification: "NotificationTypeDef"
    ForwardingAddressId: str
    TaxDocuments: "TaxDocumentsTypeDef"


class CompatibleImageTypeDef(TypedDict, total=False):
    AmiId: str
    Name: str


class CreateAddressResultTypeDef(TypedDict, total=False):
    AddressId: str


class CreateClusterResultTypeDef(TypedDict, total=False):
    ClusterId: str


class CreateJobResultTypeDef(TypedDict, total=False):
    JobId: str


class CreateLongTermPricingResultTypeDef(TypedDict, total=False):
    LongTermPricingId: str


class CreateReturnShippingLabelResultTypeDef(TypedDict, total=False):
    Status: ShippingLabelStatus


class DataTransferTypeDef(TypedDict, total=False):
    BytesTransferred: int
    ObjectsTransferred: int
    TotalBytes: int
    TotalObjects: int


class DescribeAddressResultTypeDef(TypedDict, total=False):
    Address: "AddressTypeDef"


class DescribeAddressesResultTypeDef(TypedDict, total=False):
    Addresses: List["AddressTypeDef"]
    NextToken: str


class DescribeClusterResultTypeDef(TypedDict, total=False):
    ClusterMetadata: "ClusterMetadataTypeDef"


class DescribeJobResultTypeDef(TypedDict, total=False):
    JobMetadata: "JobMetadataTypeDef"
    SubJobMetadata: List["JobMetadataTypeDef"]


class DescribeReturnShippingLabelResultTypeDef(TypedDict, total=False):
    Status: ShippingLabelStatus
    ExpirationDate: datetime


class DeviceConfigurationTypeDef(TypedDict, total=False):
    SnowconeDeviceConfiguration: "SnowconeDeviceConfigurationTypeDef"


class _RequiredEc2AmiResourceTypeDef(TypedDict):
    AmiId: str


class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, total=False):
    SnowballAmiId: str


class EventTriggerDefinitionTypeDef(TypedDict, total=False):
    EventResourceARN: str


class GetJobManifestResultTypeDef(TypedDict, total=False):
    ManifestURI: str


class GetJobUnlockCodeResultTypeDef(TypedDict, total=False):
    UnlockCode: str


class GetSnowballUsageResultTypeDef(TypedDict, total=False):
    SnowballLimit: int
    SnowballsInUse: int


class GetSoftwareUpdatesResultTypeDef(TypedDict, total=False):
    UpdatesURI: str


class INDTaxDocumentsTypeDef(TypedDict, total=False):
    GSTIN: str


class JobListEntryTypeDef(TypedDict, total=False):
    JobId: str
    JobState: JobState
    IsMaster: bool
    JobType: JobType
    SnowballType: SnowballType
    CreationDate: datetime
    Description: str


class JobLogsTypeDef(TypedDict, total=False):
    JobCompletionReportURI: str
    JobSuccessLogURI: str
    JobFailureLogURI: str


class JobMetadataTypeDef(TypedDict, total=False):
    JobId: str
    JobState: JobState
    JobType: JobType
    SnowballType: SnowballType
    CreationDate: datetime
    Resources: "JobResourceTypeDef"
    Description: str
    KmsKeyARN: str
    RoleARN: str
    AddressId: str
    ShippingDetails: "ShippingDetailsTypeDef"
    SnowballCapacityPreference: SnowballCapacity
    Notification: "NotificationTypeDef"
    DataTransferProgress: "DataTransferTypeDef"
    JobLogInfo: "JobLogsTypeDef"
    ClusterId: str
    ForwardingAddressId: str
    TaxDocuments: "TaxDocumentsTypeDef"
    DeviceConfiguration: "DeviceConfigurationTypeDef"
    LongTermPricingId: str


class JobResourceTypeDef(TypedDict, total=False):
    S3Resources: List["S3ResourceTypeDef"]
    LambdaResources: List["LambdaResourceTypeDef"]
    Ec2AmiResources: List["Ec2AmiResourceTypeDef"]


class KeyRangeTypeDef(TypedDict, total=False):
    BeginMarker: str
    EndMarker: str


class LambdaResourceTypeDef(TypedDict, total=False):
    LambdaArn: str
    EventTriggers: List["EventTriggerDefinitionTypeDef"]


class ListClusterJobsResultTypeDef(TypedDict, total=False):
    JobListEntries: List["JobListEntryTypeDef"]
    NextToken: str


class ListClustersResultTypeDef(TypedDict, total=False):
    ClusterListEntries: List["ClusterListEntryTypeDef"]
    NextToken: str


class ListCompatibleImagesResultTypeDef(TypedDict, total=False):
    CompatibleImages: List["CompatibleImageTypeDef"]
    NextToken: str


class ListJobsResultTypeDef(TypedDict, total=False):
    JobListEntries: List["JobListEntryTypeDef"]
    NextToken: str


class ListLongTermPricingResultTypeDef(TypedDict, total=False):
    LongTermPricingEntries: List["LongTermPricingListEntryTypeDef"]
    NextToken: str


class LongTermPricingListEntryTypeDef(TypedDict, total=False):
    LongTermPricingId: str
    LongTermPricingEndDate: datetime
    LongTermPricingStartDate: datetime
    LongTermPricingType: LongTermPricingType
    CurrentActiveJob: str
    ReplacementJob: str
    IsLongTermPricingAutoRenew: bool
    LongTermPricingStatus: str
    SnowballType: SnowballType
    JobIds: List[str]


class NotificationTypeDef(TypedDict, total=False):
    SnsTopicARN: str
    JobStatesToNotify: List[JobState]
    NotifyAll: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class S3ResourceTypeDef(TypedDict, total=False):
    BucketArn: str
    KeyRange: "KeyRangeTypeDef"


class ShipmentTypeDef(TypedDict, total=False):
    Status: str
    TrackingNumber: str


class ShippingDetailsTypeDef(TypedDict, total=False):
    ShippingOption: ShippingOption
    InboundShipment: "ShipmentTypeDef"
    OutboundShipment: "ShipmentTypeDef"


class SnowconeDeviceConfigurationTypeDef(TypedDict, total=False):
    WirelessConnection: "WirelessConnectionTypeDef"


class TaxDocumentsTypeDef(TypedDict, total=False):
    IND: "INDTaxDocumentsTypeDef"


class WirelessConnectionTypeDef(TypedDict, total=False):
    IsWifiEnabled: bool
