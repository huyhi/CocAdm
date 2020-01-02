#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 15:04
# File Name : testfile.py

from django.http import JsonResponse
from django.views import View

from DB.sqlalchemy_session import session
from Models.enums import ErrEnums
from Models.models import DailyStatistic
from errors import CustomError
from spider.clan import ClanSpider


class TestView(View):
    def get(self, request):
        # var = ClanSpider.player_information(playerTag='#22GU0VCQR')
        # session.add(FlowingData(**var))
        # session.commit()
        return JsonResponse({
            'var': 1 / 0
        })


