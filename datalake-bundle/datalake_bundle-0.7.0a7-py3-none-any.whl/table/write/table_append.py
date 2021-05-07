from typing import Union
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface
from pyspark.sql import DataFrame
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.write.TableAppender import TableAppender


@DecoratedDecorator
class table_append(OutputDecorator):  # noqa: N801
    def __init__(self, table_identifier_or_class: Union[str, type]):
        self.__table_identifier_or_class = table_identifier_or_class

    def process_result(self, result: DataFrame, container: ContainerInterface):
        table_definition_factory: TableDefinitionFactory = container.get(TableDefinitionFactory)
        table_appender: TableAppender = container.get(TableAppender)

        if isinstance(self.__table_identifier_or_class, str):
            table_definition = table_definition_factory.create_from_dataframe(self.__table_identifier_or_class, result)
        elif isinstance(self.__table_identifier_or_class, type):
            table_definition = table_definition_factory.create_from_class(self.__table_identifier_or_class)
        else:
            raise Exception(f"Invalid table identifier: {self.__table_identifier_or_class}")

        table_appender.append(result, table_definition)
