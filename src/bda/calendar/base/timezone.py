# -*- coding: utf-8 -*-
# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public Licence Version 2 or later

import time
import pytz
from datetime import datetime
from zope.interface import implementer
from interfaces import ITimezoneFactory

@implementer(ITimezoneFactory)
def ServerTimezoneFactory(context):
    """The timezone of the server."""
    zones =  time.tzname
    if zones and len(zones) > 0:
        zone = zones[0]
    else:
        zone = 'UTC'
    return pytz.timezone(zone)
    
def timezoneAdjuster(context, dt):
    """convinience: new datetime with given timezone."""
    newtz = ITimezoneFactory(context)
    return dt.astimezone(newtz)

def tzawarenow():
    now = datetime.utcnow()
    return datetime(now.year, now.month, now.day, now.hour, now.minute,
                    now.second, tzinfo=pytz.timezone('UTC'))