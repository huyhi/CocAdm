# coding: utf-8
# Create by Annhuny On 2019-12-28 19:16
# File Name : enums.py
from enum import Enum


class ErrEnums(Enum):
    TestError = (200, 'test')
    DatetimeParamsError = (101, '开始时间晚于结束时间')
    IntervalStepError = (102, '由于时间采集粒度为2小时，间隔必须为2的整数倍')
    DatetimeIntervalError = (103, '间隔过多，最大行数24')


class SeasonStatus(object):
    INACTIVE = 0
    ACTIVE = 1


class IntervalType(object):
    HOURS = 1
    DAY = 2
    MONTH = 3
