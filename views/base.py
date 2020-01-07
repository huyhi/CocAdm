# coding: utf-8
# Create by Annhuny On 2020-01-07 16:17
# File Name : base.py
from django.http import JsonResponse
from django.views import View


DEFAULT_SUCCESS_CODE = 200


class BaseView(View):
    def success(self, data):
        return JsonResponse({
            'code': DEFAULT_SUCCESS_CODE,
            'data': data
        })
