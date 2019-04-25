from datetime import datetime
from interfaces import ITimezoneFactory
from zope.interface import implementer
import pytz
import time


@implementer(ITimezoneFactory)
def ServerTimezoneFactory(context):
    """The timezone of the server."""
    zones = time.tzname
    if zones and len(zones) > 0:
        zone = zones[0]
    else:
        zone = 'UTC'
    return pytz.timezone(zone)


def timezoneAdjuster(context, dt):
    """Convinience: new datetime with given timezone."""
    newtz = ITimezoneFactory(context)
    return dt.astimezone(newtz)


def tzawarenow():
    now = datetime.utcnow()
    return datetime(now.year, now.month, now.day, now.hour, now.minute,
                    now.second, tzinfo=pytz.timezone('UTC'))
