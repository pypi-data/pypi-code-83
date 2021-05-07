"""
Global test fixtures
"""
from datetime import datetime
from pathlib import Path
from random import randint
from typing import Tuple

import pytest
from astropy.io import fits

from dkist_processing_common._util.constants import Constants
from dkist_processing_common._util.scratch import WorkflowFileSystem
from dkist_processing_common._util.tags import TagDB


@pytest.fixture()
def recipe_run_id():
    return randint(0, 99999)


@pytest.fixture()
def tag_db(recipe_run_id) -> TagDB:
    t = TagDB(recipe_run_id=recipe_run_id, task_name="test_tags")
    yield t
    t.purge()
    t.close()


@pytest.fixture()
def tag_db2(recipe_run_id) -> TagDB:
    """
    Another instance of a tag db in the same redis db
    """
    recipe_run_id = recipe_run_id + 15  # same db number but different namespace
    t = TagDB(recipe_run_id=recipe_run_id, task_name="test_tags2")
    yield t
    t.purge()
    t.close()


@pytest.fixture(params=[None, "use_tmp_path"])
def workflow_file_system(request, recipe_run_id, tmp_path) -> Tuple[WorkflowFileSystem, int, Path]:
    if request.param == "use_tmp_path":
        path = tmp_path
    else:
        path = request.param
    wkflow_fs = WorkflowFileSystem(
        recipe_run_id=recipe_run_id,
        task_name="wkflow_fs_test",
        scratch_base_path=path,
    )
    yield wkflow_fs, recipe_run_id, tmp_path
    wkflow_fs.purge(ignore_errors=True)
    tmp_path.rmdir()
    wkflow_fs.close()


@pytest.fixture()
def constants(recipe_run_id) -> Constants:
    constants = Constants(recipe_run_id=recipe_run_id, task_name="test_constants")
    yield constants
    constants.purge()
    constants.close()


@pytest.fixture()
def complete_common_header():
    """
    A header with some common by-frame keywords and a single instrument specific one
    """
    hdu = fits.PrimaryHDU()
    hdu.header["TELEVATN"] = 6.28
    hdu.header["TAZIMUTH"] = 3.14
    hdu.header["TTBLANGL"] = 1.23
    hdu.header["DATE-OBS"] = "1988-05-25T01:23:45.678"
    hdu.header["INST_FOO"] = "bar"
    hdu.header["DKIST004"] = "ip task type"
    hdu.header["ID___004"] = "ip id"
    hdu.header["PAC__004"] = "polarizer"
    hdu.header["PAC__005"] = 31.2
    hdu.header["PAC__006"] = "retarder"
    hdu.header["PAC__007"] = 6.66
    hdu.header["PAC__008"] = "dark shutter"
    hdu.header["INSTRUME"] = "VBI"

    return hdu.header
