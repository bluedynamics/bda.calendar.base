from DateTime import DateTime
from math import floor
import datetime
import pytz


ONEDAYINMILLIS = 86400000.0


def dt2DT(dt):
    """Convert Python's datetime to Zope's DateTime.

    Acts timezone-aware.
    """
    if isinstance(dt, DateTime):
        return dt
    return DateTime(dt.isoformat())


def DT2dt(DT):
    """Convert Zope's DateTime to Pythons's datetime.

    Act timezone-neutral, outcome is on UTC.
    """
    if isinstance(DT, datetime.datetime):
        return DT
    # seconds (parts[6]) is a float, so we map to int
    DTutc = DT.toZone('UTC')
    year, month, day, hour, min, sec = DTutc.parts()[:6]
    sec = int(sec)
    utc = pytz.timezone('UTC')
    dt = datetime.datetime(year, month, day, hour, min, sec, tzinfo=utc)
    return dt


def dt2UTCString(dt):
    """Build a string from the timetuple as UTC.
    """
    dt = dt.astimezone(pytz.timezone('UTC'))
    return '-'.join(['%d' % v for v in dt.timetuple()[:6]])


def dtFromUTCString(utcstr):
    """Build datetime from timetuple UTC string.
    """
    y, m, d, h, mi, s = utcstr.split('-')
    dt = datetime.datetime(int(y), int(m), int(d), int(h), int(mi), int(s),
                           tzinfo=pytz.timezone('UTC'))
    return dt


def dt2epochday(dt):
    """Number of days since epoch.

    Timezone gets a problem here, we need to normalize all to GMT to make it
    recognize the same day even if it a different timezone:
    i.e. 2008-05-01T00:00:00+02:00 (CEST)
    """
    DT = dt2DT(dt)  # if possible replace this one and call in next line
    days = DT.earliestTime().millis() / ONEDAYINMILLIS
    idays = floor(days)
    return idays
