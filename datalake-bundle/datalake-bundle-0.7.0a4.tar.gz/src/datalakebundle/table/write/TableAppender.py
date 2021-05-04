from logging import Logger
from pyspark.sql.dataframe import DataFrame
from datalakebundle.table.write.DataWriter import DataWriter
from datalakebundle.table.create.TableCreator import TableCreator
from datalakebundle.table.parameters.TableParameters import TableParameters


class TableAppender:
    def __init__(self, logger: Logger, table_creator: TableCreator, data_writer: DataWriter):
        self.__logger = logger
        self.__table_creator = table_creator
        self.__data_writer = data_writer

    def append(self, result: DataFrame, table_parameters: TableParameters):
        output_table_name = table_parameters.full_table_name

        self.__logger.info(f"Data to be appended into table: {output_table_name}")

        self.__table_creator.create_if_not_exists(table_parameters)

        self.__logger.info(f"Appending data to table: {output_table_name}")

        self.__data_writer.append(result, output_table_name, table_parameters.table_structure.schema)

        self.__logger.info(f"Data successfully appended to: {output_table_name}")
