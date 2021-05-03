# -*- coding: utf-8

from tests.test_base import TsdbTestCase
from tisdb.model import TsdbData, TsdbTags
from hashlib import md5
import json


class TsdbTest(TsdbTestCase):
    def test_taguk(self):
        gen = md5()
        data = TsdbData(metric="zzf_test", tags=TsdbTags(gameid="zzf", channel="haha"))
        a = json.dumps({"channel": "haha", "gameid": "zzf"})
        gen.update(a.encode("utf-8"))
        taguk = gen.hexdigest()
        b = json.dumps(data.tags)
        self.assertValueEqual(a, b)
        self.assertValueEqual(taguk, data.tags_uuid)

    def test_save(self):
        res = self.tsdb.save(
            self.tsdb.parse(
                {
                    "metric": "zzf_test",
                    "ts": "2021-04-01T01:01:01+08:00",
                    "tag": {"gameid": "zzf", "channel": "haha"},
                    "field": {"value": 1},
                }
            )
        )
        self.assertNotEqual(res.data[0], -1)
