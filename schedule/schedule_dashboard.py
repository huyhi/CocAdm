#!/usr/bin/env python
# Create by Annhuny On 2019-12-27 00:09
# File Name : schedule_dashboard.py
import logging
import traceback
from logging import config

from apscheduler.schedulers.blocking import BlockingScheduler

from schedule.fetch_data import fetch_player_flowing_data
from settings import LOGGING

config.dictConfig(LOGGING)
logger = logging.getLogger('django.schedule')


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_player_flowing_data, 'interval', hours=2,
                      start_date='2000-01-01 00:00:00', end_date='2030-01-01 00:00:00')

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit) as e:
        logger.error(traceback.format_exc())

