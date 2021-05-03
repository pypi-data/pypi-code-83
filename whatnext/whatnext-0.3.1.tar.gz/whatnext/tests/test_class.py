import logging
import os
import tempfile
import unittest

logger = logging.getLogger(__file__)


class WhatNextTestCase(unittest.TestCase):

    project_name: str = None
    graph_storage_dir: str = None
    test_graph_storage_dir: str = None

    @classmethod
    def setUpClass(cls):
        """This preserves the environmental variables"""

        logger.debug("Original Settings: ")
        logger.debug("\tWN_PROJECT={}".format(os.environ.get("WN_PROJECT", None)))
        logger.debug(
            "\tWN_STORAGE_DIR={}".format(os.environ.get("WN_STORAGE_DIR", None))
        )

        new_project_name = cls.__name__
        cls.project_name = os.environ.get("WN_PROJECT", None)
        os.environ["WN_PROJECT"] = new_project_name

        cls.graph_storage_dir = os.environ.get("WN_STORAGE_DIR", None)
        cls.test_graph_storage_dir = tempfile.mkdtemp(
            prefix="wn_unittest_", suffix="_" + new_project_name
        )
        os.environ["WN_STORAGE_DIR"] = cls.test_graph_storage_dir
        logger.debug("Test Settings: ")
        logger.debug("\tWN_PROJECT={}".format(os.environ.get("WN_PROJECT", None)))
        logger.debug(
            "\tWN_STORAGE_DIR={}".format(os.environ.get("WN_STORAGE_DIR", None))
        )

    @classmethod
    def tearDownClass(cls):
        if cls.project_name is not None:
            os.environ["WN_PROJECT"] = cls.project_name
        elif "WN_PROJECT" in os.environ:
            del os.environ["WN_PROJECT"]

        if cls.graph_storage_dir is not None:
            os.environ["WN_STORAGE_DIR"] = cls.graph_storage_dir
        elif "WN_STORAGE_DIR" in os.environ:
            del os.environ["WN_STORAGE_DIR"]

        if cls.test_graph_storage_dir is not None:
            try:
                os.remove(os.path.join(cls.test_graph_storage_dir, ".whatnext.gml"))
            except FileNotFoundError:
                pass
            try:
                os.remove(
                    os.path.join(cls.test_graph_storage_dir, ".whatnext.gml.backup")
                )
            except FileNotFoundError:
                pass
            try:
                os.rmdir(cls.test_graph_storage_dir)
            except FileNotFoundError:
                pass

        logger.debug("Restored Settings: ")
        logger.debug("\tWN_PROJECT={}".format(os.environ.get("WN_PROJECT", None)))
        logger.debug(
            "\tWN_STORAGE_DIR={}".format(os.environ.get("WN_STORAGE_DIR", None))
        )
