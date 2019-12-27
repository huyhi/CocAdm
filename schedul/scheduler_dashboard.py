#!/usr/bin/env python
# Create by Annhuny On 2019-12-27 00:09
# File Name : scheduler_dashboard.py
import datetime

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

from schedul.fetch_members_data import fetch_player_flowing_data


executors = {
    'default': ThreadPoolExecutor(3),
}

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_player_flowing_data, 'interval', minutes=1,
                      start_date='2000-01-01 00:00:00', executors=executors)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit) as e:
        print(e)

