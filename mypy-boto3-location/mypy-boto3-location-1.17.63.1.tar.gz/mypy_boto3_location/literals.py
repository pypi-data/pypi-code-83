"""
Type annotations for location service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_location/literals.html)

Usage::

    ```python
    from mypy_boto3_location.literals import BatchItemErrorCode

    data: BatchItemErrorCode = "AccessDeniedError"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchItemErrorCode",
    "GetDevicePositionHistoryPaginatorName",
    "IntendedUse",
    "ListGeofenceCollectionsPaginatorName",
    "ListGeofencesPaginatorName",
    "ListMapsPaginatorName",
    "ListPlaceIndexesPaginatorName",
    "ListTrackerConsumersPaginatorName",
    "ListTrackersPaginatorName",
    "PricingPlan",
)


BatchItemErrorCode = Literal[
    "AccessDeniedError",
    "ConflictError",
    "InternalServerError",
    "ResourceNotFoundError",
    "ThrottlingError",
    "ValidationError",
]
GetDevicePositionHistoryPaginatorName = Literal["get_device_position_history"]
IntendedUse = Literal["SingleUse", "Storage"]
ListGeofenceCollectionsPaginatorName = Literal["list_geofence_collections"]
ListGeofencesPaginatorName = Literal["list_geofences"]
ListMapsPaginatorName = Literal["list_maps"]
ListPlaceIndexesPaginatorName = Literal["list_place_indexes"]
ListTrackerConsumersPaginatorName = Literal["list_tracker_consumers"]
ListTrackersPaginatorName = Literal["list_trackers"]
PricingPlan = Literal["MobileAssetManagement", "MobileAssetTracking", "RequestBasedUsage"]
