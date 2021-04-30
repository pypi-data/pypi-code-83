"""
Main interface for mediastore-data service literal definitions.

Usage::

    ```python
    from mypy_boto3_mediastore_data.literals import ItemType

    data: ItemType = "FOLDER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ItemType", "ListItemsPaginatorName", "StorageClass", "UploadAvailability")


ItemType = Literal["FOLDER", "OBJECT"]
ListItemsPaginatorName = Literal["list_items"]
StorageClass = Literal["TEMPORAL"]
UploadAvailability = Literal["STANDARD", "STREAMING"]
