from datetime import datetime
from typing import Union, List, Dict

from pydantic import BaseModel, Field


class Reference(BaseModel):
    index: int
    handle: str


class PidData(BaseModel):
    type: str
    parsed_data: Union[str, Dict]
    timestamp: datetime = Field(default_factory=datetime.now)
    ttl_type: int = Field(0, ge=0, le=1)
    ttl: int = 86400
    refs: List[Reference] = None
    privs: str = Field('rwr-', regex='^[r-][w-][r-][w-]')


class Pid(BaseModel):
    prefix: str = None
    suffix: str = None
    data: List[PidData] = None

    @property
    def pid_str(self) -> str:
        return f'{self.prefix}/{self.suffix}'

    # Setter doesn't work with Pydantic at the moment.
    # See github.com/samuelcolvin/pydantic/issues/1577
    def set_pid_str(self, value: str):
        items = value.split('/', 1)
        self.prefix = items[0]
        self.suffix = items[1]
