import unittest

import easyglue

from pyspark.context import SparkContext
from awsglue.context import GlueContext


class TestEasyDynamicFrameReader(unittest.TestCase):
    glue = GlueContext(SparkContext.getOrCreate())

    def test_format_option(self):
        data = self.glue.read().format_option("withHeader", True).csv("s3://bertolb/sampledata/mockaroo/csv/")
        self.assertEqual(1000, data.count())

    def test_format_options(self):
        data = self.glue.read().format_options({"withHeader": True}).csv("s3://bertolb/sampledata/mockaroo/csv/")
        self.assertEqual(1000, data.count())

    def test_connection_option(self):
        data = self.glue.read().connection_option("compression", "gzip")\
            .json("s3://bertolb/sampledata/mockaroo/json-gzip/")
        self.assertEqual(1000, data.count())

    def test_connection_options(self):
        data = self.glue.read().connection_options({"compression": "gzip"})\
            .json("s3://bertolb/sampledata/mockaroo/json-gzip/")
        self.assertEqual(1000, data.count())

    # TODO test additional_options


if __name__ == '__main__':
    unittest.main()
