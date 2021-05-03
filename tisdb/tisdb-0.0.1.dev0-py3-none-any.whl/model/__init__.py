# -*- coding; utf-8

from sortedcontainers import SortedDict
from datetime import datetime
from hashlib import md5
import json

from tisdb.errors import BaseInfo

__all__ = ("TsdbData",)


class TsdbTags(SortedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TsdbFields(SortedDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TsdbData(object):
    """Tsdb Data Value Object

    Args:
        metric (str): metric name
        ts (datetime): timestamp of this data
        tags (TsdbTags): tags of this data
        fields (TsdbFields): fields of this data
    """

    def __init__(
        self,
        metric: str,
        ts: datetime = datetime.now(),
        tags: TsdbTags = TsdbTags(),
        fields: TsdbFields = TsdbFields(value=0),
    ):
        super().__init__()
        self._metric = metric
        self._ts = ts
        self._tags = tags
        uuid_gen = md5()
        uuid_gen.update(json.dumps(tags).encode(encoding="utf-8"))
        self._tags_uuid = uuid_gen.hexdigest()
        self._fields = fields
        self._value_id = -1

    @property
    def metric(self) -> str:
        return self._metric

    @property
    def ts(self) -> datetime:
        return self._ts

    @property
    def tags_uuid(self) -> str:
        return self._tags_uuid

    @property
    def tags(self) -> TsdbTags:
        return self._tags

    def get_value(self, field_name: str) -> float:
        return self._fields[field_name]

    @property
    def value_id(self) -> int:
        return self._value_id

    @value_id.setter
    def value_id(self, value_id: int):
        self._value_id = value_id


class SaveResult(object):
    """Result of the save function

    Args:
        data (list[TsdbData]): Tsdb data to save this time
        subcode (int): return subcode of this save result
        status (str): status of this save result
    """

    def __init__(
        self,
        data: list[TsdbData],
        subcode: int = BaseInfo.SUBCODE,
        status: str = BaseInfo.STATUS,
    ) -> None:
        super().__init__()
        self._data = data
        self._subcode = BaseInfo.SUBCODE
        self._status = BaseInfo.STATUS

    @property
    def data(self):
        return self._data
