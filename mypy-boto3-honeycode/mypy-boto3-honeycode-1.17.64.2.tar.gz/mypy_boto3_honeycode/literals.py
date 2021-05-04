"""
Type annotations for honeycode service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/literals.html)

Usage::

    ```python
    from mypy_boto3_honeycode.literals import Format

    data: Format = "ACCOUNTING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Format",
    "ImportDataCharacterEncoding",
    "ImportSourceDataFormat",
    "ListTableColumnsPaginatorName",
    "ListTableRowsPaginatorName",
    "ListTablesPaginatorName",
    "QueryTableRowsPaginatorName",
    "TableDataImportJobStatus",
    "UpsertAction",
)


Format = Literal[
    "ACCOUNTING",
    "AUTO",
    "CONTACT",
    "CURRENCY",
    "DATE",
    "DATE_TIME",
    "NUMBER",
    "PERCENTAGE",
    "ROWLINK",
    "TEXT",
    "TIME",
]
ImportDataCharacterEncoding = Literal[
    "ISO-8859-1", "US-ASCII", "UTF-16", "UTF-16BE", "UTF-16LE", "UTF-8"
]
ImportSourceDataFormat = Literal["DELIMITED_TEXT"]
ListTableColumnsPaginatorName = Literal["list_table_columns"]
ListTableRowsPaginatorName = Literal["list_table_rows"]
ListTablesPaginatorName = Literal["list_tables"]
QueryTableRowsPaginatorName = Literal["query_table_rows"]
TableDataImportJobStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"]
UpsertAction = Literal["APPENDED", "UPDATED"]
