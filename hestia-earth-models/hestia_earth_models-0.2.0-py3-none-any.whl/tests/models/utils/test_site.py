from unittest.mock import patch

from hestia_earth.models.utils.site import related_cycles

class_path = 'hestia_earth.models.utils.site'
CYCLE = {'@id': 'id'}


@patch(f"{class_path}.find_related", return_value=[CYCLE])
@patch(f"{class_path}.download_hestia", return_value=CYCLE)
def test_related_cycles(*args):
    assert related_cycles('id') == [CYCLE]
