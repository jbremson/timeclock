# timeclock.py
# Joel Bremson
# 1/3/17
import arrow
import datetime
import dateutil


def check(dt, tz='UTC'):
    """Check to see if it is passed the given datetime in the given timezone.

    Args:
        dt: a datetime object, naive or tz aware.
        tz: a timezone name string.

    Returns:
        Boolean. True if it is past the given datetime in the
        timezone. False otherwise.
    """
    _dt = None
    if type(dt) == datetime.datetime:
        if not dt.tzinfo:
            _dt = arrow.get(dt, tz)
        else:
            _dt = arrow.get(dt)
    elif type(dt) == arrow.arrow.Arrow:
        if type(dt.tzinfo) == dateutil.tz.tz.tzlocal:
            # naive arrow time object
            _dt = arrow.get(dt, tz)
        else:
            _dt = arrow.get(dt)
    else:
        raise ValueError("Bad arguments sent to timeclock.check(): {} - {}".format(dt, tz))
    return _dt > arrow.now(tz)


periods = dict(annual=dict(months=12), semiannual=dict(months=6), triannual=dict(months=4),
                quarterly=dict(months=3), bimonthly=dict(months=2), monthly=dict(months=1),
                semimonthly=dict(days=15, hours=5), weekly=dict(days=7), daily=dict(days=1))


def period_passed(last_dt, period='annual'):
    """
    Has this period of time passed since the given date?

    Period options: annual, semi-annual, tri-annual, quarterly, bimonthly, monthly, semi-monthly, weekly, daily.

    Arguments:
        last_dt, datetime object.
        period, string (partial string of one of the period options.

    Returns:
        List of datetime objects indicating the datetimes in the year for the period.
    """
    if period not in periods.keys():
        raise ValueError("Invalid period sent to timeclock.period_passed: {}\nShould be in: {}".
                         format(period, periods.keys()))
    _dt = arrow.get(last_dt).shift(**periods[period])
    return not check(_dt)
