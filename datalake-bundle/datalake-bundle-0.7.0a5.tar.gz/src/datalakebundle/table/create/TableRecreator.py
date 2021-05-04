from logging import Logger
from datalakebundle.table.TableExistenceChecker import TableExistenceChecker
from datalakebundle.delta.DeltaStorage import DeltaStorage
from datalakebundle.table.create.TableDefinition import TableDefinition


class TableRecreator:
    def __init__(
        self,
        logger: Logger,
        delta_storage: DeltaStorage,
        table_existence_checker: TableExistenceChecker,
    ):
        self.__logger = logger
        self.__delta_storage = delta_storage
        self.__table_existence_checker = table_existence_checker

    def recreate(self, table_definition: TableDefinition):
        self.__logger.info(f"Recreating table {table_definition.full_table_name}")

        self.__delta_storage.recreate_table(table_definition)

        self.__logger.info(f"Table {table_definition.full_table_name} successfully recreated")
