#!/usr/bin/env python
# Create by Annhuny On 2019-12-26 21:03
# File Name : errors.py


class CustomError(Exception):
    def __init__(self, err):
        self.code = err.value[0]
        self.msg = err.value[1]

    def __str__(self):
        return 'code: {}, msg:{}'.format(self.code, self.msg)


DEFAULT_ERR_CODE = -1
