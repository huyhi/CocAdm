# coding: utf-8
# Create by Annhuny On 2020-01-02 23:44
# File Name : realtime.py
import json
import os

from django.http import JsonResponse
from django.views import View

from DB.redis_session import r_session
from settings import PROJECT_ROOT_DIR
from spider.clan import ClanSpider

REALTIME_DATA_CACHE_KEY = 'realtime_data_cache'
DEFAULT_EXP_SECONDS = 60


class Realtime(View):
    def get(self, request):
        # 使用 r_session 缓存 api 数据
        cache = r_session.get(REALTIME_DATA_CACHE_KEY)
        if cache:
            res = json.loads(cache)
        else:
            res = ClanSpider.clan_detail()
            # res = json.loads(open(os.path.join(PROJECT_ROOT_DIR, 'json_example', 'clan_detail.json')).read())
            r_session.set(REALTIME_DATA_CACHE_KEY, json.dumps(res), ex=DEFAULT_EXP_SECONDS)

        return JsonResponse({
            'data': res
        })


class PlayerRealtimeInf(View):
    def get(self, request, player_tag):
        return JsonResponse({
            'data': ClanSpider.player_information(player_tag=player_tag)
        })
