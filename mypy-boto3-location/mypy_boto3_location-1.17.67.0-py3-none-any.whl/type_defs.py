"""
Type annotations for location service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/type_defs.html)

Usage::

    ```python
    from mypy_boto3_location.type_defs import BatchDeleteGeofenceErrorTypeDef

    data: BatchDeleteGeofenceErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_location.literals import BatchItemErrorCode, IntendedUse, PricingPlan

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchDeleteGeofenceErrorTypeDef",
    "BatchDeleteGeofenceResponseTypeDef",
    "BatchEvaluateGeofencesErrorTypeDef",
    "BatchEvaluateGeofencesResponseTypeDef",
    "BatchGetDevicePositionErrorTypeDef",
    "BatchGetDevicePositionResponseTypeDef",
    "BatchItemErrorTypeDef",
    "BatchPutGeofenceErrorTypeDef",
    "BatchPutGeofenceRequestEntryTypeDef",
    "BatchPutGeofenceResponseTypeDef",
    "BatchPutGeofenceSuccessTypeDef",
    "BatchUpdateDevicePositionErrorTypeDef",
    "BatchUpdateDevicePositionResponseTypeDef",
    "CreateGeofenceCollectionResponseTypeDef",
    "CreateMapResponseTypeDef",
    "CreatePlaceIndexResponseTypeDef",
    "CreateTrackerResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DescribeGeofenceCollectionResponseTypeDef",
    "DescribeMapResponseTypeDef",
    "DescribePlaceIndexResponseTypeDef",
    "DescribeTrackerResponseTypeDef",
    "DevicePositionTypeDef",
    "DevicePositionUpdateTypeDef",
    "GeofenceGeometryTypeDef",
    "GetDevicePositionHistoryResponseTypeDef",
    "GetDevicePositionResponseTypeDef",
    "GetGeofenceResponseTypeDef",
    "GetMapGlyphsResponseTypeDef",
    "GetMapSpritesResponseTypeDef",
    "GetMapStyleDescriptorResponseTypeDef",
    "GetMapTileResponseTypeDef",
    "ListGeofenceCollectionsResponseEntryTypeDef",
    "ListGeofenceCollectionsResponseTypeDef",
    "ListGeofenceResponseEntryTypeDef",
    "ListGeofencesResponseTypeDef",
    "ListMapsResponseEntryTypeDef",
    "ListMapsResponseTypeDef",
    "ListPlaceIndexesResponseEntryTypeDef",
    "ListPlaceIndexesResponseTypeDef",
    "ListTrackerConsumersResponseTypeDef",
    "ListTrackersResponseEntryTypeDef",
    "ListTrackersResponseTypeDef",
    "MapConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PlaceGeometryTypeDef",
    "PlaceTypeDef",
    "PutGeofenceResponseTypeDef",
    "SearchForPositionResultTypeDef",
    "SearchForTextResultTypeDef",
    "SearchPlaceIndexForPositionResponseTypeDef",
    "SearchPlaceIndexForPositionSummaryTypeDef",
    "SearchPlaceIndexForTextResponseTypeDef",
    "SearchPlaceIndexForTextSummaryTypeDef",
)


class BatchDeleteGeofenceErrorTypeDef(TypedDict):
    Error: "BatchItemErrorTypeDef"
    GeofenceId: str


class BatchDeleteGeofenceResponseTypeDef(TypedDict):
    Errors: List["BatchDeleteGeofenceErrorTypeDef"]


class BatchEvaluateGeofencesErrorTypeDef(TypedDict):
    DeviceId: str
    Error: "BatchItemErrorTypeDef"
    SampleTime: datetime


class BatchEvaluateGeofencesResponseTypeDef(TypedDict):
    Errors: List["BatchEvaluateGeofencesErrorTypeDef"]


class BatchGetDevicePositionErrorTypeDef(TypedDict):
    DeviceId: str
    Error: "BatchItemErrorTypeDef"


class BatchGetDevicePositionResponseTypeDef(TypedDict):
    DevicePositions: List["DevicePositionTypeDef"]
    Errors: List["BatchGetDevicePositionErrorTypeDef"]


class BatchItemErrorTypeDef(TypedDict, total=False):
    Code: BatchItemErrorCode
    Message: str


class BatchPutGeofenceErrorTypeDef(TypedDict):
    Error: "BatchItemErrorTypeDef"
    GeofenceId: str


class BatchPutGeofenceRequestEntryTypeDef(TypedDict):
    GeofenceId: str
    Geometry: "GeofenceGeometryTypeDef"


class BatchPutGeofenceResponseTypeDef(TypedDict):
    Errors: List["BatchPutGeofenceErrorTypeDef"]
    Successes: List["BatchPutGeofenceSuccessTypeDef"]


class BatchPutGeofenceSuccessTypeDef(TypedDict):
    CreateTime: datetime
    GeofenceId: str
    UpdateTime: datetime


class BatchUpdateDevicePositionErrorTypeDef(TypedDict):
    DeviceId: str
    Error: "BatchItemErrorTypeDef"
    SampleTime: datetime


class BatchUpdateDevicePositionResponseTypeDef(TypedDict):
    Errors: List["BatchUpdateDevicePositionErrorTypeDef"]


class CreateGeofenceCollectionResponseTypeDef(TypedDict):
    CollectionArn: str
    CollectionName: str
    CreateTime: datetime


class CreateMapResponseTypeDef(TypedDict):
    CreateTime: datetime
    MapArn: str
    MapName: str


class CreatePlaceIndexResponseTypeDef(TypedDict):
    CreateTime: datetime
    IndexArn: str
    IndexName: str


class CreateTrackerResponseTypeDef(TypedDict):
    CreateTime: datetime
    TrackerArn: str
    TrackerName: str


class DataSourceConfigurationTypeDef(TypedDict, total=False):
    IntendedUse: IntendedUse


class _RequiredDescribeGeofenceCollectionResponseTypeDef(TypedDict):
    CollectionArn: str
    CollectionName: str
    CreateTime: datetime
    Description: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class DescribeGeofenceCollectionResponseTypeDef(
    _RequiredDescribeGeofenceCollectionResponseTypeDef, total=False
):
    PricingPlanDataSource: str


class DescribeMapResponseTypeDef(TypedDict):
    Configuration: "MapConfigurationTypeDef"
    CreateTime: datetime
    DataSource: str
    Description: str
    MapArn: str
    MapName: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class DescribePlaceIndexResponseTypeDef(TypedDict):
    CreateTime: datetime
    DataSource: str
    DataSourceConfiguration: "DataSourceConfigurationTypeDef"
    Description: str
    IndexArn: str
    IndexName: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class _RequiredDescribeTrackerResponseTypeDef(TypedDict):
    CreateTime: datetime
    Description: str
    PricingPlan: PricingPlan
    TrackerArn: str
    TrackerName: str
    UpdateTime: datetime


class DescribeTrackerResponseTypeDef(_RequiredDescribeTrackerResponseTypeDef, total=False):
    PricingPlanDataSource: str


class _RequiredDevicePositionTypeDef(TypedDict):
    Position: List[float]
    ReceivedTime: datetime
    SampleTime: datetime


class DevicePositionTypeDef(_RequiredDevicePositionTypeDef, total=False):
    DeviceId: str


class DevicePositionUpdateTypeDef(TypedDict):
    DeviceId: str
    Position: List[float]
    SampleTime: datetime


class GeofenceGeometryTypeDef(TypedDict, total=False):
    Polygon: List[List[List[float]]]


class _RequiredGetDevicePositionHistoryResponseTypeDef(TypedDict):
    DevicePositions: List["DevicePositionTypeDef"]


class GetDevicePositionHistoryResponseTypeDef(
    _RequiredGetDevicePositionHistoryResponseTypeDef, total=False
):
    NextToken: str


class _RequiredGetDevicePositionResponseTypeDef(TypedDict):
    Position: List[float]
    ReceivedTime: datetime
    SampleTime: datetime


class GetDevicePositionResponseTypeDef(_RequiredGetDevicePositionResponseTypeDef, total=False):
    DeviceId: str


class GetGeofenceResponseTypeDef(TypedDict):
    CreateTime: datetime
    GeofenceId: str
    Geometry: "GeofenceGeometryTypeDef"
    Status: str
    UpdateTime: datetime


class GetMapGlyphsResponseTypeDef(TypedDict, total=False):
    Blob: Union[bytes, IO[bytes]]
    ContentType: str


class GetMapSpritesResponseTypeDef(TypedDict, total=False):
    Blob: Union[bytes, IO[bytes]]
    ContentType: str


class GetMapStyleDescriptorResponseTypeDef(TypedDict, total=False):
    Blob: Union[bytes, IO[bytes]]
    ContentType: str


class GetMapTileResponseTypeDef(TypedDict, total=False):
    Blob: Union[bytes, IO[bytes]]
    ContentType: str


class _RequiredListGeofenceCollectionsResponseEntryTypeDef(TypedDict):
    CollectionName: str
    CreateTime: datetime
    Description: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class ListGeofenceCollectionsResponseEntryTypeDef(
    _RequiredListGeofenceCollectionsResponseEntryTypeDef, total=False
):
    PricingPlanDataSource: str


class _RequiredListGeofenceCollectionsResponseTypeDef(TypedDict):
    Entries: List["ListGeofenceCollectionsResponseEntryTypeDef"]


class ListGeofenceCollectionsResponseTypeDef(
    _RequiredListGeofenceCollectionsResponseTypeDef, total=False
):
    NextToken: str


class ListGeofenceResponseEntryTypeDef(TypedDict):
    CreateTime: datetime
    GeofenceId: str
    Geometry: "GeofenceGeometryTypeDef"
    Status: str
    UpdateTime: datetime


class _RequiredListGeofencesResponseTypeDef(TypedDict):
    Entries: List["ListGeofenceResponseEntryTypeDef"]


class ListGeofencesResponseTypeDef(_RequiredListGeofencesResponseTypeDef, total=False):
    NextToken: str


class ListMapsResponseEntryTypeDef(TypedDict):
    CreateTime: datetime
    DataSource: str
    Description: str
    MapName: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class _RequiredListMapsResponseTypeDef(TypedDict):
    Entries: List["ListMapsResponseEntryTypeDef"]


class ListMapsResponseTypeDef(_RequiredListMapsResponseTypeDef, total=False):
    NextToken: str


class ListPlaceIndexesResponseEntryTypeDef(TypedDict):
    CreateTime: datetime
    DataSource: str
    Description: str
    IndexName: str
    PricingPlan: PricingPlan
    UpdateTime: datetime


class _RequiredListPlaceIndexesResponseTypeDef(TypedDict):
    Entries: List["ListPlaceIndexesResponseEntryTypeDef"]


class ListPlaceIndexesResponseTypeDef(_RequiredListPlaceIndexesResponseTypeDef, total=False):
    NextToken: str


class _RequiredListTrackerConsumersResponseTypeDef(TypedDict):
    ConsumerArns: List[str]


class ListTrackerConsumersResponseTypeDef(
    _RequiredListTrackerConsumersResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListTrackersResponseEntryTypeDef(TypedDict):
    CreateTime: datetime
    Description: str
    PricingPlan: PricingPlan
    TrackerName: str
    UpdateTime: datetime


class ListTrackersResponseEntryTypeDef(_RequiredListTrackersResponseEntryTypeDef, total=False):
    PricingPlanDataSource: str


class _RequiredListTrackersResponseTypeDef(TypedDict):
    Entries: List["ListTrackersResponseEntryTypeDef"]


class ListTrackersResponseTypeDef(_RequiredListTrackersResponseTypeDef, total=False):
    NextToken: str


class MapConfigurationTypeDef(TypedDict):
    Style: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlaceGeometryTypeDef(TypedDict, total=False):
    Point: List[float]


class _RequiredPlaceTypeDef(TypedDict):
    Geometry: "PlaceGeometryTypeDef"


class PlaceTypeDef(_RequiredPlaceTypeDef, total=False):
    AddressNumber: str
    Country: str
    Label: str
    Municipality: str
    Neighborhood: str
    PostalCode: str
    Region: str
    Street: str
    SubRegion: str


class PutGeofenceResponseTypeDef(TypedDict):
    CreateTime: datetime
    GeofenceId: str
    UpdateTime: datetime


class SearchForPositionResultTypeDef(TypedDict):
    Place: "PlaceTypeDef"


class SearchForTextResultTypeDef(TypedDict):
    Place: "PlaceTypeDef"


class SearchPlaceIndexForPositionResponseTypeDef(TypedDict):
    Results: List["SearchForPositionResultTypeDef"]
    Summary: "SearchPlaceIndexForPositionSummaryTypeDef"


class _RequiredSearchPlaceIndexForPositionSummaryTypeDef(TypedDict):
    DataSource: str
    Position: List[float]


class SearchPlaceIndexForPositionSummaryTypeDef(
    _RequiredSearchPlaceIndexForPositionSummaryTypeDef, total=False
):
    MaxResults: int


class SearchPlaceIndexForTextResponseTypeDef(TypedDict):
    Results: List["SearchForTextResultTypeDef"]
    Summary: "SearchPlaceIndexForTextSummaryTypeDef"


_RequiredSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_RequiredSearchPlaceIndexForTextSummaryTypeDef", {"DataSource": str, "Text": str}
)
_OptionalSearchPlaceIndexForTextSummaryTypeDef = TypedDict(
    "_OptionalSearchPlaceIndexForTextSummaryTypeDef",
    {
        "BiasPosition": List[float],
        "FilterBBox": List[float],
        "FilterCountries": List[str],
        "MaxResults": int,
        "ResultBBox": List[float],
    },
    total=False,
)


class SearchPlaceIndexForTextSummaryTypeDef(
    _RequiredSearchPlaceIndexForTextSummaryTypeDef, _OptionalSearchPlaceIndexForTextSummaryTypeDef
):
    pass
