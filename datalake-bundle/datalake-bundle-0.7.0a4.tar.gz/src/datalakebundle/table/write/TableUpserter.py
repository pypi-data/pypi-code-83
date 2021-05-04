from logging import Logger
from pyspark.sql.dataframe import DataFrame
from datalakebundle.table.write.DataWriter import DataWriter
from datalakebundle.table.create.TableCreator import TableCreator
from datalakebundle.table.parameters.TableParameters import TableParameters


class TableUpserter:
    def __init__(self, logger: Logger, table_creator: TableCreator, data_writer: DataWriter):
        self.__logger = logger
        self.__table_creator = table_creator
        self.__data_writer = data_writer

    def upsert(self, result: DataFrame, table_parameters: TableParameters):
        if len(table_parameters.table_structure.primary_key) > 1:
            columns_string = f"columns [{', '.join(table_parameters.table_structure.primary_key)}]"
        else:
            columns_string = f"column {table_parameters.table_structure.primary_key[0]}"

        output_table_name = table_parameters.full_table_name

        self.__logger.info(f"Data to be upserted into table: {output_table_name} (by {columns_string})")

        self.__table_creator.create_if_not_exists(table_parameters)

        self.__logger.info(f"Upserting data to table: {output_table_name}")

        table_structure = table_parameters.table_structure

        self.__data_writer.upsert(result, output_table_name, table_structure.schema, table_structure.primary_key)

        self.__logger.info(f"Data successfully upserted to: {output_table_name}")
