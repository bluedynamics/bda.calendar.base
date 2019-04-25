# -*- coding: utf-8 -*-
# Copyright 2008-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
# GNU General Public Licence Version 2 or later

from zope.interface import Interface

class ITimezoneFactory(Interface):
    """Find the current timezone as pytz timezone."""

    def __call__():
        """perform the detection."""
        
