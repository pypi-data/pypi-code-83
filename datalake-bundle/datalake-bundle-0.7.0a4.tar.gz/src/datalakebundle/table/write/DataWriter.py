import yaml
import string
import random
from logging import Logger
from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import StructType
from datalakebundle.table.upsert.UpsertQueryCreator import UpsertQueryCreator
from datalakebundle.delta.DeltaStorage import DeltaStorage


class DataWriter:
    def __init__(
        self,
        logger: Logger,
        spark: SparkSession,
        delta_storage: DeltaStorage,
        upsert_query_creator: UpsertQueryCreator,
    ):
        self.__logger = logger
        self.__spark = spark
        self.__delta_storage = delta_storage
        self.__upsert_query_creator = upsert_query_creator

    def append(self, df: DataFrame, full_table_name: str, schema: StructType):
        self.__check_schema(df, full_table_name, schema)

        # insertInto() requires dataframe columns order to match schema columns order
        df.select([field.name for field in schema.fields]).write.insertInto(full_table_name, overwrite=False)

    def overwrite(self, df: DataFrame, full_table_name: str, schema: StructType, partition_by: list):
        self.__check_schema(df, full_table_name, schema)

        self.__delta_storage.overwrite_data(df, full_table_name, partition_by)

    def upsert(self, df: DataFrame, full_table_name: str, schema: StructType, primary_key: list):
        self.__check_schema(df, full_table_name, schema)

        temp_source_table = f"upsert_{full_table_name}_{''.join(random.choice(string.ascii_lowercase) for _ in range(6))}"

        df.createOrReplaceTempView(temp_source_table)

        upsert_sql_statement = self.__upsert_query_creator.create(full_table_name, schema, primary_key, temp_source_table)

        try:
            self.__spark.sql(upsert_sql_statement)

        except BaseException:
            raise

        finally:
            self.__spark.catalog.dropTempView(temp_source_table)

    def __check_schema(self, df: DataFrame, full_table_name: str, schema: StructType):
        def print_schema(schema_json: dict):
            return yaml.dump(schema_json)

        def remove_metadata(json_schema):
            for field in json_schema["fields"]:
                field["metadata"] = dict()

            return json_schema

        expected_schema_json = remove_metadata(schema.jsonValue())
        df_schema_json = remove_metadata(df.schema.jsonValue())

        if expected_schema_json != df_schema_json:
            error_message = "Table and dataframe schemas do NOT match"

            self.__logger.error(
                error_message,
                extra={
                    "df_schema": print_schema(df_schema_json),
                    "expected_schema": print_schema(expected_schema_json),
                    "table": full_table_name,
                },
            )

            raise Exception(error_message)
