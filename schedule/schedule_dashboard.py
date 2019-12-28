#!/usr/bin/env python
# Create by Annhuny On 2019-12-27 00:09
# File Name : schedule_dashboard.py
import datetime

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from schedule.fetch_data import fetch_player_flowing_data


def foo():
    print(datetime.datetime.now())


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_player_flowing_data, 'interval', seconds=10,
                      start_date='2000-01-01 00:00:00', end_date='2030-01-01 00:00:00')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)

