from typing import Union
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface
from pyspark.sql import DataFrame
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.write.TableOverwriter import TableOverwriter


@DecoratedDecorator
class table_overwrite(OutputDecorator):  # noqa: N801
    def __init__(self, table_identifier_or_class: Union[str, type], recreate_table=False):
        self.__table_identifier_or_class = table_identifier_or_class
        self.__recreate_table = recreate_table

    def process_result(self, result: DataFrame, container: ContainerInterface):
        table_definition_factory: TableDefinitionFactory = container.get(TableDefinitionFactory)
        table_overwriter: TableOverwriter = container.get(TableOverwriter)

        if isinstance(self.__table_identifier_or_class, str):
            table_definition = table_definition_factory.create_from_dataframe(self.__table_identifier_or_class, result)
        elif isinstance(self.__table_identifier_or_class, type):
            table_definition = table_definition_factory.create_from_class(self.__table_identifier_or_class)
        else:
            raise Exception(f"Invalid table identifier: {self.__table_identifier_or_class}")

        table_overwriter.overwrite(result, table_definition, self.__recreate_table)
