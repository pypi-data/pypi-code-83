"""
Main interface for snowball service type definitions.

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
    "DataTransferTypeDef",
    "DeviceConfigurationTypeDef",
    "Ec2AmiResourceTypeDef",
    "EventTriggerDefinitionTypeDef",
    "INDTaxDocumentsTypeDef",
    "JobListEntryTypeDef",
    "JobLogsTypeDef",
    "JobMetadataTypeDef",
    "JobResourceTypeDef",
    "KeyRangeTypeDef",
    "LambdaResourceTypeDef",
    "NotificationTypeDef",
    "S3ResourceTypeDef",
    "ShipmentTypeDef",
    "ShippingDetailsTypeDef",
    "SnowconeDeviceConfigurationTypeDef",
    "TaxDocumentsTypeDef",
    "WirelessConnectionTypeDef",
    "CreateAddressResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateJobResultTypeDef",
    "CreateReturnShippingLabelResultTypeDef",
    "DescribeAddressResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeClusterResultTypeDef",
    "DescribeJobResultTypeDef",
    "DescribeReturnShippingLabelResultTypeDef",
    "GetJobManifestResultTypeDef",
    "GetJobUnlockCodeResultTypeDef",
    "GetSnowballUsageResultTypeDef",
    "GetSoftwareUpdatesResultTypeDef",
    "ListClusterJobsResultTypeDef",
    "ListClustersResultTypeDef",
    "ListCompatibleImagesResultTypeDef",
    "ListJobsResultTypeDef",
    "PaginatorConfigTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "AddressId": str,
        "Name": str,
        "Company": str,
        "Street1": str,
        "Street2": str,
        "Street3": str,
        "City": str,
        "StateOrProvince": str,
        "PrefectureOrDistrict": str,
        "Landmark": str,
        "Country": str,
        "PostalCode": str,
        "PhoneNumber": str,
        "IsRestricted": bool,
    },
    total=False,
)

ClusterListEntryTypeDef = TypedDict(
    "ClusterListEntryTypeDef",
    {"ClusterId": str, "ClusterState": ClusterState, "CreationDate": datetime, "Description": str},
    total=False,
)

ClusterMetadataTypeDef = TypedDict(
    "ClusterMetadataTypeDef",
    {
        "ClusterId": str,
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "ClusterState": ClusterState,
        "JobType": JobType,
        "SnowballType": SnowballType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "AddressId": str,
        "ShippingOption": ShippingOption,
        "Notification": "NotificationTypeDef",
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
    },
    total=False,
)

CompatibleImageTypeDef = TypedDict(
    "CompatibleImageTypeDef", {"AmiId": str, "Name": str}, total=False
)

DataTransferTypeDef = TypedDict(
    "DataTransferTypeDef",
    {"BytesTransferred": int, "ObjectsTransferred": int, "TotalBytes": int, "TotalObjects": int},
    total=False,
)

DeviceConfigurationTypeDef = TypedDict(
    "DeviceConfigurationTypeDef",
    {"SnowconeDeviceConfiguration": "SnowconeDeviceConfigurationTypeDef"},
    total=False,
)

_RequiredEc2AmiResourceTypeDef = TypedDict("_RequiredEc2AmiResourceTypeDef", {"AmiId": str})
_OptionalEc2AmiResourceTypeDef = TypedDict(
    "_OptionalEc2AmiResourceTypeDef", {"SnowballAmiId": str}, total=False
)


class Ec2AmiResourceTypeDef(_RequiredEc2AmiResourceTypeDef, _OptionalEc2AmiResourceTypeDef):
    pass


EventTriggerDefinitionTypeDef = TypedDict(
    "EventTriggerDefinitionTypeDef", {"EventResourceARN": str}, total=False
)

INDTaxDocumentsTypeDef = TypedDict("INDTaxDocumentsTypeDef", {"GSTIN": str}, total=False)

JobListEntryTypeDef = TypedDict(
    "JobListEntryTypeDef",
    {
        "JobId": str,
        "JobState": JobState,
        "IsMaster": bool,
        "JobType": JobType,
        "SnowballType": SnowballType,
        "CreationDate": datetime,
        "Description": str,
    },
    total=False,
)

JobLogsTypeDef = TypedDict(
    "JobLogsTypeDef",
    {"JobCompletionReportURI": str, "JobSuccessLogURI": str, "JobFailureLogURI": str},
    total=False,
)

JobMetadataTypeDef = TypedDict(
    "JobMetadataTypeDef",
    {
        "JobId": str,
        "JobState": JobState,
        "JobType": JobType,
        "SnowballType": SnowballType,
        "CreationDate": datetime,
        "Resources": "JobResourceTypeDef",
        "Description": str,
        "KmsKeyARN": str,
        "RoleARN": str,
        "AddressId": str,
        "ShippingDetails": "ShippingDetailsTypeDef",
        "SnowballCapacityPreference": SnowballCapacity,
        "Notification": "NotificationTypeDef",
        "DataTransferProgress": "DataTransferTypeDef",
        "JobLogInfo": "JobLogsTypeDef",
        "ClusterId": str,
        "ForwardingAddressId": str,
        "TaxDocuments": "TaxDocumentsTypeDef",
        "DeviceConfiguration": "DeviceConfigurationTypeDef",
    },
    total=False,
)

JobResourceTypeDef = TypedDict(
    "JobResourceTypeDef",
    {
        "S3Resources": List["S3ResourceTypeDef"],
        "LambdaResources": List["LambdaResourceTypeDef"],
        "Ec2AmiResources": List["Ec2AmiResourceTypeDef"],
    },
    total=False,
)

KeyRangeTypeDef = TypedDict("KeyRangeTypeDef", {"BeginMarker": str, "EndMarker": str}, total=False)

LambdaResourceTypeDef = TypedDict(
    "LambdaResourceTypeDef",
    {"LambdaArn": str, "EventTriggers": List["EventTriggerDefinitionTypeDef"]},
    total=False,
)

NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {"SnsTopicARN": str, "JobStatesToNotify": List[JobState], "NotifyAll": bool},
    total=False,
)

S3ResourceTypeDef = TypedDict(
    "S3ResourceTypeDef", {"BucketArn": str, "KeyRange": "KeyRangeTypeDef"}, total=False
)

ShipmentTypeDef = TypedDict("ShipmentTypeDef", {"Status": str, "TrackingNumber": str}, total=False)

ShippingDetailsTypeDef = TypedDict(
    "ShippingDetailsTypeDef",
    {
        "ShippingOption": ShippingOption,
        "InboundShipment": "ShipmentTypeDef",
        "OutboundShipment": "ShipmentTypeDef",
    },
    total=False,
)

SnowconeDeviceConfigurationTypeDef = TypedDict(
    "SnowconeDeviceConfigurationTypeDef",
    {"WirelessConnection": "WirelessConnectionTypeDef"},
    total=False,
)

TaxDocumentsTypeDef = TypedDict(
    "TaxDocumentsTypeDef", {"IND": "INDTaxDocumentsTypeDef"}, total=False
)

WirelessConnectionTypeDef = TypedDict(
    "WirelessConnectionTypeDef", {"IsWifiEnabled": bool}, total=False
)

CreateAddressResultTypeDef = TypedDict(
    "CreateAddressResultTypeDef", {"AddressId": str}, total=False
)

CreateClusterResultTypeDef = TypedDict(
    "CreateClusterResultTypeDef", {"ClusterId": str}, total=False
)

CreateJobResultTypeDef = TypedDict("CreateJobResultTypeDef", {"JobId": str}, total=False)

CreateReturnShippingLabelResultTypeDef = TypedDict(
    "CreateReturnShippingLabelResultTypeDef", {"Status": ShippingLabelStatus}, total=False
)

DescribeAddressResultTypeDef = TypedDict(
    "DescribeAddressResultTypeDef", {"Address": "AddressTypeDef"}, total=False
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {"Addresses": List["AddressTypeDef"], "NextToken": str},
    total=False,
)

DescribeClusterResultTypeDef = TypedDict(
    "DescribeClusterResultTypeDef", {"ClusterMetadata": "ClusterMetadataTypeDef"}, total=False
)

DescribeJobResultTypeDef = TypedDict(
    "DescribeJobResultTypeDef",
    {"JobMetadata": "JobMetadataTypeDef", "SubJobMetadata": List["JobMetadataTypeDef"]},
    total=False,
)

DescribeReturnShippingLabelResultTypeDef = TypedDict(
    "DescribeReturnShippingLabelResultTypeDef",
    {"Status": ShippingLabelStatus, "ExpirationDate": datetime},
    total=False,
)

GetJobManifestResultTypeDef = TypedDict(
    "GetJobManifestResultTypeDef", {"ManifestURI": str}, total=False
)

GetJobUnlockCodeResultTypeDef = TypedDict(
    "GetJobUnlockCodeResultTypeDef", {"UnlockCode": str}, total=False
)

GetSnowballUsageResultTypeDef = TypedDict(
    "GetSnowballUsageResultTypeDef", {"SnowballLimit": int, "SnowballsInUse": int}, total=False
)

GetSoftwareUpdatesResultTypeDef = TypedDict(
    "GetSoftwareUpdatesResultTypeDef", {"UpdatesURI": str}, total=False
)

ListClusterJobsResultTypeDef = TypedDict(
    "ListClusterJobsResultTypeDef",
    {"JobListEntries": List["JobListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListClustersResultTypeDef = TypedDict(
    "ListClustersResultTypeDef",
    {"ClusterListEntries": List["ClusterListEntryTypeDef"], "NextToken": str},
    total=False,
)

ListCompatibleImagesResultTypeDef = TypedDict(
    "ListCompatibleImagesResultTypeDef",
    {"CompatibleImages": List["CompatibleImageTypeDef"], "NextToken": str},
    total=False,
)

ListJobsResultTypeDef = TypedDict(
    "ListJobsResultTypeDef",
    {"JobListEntries": List["JobListEntryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
