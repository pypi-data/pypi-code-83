from .calendar import Calendar


def get(calendar_id):
    cal = Calendar(id=calendar_id)
    cal.load()
    return(cal)
