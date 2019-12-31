#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 17:15
# File Name : fetch_data.py

import datetime
import traceback

from DB.sqlalchemy_session import session
from Models.models import FlowingData
from spider.clan import ClanSpider


def fetch_players_tag_list():
    members = ClanSpider.clan_members()
    return [member.get('tag') for member in members]


def fetch_player_flowing_data():
    from schedule.schedule_dashboard import logger

    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:00:00')
    logger.info('***** start fetching flowing data. datetimeTag: {} *****'.format(time_now))

    try:
        players_tag_list = fetch_players_tag_list()
        for player_tag in players_tag_list:
            player_data = ClanSpider.player_information(player_tag=player_tag)
            player_data['datetimeTag'] = time_now
            logger.info('***** fetching playerTag: {} datetimeTag: {} *****'.format(player_tag, time_now))
            session.add(FlowingData(**player_data))
        session.commit()
    except Exception as e:
        logger.error(traceback.format_exc())

    logger.info('***** fetching flowing data OK. datetimeTag: {} *****'.format(time_now))
    return True


if __name__ == '__main__':
    fetch_player_flowing_data()





