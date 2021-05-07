from argparse import ArgumentParser, Namespace
from logging import Logger
from time import sleep
from consolebundle.ConsoleCommand import ConsoleCommand
from pysparkbundle.filesystem.FilesystemInterface import FilesystemInterface
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.create.TableRecreator import TableRecreator
from datalakebundle.table.class_ import table_class_loader


class TableRecreatorCommand(ConsoleCommand):
    def __init__(
        self,
        logger: Logger,
        filesystem: FilesystemInterface,
        table_definition_factory: TableDefinitionFactory,
        table_recreator: TableRecreator,
    ):
        self.__logger = logger
        self.__filesystem = filesystem
        self.__table_definition_factory = table_definition_factory
        self.__table_recreator = table_recreator

    def get_command(self) -> str:
        return "datalake:table:recreate"

    def get_description(self):
        return "Recreates a table based on it's table class"

    def configure(self, argument_parser: ArgumentParser):
        argument_parser.add_argument(dest="table_class_path", help="Table class path [module_path].[class_name]")
        argument_parser.add_argument(
            "-s",
            "--skip-countdown",
            action="store_true",
            help="Skip data deletion countdown",
        )

    def run(self, input_args: Namespace):
        table_definition = self.__table_definition_factory.create_from_class(table_class_loader.load(input_args.table_class_path))

        if input_args.skip_countdown is False and self.__filesystem.exists(table_definition.target_path):
            self.__logger.info("Use the --skip-countdown switch to delete existing data immediately")

            countdown = 10

            for i in range(countdown):
                self.__logger.warning(f"Table data will be deleted in {countdown - i}s. Use CTRL+C to cancel.")
                sleep(1)

        self.__table_recreator.recreate(table_definition)
