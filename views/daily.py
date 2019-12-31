# coding: utf-8
# Create by Annhuny On 2019-12-31 21:28
# File Name : daily.py
from datetime import datetime

from django.http import JsonResponse
from django.views import View

from DB.service import get_daily_statistic_by_player_tag_and_datetime_tag_list
from Models.enums import ErrEnums, DatetimeInterval
from errors import CustomError
from utils.tools import two_hours, one_day


class DailyStatistic(View):
    def validate(self, req):
        start_time = datetime.strptime(req.GET.get('start_time'), '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(req.GET.get('end_time'), '%Y-%m-%d %H:%M:%S')
        datetime_interval = int(req.GET.get('interval'))
        if end_time < start_time:
            raise CustomError(ErrEnums.DatetimeParamsError)

        interval = end_time - start_time

        if datetime_interval == DatetimeInterval.HOURS:
            if int(interval / two_hours) > 24:
                raise CustomError(ErrEnums.DatetimeIntervalError)
        if datetime_interval == DatetimeInterval.DAY:
            if int(interval / one_day) > 24:
                raise CustomError(ErrEnums.DatetimeIntervalError)
        # TODO 加入对月的统计
        # if datetime_interval == DatetimeInterval.MONTH:
        #     raise CustomError(ErrEnums.DatetimeIntervalError)
        return {
            'start_time': start_time,
            'end_time': end_time,
            'datetime_interval': datetime_interval
        }

    # params
    # player_tag, start_time, end_time, interval(day, month, hours), 最多24列
    def get(self, request, player_tag):
        params = self.validate(request)
        start_time = params['start_time']
        end_time = params['end_time']
        datetime_interval = DatetimeInterval.interval(params['datetime_interval'])

        datetime_tag_list = []
        while start_time < end_time:
            datetime_tag_list.append(start_time.strftime('%Y-%m-%d %H:%M:%S'))
            start_time = start_time + datetime_interval

        daily_statistic = get_daily_statistic_by_player_tag_and_datetime_tag_list(player_tag, datetime_tag_list)

        return JsonResponse({
            'data': [i.to_dict() for i in daily_statistic]
        })


