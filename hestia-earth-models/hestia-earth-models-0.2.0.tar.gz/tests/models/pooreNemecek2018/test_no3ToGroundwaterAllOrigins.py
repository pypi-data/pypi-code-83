from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_emission

from hestia_earth.models.pooreNemecek2018.no3ToGroundwaterAllOrigins import TERM_ID, run, _should_run

class_path = f"hestia_earth.models.pooreNemecek2018.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/pooreNemecek2018/{TERM_ID}"


@patch(f"{class_path}._most_relevant_measurement_value", return_value=[])
@patch(f"{class_path}.get_average_rooting_depth", return_value=0)
def test_should_run(mock_rooting_depth, mock_most_relevant_measurement_value):
    # no measurements => no run
    cycle = {}
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with measurements => no run
    mock_most_relevant_measurement_value.return_value = [10]
    should_run, *args = _should_run(cycle)
    assert not should_run

    # no rootingDepth => no run
    should_run, *args = _should_run({})
    assert not should_run

    # with rootingDepth => run
    mock_rooting_depth.return_value = 10
    should_run, *args = _should_run({})
    assert should_run


@patch(f"{class_path}._new_emission", side_effect=fake_new_emission)
def test_run(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(cycle)
    assert value == expected
