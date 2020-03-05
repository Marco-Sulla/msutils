import arrow
import calendar
from more_itertools import numeric_range

def dayStart(arr):
    return arr.replace(hour=0, minute=0, second=0, microsecond=0)


def monthStart(arr):
    arr2 = dayStart(arr)

    return arr2.replace(day=1)


def isoWeekNum(arr):
    return arr.datetime.isocalendar()[1]


def weekDay(d):
    return int(d.format("d"))


def isFestive(d):
    weekday = weekDay(d)

    return weekday in [6, 7]


def prevWorkingDay(d):
    while isFestive(d):
        d = d.replace(days=-1)

    prevday = d.replace(days=-1)

    while isFestive(prevday):
        prevday = prevday.replace(days=-1)

    return prevday


def localize(date, tz):
    dt = arrow.get(date).datetime
    return arrow.get(dt, tz)


def span_week(start, end=None, *args, **kwargs):
    slices = arrow.Arrow.span_range(frame="week", start=start, end=end,
                                    *args, **kwargs)
    last_date = slices[len(slices) - 1][1]

    if end is not None and last_date < end:
        last_new = last_date.replace(microseconds=+1, days=+7)
        slices_2 = arrow.Arrow.span_range("week", last_date, last_new)

        return slices + slices_2

    return slices


def span_ranges(frame, start, end, *args, **kwargs):
    if frame == "week":
        slices = span_week(start=start, end=end, *args, **kwargs)
    else:
        slices = arrow.Arrow.span_range(frame=frame, start=start, end=end,
                                        *args, **kwargs)

    return slices


def millisecond_range(start, end, step=1):
    ms_start = start.float_timestamp * 1000
    ms_end = end.float_timestamp * 1000
    delta = ms_end - ms_start
    
    for x in numeric_range(0, delta, step):
        res = start.shift(microseconds=round(x)*1000)
        
        if res < end:
            yield res


def getLastDayOfMonth(date):
    days_in_month = calendar.monthrange(date.year, date.month)[1]
    return dayStart(date.replace(day=days_in_month))

__all__ = (
    dayStart.__name__,
    monthStart.__name__,
    isoWeekNum.__name__,
    weekDay.__name__,
    isFestive.__name__,
    prevWorkingDay.__name__,
    localize.__name__,
    span_week.__name__,
    span_ranges.__name__,
    getLastDayOfMonth.__name__, 
)
