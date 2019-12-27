#!/usr/bin/env python
# Create by Annhuny On 2019-12-25 20:02
# File Name : sqlalchemy_session.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import conf


Base = declarative_base()

# 初始化数据库连接
db_conf = conf.get('DB').get('mysql')
engine = create_engine('mysql+mysqlconnector://{user}:{password}@{ip}:{port}/{database}'.format(**{
    'user': db_conf.get('user'),
    'password': db_conf.get('password'),
    'ip': db_conf.get('ip'),
    'port': db_conf.get('port'),
    'database': db_conf.get('database'),
}))

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
session = DBSession()
