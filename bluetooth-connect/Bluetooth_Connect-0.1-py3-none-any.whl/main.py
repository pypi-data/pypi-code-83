from bluetooth.utils import externalcommand, decode, read_json
from bluetooth.models import BluetoothVehicle
from bluetooth.exceptions import timeout_exception, process_exception
from typing import Optional
from pathlib import Path

BLUETOOOTH_COMMAND = "bluetoothctl"
BLUETOOOTH_SUBCOMMAND_PAIRED_DEVICES = "paired-devices"
BLUETOOOTH_SUBCOMMAND_REMOVE_DEVICE = "remove"
BLUETOOOTH_SUBCOMMAND_CONNECT_DEVICE = "connect"
BLUETOOOTH_SUBCOMMAND_SCAN_DEVICE = "scan"

devices_data = read_json(Path(__file__).parent / "bluetooth_peripherals/details.json")


def list_devices() -> Optional[dict]:
    op, _ = externalcommand(
        command=BLUETOOOTH_COMMAND, args=[BLUETOOOTH_SUBCOMMAND_PAIRED_DEVICES]
    )
    if op == b"":
        return None
    op_d = decode(op, strip=True)
    b = BluetoothVehicle(op_d)
    return b.to_dict()


def _scan_devices(timeout=5):
    try:
        op, err = externalcommand(
            command=BLUETOOOTH_COMMAND,
            args=[BLUETOOOTH_SUBCOMMAND_SCAN_DEVICE, "on"],
            timeout=timeout,
            raise_error=True,
        )
    except process_exception as e:
        print(e.stdout)
        exit()
    except timeout_exception:
        print("Successfully scanned")


def pair_device_name(device_name):  # Improvize this
    device_id = devices_data[device_name]["ID"]
    pair_device(device_id)


def remove_device_name(device_name):  # Improvize this
    device_id = devices_data[device_name]["ID"]
    remove_device(device_id)


def pair_device(device_id, max_trials=2):  # Improvize
    for i in reversed(range(2)):
        _scan_devices(timeout=10)
        op, _ = externalcommand(
            command=BLUETOOOTH_COMMAND,
            args=[BLUETOOOTH_SUBCOMMAND_CONNECT_DEVICE, device_id],
            raise_error=True,
        )
        print("Device Connected")
        break
    else:
        print("Tried {0} but didn't find the device".format(max_trials))


def remove_device(device_id: str):
    device = list_devices()
    if device is None:
        print("Devices not found")
    elif device["id"] == device_id:
        _, _ = externalcommand(
            command=BLUETOOOTH_COMMAND,
            args=[BLUETOOOTH_SUBCOMMAND_REMOVE_DEVICE, device_id],
        )
    else:
        print("Device ID {0} not found".format(device_id))
