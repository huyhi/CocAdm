#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:04
# File Name : testfile.py

from django.http import JsonResponse
from django.views import View

from DB.sqlalchemySession import session
from Models.models import FlowingData
from settings import cfg
from spider.clan import ClanSpider


class TestView(View):
    def get(self, request):
        var = ClanSpider.player_information(playerTag='#22GU0VCQR')
        session.add(FlowingData(**var))
        session.commit()
        return JsonResponse({
            'var': var
        })


