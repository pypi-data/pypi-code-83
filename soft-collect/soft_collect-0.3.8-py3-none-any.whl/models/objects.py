from dataclasses import dataclass

from cx_Oracle import LOB


@dataclass
class ObjResult:
    """Class for Objects Query Result"""

    key: str
    part: int
    obj: bytes
    idcas: str = ""

    def __post_init__(self):
        if isinstance(self.obj, LOB):
            self.obj = self.obj.open().read()
