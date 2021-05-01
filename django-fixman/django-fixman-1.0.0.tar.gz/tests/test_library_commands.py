from fixman.library.commands import *
# import subprocess


def mock_bad_getstatusoutput(command):
    return 1, "fail"


def mock_good_getstatusoutput(command):
    return 0, "ok"

# Tests


class TestDumpData(object):

    def test_get_command(self):
        dd = DumpData("test_app", database="testing", natural_foreign=True, natural_primary=True,
                      settings="tenants.example.settings")

        #(cd source &&
        # ./manage.py dumpdata --database=testing --indent=4 --natural-foreign --natural-primary
        # --settings=tenants.example.settings.py test_app > ../fixtures/test_app/initial.json)
        cmd = dd.get_command()
        assert "dumpdata" in cmd
        assert "database=testing" in cmd
        assert "indent=4" in cmd
        assert "natural-foreign" in cmd
        assert "natural-primary" in cmd
        assert "settings=tenants.example.settings" in cmd
        assert "test_app > ../fixtures/test_app/initial.json"

    def test_get_output(self):
        dd = DumpData("test_app")
        assert dd.get_output() is None

    def test_preview(self):
        dd = DumpData("test_app")
        assert dd.get_command() == dd.preview()

    def test_run(self, monkeypatch):

        # https://stackoverflow.com/a/28405771/241720
        monkeypatch.setattr("subprocess.getstatusoutput.__code__", mock_good_getstatusoutput.__code__)
        dd = DumpData("test_app")
        assert dd.run() is True

        monkeypatch.setattr("subprocess.getstatusoutput.__code__", mock_bad_getstatusoutput.__code__)
        dd = DumpData("test_app")
        assert dd.run() is False
 

class TestLoadData(object):

    def test_get_command(self):
        ld = LoadData("test_app", database="testing", settings="tenant.example.settings")
        # (cd source && ./manage.py loaddata --database=testing
        # --settings=tenant.example.settings ../fixtures/test_app/initial.json)
        cmd = ld.get_command()
        assert "loaddata" in cmd
        assert "database=testing" in cmd
        assert "settings=tenant.example.settings" in cmd
        assert "../fixtures/test_app/initial.json" in cmd

    def test_get_output(self):
        ld = LoadData("test_app")
        assert ld.get_output() is None

    def test_preview(self):
        ld = LoadData("test_app")
        assert ld.preview() == ld.get_command()

    def test_run(self, monkeypatch):
        # https://stackoverflow.com/a/28405771/241720
        monkeypatch.setattr("subprocess.getstatusoutput.__code__", mock_good_getstatusoutput.__code__)
        ld = LoadData("test_app")
        assert ld.run() is True

        monkeypatch.setattr("subprocess.getstatusoutput.__code__", mock_bad_getstatusoutput.__code__)
        ld = LoadData("test_app")
        assert ld.run() is False
