from fixman.utils import *
import os


def test_filter_fixtures():
    path = os.path.join("tests", "example_project", "fixtures", "config.ini")
    fixtures = load_fixtures(path)

    assert len(filter_fixtures(fixtures, apps=["lookups"])) == 9

    # BUG: Model filter will also fail if there is a fixture with no specified model.
    assert len(filter_fixtures(fixtures, models=["Goal"])) == 2

    assert len(filter_fixtures(fixtures, groups=["defaults"])) == 10
    assert len(filter_fixtures(fixtures, groups=["examples"])) == 20

    assert len(filter_fixtures(fixtures, skip_readonly=True)) == 31


def test_load_fixtures():
    assert load_fixtures("nonexistent") is None

    path = os.path.join("tests", "example_project", "fixtures", "config.ini")
    fixtures = load_fixtures(path)
    assert len(fixtures) == 33


def test_scan_fixtures():
    path = os.path.join("tests", "example_project", "source")
    results = scan_fixtures(path)
    assert len(results) == 4
