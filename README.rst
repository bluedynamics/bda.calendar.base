==========================================================
Convinience for Datetime handling in combination with Zope
==========================================================

``bda.calendar.base`` contains functions adressing programmers all-day tasks
not (or only partly) covered by pythons datetime or zopes DateTime.

Major part of these function is timezone aware. Also ist easy to deal with 
timezones. An TimezoneFactory can be provided in the specific application
to i.e. be aware of the users timezone (i.e. in case of webapps).


calculators
-----------

CWof(date)
    the calendar week number of a date.
    
firstDayOfCW(year, cw, tzinfo=None)
    first day of a numbered calendar week
    
daysOfWeek(year, cw, tzinfo=None)
    yields 7 datetimes of the given calendar week
    
numberOfDaysInYear(dt)
    calculate number of day of the year of the given datetime year
           
numberOfDaysInMonth(dt)           
    calculates number of days of the given datetimes month 

daysOfMonth    
    yields all days as datetimes of the given month
    
hoursOfDay(year, month, day, tzinfo=None)
    yields all hours of a day as datetimes    
    
isSameDay(first, second)    
    detects if two dates are the same day. bool.
    

converter
---------

dt2DT(dt)
    Convert Python's datetime to Zope's DateTime. Acts timezone-aware.
    
DT2dt(DT)
    Convert Zope's DateTime to Pythons's datetime. Acts timezone-neutral, 
    outcome is on UTC.
    
dt2UTCString(dt)
    build a '-' separated string from the datetime timetuple as UTC.
    
dtFromUTCString(utcstr)
    build datetime from timetuple UTC string.
    
dt2epochday(dt)
   Number of days since epoch.  
   timezone gets a problem here, we need to normalize all to GMT to make it 
   recognize the same day even if it a different timezone:
   i.e. 2008-05-01T00:00:00+02:00 (CEST) 


inspector
---------

All functions are using the timezoneAdjuster (see below). therefore a context is 
passed
 
dtYear(dt, context=None):
    year of datetime.
    
dtMonth(dt, context=None)
    month of datetime.

dtDay(dt, context=None)
    day of datetime.

dtHour(dt, context=None)
    hour of datetime.

dtMinute(dt, context=None)
    minute of datetime.
    
dtWeekday(dt, context=None)
    Weekday of datetime.
    
pyDt
    Detect wether dt is instance of datetime object.

  
recurring
---------

Simple recurring features. for more sophisticated recurring feature refer to
dateutils.rrule

recueDays(start, until, recuemode, offset)
    Generates list of recue days.    


timezone
--------

Dealing with timezones is always pain. With these common features it get less 
pain. Using ZCA where registering a common ``TimezoneFactory`` using the computers 
system timezone. It is used by the ``timezoneAdjuster``. If you register a more 
specific TimezoneFactory following its simple interface - its just a callable -
, you can implement user configurated multi-timezone aware applications.
This is all based on pytz, because pytz just works.

ServerTimezoneFactory(context)
    The timezone of the server (current computer). You never need to use this 
    directly.

timezoneAdjuster(context, dt)
    New datetime with given timezone. Given datetime cant be naive!
    
tzawarenow()
    timezone aware ``now`` datetime using utc timezone. if you need 
    the current timezone adjust it.


Contributors
============

- Jens Klein <jens@bluedynamics.com>
- Robert Niederreiter <rnix@squarewave.at>


License
=======

Copyright (c) 2008-2022, BlueDynamics Alliance, Austria
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the documentation and/or
  other materials provided with the distribution.
* Neither the name of the BlueDynamics Alliance nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY BlueDynamics Alliance ``AS IS`` AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL BlueDynamics Alliance BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


Changes
=======

1.2.5 (2022-12-05)
------------------

- Try again to release wheel with zest.releaser.
  [rnix]


1.2.4 (2022-12-05)
------------------

- Release wheel.
  [rnix]


1.2.3
-----

- Remove superfluous import.
  [rnix, 2020-08-12]


1.2.2
-----

- conditional ZCML for pyramid and zope.
  [rnix, 2011-11-16]
