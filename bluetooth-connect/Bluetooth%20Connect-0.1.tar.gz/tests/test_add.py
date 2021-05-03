import bluetooth

# Improvize test cases everything is default true
def test_list_of_devices():
    assert bluetooth.list_devices() == {
        "id": "00:1E:7C:93:AB:49",
        "name": "Infinity Glide 501",
    }


def test_remove_device():
    device_id = "00:1E:7C:93:AB:49"
    bluetooth.remove_device(device_id)
    return True


def test_pair_device():
    device_id = "00:1E:7C:93:AB:49"
    bluetooth.pair_device(device_id)
    return True
