"""
Type annotations for marketplacecommerceanalytics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplacecommerceanalytics.type_defs import GenerateDataSetResultTypeDef

    data: GenerateDataSetResultTypeDef = {...}
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GenerateDataSetResultTypeDef", "StartSupportDataExportResultTypeDef")


class GenerateDataSetResultTypeDef(TypedDict, total=False):
    dataSetRequestId: str


class StartSupportDataExportResultTypeDef(TypedDict, total=False):
    dataSetRequestId: str
