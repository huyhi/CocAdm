#!/usr/bin/env python
# Create by Annhuny On 2019-12-29 22:34
# File Name : middlewares.py
import json
import logging
import sys
import traceback
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from DB.sqlalchemy_session import session
from errors import CustomError, DEFAULT_ERR_CODE

logger = logging.getLogger('django')


class SessionClose(MiddlewareMixin):
    def process_response(self, request, response):
        session.close()
        return response


class ExceptionHandler(MiddlewareMixin):
    def process_exception(self, request, e):
        if isinstance(e, CustomError):
            res = {'code': e.code, 'msg': e.msg}
            return JsonResponse(res)
        else:
            logger.warning(traceback.format_exc())
            return JsonResponse({
                'code': DEFAULT_ERR_CODE,
                'msg': traceback.format_exc(),
            })
