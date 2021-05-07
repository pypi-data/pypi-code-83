import json
from unittest.mock import patch
from tests.utils import fake_new_emission, fixtures_path

from hestia_earth.models.schererPfister2015.pToGroundwaterAllOrigins import TERM_ID, _should_run, run

class_path = f"hestia_earth.models.schererPfister2015.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/schererPfister2015/{TERM_ID}"


@patch(f"{class_path}._most_relevant_measurement_value", return_value=[])
@patch(f"{class_path}.get_organic_fertilizer_P_total", return_value=0)
def test_should_run(mock_P_total, mock_measurement):
    # no measurements => no run
    cycle = {'measurements': []}
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with measurements => no run
    mock_measurement.return_value = [10]
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with N total => run
    mock_P_total.return_value = 10
    should_run, *args = _should_run(cycle)
    assert should_run


@patch(f"{class_path}._new_emission", side_effect=fake_new_emission)
def test_run(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(cycle)
    assert value == expected
