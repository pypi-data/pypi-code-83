"""
Type annotations for location service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_location import LocationServiceClient

    client: LocationServiceClient = boto3.client("location")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_location.literals import PricingPlan
from mypy_boto3_location.paginator import (
    GetDevicePositionHistoryPaginator,
    ListGeofenceCollectionsPaginator,
    ListGeofencesPaginator,
    ListMapsPaginator,
    ListPlaceIndexesPaginator,
    ListTrackerConsumersPaginator,
    ListTrackersPaginator,
)
from mypy_boto3_location.type_defs import (
    BatchDeleteGeofenceResponseTypeDef,
    BatchEvaluateGeofencesResponseTypeDef,
    BatchGetDevicePositionResponseTypeDef,
    BatchPutGeofenceRequestEntryTypeDef,
    BatchPutGeofenceResponseTypeDef,
    BatchUpdateDevicePositionResponseTypeDef,
    CreateGeofenceCollectionResponseTypeDef,
    CreateMapResponseTypeDef,
    CreatePlaceIndexResponseTypeDef,
    CreateTrackerResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DescribeGeofenceCollectionResponseTypeDef,
    DescribeMapResponseTypeDef,
    DescribePlaceIndexResponseTypeDef,
    DescribeTrackerResponseTypeDef,
    DevicePositionUpdateTypeDef,
    GeofenceGeometryTypeDef,
    GetDevicePositionHistoryResponseTypeDef,
    GetDevicePositionResponseTypeDef,
    GetGeofenceResponseTypeDef,
    GetMapGlyphsResponseTypeDef,
    GetMapSpritesResponseTypeDef,
    GetMapStyleDescriptorResponseTypeDef,
    GetMapTileResponseTypeDef,
    ListGeofenceCollectionsResponseTypeDef,
    ListGeofencesResponseTypeDef,
    ListMapsResponseTypeDef,
    ListPlaceIndexesResponseTypeDef,
    ListTrackerConsumersResponseTypeDef,
    ListTrackersResponseTypeDef,
    MapConfigurationTypeDef,
    PutGeofenceResponseTypeDef,
    SearchPlaceIndexForPositionResponseTypeDef,
    SearchPlaceIndexForTextResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("LocationServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LocationServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_tracker_consumer(self, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.associate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#associate-tracker-consumer)
        """

    def batch_delete_geofence(
        self, CollectionName: str, GeofenceIds: List[str]
    ) -> BatchDeleteGeofenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.batch_delete_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch-delete-geofence)
        """

    def batch_evaluate_geofences(
        self, CollectionName: str, DevicePositionUpdates: List[DevicePositionUpdateTypeDef]
    ) -> BatchEvaluateGeofencesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.batch_evaluate_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch-evaluate-geofences)
        """

    def batch_get_device_position(
        self, DeviceIds: List[str], TrackerName: str
    ) -> BatchGetDevicePositionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.batch_get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch-get-device-position)
        """

    def batch_put_geofence(
        self, CollectionName: str, Entries: List[BatchPutGeofenceRequestEntryTypeDef]
    ) -> BatchPutGeofenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.batch_put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch-put-geofence)
        """

    def batch_update_device_position(
        self, TrackerName: str, Updates: List[DevicePositionUpdateTypeDef]
    ) -> BatchUpdateDevicePositionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.batch_update_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#batch-update-device-position)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#can-paginate)
        """

    def create_geofence_collection(
        self,
        CollectionName: str,
        PricingPlan: PricingPlan,
        Description: str = None,
        PricingPlanDataSource: str = None,
    ) -> CreateGeofenceCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.create_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create-geofence-collection)
        """

    def create_map(
        self,
        Configuration: "MapConfigurationTypeDef",
        MapName: str,
        PricingPlan: PricingPlan,
        Description: str = None,
    ) -> CreateMapResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.create_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create-map)
        """

    def create_place_index(
        self,
        DataSource: str,
        IndexName: str,
        PricingPlan: PricingPlan,
        DataSourceConfiguration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
    ) -> CreatePlaceIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.create_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create-place-index)
        """

    def create_tracker(
        self,
        PricingPlan: PricingPlan,
        TrackerName: str,
        Description: str = None,
        PricingPlanDataSource: str = None,
    ) -> CreateTrackerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.create_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#create-tracker)
        """

    def delete_geofence_collection(self, CollectionName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.delete_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete-geofence-collection)
        """

    def delete_map(self, MapName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.delete_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete-map)
        """

    def delete_place_index(self, IndexName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.delete_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete-place-index)
        """

    def delete_tracker(self, TrackerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.delete_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#delete-tracker)
        """

    def describe_geofence_collection(
        self, CollectionName: str
    ) -> DescribeGeofenceCollectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.describe_geofence_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe-geofence-collection)
        """

    def describe_map(self, MapName: str) -> DescribeMapResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.describe_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe-map)
        """

    def describe_place_index(self, IndexName: str) -> DescribePlaceIndexResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.describe_place_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe-place-index)
        """

    def describe_tracker(self, TrackerName: str) -> DescribeTrackerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.describe_tracker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#describe-tracker)
        """

    def disassociate_tracker_consumer(self, ConsumerArn: str, TrackerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.disassociate_tracker_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#disassociate-tracker-consumer)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#generate-presigned-url)
        """

    def get_device_position(
        self, DeviceId: str, TrackerName: str
    ) -> GetDevicePositionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_device_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-device-position)
        """

    def get_device_position_history(
        self,
        DeviceId: str,
        TrackerName: str,
        EndTimeExclusive: datetime = None,
        NextToken: str = None,
        StartTimeInclusive: datetime = None,
    ) -> GetDevicePositionHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_device_position_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-device-position-history)
        """

    def get_geofence(self, CollectionName: str, GeofenceId: str) -> GetGeofenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-geofence)
        """

    def get_map_glyphs(
        self, FontStack: str, FontUnicodeRange: str, MapName: str
    ) -> GetMapGlyphsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_map_glyphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-map-glyphs)
        """

    def get_map_sprites(self, FileName: str, MapName: str) -> GetMapSpritesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_map_sprites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-map-sprites)
        """

    def get_map_style_descriptor(self, MapName: str) -> GetMapStyleDescriptorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_map_style_descriptor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-map-style-descriptor)
        """

    def get_map_tile(self, MapName: str, X: str, Y: str, Z: str) -> GetMapTileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.get_map_tile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#get-map-tile)
        """

    def list_geofence_collections(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListGeofenceCollectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_geofence_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-geofence-collections)
        """

    def list_geofences(
        self, CollectionName: str, NextToken: str = None
    ) -> ListGeofencesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_geofences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-geofences)
        """

    def list_maps(self, MaxResults: int = None, NextToken: str = None) -> ListMapsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_maps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-maps)
        """

    def list_place_indexes(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListPlaceIndexesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_place_indexes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-place-indexes)
        """

    def list_tracker_consumers(
        self, TrackerName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackerConsumersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_tracker_consumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-tracker-consumers)
        """

    def list_trackers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListTrackersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.list_trackers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#list-trackers)
        """

    def put_geofence(
        self, CollectionName: str, GeofenceId: str, Geometry: "GeofenceGeometryTypeDef"
    ) -> PutGeofenceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.put_geofence)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#put-geofence)
        """

    def search_place_index_for_position(
        self, IndexName: str, Position: List[float], MaxResults: int = None
    ) -> SearchPlaceIndexForPositionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.search_place_index_for_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search-place-index-for-position)
        """

    def search_place_index_for_text(
        self,
        IndexName: str,
        Text: str,
        BiasPosition: List[float] = None,
        FilterBBox: List[float] = None,
        FilterCountries: List[str] = None,
        MaxResults: int = None,
    ) -> SearchPlaceIndexForTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Client.search_place_index_for_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/client.html#search-place-index-for-text)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_device_position_history"]
    ) -> GetDevicePositionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.GetDevicePositionHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#getdevicepositionhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_geofence_collections"]
    ) -> ListGeofenceCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListGeofenceCollections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencecollectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_geofences"]) -> ListGeofencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListGeofences)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listgeofencespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_maps"]) -> ListMapsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListMaps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listmapspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_place_indexes"]
    ) -> ListPlaceIndexesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListPlaceIndexes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listplaceindexespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tracker_consumers"]
    ) -> ListTrackerConsumersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListTrackerConsumers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerconsumerspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trackers"]) -> ListTrackersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/location.html#LocationService.Paginator.ListTrackers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/paginators.html#listtrackerspaginator)
        """
