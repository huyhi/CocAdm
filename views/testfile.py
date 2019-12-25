#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:04
# File Name : testfile.py

from django.http import JsonResponse
from django.views import View

from settings import cfg
from spider.clan import ClanSpider


class TestView(View):
    def get(self, request):
        var = ClanSpider().clanDetail(clanTag='#PCCR9LQU')

        return JsonResponse({
            'test': var
        })
    pass
