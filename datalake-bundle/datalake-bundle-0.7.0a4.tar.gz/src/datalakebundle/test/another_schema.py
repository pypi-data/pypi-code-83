import pyspark.sql.types as t


def get_schema():
    return t.StructType(
        [
            t.StructField("name", t.StringType(), True),
            t.StructField("create_time", t.TimestampType(), True),
        ]
    )


def get_primary_key():
    return "name"


def get_partition_by():
    return "create_time"
