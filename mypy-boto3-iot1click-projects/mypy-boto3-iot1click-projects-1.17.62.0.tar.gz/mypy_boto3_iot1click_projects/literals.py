"""
Main interface for iot1click-projects service literal definitions.

Usage::

    ```python
    from mypy_boto3_iot1click_projects.literals import ListPlacementsPaginatorName

    data: ListPlacementsPaginatorName = "list_placements"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListPlacementsPaginatorName", "ListProjectsPaginatorName")


ListPlacementsPaginatorName = Literal["list_placements"]
ListProjectsPaginatorName = Literal["list_projects"]
