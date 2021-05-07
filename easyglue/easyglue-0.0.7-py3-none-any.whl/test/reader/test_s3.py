import unittest

import easyglue

from pyspark.context import SparkContext
from awsglue.context import GlueContext


class TestS3Read(unittest.TestCase):

    glue = GlueContext(SparkContext.getOrCreate())

    def test_process_s3_path(self):
        from easyglue.reader._S3Mixin import _process_s3_path
        result = _process_s3_path('s3://test')
        self.assertTrue(isinstance(result, list))

    def test_process_s3_path_incorrect(self):
        from easyglue.reader._S3Mixin import _process_s3_path
        self.assertRaises(TypeError, _process_s3_path, 1)

    def test_process_s3_path_empty(self):
        from easyglue.reader._S3Mixin import _process_s3_path
        self.assertRaises(ValueError, _process_s3_path, '')

    def test_csv(self):
        data = self.glue.read().csv("s3://bertolb/sampledata/mockaroo/csv/")
        self.assertEqual(1001, data.count())  # 1001 because of the header

    def test_json(self):
        data = self.glue.read().json("s3://bertolb/sampledata/mockaroo/json/")
        self.assertEqual(1000, data.count())

    def test_avro(self):
        data = self.glue.read().avro("s3://bertolb/sampledata/mockaroo/avro/")
        self.assertEqual(1000, data.count())

    def test_ion(self):
        data = self.glue.read().ion("s3://bertolb/sampledata/mockaroo/json/")  # Testing with JSON for now
        self.assertEqual(1000, data.count())

    # TODO test groklog

    def test_orc(self):
        data = self.glue.read().orc("s3://bertolb/sampledata/mockaroo/orc/")
        self.assertEqual(1000, data.count())

    def test_parquet(self):
        data = self.glue.read().parquet("s3://bertolb/sampledata/mockaroo/parquet/")
        self.assertEqual(1000, data.count())

    def test_glueparquet(self):
        data = self.glue.read().glueparquet("s3://bertolb/sampledata/mockaroo/glueparquet/")
        self.assertEqual(1000, data.count())

    def test_xml(self):
        data = self.glue.read().format_option("rowTag", "row").xml("s3://bertolb/sampledata/mockaroo/xml/")
        self.assertEqual(1000, data.count())


if __name__ == '__main__':
    unittest.main()
