#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2022
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from dateutil.easter import EASTER_ORTHODOX, easter
from dateutil.relativedelta import relativedelta as rd
from dateutil.relativedelta import SU

from holidays.constants import JAN, FEB, MAY, NOV
from holidays.holiday_base import HolidayBase


class Serbia(HolidayBase):
    # https://en.wikipedia.org/wiki/Public_holidays_in_Serbia

    country = "RS"

    def __init__(self, **kwargs):
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        # New Year's Day
        name = "Нова година"
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name
        if self.observed and self._is_weekend(date(year, JAN, 1)):
            self[date(year, JAN, 3)] = name + " (Observed)"
        # Orthodox Christmas
        name = "Божић"
        self[date(year, JAN, 7)] = name
        # Statehood day
        name = "Дан државности Србије"
        self[date(year, FEB, 15)] = name
        self[date(year, FEB, 16)] = name
        if self.observed and self._is_weekend(date(year, FEB, 15)):
            self[date(year, FEB, 17)] = name + " (Observed)"
        # International Workers' Day
        name = "Празник рада"
        self[date(year, MAY, 1)] = name
        self[date(year, MAY, 2)] = name
        if self.observed and self._is_weekend(date(year, MAY, 1)):
            if date(year, MAY, 2) == easter(year, method=EASTER_ORTHODOX):
                self[date(year, MAY, 4)] = name + " (Observed)"
            else:
                self[date(year, MAY, 3)] = name + " (Observed)"
        # Armistice day
        name = "Дан примирја у Првом светском рату"
        self[date(year, NOV, 11)] = name
        if self.observed and date(year, NOV, 11).weekday() == SU.weekday:
            self[date(year, NOV, 12)] = name + " (Observed)"
        # Easter
        self[
            easter(year, method=EASTER_ORTHODOX) - rd(days=2)
        ] = "Велики петак"
        self[
            easter(year, method=EASTER_ORTHODOX) - rd(days=1)
        ] = "Велика субота"
        self[easter(year, method=EASTER_ORTHODOX)] = "Васкрс"
        self[
            easter(year, method=EASTER_ORTHODOX) + rd(days=1)
        ] = "Други дан Васкрса"


class RS(Serbia):
    pass


class SRB(Serbia):
    pass
