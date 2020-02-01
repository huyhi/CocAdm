#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 20:02
# File Name : sqlalchemy_session.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import conf


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base()
Base.to_dict = to_dict

db_conf = conf.get('DB').get('mysql')
engine = create_engine('mysql+mysqlconnector://{user}:{password}@{ip}:{port}/{database}'.format(**{
    'user': db_conf.get('user'),
    'password': db_conf.get('password'),
    'ip': db_conf.get('ip'),
    'port': db_conf.get('port'),
    'database': db_conf.get('database'),
}), pool_size=5, max_overflow=10, pool_timeout=30, pool_pre_ping=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession(expire_on_commit=False)
