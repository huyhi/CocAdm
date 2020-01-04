# coding: utf-8
# Create by Annhuny On 2020-01-02 23:44
# File Name : realtime.py
import json
import os

from django.http import JsonResponse
from django.views import View

from settings import PROJECT_ROOT_DIR
from spider.clan import ClanSpider


class Realtime(View):
    def get(self, request):
        return JsonResponse({
            'data': ClanSpider.clan_detail()
            # 'data': json.loads(open(os.path.join(PROJECT_ROOT_DIR, 'json_example', 'clan_detail.json')).read())
        })


class PlayerRealtimeInf(View):
    def get(self, request, player_tag):
        return JsonResponse({
            'data': ClanSpider.player_information(player_tag=player_tag)
        })
