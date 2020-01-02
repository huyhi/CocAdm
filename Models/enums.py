# coding: utf-8
# Create by Annhuny On 2019-12-28 19:16
# File Name : enums.py
import datetime
from enum import Enum

from utils.tools import two_hours, one_day


class ErrEnums(Enum):
    TestError = (200, 'test')
    DatetimeParamsError = (101, '开始时间晚于结束时间')
    DatetimeIntervalError = (102, '间隔过多')


class SeasonStatus(object):
    INACTIVE = 0
    ACTIVE = 1


class DatetimeInterval(object):
    HOURS = 1
    DAY = 2
    MONTH = 3

    @classmethod
    def interval(cls, key):
        m = {
            cls.HOURS: two_hours,
            cls.DAY: one_day
        }
        return m.get(key)
