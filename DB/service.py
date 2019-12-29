#!/usr/bin/env python
# Create by Annhuny On 2019-12-28 01:58
# File Name : service.py
from DB.sqlalchemy_session import session
from Models.models import SeasonStatistic, Season


def get_season_list():
    return session.query(Season).all()


def get_season_statistic_by_season_id(season_id):
    return session.query(SeasonStatistic).filter_by(seasonId=season_id).all()


