#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 01:28
# File Name : season.py
from django.shortcuts import render
from django.views import View

from DB.service import get_season_statistic_by_season_id, get_season_list, get_season_by_id


class Season(View):
    def get(self, request):
        # return JsonResponse({
        #     'data': [i.to_dict() for i in get_season_list()]
        # })
        return render(request, 'season/season_statistic.html', {})


class SeasonStatistics(View):
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
        # return JsonResponse({
        #     'data': season_statistic_raw
        # })

        return render(request, 'season/season_statistic.html', {
            'data': season_statistic_raw,
            'season_list': [i.to_dict() for i in get_season_list()],
            'season': get_season_by_id(season_id)
        })

