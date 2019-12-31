#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 19:16
# File Name : enums.py
from enum import Enum


class ErrEnums(Enum):
    TestError = (200, 'test')


class SeasonStatus(object):
    INACTIVE = 0
    ACTIVE = 1
