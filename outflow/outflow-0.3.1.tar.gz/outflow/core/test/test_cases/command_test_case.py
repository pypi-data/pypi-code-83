# -*- coding: utf-8 -*-
import pytest
from outflow.core.commands import RootCommand
from outflow.core.logging import default_config as default_logger_config
from outflow.core.pipeline import Pipeline
from outflow.core.pipeline.context_manager import PipelineContextManager
from outflow.core.pipeline.lazy_config import Config
from outflow.core.pipeline.lazy_context import PipelineContext
from outflow.core.pipeline.lazy_settings import Settings


class CommandTestCase:
    """
    The CommandTestCase class is designed to be overridden in derived classes to create unit tests for commands.

    Example:
        class TestMyPluginCommands(CommandTestCase):
            def test_sub_command1(self):

                # --- create some fake data ---

                value1 = 'value1'
                value2 = 'value2'

                # --- initialize the command ---

                self.root_command_class = MyRootCommand


                arg_list = ['my_sub_command',
                            '--my_option1', value1,
                            '--my_option2', value2]

                # --- run the command ---

                return_code, result = self.run_command(arg_list)

                # --- make assertions ---

                # test the result
                assert return_code == 0
                assert result == {}

                # (...)
    """

    def setup_method(self):
        """
        Setup the pipeline before each test
        :return:
        """

        # reset the command
        self.root_command_class = None

    @pytest.yield_fixture(autouse=True)
    def with_pipeline_context_manager(self):
        default_config = {
            "logging": default_logger_config,
            "cluster": {},
        }
        with PipelineContextManager():
            self.settings = Settings(
                "outflow.core.pipeline.default_settings",
            )
            self.config = Config(default_config)
            self.context = PipelineContext()
            self.context.force_dry_run = True

            yield

    def teardown_method(self):
        pass

    def run_command(self, arg_list=[], force_dry_run=True, **kwargs):
        self.settings.ROOT_COMMAND_CLASS = (
            RootCommand if self.root_command_class is None else self.root_command_class
        )

        pipeline = Pipeline()
        pipeline._init(
            root_directory=None,
            settings_module=None,
            argv=arg_list,
            force_dry_run=force_dry_run,
            **kwargs
        )
        return_code = pipeline.run()

        return return_code, pipeline.result
