"""
Task(s) for the clean up tasks at the conclusion of a processing pipeline
"""
import logging

from dkist_processing_common.tasks.base import WorkflowDataTaskBase
from dkist_processing_common.tasks.mixin.metadata_store import MetadataStoreMixin


logger = logging.getLogger(__name__)


class Teardown(WorkflowDataTaskBase, MetadataStoreMixin):
    """
    Changes the status of the recipe run to "COMPLETEDSUCCESSFULLY"
    Deletes the scratch directory containing all data from this pipeline run
    """

    def purge_data(self) -> None:
        """
        Wrapper for the purge method in WorkflowFileSystem
        """
        self._scratch.purge()
        self.constants.purge()

    def run(self) -> None:
        with self.apm_step("Change Recipe Run to Complete Successfully"):
            self.metadata_store_change_recipe_run_to_completed_successfully()

        logger.info(f"Removing data and tags for recipe run {self.recipe_run_id}")

        with self.apm_step("Remove Data and Tags"):
            self.purge_data()
