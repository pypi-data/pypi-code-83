"""
Type annotations for mediapackage-vod service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/literals.html)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.literals import AdMarkers

    data: AdMarkers = "NONE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdMarkers",
    "EncryptionMethod",
    "ListAssetsPaginatorName",
    "ListPackagingConfigurationsPaginatorName",
    "ListPackagingGroupsPaginatorName",
    "ManifestLayout",
    "Profile",
    "SegmentTemplateFormat",
    "StreamOrder",
    "__PeriodTriggersElement",
)


AdMarkers = Literal["NONE", "PASSTHROUGH", "SCTE35_ENHANCED"]
EncryptionMethod = Literal["AES_128", "SAMPLE_AES"]
ListAssetsPaginatorName = Literal["list_assets"]
ListPackagingConfigurationsPaginatorName = Literal["list_packaging_configurations"]
ListPackagingGroupsPaginatorName = Literal["list_packaging_groups"]
ManifestLayout = Literal["COMPACT", "FULL"]
Profile = Literal["HBBTV_1_5", "NONE"]
SegmentTemplateFormat = Literal[
    "NUMBER_WITH_DURATION", "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE"
]
StreamOrder = Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"]
__PeriodTriggersElement = Literal["ADS"]
