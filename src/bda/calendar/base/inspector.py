from datetime import datetime
from timezone import timezoneAdjuster


def dtYear(dt, context=None):
    """Return the year of dt.
    """
    if pyDt(dt):
        dt = timezoneAdjuster(context, dt)
        return dt.year
    return dt.year()


def dtMonth(dt, context=None):
    """Return the month of dt.
    """
    if pyDt(dt):
        dt = timezoneAdjuster(context, dt)
        return dt.month
    return dt.month()


def dtDay(dt, context=None):
    """Return the day of dt.
    """
    if pyDt(dt):
        dt = timezoneAdjuster(context, dt)
        return dt.day
    return dt.day()


def dtHour(dt, context=None):
    """Return the hour of dt.
    """
    if pyDt(dt):
        dt = timezoneAdjuster(context, dt)
        return dt.hour
    return dt.hour()


def dtMinute(dt, context=None):
    """Return the minute of dt.
    """
    if pyDt(dt):
        dt = timezoneAdjuster(context, dt)
        return dt.minute
    return dt.minute()


def dtWeekday(dt, context=None):
    """Return the weekday of dt.
    """
    if pyDt(dt, context=None):
        dt = timezoneAdjuster(context, dt)
        return dt.weekday() + 1
    return dt.dow()


def pyDt(dt, context=None):
    """Return wether dt is instance of datetime object.
    """
    return isinstance(dt, datetime)
