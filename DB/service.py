#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 01:58
# File Name : service.py
from DB.sqlalchemy_session import session
from Models.models import SeasonStatistic, Season, DailyStatistic


# season
def get_season_list():
    return session.query(Season).all()


def get_season_by_id(season_id):
    return session.query(Season).filter_by(id=season_id).first()


def get_season_statistic_by_season_id(season_id):
    return session.query(SeasonStatistic).filter_by(seasonId=season_id).all()


# daily
def get_daily_statistic_by_player_tag_and_datetime_tag_list(player_tag, datetime_tag_list):
    return session.query(DailyStatistic)\
        .filter_by(tag=player_tag)\
        .filter(DailyStatistic.datetimeTag.in_(datetime_tag_list))\
        .all()

