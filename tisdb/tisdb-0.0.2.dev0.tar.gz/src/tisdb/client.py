# -*- coding: utf-8


from datetime import datetime
from tisdb.api import TsdbApi
from tisdb.config import TsdbConfig
from tisdb.types import OpType, StoreType
from tisdb.model import SaveResult, TsdbData, TsdbFields, TsdbTags


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

    def save(
        self, value: TsdbData, op_type: OpType = OpType.INSERT_IGNORE
    ) -> SaveResult:
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
            # ret = self.api.upsert(value)
            pass
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
        else:
            ts = datetime.fromisoformat(ts_tmp)
        return TsdbData(
            metric=value["metric"],
            ts=ts,
            tags=TsdbTags(**value.get("tag", {})),
            fields=TsdbFields(value=value.get("field", {}).get("value", 0)),
        )
