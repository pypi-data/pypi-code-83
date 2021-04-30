from typing import Union
from datetime import datetime


def flarum_to_datetime(flarum_dt: Union[str, None]=None) -> datetime:
    """
        Converts Flarum's datetime string to Python's datetime object.
        Doesn't convert if the parameter is already a datetime object.
        
        Flarum's datetime format is `%Y-%m-%dT%H:%M:%S%z`
    """

    if flarum_dt is None:
        return None

    if type(flarum_dt) == datetime:
        return flarum_dt

    return datetime.strptime(flarum_dt, '%Y-%m-%dT%H:%M:%S%z')


def datetime_to_flarum(dt: Union[datetime, None]=None) -> str:
    """
        Converts Python's datetime object to Flarum's datetime string.
        Doesn't convert if the parameter is already a string.
        
        Flarum's datetime format is `%Y-%m-%dT%H:%M:%S%z`
    """

    if dt is None:
        return None

    if type(dt) == str:
        return dt

    return dt.strftime('%Y-%m-%dT%H:%M:%S%z')
