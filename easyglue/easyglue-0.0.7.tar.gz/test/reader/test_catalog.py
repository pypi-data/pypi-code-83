import unittest

import easyglue

from pyspark.context import SparkContext
from awsglue.context import GlueContext


class TestCatalogRead(unittest.TestCase):

    glue = GlueContext(SparkContext.getOrCreate())

    def test_validate_qualified_name(self):
        from easyglue.reader._CatalogMixin import _validate_qualified_name
        database, table = _validate_qualified_name("default.legislators")
        self.assertEqual("default", database)
        self.assertEqual("legislators", table)

    def test_validate_qualified_name_error(self):
        from easyglue.reader._CatalogMixin import _validate_qualified_name
        self.assertRaises(ValueError, _validate_qualified_name, "legislators")

    def test_table(self):
        data = self.glue.read().table("sampledata.mockaroo_csv")
        self.assertEqual(1000, data.count())

    def test_catalog(self):
        data = self.glue.read().catalog("sampledata", "mockaroo_csv")
        self.assertEqual(1000, data.count())


if __name__ == '__main__':
    unittest.main()
