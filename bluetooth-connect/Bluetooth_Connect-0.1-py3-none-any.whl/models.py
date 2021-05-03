from bluetooth.utils import to_id_name


class BluetoothVehicle:
    def __init__(self, p):
        b_id, name = to_id_name(p)
        self.id = b_id
        self.name = name

    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}
