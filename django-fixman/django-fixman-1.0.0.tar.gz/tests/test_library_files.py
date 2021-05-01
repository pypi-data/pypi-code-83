from fixman.library.files import *

# Tests


class TestFixtureFile(object):

    def test_get_full_path(self):
        f = FixtureFile("testing")
        assert f.get_full_path() == "fixtures/testing/initial.json"

    def test_get_path(self):
        f = FixtureFile("testing")
        assert f.get_path() == "fixtures/testing"

    def test_init(self):
        f = FixtureFile("testing", model="TestModel")
        assert f.export == "testing.TestModel"
        assert f.file_name == "testmodel.json"

        f = FixtureFile("testing")
        assert f.export == "testing"

        f = FixtureFile("testing", path="testing")
        assert f.path == "testing"

        f = FixtureFile("testing")
        assert f.path == "fixtures/testing"

        f = FixtureFile("testing")
        assert f._full_path == "fixtures/testing/initial.json"

        f = FixtureFile("testing", project_root="/path/to/example_project")
        assert f._full_path == "/path/to/example_project/fixtures/testing/initial.json"

    def test_label(self):
        f = FixtureFile("testing", model="TestModel")
        assert f.label == "testing.TestModel"

        f = FixtureFile("testing")
        assert f.label == "testing"

    def test_repr(self):
        f = FixtureFile("testing")
        assert repr(f) == "<FixtureFile fixtures/testing/initial.json>"
