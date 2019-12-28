#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 17:15
# File Name : fetch_data.py

import datetime
import logging
from logging import config

from DB.sqlalchemy_session import session
from Models.models import FlowingData
from settings import LOGGING
from spider.clan import ClanSpider

config.dictConfig(LOGGING)
logger = logging.getLogger('django.schedule')


def fetch_players_tag_list():
    members = ClanSpider.clan_members()
    return [member.get('tag') for member in members]


def fetch_player_flowing_data():
    logger.info('--------------------------------------')
    logger.info('-  fetch players flowing data start  -')
    logger.info('--------------------------------------')

    players_tag_list = fetch_players_tag_list()
    for player_tag in players_tag_list:
        player_data = ClanSpider.player_information(player_tag=player_tag)
        player_data['datetimeTag'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(' fetch player tag: %s ' % player_tag)
        session.add(FlowingData(**player_data))

    session.commit()
    logger.info('--------------')
    logger.info('-  fetch ok  -')
    logger.info('--------------')
    return True


if __name__ == '__main__':
    fetch_player_flowing_data()





