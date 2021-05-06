"""
Wrappers for all workflow tasks
"""
import json
from abc import ABC
from io import BytesIO
from pathlib import Path
from string import ascii_uppercase
from typing import Generator
from typing import Iterable
from typing import List
from typing import Optional
from typing import Union
from uuid import uuid4

import pkg_resources
from dkist_processing_core import TaskBase
from hashids import Hashids

from dkist_processing_common._util.constants import Constants
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common.tasks.mixin.fits import FitsDataMixin
from dkist_processing_common.tasks.mixin.metadata_store import MetadataStoreMixin

__all__ = ["ParsedL0InputTaskBase", "ScienceTaskL0ToL1Base", "WorkflowDataTaskBase"]

tag_type_hint = Union[Iterable[str], str]


class WorkflowDataTaskBase(TaskBase, ABC):
    """
    Wrapper for all tasks that need to access the persistent automated processing data stores.
    Adds capabilities for accessing:
      scratch
      tags
      constants
    """

    def __init__(
        self,
        recipe_run_id: int,
        workflow_name: str,
        workflow_version: str,
        apm_client_config: Optional[dict] = None,
    ):
        super().__init__(
            recipe_run_id=recipe_run_id,
            workflow_name=workflow_name,
            workflow_version=workflow_version,
            apm_client_config=apm_client_config,
        )
        task_name = self.__class__.__name__
        self._scratch = WorkflowFileSystem(recipe_run_id=recipe_run_id, task_name=task_name)
        self.constants = Constants(recipe_run_id=recipe_run_id, task_name=task_name)

    def read(self, tags: tag_type_hint) -> Generator[Path, None, None]:
        tags = self._parse_tags(tags)
        return self._scratch.find_all(tags=tags)

    def write(
        self,
        file_obj: Union[BytesIO, bytes],
        tags: tag_type_hint,
        relative_path: Union[Path, str, None] = None,
    ) -> Path:
        if not tags:
            raise ValueError(f"Tags are required")
        if isinstance(file_obj, BytesIO):
            file_obj = file_obj.read()
        tags = self._parse_tags(tags)
        relative_path = relative_path or f"{uuid4().hex}.dat"
        relative_path = Path(relative_path)
        self._scratch.write(file_obj=file_obj, relative_path=relative_path, tags=tags)
        return relative_path

    def tag(self, path: Union[Path, str], tags: tag_type_hint) -> None:
        """
        Wrapper for the tag method in WorkflowFileSystem
        """
        tags = self._parse_tags(tags)
        return self._scratch.tag(path=path, tags=tags)

    def tags(self, path: Union[Path, str]) -> List[str]:
        """
        Return list of tags that a path belongs to
        """
        return self._scratch.tags(path=path)

    @staticmethod
    def _parse_tags(tags: tag_type_hint) -> Iterable[str]:
        result = []
        if isinstance(tags, str):
            tags = [tags]
        for tag in tags:
            if not isinstance(tag, str):
                raise TypeError(f"Tags must be strings. Got {type(tag)} instead.")
            result.append(tag)
        return result

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self._scratch.close()
        self.constants.close()


class ParsedL0InputTaskBase(WorkflowDataTaskBase, ABC):
    @property
    def proposal_id(self) -> str:
        return self.constants["PROPOSAL_ID"]

    @property
    def dataset_id(self) -> str:
        return Hashids(min_length=5, alphabet=ascii_uppercase).encode(self.recipe_run_id)


class ScienceTaskL0ToL1Base(ParsedL0InputTaskBase, MetadataStoreMixin, FitsDataMixin, ABC):
    """"""

    is_task_manual: bool = False

    @property
    def library_versions(self) -> str:
        """
        Harvest the dependency names and versions from the environment for
          all packages beginning with 'dkist' or are a requirement for a package
          beginning with 'dkist'
        """
        distributions = {d.key: d.version for d in pkg_resources.working_set}
        libraries = {}
        for pkg in pkg_resources.working_set:
            if pkg.key.startswith("dkist"):
                libraries[pkg.key] = pkg.version
                for req in pkg.requires():
                    libraries[req.key] = distributions[req.key]
        return json.dumps(libraries)

    def record_provenance(self):
        self.metadata_store_record_provenance(
            is_task_manual=self.is_task_manual, library_versions=self.library_versions
        )

    def post_run(self) -> None:
        super().post_run()
        with self.apm_step("Record Provenance"):
            self.record_provenance()


# class ScienceTaskL0ToL1(WorkflowDataTaskBase, ABC):
#     """
#     Wrapper for all science tasks creating L1 data from L0 raw inputs
#     """
# @pytest.fixture()
# def package_dependencies() -> set:
#     """
#     Extract dependencies from setup.cfg and format into a set of package names
#     """
#     module_path = Path(dkist_processing_core.__path__[0])
#     setup_cfg = module_path.parent / "setup.cfg"
#     config = ConfigParser()
#     config.read(setup_cfg)
#     install_requires = [d for d in config["options"]["install_requires"].splitlines() if d]
#     requirements = install_requires + ["dkist-processing-core"]
#     dependencies = {pkg.split(" ")[0] for pkg in requirements}
#     dependencies_without_optionals = {d.split("[")[0] for d in dependencies}
#     return dependencies_without_optionals
#
# def test_library_versions(task_instance, package_dependencies):
#     """
#     Given: An instance of a TaskBase subclass
#     When: accessing library_versions attr
#     Then: Result contains the dkist-processing-core package and packages specified in setup.cfg
#       - options.install_requires
#       - options.extras_require.test
#       Result does not contain any other packages
#       Result structure is Dict[str,str] where the key is library name and value is the version
#     """
#     library_names = task_instance.library_versions.keys()
#     assert len(library_names) == len(set(library_names))  # no duplicates
#     assert set(library_names) == package_dependencies  # only expected packages
#     library_versions = task_instance.library_versions.values()
#     assert all(library_versions)  # values for all versions
