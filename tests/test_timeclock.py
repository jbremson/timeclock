from __future__ import absolute_import
import datetime
from pytz import timezone
from timeclock import check, period_passed
import unittest


class TestTimeclock(unittest.TestCase):

    def test_check(self):
        dt = datetime.datetime.now() + datetime.timedelta(days=1)
        self.assertTrue(check(dt, 'US/Pacific'))
        dt = datetime.datetime.now() - datetime.timedelta(days=1)
        self.assertFalse(check(dt, 'US/Pacific'))
        dt = datetime.datetime.utcnow()
        self.assertFalse(check(dt))
        dt = datetime.datetime.now(timezone('Australia/Sydney'))
        self.assertTrue(dt)

    def test_period_passed(self):
        dt = datetime.datetime.now() + datetime.timedelta(days=1)
        self.assertFalse(period_passed(dt))
        dt = datetime.datetime.now() - datetime.timedelta(days=188)
        self.assertTrue(period_passed(dt,'semiannual'))
        dt = datetime.datetime.now() - datetime.timedelta(days=8)
        self.assertTrue(period_passed(dt,'weekly'))
