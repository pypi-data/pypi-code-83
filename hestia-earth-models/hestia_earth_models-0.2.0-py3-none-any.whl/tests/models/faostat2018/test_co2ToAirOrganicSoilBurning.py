from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_emission

from hestia_earth.models.faostat2018.co2ToAirOrganicSoilBurning import TERM_ID, run, _should_run

class_path = f"hestia_earth.models.faostat2018.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/faostat2018/{TERM_ID}"


@patch(f"{class_path}._most_relevant_measurement_value", return_value=[])
@patch(f"{class_path}.find_primary_product", return_value=None)
def test_should_run(mock_primary_product, mock_measurement):
    # no measurements => no run
    cycle = {'site': {'country': {}}}
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with measurements => no run
    mock_measurement.return_value = [10]
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with country id => no run
    cycle['site']['country'] = {'@id': 'GADM-BOL'}
    should_run, *args = _should_run(cycle)
    assert not should_run

    # with primary product => run
    mock_primary_product.return_value = {'term': {'@id': 'wheatGrain'}}
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
