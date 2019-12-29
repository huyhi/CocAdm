#!/usr/bin/env python
# Create by Annhuny On 2019-12-29 22:34
# File Name : middlewares.py
from django.utils.deprecation import MiddlewareMixin

from DB.sqlalchemy_session import session


class SessionClose(MiddlewareMixin):
    def process_response(self, request, response):
        session.close()
        return response
