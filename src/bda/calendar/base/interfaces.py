from zope.interface import Interface


class ITimezoneFactory(Interface):
    """Find the current timezone as pytz timezone."""

    def __call__():
        """Perform the detection."""
