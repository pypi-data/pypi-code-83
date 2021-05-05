"""
Type annotations for mediapackage service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/literals.html)

Usage::

    ```python
    from mypy_boto3_mediapackage.literals import AdMarkers

    data: AdMarkers = "DATERANGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdMarkers",
    "AdsOnDeliveryRestrictions",
    "EncryptionMethod",
    "ListChannelsPaginatorName",
    "ListHarvestJobsPaginatorName",
    "ListOriginEndpointsPaginatorName",
    "ManifestLayout",
    "Origination",
    "PlaylistType",
    "PresetSpeke20Audio",
    "PresetSpeke20Video",
    "Profile",
    "SegmentTemplateFormat",
    "Status",
    "StreamOrder",
    "UtcTiming",
    "__AdTriggersElement",
    "__PeriodTriggersElement",
)


AdMarkers = Literal["DATERANGE", "NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
AdsOnDeliveryRestrictions = Literal["BOTH", "NONE", "RESTRICTED", "UNRESTRICTED"]
EncryptionMethod = Literal["AES_128", "SAMPLE_AES"]
ListChannelsPaginatorName = Literal["list_channels"]
ListHarvestJobsPaginatorName = Literal["list_harvest_jobs"]
ListOriginEndpointsPaginatorName = Literal["list_origin_endpoints"]
ManifestLayout = Literal["COMPACT", "FULL"]
Origination = Literal["ALLOW", "DENY"]
PlaylistType = Literal["EVENT", "NONE", "VOD"]
PresetSpeke20Audio = Literal["PRESET-AUDIO-1"]
PresetSpeke20Video = Literal["PRESET-VIDEO-1"]
Profile = Literal["HBBTV_1_5", "NONE"]
SegmentTemplateFormat = Literal[
    "NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"
]
Status = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
StreamOrder = Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"]
UtcTiming = Literal["HTTP-HEAD", "HTTP-ISO", "NONE"]
__AdTriggersElement = Literal[
    "BREAK",
    "DISTRIBUTOR_ADVERTISEMENT",
    "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
    "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
    "PROVIDER_ADVERTISEMENT",
    "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
    "PROVIDER_PLACEMENT_OPPORTUNITY",
    "SPLICE_INSERT",
]
__PeriodTriggersElement = Literal["ADS"]
