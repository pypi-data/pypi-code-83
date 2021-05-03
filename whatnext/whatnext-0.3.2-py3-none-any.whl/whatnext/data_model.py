# pylint: disable=E0611
import datetime
from typing import List, Optional

from pydantic import BaseModel


class TimeLog(BaseModel):
    task_id: int
    user_id: str
    start_time: Optional[datetime.datetime]
    end_time: Optional[datetime.datetime]
    note: Optional[str]


class Task(BaseModel):
    user_id: str
    task_id: int
    name: str
    project: str
    importance: float
    completed: Optional[bool]
    due: Optional[datetime.datetime]
    tags: Optional[List[str]]
    urls: Optional[List[str]]
    users: Optional[List[str]]
    notes: Optional[List[str]]
    time_logs: Optional[List[TimeLog]]
