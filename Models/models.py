#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 20:04
# File Name : Members.py
from sqlalchemy import Column, String, Integer, JSON, DateTime, func

from DB.sqlalchemy_session import Base


class Season(Base):
    __tablename__ = 'season'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Integer)
    createAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, server_default=func.now())


class SeasonStatistic(Base):
    __tablename__ = 'season_statistic'

    id = Column(Integer, primary_key=True)
    seasonId = Column(Integer)
    tag = Column(String)
    name = Column(String)
    role = Column(String)
    expLevel = Column(Integer)
    league = Column(JSON)
    trophies = Column(Integer)
    versusTrophies = Column(Integer)
    clanRank = Column(Integer)
    previousClanRank = Column(Integer)
    attackWins = Column(Integer)
    donations = Column(Integer)
    donationsReceived = Column(Integer)
    createAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, server_default=func.now())


class FlowingData(Base):
    __tablename__ = 'flowing_data'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    expLevel = Column(Integer)
    trophies = Column(Integer)
    versusTrophies = Column(Integer)
    attackWins = Column(Integer)
    donations = Column(Integer)
    donationsReceived = Column(Integer)
    gold = Column(Integer)
    elixir = Column(Integer)
    darkElixir = Column(Integer)
    datetimeTag = Column(DateTime)
    createAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, server_default=func.now())

