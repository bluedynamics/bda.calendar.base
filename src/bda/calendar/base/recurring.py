"""Module recurring.

This module provide functions to calculate recurring.

How to get the current day:

    from DateTime import DateTime
    from math import floor
    dt = DateTime('2007/03/20 10:00:00')
    # moment results in 13591.0
    moment = floor(float(dt.millis() / float(86400000)))

Remarks: millis is always relative to GMT
"""

__author__ = """Pawel Marzec <marzec@cjg.pl>,
                Robert Niederreiter <office@squarewave.at>,
                Jens Klein <jens@bluedynamics.com>"""
__docformat__ = 'plaintext'


from calculator import numberOfDaysInMonth
from calculator import numberOfDaysInYear
from converter import dt2epochday
from datetime import datetime
from datetime import timedelta
import pytz


RO_DAILY = "daily"
RO_MONTHLY = "monthly"
RO_WEEKLY = "weekly"
RO_YEARLY = "yearly"

RM_ONE_TIME = "one time"
RM_UNTIL = "until"
RM_FOREVER = "forever"

# the date in future which we assume as "end of forever"
FROZEN_DATE_IN_FUTURE = datetime(datetime.now().year + 10, 12, 31, 23, 59, 59,
                                 tzinfo=pytz.timezone('UTC'))


# calculators for recue indexes. i.e. for fast search via portal_catalog
def recueDays(start, until, recuemode, offset):
    """Generates list of recue days.

    * start - datetime
    * until - datetime, hour and minute matters!
    * recuemode - from RECUE_MODES
    * offset - current offset
    """
    if recuemode == RM_ONE_TIME:
        days = [dt2epochday(start)]
    elif recuemode == RM_UNTIL:
        days = _generateDays(start, until, offset)
    elif recuemode == RM_FOREVER:
        days = _generateDays(start, FROZEN_DATE_IN_FUTURE, offset)
    else:
        days = None
    return days


def _recueTimeDeltaDays(dt, offset):
    if offset == RO_DAILY:
        return timedelta(1)
    if offset == RO_WEEKLY:
        return timedelta(7)
    if offset == RO_MONTHLY:
        return timedelta(numberOfDaysInMonth(dt))
    if offset == RO_YEARLY:
        return timedelta(numberOfDaysInYear(dt))
    raise ValueError('Invalid offset type')


# private index values generators
def _generateDays(start, end, offset):
    days = []
    idt = start
    # print "start %s to end %s" % (idt, end)
    while idt <= end:
        days.append(dt2epochday(idt))
        idt = idt + _recueTimeDeltaDays(idt, offset)
    return days
