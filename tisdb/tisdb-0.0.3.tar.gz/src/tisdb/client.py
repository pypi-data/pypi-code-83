# -*- coding: utf-8


from copy import deepcopy
from datetime import datetime, date

from sortedcontainers.sorteddict import SortedDict
from tisdb.api import TsdbApi
from tisdb.config import TsdbConfig
from tisdb.errors import ParamError
from tisdb.model.mysql import TSDB_CONFIG
from tisdb.types import OpType, StoreType
from tisdb.model import SaveResult, TsdbData, TsdbFields, TsdbTags
from porm.databases import MyDBApi


class TsdbClient(object):
    """Tsdb Client

    Args:
        store_type (StoreType): Tsdb store type support PORM,MYSQL,TIDB
        conn_conf (TsdbConfig): Tsdb connecting configuration
    """

    def __init__(
        self,
        store_type: StoreType = StoreType.PORM,
        conn_conf: TsdbConfig = TsdbConfig(),
    ):
        super().__init__()
        self.store_type = store_type
        self.config = conn_conf
        self.api = TsdbApi(self.store_type, self.config)
        self.api.activate()

    def save(self, value: TsdbData, op_type: OpType = OpType.UPSERT) -> SaveResult:
        """Save timestamp data

        Args:
            value (TsdbData): Timestamp value to save
            op_type (OpType, optional): Saving operation type. Defaults to OpType.INSERT_IGNORE.

        Returns:
            SaveResult: Result of this save
        """
        if op_type == OpType.INSERT_IGNORE:
            ret = self.api.insert_ignore(value)
        elif op_type == OpType.UPSERT:
            ret = self.api.upsert(value)
        elif op_type == OpType.INSERT_ON_DUPLICATE_KEY_UPDATE:
            # ret = self.api.insert_on_duplicate_key_update(value)
            pass
        else:
            ret = self.api.insert_ignore(value)

        return SaveResult(data=[ret])

    def parse(self, value: dict) -> TsdbData:
        """Parse tsdb data from dictionary

        Args:
            value (dict): Tsdb data presents in dict type

        Returns:
            TsdbData: parsed tsdb data
        """
        ts_tmp = value["ts"]
        if isinstance(ts_tmp, datetime):
            ts = ts_tmp
        elif isinstance(ts_tmp, str):
            ts = datetime.fromisoformat(ts_tmp)
        elif isinstance(ts_tmp, date):
            ts = datetime(*ts_tmp.timetuple()[:6])
        else:
            ts = datetime.fromisoformat(ts_tmp)
        return TsdbData(
            metric=value["metric"],
            ts=ts,
            tags=TsdbTags(**value.get("tag", {})),
            fields=TsdbFields(
                value=value.get("field", {}).get("value", value.get("value", 0))
            ),
        )

    def parse_many(self, values: list[dict]) -> list[TsdbData]:
        ret = []
        for val in values:
            ret.append(self.parse(val))
        return ret

    def create_tsdbdata_mydb(
        self, sql: str, param: dict = None, conn_conf: dict = None
    ) -> list[dict]:
        """Create tsdbdata from mydb

        Args:
            sql (str): sql to excute that create ts data
            param (dict, optional): sql param. Defaults to None.
            conn_conf (dict, optional): connection config. Defaults to None.

        Returns:
            list[dict]: ts data created from sql
        """
        conf = TSDB_CONFIG.copy()
        if conn_conf is not None:
            conf.update(conn_conf)
        mydb = MyDBApi(database_name=conf.get("db", None), **conf)
        ret = []
        for res in mydb.query_many(sql, param=param):
            ret.append(self._parse_mydb_result(res))
        return ret

    def _parse_mydb_result(self, result: dict) -> dict:
        """Parse mydb query result to tsdb dict like format

        Args:
            result (dict): Mydb format data

        Raises:
            ParamError: Error when missing key needed or meeting key undefined

        Returns:
            dict: Tsdb dict format data
        """
        ts_data = SortedDict()
        ts_tag = SortedDict()
        ts_data["tag"] = ts_tag
        for key, val in result.items():
            if "metric" == key:
                ts_data[key] = val
            elif key.startswith("tag"):
                # select 'm' as metric, 'g18' as tag_gameid, 'ntes' as tag_channel
                # 中抽取tag_后的字段作为tsvals的tag key
                ts_tag[key.split("_", 1)[1]] = val
            elif "ts" == key:
                ts_data[key] = val
            elif "value" == key:
                ts_data[key] = val
            else:
                raise ParamError("Error key: " + key)
        return ts_data
