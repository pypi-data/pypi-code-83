from logging import Logger
import yaml
from pyspark.sql import DataFrame
from pyspark.sql.types import StructType


class SchemaChecker:
    def __init__(self, logger: Logger):
        self.__logger = logger

    def check(self, df: DataFrame, full_table_name: str, schema: StructType):
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
