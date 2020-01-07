#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:04
# File Name : testfile.py

from django.http import JsonResponse

from views.base import BaseView


class TestView(BaseView):
    def get(self, request):
        return self.success(1 / 0)
