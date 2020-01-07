# coding: utf-8
# Create by Annhuny On 2020-01-02 23:44
# File Name : realtime.py
import datetime
import json
import os

from django.http import JsonResponse

from DB.redis_session import r_session
from DB.service import get_daily_statistic_by_datetime_tag
from settings import PROJECT_ROOT_DIR
from spider.clan import ClanSpider
from utils.tools import to_percentage, floor_2hours
from views.base import BaseView

REALTIME_DATA_CACHE_KEY = 'realtime_data_cache'
DEFAULT_EXP_SECONDS = 60


class Realtime(BaseView):
    def get(self, request):
        # 使用 r_session 缓存 api 数据
        cache = r_session.get(REALTIME_DATA_CACHE_KEY)
        if cache:
            realtime = json.loads(cache)
        else:
            # realtime = ClanSpider.clan_detail()
            realtime = json.loads(open(os.path.join(PROJECT_ROOT_DIR, 'json_example', 'clan_detail.json')).read())
            r_session.set(REALTIME_DATA_CACHE_KEY, json.dumps(realtime), ex=DEFAULT_EXP_SECONDS)

        total_donations = sum([i['donations'] for i in realtime.get('memberList', [])])
        for item in realtime.get('memberList', []):
            item['donation_ratio'] = -1 if total_donations == 0 else to_percentage(item['donations'] / total_donations)

        daily_statistic = [item.to_dict() for item in get_daily_statistic_by_datetime_tag(floor_2hours())]
        th_level_ratio = {}
        total_players = len(daily_statistic)
        for item in daily_statistic:
            if item['townHallLevel'] in th_level_ratio:
                th_level_ratio[item['townHallLevel']]['count'] += 1
            else:
                th_level_ratio[item['townHallLevel']] = {
                    'count': 1
                }
        for item in th_level_ratio:
            print(item)
            th_level_ratio[item].update(**{
                'ratio': to_percentage(th_level_ratio[item]['count'] / total_players)
            })

        return self.success({
            'realtime': realtime,
            'total_donate': total_donations,
            'th_level_ratio': {
                'total': total_players,
                'ratio': th_level_ratio
            }
        })


class PlayerRealtimeInf(BaseView):
    def get(self, request, player_tag):
        return self.success(ClanSpider.player_information(player_tag=player_tag))
