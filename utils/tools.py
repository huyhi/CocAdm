# coding: utf-8
# Create by Annhuny On 2019-12-31 23:37
# File Name : tools.py
import datetime


def is_even(num):
    if not isinstance(num, (float, int)):
        return False
    else:
        return True if int(num % 2) == 0 else False


def days(val):
    return datetime.timedelta(days=val)


def hours(val):
    return datetime.timedelta(hours=val)


def to_percentage(f_val):
    return round(f_val * 100, 1)
