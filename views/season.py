#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 01:28
# File Name : season.py
from django.http import JsonResponse

from DB.service import get_season_statistic_by_season_id, get_season_list
from views.base import BaseView


class Season(BaseView):
    def get(self, request):
        return self.success([i.to_dict() for i in get_season_list()])


class SeasonStatistics(BaseView):
    def validate(self):
        order_by_param = {
            'expLevel', 'role', 'trophies', 'attackWins', 'donations', 'donationsReceived',
            'RD_ratio', 'DR_ratio'
        }

    def get(self, request, season_id):
        order_by = request.GET.get('orderBy', 'donations')
        is_reverse = True if request.GET.get('isReverse', 'true') == 'true' else False

        season_statistic_raw = [i.to_dict() for i in get_season_statistic_by_season_id(season_id)]
        for item in season_statistic_raw:
            item['RD_ratio'] = -1 if item['donations'] == 0 else round(item['donationsReceived'] / item['donations'], 3)
            item['DR_ratio'] = -1 if item['donationsReceived'] == 0 else round(item['donations'] / item['donationsReceived'], 3)

        season_statistic_raw.sort(key=lambda i: i.get(order_by), reverse=is_reverse)
        return self.success(season_statistic_raw)
