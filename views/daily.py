# coding: utf-8
# Create by Annhuny On 2019-12-31 21:28
# File Name : daily.py
from datetime import datetime

from django.http import JsonResponse
from django.views import View

from DB.service import get_daily_statistic_by_player_tag_and_datetime_tag_list
from Models.enums import ErrEnums, IntervalType
from errors import CustomError
from utils.tools import is_even, hours, days


class DailyStatistic(View):
    def validate(self, req):
        start_time = datetime.strptime(req.GET.get('start_time'), '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(req.GET.get('end_time'), '%Y-%m-%d %H:%M:%S')
        interval_type = int(req.GET.get('interval_type'))
        interval_step = int(req.GET.get('interval_step'))   # 由于粒度是2h，所以这个必须是偶数
        if end_time < start_time:
            raise CustomError(ErrEnums.DatetimeParamsError)
        if interval_type == IntervalType.HOURS and not is_even(interval_step):
            raise CustomError(ErrEnums.IntervalStepError)

        interval = end_time - start_time

        if interval_type == IntervalType.HOURS:
            if int(interval / hours(interval_step)) > 24:
                raise CustomError(ErrEnums.DatetimeIntervalError)
            interval_step = hours(interval_step)
        if interval_type == IntervalType.DAY:
            if int(interval / days(interval_step)) > 24:
                raise CustomError(ErrEnums.DatetimeIntervalError)
            interval_step = days(interval_step)

        return {
            'start_time': start_time,
            'end_time': end_time,
            'interval_step': interval_step
        }

    # params
    # player_tag, start_time, end_time, interval(day, month, hours), 最多24列
    def get(self, request, player_tag):
        params = self.validate(request)
        start_time = params['start_time']
        end_time = params['end_time']
        interval_step = params['interval_step']

        datetime_tag_list = []
        while start_time <= end_time:
            datetime_tag_list.append(start_time.strftime('%Y-%m-%d %H:%M:%S'))
            start_time = start_time + interval_step

        daily_statistic = get_daily_statistic_by_player_tag_and_datetime_tag_list('#' + player_tag, datetime_tag_list)

        return JsonResponse({
            'data': [i.to_dict() for i in daily_statistic]
        })
