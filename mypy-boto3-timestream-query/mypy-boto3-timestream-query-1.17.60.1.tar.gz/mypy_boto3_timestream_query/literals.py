"""
Main interface for timestream-query service literal definitions.

Usage::

    ```python
    from mypy_boto3_timestream_query.literals import QueryPaginatorName

    data: QueryPaginatorName = "query"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("QueryPaginatorName",)


QueryPaginatorName = Literal["query"]
