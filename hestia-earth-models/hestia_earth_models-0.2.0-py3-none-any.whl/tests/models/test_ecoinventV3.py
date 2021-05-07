from unittest.mock import patch
import json
from tests.utils import fixtures_path, fake_new_emission

from hestia_earth.models.ecoinventV3 import run

class_path = 'hestia_earth.models.ecoinventV3'
fixtures_folder = f"{fixtures_path}/ecoinventV3"
TERMS = [
    '11DichlorotetrafluoroethaneToAirInputsProduction',
    '112TrichlorotrifluoroethaneToAirInputsProduction',
    '1112TetrafluoroethaneToAirInputsProduction',
    'bromochlorodifluoromethaneToAirInputsProduction',
    'ch4ToAirInputsProductionFossil',
    'ch4ToAirInputsProductionNonFossil',
    'chlorodifluoromethaneToAirInputsProduction',
    'co2ToAirInputsProduction',
    'dichlorodifluoromethaneToAirInputsProduction',
    'n2OToAirInputsProduction',
    'nh3ToAirInputsProduction',
    'noxToAirInputsProduction',
    'so2ToAirInputsProduction'
]


@patch(f"{class_path}.get_emission_inputs_production_terms", return_value=TERMS)
@patch(f"{class_path}._emission", return_value={})
def test_run_all_models(mock_emission, *args):
    run(None, {})
    assert mock_emission.call_count == len(TERMS)

    mock_emission.reset_mock()
    run('', {})
    assert mock_emission.call_count == len(TERMS)

    mock_emission.reset_mock()
    run('null', {})
    assert mock_emission.call_count == len(TERMS)

    mock_emission.reset_mock()
    run('all', {})
    assert mock_emission.call_count == len(TERMS)


@patch(f"{class_path}.get_emission_inputs_production_terms", return_value=TERMS)
@patch(f"{class_path}._new_emission", side_effect=fake_new_emission)
def test_run_all(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    result = run(None, cycle)
    assert result == expected
