from logging import Logger
from pyspark.sql import DataFrame
from pyspark.sql.types import StructType
from datalakebundle.table.class_ import identifier_parser
from datalakebundle.table.parameters.TableParameters import TableParameters
from datalakebundle.table.parameters.TableParametersManager import TableParametersManager
from datalakebundle.table.create.TableDefinition import TableDefinition


class TableDefinitionFactory:

    __allowed_attrs = [
        {"name": "db", "mandatory": True},
        {"name": "fields", "mandatory": True},
        {"name": "primary_key", "mandatory": True},
        {"name": "partition_by", "mandatory": False},
    ]

    def __init__(self, logger: Logger, table_parameters_manager: TableParametersManager):
        self.__logger = logger
        self.__table_parameters_manager = table_parameters_manager

    def create_from_class(self, table_class: type):
        self.__check_table_class(table_class)

        identifier = identifier_parser.parse(table_class)
        table_parameters = self.__table_parameters_manager.get_or_parse(identifier)

        schema = StructType(table_class.fields)
        primary_key = [table_class.primary_key] if isinstance(table_class.primary_key, str) else table_class.primary_key

        if hasattr(table_class, "partition_by"):
            partition_by = [table_class.partition_by] if isinstance(table_class.partition_by, str) else table_class.partition_by
        else:
            partition_by = []

        return self.__create(table_parameters, schema, primary_key, partition_by)

    def create_from_dataframe(self, table_identifier: str, df: DataFrame):
        self.__logger.warning("No explicit schema provided, using dataframe schema instead")
        table_parameters = self.__table_parameters_manager.get_or_parse(table_identifier)

        return self.__create(table_parameters, df.schema, [], [])

    def __check_table_class(self, table_class: type):
        table_class_attr_names = [index for index, val in vars(table_class).items() if index[0:2] != "__"]
        allowed_attr_names = [attr["name"] for attr in self.__allowed_attrs]

        for attr_name in table_class_attr_names:
            if attr_name not in allowed_attr_names:
                raise Exception(f"Unexpected table class attribute \"{attr_name}\". Allowed: {', '.join(allowed_attr_names)}")

        mandatory_attr_names = [field["name"] for field in self.__allowed_attrs if field["mandatory"] is True]

        for attr_name in mandatory_attr_names:
            if not hasattr(table_class, attr_name):
                raise Exception(f'Table class missing mandatory "{attr_name}" attribute')

    def __create(self, table_parameters: TableParameters, schema: StructType, primary_key: list, partition_by: list):
        return TableDefinition(
            table_parameters.db_name, table_parameters.table_name, schema, primary_key, partition_by, table_parameters.target_path
        )
