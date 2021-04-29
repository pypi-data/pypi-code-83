"""Shared types."""
from typing import Any, List, Mapping, Optional, Tuple, Union

ConnectArgs = Mapping[str, Any]
ConnectionArgs = Union[ConnectArgs, str]

InsertAssignments = Union[
    Mapping[str, Any],
    List[Tuple[str, Any]],
]

LimitOffset = Tuple[Optional[int], Optional[int]]

Record = Mapping[str, Any]
Records = List[Record]
RecordsAndCount = Tuple[Records, int]

SQL = Tuple[Optional[str], List[Any]]
