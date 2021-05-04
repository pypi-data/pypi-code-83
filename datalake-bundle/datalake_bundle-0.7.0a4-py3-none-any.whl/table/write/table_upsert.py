from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface
from pyspark.sql import DataFrame
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.write.TableUpserter import TableUpserter


@DecoratedDecorator
class table_upsert(OutputDecorator):  # noqa: N801
    def __init__(self, table_class: type):
        self.__table_class = table_class

    def process_result(self, result: DataFrame, container: ContainerInterface):
        table_definition_factory: TableDefinitionFactory = container.get(TableDefinitionFactory)
        table_upserter: TableUpserter = container.get(TableUpserter)

        if not isinstance(self.__table_class, type):
            raise Exception(f"Invalid table class: {self.__table_class}")

        table_definition = table_definition_factory.create_from_class(self.__table_class)

        table_upserter.upsert(result, table_definition)
