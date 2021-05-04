"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_featurestore_runtime.type_defs import FeatureValueTypeDef

    data: FeatureValueTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("FeatureValueTypeDef", "GetRecordResponseTypeDef")


class FeatureValueTypeDef(TypedDict):
    FeatureName: str
    ValueAsString: str


class GetRecordResponseTypeDef(TypedDict, total=False):
    Record: List["FeatureValueTypeDef"]
