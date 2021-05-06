# -*- coding: utf-8

from porm.databases.api import _transaction
from tisdb.config import TsdbConfig
from tisdb.errors import FakeError
from tisdb.types import StoreType
from tisdb.model.mysql import Mtsv, Tkv, TkvUkRel
from tisdb.model import TsdbData, TsdbTags


class TsdbApi(object):
    def __init__(self, store_type: StoreType, config: TsdbConfig):
        super().__init__()
        self._store_type = store_type
        self._config = config
        Mtsv.__CONFIG__.update(self._config)
        Tkv.__CONFIG__.update(self._config)
        TkvUkRel.__CONFIG__.update(self._config)

    def activate(self):
        value = TsdbData(metric="tisdb_test", tags=TsdbTags(env="test"))
        try:
            if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
                return self._test_insert_mydb(value)
            else:
                return self._test_insert_mydb(value)
        except Exception as ex:
            if not isinstance(ex, FakeError):
                raise ex

    def insert_ignore(self, value: TsdbData):
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb(value)
        else:
            return self._insert_ignore_mydb(value)

    def _insert_tsdbdata(
        self, mtsv: Mtsv, tags: TsdbTags, _t: _transaction
    ) -> TsdbData:
        rels = []
        for tagk, tagv in tags.items():
            tkv = Tkv.new(tagk=tagk, tagv=tagv)
            Tkv.insert_many([tkv], t=_t, ignore=True)
            tkv = Tkv.get_one(t=_t, **tkv)
            rel = TkvUkRel.new(tkv_pk=tkv.zzid, taguk=mtsv.taguk)
            rels.append(rel)
            TkvUkRel.insert_many(rels, t=_t, ignore=True)
        Mtsv.insert_many([mtsv], t=_t, ignore=True)
        ret = Mtsv.get_one(t=_t, metric=mtsv.metric, ts=mtsv.ts, taguk=mtsv.taguk)
        return ret.zzid

    def _insert_ignore_mydb(self, value: TsdbData) -> TsdbData:
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        rels = []
        with mtsv.start_transaction() as _t:
            value.value_id = self._insert_tsdbdata(mtsv, value.tags, _t)
            return value

    def upsert(self, value: TsdbData):
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._upsert_mydb(value)
        else:
            return self._upsert_mydb(value)

    def _upsert_mydb(self, value: TsdbData) -> TsdbData:
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        with mtsv.start_transaction() as _t:
            Mtsv.delete_many(t=_t, metric=mtsv.metric, ts=mtsv.ts, taguk=mtsv.taguk)
            value.value_id = self._insert_tsdbdata(mtsv, value.tags, _t)
            return value

    def _test_insert_mydb(self, value: TsdbData) -> TsdbData:
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        with mtsv.start_transaction() as _t:
            self._insert_tsdbdata(mtsv, value.tags, _t)
            raise FakeError()
