from datalakebundle.table.TableExistenceChecker import TableExistenceChecker
from datalakebundle.table.create.TableDefinition import TableDefinition
from datalakebundle.table.parameters.TableParameters import TableParameters
from datalakebundle.table.create.TableCreator import TableCreator
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.delete.TableDeleter import TableDeleter
from datalakebundle.table.class_ import identifier_parser
from datalakebundle.table.parameters.TableParametersManager import TableParametersManager


class TableManager:
    def __init__(
        self,
        table_parameters_manager: TableParametersManager,
        table_definition_factory: TableDefinitionFactory,
        table_creator: TableCreator,
        table_deleter: TableDeleter,
        table_existence_checker: TableExistenceChecker,
    ):
        self.__table_parameters_manager = table_parameters_manager
        self.__table_definition_factory = table_definition_factory
        self.__table_creator = table_creator
        self.__table_deleter = table_deleter
        self.__table_existence_checker = table_existence_checker

    def get_parameters(self, identifier: str) -> TableParameters:
        return self.__table_parameters_manager.get_or_parse(identifier)

    def get_definition(self, table_class: type) -> TableDefinition:
        return self.__table_definition_factory.create_from_class(table_class)

    def create(self, table_class: type):
        table_definition = self.__table_definition_factory.create_from_class(table_class)

        self.__table_creator.create(table_definition)

    def create_if_not_exists(self, table_class: type):
        table_definition = self.__table_definition_factory.create_from_class(identifier_parser.parse(table_class))

        self.__table_creator.create_if_not_exists(table_definition)

    def exists(self, identifier: str):
        table_parameters = self.__table_parameters_manager.get_or_parse(identifier)

        return self.__table_existence_checker.table_exists(table_parameters.db_name, table_parameters.table_name)

    def delete_including_data(self, identifier: str):
        table_parameters = self.__table_parameters_manager.get_or_parse(identifier)

        self.__table_deleter.delete_including_data(table_parameters)
