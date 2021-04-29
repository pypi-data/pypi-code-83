"""
Main interface for cloudsearchdomain service literal definitions.

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.literals import ContentType

    data: ContentType = "application/json"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ContentType", "QueryParser")


ContentType = Literal["application/json", "application/xml"]
QueryParser = Literal["dismax", "lucene", "simple", "structured"]
