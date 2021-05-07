import unittest

import easyglue

from pyspark.context import SparkContext
from awsglue.context import GlueContext


class TestReadOthers(unittest.TestCase):

    glue = GlueContext(SparkContext.getOrCreate())

    def test_dynamodb(self):
        data = self.glue.read().dynamodb("easyglue")
        self.assertEqual(4, data.count())

    def test_ddb(self):
        data = self.glue.read().ddb("easyglue")
        self.assertEqual(4, data.count())


if __name__ == '__main__':
    unittest.main()
