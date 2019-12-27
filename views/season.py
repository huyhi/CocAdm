#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 01:28
# File Name : season.py
from django.views import View


class SeasonStatistics(View):
    def get(self, request):
        params = {
            'season': request.GET.get('season'),
            'orderBy': request.GET.get('season')
        }

        pass




