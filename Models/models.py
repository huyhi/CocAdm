#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 20:04
# File Name : Members.py
from sqlalchemy import Column, String, Integer, JSON, DateTime

from DB.sqlalchemySession import Base


class Member(Base):
    __tablename__ = 'members'

    tag = Column('id', String, primary_key=True)
    name = Column(String)
    role = Column(String)
    expLevel = Column(Integer)
    league = Column(JSON)
    trophies = Column(Integer)
    versusTrophies = Column(Integer)
    clanRank = Column(Integer)
    previousClanRank = Column(Integer)
    donations = Column(Integer)
    donationsReceived = Column(Integer)


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





