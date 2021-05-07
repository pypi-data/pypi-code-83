from collections import namedtuple
import datetime
import math

WeekTow = namedtuple('WeekTow', 'week tow day_of_week')

GPS_TIME_START = datetime.datetime(1980, 1, 6, 0, 0, 0)
SECONDS_IN_DAY = 24 * 60 * 60

# ------------------------------------------------------------------------------

def to_week_tow(epoch: datetime.datetime) -> WeekTow:
    """
    Convert from datetime to GPS week

    >>> to_week_tow(datetime.datetime(1980, 1, 6))
    WeekTow(week=0, tow=0.0, day_of_week=0)
    >>> to_week_tow(datetime.datetime(2005, 1, 28, 13, 30))
    WeekTow(week=1307, tow=480600.0, day_of_week=5)

    Conversion method based on algorithm provided in this link
    http://www.novatel.com/support/knowledge-and-learning/published-papers-and-documents/unit-conversions/
    """

    timedelta = epoch - GPS_TIME_START

    gpsw = int(timedelta.days / 7)
    day = timedelta.days - 7 * gpsw
    tow = timedelta.microseconds * 1e-6 + timedelta.seconds + day * SECONDS_IN_DAY

    return WeekTow(gpsw, tow, day)


# ------------------------------------------------------------------------------

def from_week_tow(week: int, tow: float) -> datetime.datetime:
    """
    Convert from datetime to GPS week

    >>> from_week_tow(0, 0.0)
    datetime.datetime(1980, 1, 6, 0, 0)
    >>> from_week_tow(1307, 480600.0)
    datetime.datetime(2005, 1, 28, 13, 30)
    """

    delta = datetime.timedelta(weeks=week, seconds=tow)

    return GPS_TIME_START + delta


def weektow_to_datetime(tow: float, week: int) -> datetime.datetime:
    import warnings
    warnings.warn("This function will be replaced by 'from_week_tow'", DeprecationWarning, stacklevel=2)
    return from_week_tow(week, tow)


def epoch_range(start_epoch, end_epoch, interval_s):
    """
    Iterate between 2 epochs with a given interval

    >>> import datetime
    >>> st = datetime.datetime(2015, 10, 1,  0,  0,  0)
    >>> en = datetime.datetime(2015, 10, 1,  0, 59, 59)
    >>> interval_s = 15 * 60
    >>> ','.join([str(d) for d in epoch_range(st, en, interval_s)])
    '2015-10-01 00:00:00,2015-10-01 00:15:00,2015-10-01 00:30:00,2015-10-01 00:45:00'
    >>> st = datetime.datetime(2015, 10, 1,  0,  0,  0)
    >>> en = datetime.datetime(2015, 10, 1,  1,  0,  0)
    >>> interval_s = 15 * 60
    >>> ','.join([str(d) for d in epoch_range(st, en, interval_s)])
    '2015-10-01 00:00:00,2015-10-01 00:15:00,2015-10-01 00:30:00,2015-10-01 00:45:00,2015-10-01 01:00:00'
    """

    total_seconds = (end_epoch - start_epoch).total_seconds() + interval_s / 2.0
    n_intervals_as_float = total_seconds / interval_s
    n_intervals = int(n_intervals_as_float)
    if math.fabs(n_intervals - n_intervals_as_float) >= 0.5:
        n_intervals = n_intervals + 1

    for q in range(n_intervals):
        yield start_epoch + datetime.timedelta(seconds=interval_s * q)



