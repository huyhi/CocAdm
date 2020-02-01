# coding: utf-8
# Create by Annhuny On 2020-02-01 13:10
# File Name : test_mysql_connection.py
import logging
import time
import traceback

import sqlalchemy

from DB.service import get_season_list

if __name__ == '__main__':
    logger = logging.getLogger('django.request')

    success, failed = 0, 0;
    for i in range(100):
        try:
            get_season_list()
            time.sleep(60)
            success += 1
        except Exception as e:
            failed += 1
            logger.info(traceback.format_exc())
            break;

    logger.info(success, failed)
    print(success, failed)
